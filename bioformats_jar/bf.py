#!/usr/bin/env python
from __future__ import annotations

from functools import lru_cache
from threading import Lock
from typing import TYPE_CHECKING, Any, Callable, NamedTuple

import numpy as np
from wrapt import ObjectProxy

if TYPE_CHECKING:
    from pathlib import Path

    import dask.array as da

    from bioformats_jar import loci


class CoreMeta(NamedTuple):
    """NamedTuple with core bioformats metadata. (not OME meta)"""

    shape: tuple[int, int, int, int, int, int]
    dtype: str
    series_count: int
    is_rgb: bool
    is_interleaved: bool
    dimension_order: str
    resolution_count: int


class LociFile:
    """Read image and metadata from file supported by Bioformats.

    LociFile instances must be closed using the 'close' method, which is
    automatically called when using the 'with' context manager.

    LociFile instances are not thread-safe.

    Parameters
    ----------
    path : Union[str, Path]
        path to file
    series : int, optional
        the image series to read, by default 0
    meta : bool, optional
        whether to get metadata as well, by default True
    memoize : int, optional
        threshold for memoizing the reader. If the time required to call
        `reader.setId()` is larger than this number, the initialized reader
        (including all reader wrappers) will be cached in a memo file for later
        retrieval. by default 50.  set to 0 or less to turn off memoization.
        https://downloads.openmicroscopy.org/bio-formats/latest/api/loci/formats/Memoizer.html
    """

    def __init__(
        self,
        path: str | Path,
        series: int = 0,
        meta: bool = True,
        original_meta: bool = False,
        memoize: int | bool = 0,
    ):
        from bioformats_jar import get_loci

        loci = get_loci()
        self._path = str(path)
        self._r = loci.formats.ImageReader()
        if meta:
            self._r.setMetadataStore(self._create_ome_meta())
        if original_meta:
            self._r.setOriginalMetadataPopulated(True)

        # memoize to save time on later re-openings of the same file.
        if memoize > 0:
            _hide_memoization_warning()
            self._r = loci.formats.Memoizer(self._r, memoize)

        self.open()
        self._lock = Lock()

        if "ND2" in str(self._r.getReader()):
            # https://github.com/openmicroscopy/bioformats/issues/2955
            mo = loci.formats.in_.DynamicMetadataOptions()
            mo.set("nativend2.chunkmap", "False")
            self._r.setMetadataOptions(mo)

        self.set_series(series)

    def set_series(self, series: int = 0) -> None:
        self._r.setSeries(series)
        self._core_meta = CoreMeta(
            (
                self._r.getSizeT(),
                self._r.getEffectiveSizeC(),
                self._r.getSizeZ(),
                self._r.getSizeY(),
                self._r.getSizeX(),
                self._r.getRGBChannelCount(),
            ),
            _pixtype2dtype(self._r.getPixelType(), self._r.isLittleEndian()),
            self._r.getSeriesCount(),
            self._r.isRGB(),
            self._r.isInterleaved(),
            self._r.getDimensionOrder(),
            self._r.getResolutionCount(),
        )

    @property
    def core_meta(self) -> CoreMeta:
        return self._core_meta

    def open(self) -> None:
        """Open file."""
        self._r.setId(self._path)

    def close(self) -> None:
        """Close file."""
        try:
            self._r.close()
        except (AttributeError, ImportError, RuntimeError):
            pass

    def to_numpy(self, series: int | None = None) -> np.ndarray:
        """Create numpy array for the current series."""
        return np.asarray(self.to_dask(series))

    def to_dask(self, series: int | None = None) -> da.Array:
        """Create dask array for the current series."""
        import dask.array as da

        if series is not None:
            self._r.setSeries(series)

        nt, nc, nz, ny, nx, nrgb = self.core_meta.shape
        chunks = ((1,) * nt, (1,) * nc, (1,) * nz, ny, nx)
        if nrgb > 1:
            chunks = chunks + (nrgb,)  # type: ignore
        return da.map_blocks(
            self._dask_chunk,
            chunks=chunks,
            dtype=self.core_meta.dtype,
        )
        # return _DaskArrayProxy(arr, self)

    @property
    def is_open(self) -> bool:
        """Whether the underlying file is currently open"""
        return bool(self._r.getCurrentFile())

    @property
    def filename(self) -> str:
        """Return name of file handle."""
        # return self._r.getCurrentFile()
        return self._path

    @property
    def ome_xml(self) -> str:
        """return OME XML string."""
        with self:
            store = self._r.getMetadataStore()

            return str(store.dumpXML()) if store else ""

    def __enter__(self) -> LociFile:
        if not self.is_open:
            self.open()
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def __del__(self) -> None:
        self.close()

    def _get_plane(
        self,
        t: int = 0,
        c: int = 0,
        z: int = 0,
        y: slice = slice(None),
        x: slice = slice(None),
    ) -> np.ndarray:
        """Load a single plane."""
        with self._lock:
            was_open = self.is_open
            if not was_open:
                self.open()
            idx = self._r.getIndex(z, c, t)
            *_, ny, nx, nrgb = self.core_meta.shape
            ystart, ywidth = _slice2width(y, ny)
            xstart, xwidth = _slice2width(x, nx)
            buffer = self._r.openBytes(idx, xstart, ystart, xwidth, ywidth)
            # TODO: check what the bare minimim amount of copying is to prevent
            # reading incorrect regions (doesnt' segfault, but can get weird)
            im = np.frombuffer(buffer[:], self.core_meta.dtype).copy()
            if nrgb > 1:
                # TODO: check this with some examples
                if self.core_meta.is_interleaved:
                    im.shape = (ywidth, xwidth, nrgb)
                else:
                    im.shape = (nrgb, ywidth, xwidth)
                    im = np.transpose(im, (1, 2, 0))
            else:
                im.shape = (ywidth, xwidth)
            # TODO: check this... we might need to reshaped the non interleaved case
            if not was_open:
                self.close()
        return im

    def _dask_chunk(self, block_id: tuple[int, ...]) -> np.ndarray:
        # if someone indexes a 5D dask array as `arr[0,1,2]`, then the `info`
        # dict will contain the key: 'chunk-location': (0, 1, 2, 0, 0)
        # reader.getIndex() expects (Z, C, T) ...
        # We ASSUME that the final dask array is in the order TCZYX, so chunk-location
        # will be coming in as (T, C, Z, Y, X). `[2::-1]`` converts that to (Z, C, T)
        # TODO: we could either use the native getDimensionOrder? (or not) or let
        # the user
        t, c, z, *_ = block_id
        im = self._get_plane(t, c, z)
        return im[np.newaxis, np.newaxis, np.newaxis]

    _service: loci.common.services.ServiceFactory | None = None

    @classmethod
    def _create_ome_meta(cls) -> Any:
        from bioformats_jar import loci

        if not cls._service:
            factory = loci.common.services.ServiceFactory()
            cls._service = factory.getInstance(loci.formats.services.OMEXMLService)
        return cls._service.createOMEXMLMetadata()


