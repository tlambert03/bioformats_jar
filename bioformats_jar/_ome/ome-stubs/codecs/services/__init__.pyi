import java.awt.image
import java.io
import java.lang
import loci.common.services
import bioformats_jar._ome.codecs
import typing



class JAIIIOService(loci.common.services.Service):
    @typing.overload
    def readImage(self, inputStream: java.io.InputStream) -> java.awt.image.BufferedImage: ...
    @typing.overload
    def readImage(self, inputStream: java.io.InputStream, jPEG2000CodecOptions: bioformats_jar._ome.codecs.JPEG2000CodecOptions) -> java.awt.image.BufferedImage: ...
    @typing.overload
    def readRaster(self, inputStream: java.io.InputStream) -> java.awt.image.Raster: ...
    @typing.overload
    def readRaster(self, inputStream: java.io.InputStream, jPEG2000CodecOptions: bioformats_jar._ome.codecs.JPEG2000CodecOptions) -> java.awt.image.Raster: ...
    def writeImage(self, outputStream: java.io.OutputStream, bufferedImage: java.awt.image.BufferedImage, jPEG2000CodecOptions: bioformats_jar._ome.codecs.JPEG2000CodecOptions) -> None: ...

class LuraWaveService(loci.common.services.Service):
    def decodeToMemoryGray16(self, shortArray: typing.List[int], int: int, int2: int, int3: int, int4: int, int5: int, int6: int, int7: int, int8: int, int9: int, int10: int) -> None: ...
    def decodeToMemoryGray8(self, byteArray: typing.List[int], int: int, int2: int, int3: int) -> None: ...
    def getHeight(self) -> int: ...
    def getLicenseCode(self) -> java.lang.String: ...
    def getWidth(self) -> int: ...
    def initialize(self, inputStream: java.io.InputStream) -> None: ...
    def setLicenseCode(self, string: typing.Union[java.lang.String, str]) -> None: ...

class JAIIIOServiceImpl(loci.common.services.AbstractService, JAIIIOService):
    NO_J2K_MSG: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    @typing.overload
    def readImage(self, inputStream: java.io.InputStream) -> java.awt.image.BufferedImage: ...
    @typing.overload
    def readImage(self, inputStream: java.io.InputStream, jPEG2000CodecOptions: bioformats_jar._ome.codecs.JPEG2000CodecOptions) -> java.awt.image.BufferedImage: ...
    @typing.overload
    def readRaster(self, inputStream: java.io.InputStream) -> java.awt.image.Raster: ...
    @typing.overload
    def readRaster(self, inputStream: java.io.InputStream, jPEG2000CodecOptions: bioformats_jar._ome.codecs.JPEG2000CodecOptions) -> java.awt.image.Raster: ...
    def writeImage(self, outputStream: java.io.OutputStream, bufferedImage: java.awt.image.BufferedImage, jPEG2000CodecOptions: bioformats_jar._ome.codecs.JPEG2000CodecOptions) -> None: ...

class LuraWaveServiceImpl(loci.common.services.AbstractService, LuraWaveService):
    LICENSE_PROPERTY: typing.ClassVar[java.lang.String] = ...
    NO_LURAWAVE_MSG: typing.ClassVar[java.lang.String] = ...
    NO_LICENSE_MSG: typing.ClassVar[java.lang.String] = ...
    INVALID_LICENSE_MSG: typing.ClassVar[java.lang.String] = ...
    STUB_FIELD: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    def decodeToMemoryGray16(self, shortArray: typing.List[int], int: int, int2: int, int3: int, int4: int, int5: int, int6: int, int7: int, int8: int, int9: int, int10: int) -> None: ...
    def decodeToMemoryGray8(self, byteArray: typing.List[int], int: int, int2: int, int3: int) -> None: ...
    def getHeight(self) -> int: ...
    def getLicenseCode(self) -> java.lang.String: ...
    def getWidth(self) -> int: ...
    def initialize(self, inputStream: java.io.InputStream) -> None: ...
    def setLicenseCode(self, string: typing.Union[java.lang.String, str]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("ome.codecs.services")``.

    JAIIIOService: typing.Type[JAIIIOService]
    JAIIIOServiceImpl: typing.Type[JAIIIOServiceImpl]
    LuraWaveService: typing.Type[LuraWaveService]
    LuraWaveServiceImpl: typing.Type[LuraWaveServiceImpl]