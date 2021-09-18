from pathlib import Path

import jpype

from bioformats_jar import get_loci


def test_import():
    loc = get_loci()
    assert jpype.isJVMStarted()

    from bioformats_jar import loci

    assert loc is loci

    assert loci.formats
    assert loci.common
    assert loci.plugins
    assert loci.poi


def test_loci():
    from bioformats_jar.bf import LociFile

    with LociFile(str(Path(__file__).parent / "sample.czi")) as lf:
        d = lf.to_dask()

    d.mean().compute()


def test_read():
    loci = get_loci()
    reader = loci.formats.ImageReader()
    factory = loci.common.services.ServiceFactory()
    service = factory.getInstance(loci.formats.services.OMEXMLService)
    reader.setMetadataStore(service.createOMEXMLMetadata())
    reader.setId(str(Path(__file__).parent / "sample.czi"))
    assert str(reader.getMetadataStore().dumpXML())
    assert reader.openBytes(0)[0] != 0