def _pixtype2dtype(pixeltype: int, little_endian: bool) -> str:
    """convert a loci pixel type into a numpy dtype string."""
    from bioformats_jar import loci

    FT = loci.formats.FormatTools
    fmt2type: dict[int, str] = {
        FT.INT8: "i1",
        FT.UINT8: "u1",
        FT.INT16: "i2",
        FT.UINT16: "u2",
        FT.INT32: "i4",
        FT.UINT32: "u4",
        FT.FLOAT: "f4",
        FT.DOUBLE: "f8",
    }
    return ("<" if little_endian else ">") + fmt2type[pixeltype]


class _DaskArrayProxy(ObjectProxy):
    """Dask array wrapper that provides a 'file open' context when computing.

    This is necessary because `LociFile.to_dask` returns an array with a mapped
    underlying reader function that requires the file to be open.  But we don't want to
    open/close the file on every single chunk.  So this wrap the `compute` and
    `__array__` method in an open-file context manager.  For __getattr__, we return an
    `ArrayMethodProxy` that again wraps the resulting object in a DaskArrayProxy if it
    is a dask array.
    """

    def __init__(self, wrapped: da.Array, loci_file: LociFile) -> None:
        super().__init__(wrapped)
        self.lf = loci_file

    def __getitem__(self, key: Any) -> _DaskArrayProxy:
        return _DaskArrayProxy(self.__wrapped__.__getitem__(key), self.lf)

    def __getattr__(self, key: Any) -> Any:
        attr = getattr(self.__wrapped__, key)
        if callable(attr):
            return _ArrayMethodProxy(attr, self.lf)
        return attr

    def __repr__(self) -> str:
        return repr(self.__wrapped__)

    def compute(self, **kwargs: Any) -> np.ndarray:
        with self.lf:
            return self.__wrapped__.compute(**kwargs)

    def __array__(self, dtype: str = None, **kwargs: Any) -> np.ndarray:
        with self.lf:
            return self.__wrapped__.__array__(dtype, **kwargs)

    def __array_function__(self, *args: Any) -> Any:
        with self.lf:
            return self.__wrapped__.__array_function__(*args)


class _ArrayMethodProxy:
    """Wraps method on a dask array and returns a DaskArrayProxy if the result of the
    method is a dask array.  see details in DaskArrayProxy docstring."""

    def __init__(self, method: Callable, loci_file: LociFile) -> None:
        self.method = method
        self.lf = loci_file

    def __repr__(self) -> str:
        return repr(self.method)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        import dask.array as da

        with self.lf:
            result = self.method(*args, **kwds)
        if isinstance(result, da.Array):
            return _DaskArrayProxy(result, self.lf)
        return result


def _slice2width(slc: slice, length: int) -> tuple[int, int]:
    """convert `slice` object into (start, width)"""
    if slc.stop is not None or slc.start is not None:
        # NOTE: we're ignoring step != 1 here
        start, stop, _ = slc.indices(length)
        return min(start, stop), abs(stop - start)
    return 0, length


@lru_cache(maxsize=1)
def _hide_memoization_warning() -> None:
    """HACK: this silences a warning about memoization for now

    An illegal reflective access operation has occurred
    https://github.com/ome/bioformats/issues/3659
    """
    import jpype

    System = jpype.JPackage("java").lang.System
    System.err.close()