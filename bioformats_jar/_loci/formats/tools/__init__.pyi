import java.awt.event
import java.awt.image
import java.io
import java.lang
import java.util
import javax.swing
import jpype.protocol
import bioformats_jar._loci.common
import bioformats_jar._loci.formats
import typing



class AmiraParameters:
    width: int = ...
    height: int = ...
    depth: int = ...
    firstDataStream: int = ...
    x0: float = ...
    y0: float = ...
    z0: float = ...
    x1: float = ...
    y1: float = ...
    z1: float = ...
    littleEndian: bool = ...
    ascii: bool = ...
    nStreams: int = ...
    streamNames: typing.List[java.lang.String] = ...
    streamTypes: typing.List[java.lang.String] = ...
    @typing.overload
    def __init__(self, string: typing.Union[java.lang.String, str]): ...
    @typing.overload
    def __init__(self, randomAccessInputStream: bioformats_jar._loci.common.RandomAccessInputStream): ...
    @staticmethod
    def entryToString(object: typing.Any, string: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    def getMap(self) -> java.util.Map: ...
    def getStreams(self) -> java.util.Map: ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...
    @typing.overload
    def toString(self) -> java.lang.String: ...
    @typing.overload
    @staticmethod
    def toString(map: typing.Union[java.util.Map, typing.Mapping], string: typing.Union[java.lang.String, str]) -> java.lang.String: ...

class AsciiImage:
    def __init__(self, bufferedImage: java.awt.image.BufferedImage): ...
    def toString(self) -> java.lang.String: ...

class BioFormatsExtensionPrinter:
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...

class CacheConsole:
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...

class CommandLineTools:
    VERSION: typing.ClassVar[java.lang.String] = ...
    NO_UPGRADE_CHECK: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    @staticmethod
    def printVersion() -> None: ...
    @staticmethod
    def runUpgradeCheck(stringArray: typing.List[java.lang.String]) -> None: ...

class EditTiffG(javax.swing.JFrame, java.awt.event.ActionListener):
    def __init__(self): ...
    def actionPerformed(self, actionEvent: java.awt.event.ActionEvent) -> None: ...
    def exit(self) -> None: ...
    def getXML(self) -> java.lang.String: ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...
    @typing.overload
    @staticmethod
    def open(string: typing.Union[java.lang.String, str]) -> bioformats_jar._loci.common.RandomAccessInputStream: ...
    @typing.overload
    def open(self) -> None: ...
    @typing.overload
    @staticmethod
    def openFile(string: typing.Union[java.lang.String, str]) -> None: ...
    @typing.overload
    def openFile(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...
    @typing.overload
    def openFile(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], randomAccessInputStream: bioformats_jar._loci.common.RandomAccessInputStream) -> None: ...
    def save(self) -> None: ...
    def saveFile(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...
    def setXML(self, string: typing.Union[java.lang.String, str]) -> None: ...
    def showError(self, throwable: java.lang.Throwable) -> None: ...

class FakeImage:
    def __init__(self, location: bioformats_jar._loci.common.Location): ...
    def generateScreen(self, int: int, int2: int, int3: int, int4: int, int5: int) -> bioformats_jar._loci.common.Location: ...
    @staticmethod
    def isValidRange(int: int, int2: int, int3: int) -> None: ...

class GenerateCache:
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...

class ImageConverter:
    def __init__(self): ...
    def getTileColumns(self, string: typing.Union[java.lang.String, str]) -> int: ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...
    def testConvert(self, iFormatWriter: bioformats_jar._loci.formats.IFormatWriter, stringArray: typing.List[java.lang.String]) -> bool: ...

class ImageFaker:
    def __init__(self): ...
    def fakeScreen(self, stringArray: typing.List[java.lang.String]) -> bool: ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...
    def parseArgs(self, stringArray: typing.List[java.lang.String]) -> bool: ...
    def printUsage(self) -> None: ...

class ImageInfo:
    def __init__(self): ...
    def checkWarnings(self) -> None: ...
    def configureReaderPostInit(self) -> None: ...
    def configureReaderPreInit(self) -> None: ...
    def createReader(self) -> None: ...
    def initPreMinMaxValues(self) -> None: ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...
    def mapLocation(self) -> None: ...
    def parseArgs(self, stringArray: typing.List[java.lang.String]) -> bool: ...
    def printGlobalMetadata(self) -> None: ...
    def printMinMaxValues(self) -> None: ...
    def printOMEXML(self) -> None: ...
    def printOriginalMetadata(self) -> None: ...
    def printUsage(self) -> None: ...
    def readCoreMetadata(self) -> None: ...
    def readPixels(self) -> None: ...
    def setReader(self, iFormatReader: bioformats_jar._loci.formats.IFormatReader) -> None: ...
    def testRead(self, stringArray: typing.List[java.lang.String]) -> bool: ...

class MakeTestOmeTiff:
    sizeZsub: int = ...
    sizeTsub: int = ...
    sizeCsub: int = ...
    isModulo: bool = ...
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...
    @typing.overload
    def makeOmeTiff(self, stringArray: typing.List[java.lang.String]) -> int: ...
    @typing.overload
    def makeOmeTiff(self, string: typing.Union[java.lang.String, str], coreMetadata: bioformats_jar._loci.formats.CoreMetadata) -> None: ...
    def makeOmeTiffExtensions(self, stringArray: typing.List[java.lang.String]) -> None: ...
    def makeSamples(self) -> None: ...

class PrintDomains:
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...

class PrintFormatTable:
    def __init__(self): ...
    @staticmethod
    def getFooter(printStyles: 'PrintFormatTable.PrintStyles') -> java.lang.String: ...
    @staticmethod
    def getFormatLine(printStyles: 'PrintFormatTable.PrintStyles', string: typing.Union[java.lang.String, str], boolean: bool, boolean2: bool, boolean3: bool, string2: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    @staticmethod
    def getHeader(printStyles: 'PrintFormatTable.PrintStyles') -> java.lang.String: ...
    @staticmethod
    def getHtmlFooter() -> java.lang.String: ...
    @staticmethod
    def getHtmlFormatLine(string: typing.Union[java.lang.String, str], boolean: bool, boolean2: bool, string2: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    @staticmethod
    def getHtmlHeader() -> java.lang.String: ...
    @staticmethod
    def getTextFooter() -> java.lang.String: ...
    @staticmethod
    def getTextFormatLine(string: typing.Union[java.lang.String, str], boolean: bool, boolean2: bool, boolean3: bool, string2: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    @staticmethod
    def getTextHeader() -> java.lang.String: ...
    @staticmethod
    def getXmlFooter() -> java.lang.String: ...
    @staticmethod
    def getXmlFormatLine(string: typing.Union[java.lang.String, str], boolean: bool, boolean2: bool, boolean3: bool, string2: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    @staticmethod
    def getXmlHeader() -> java.lang.String: ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...
    @staticmethod
    def printSupportedFormats(stringArray: typing.List[java.lang.String]) -> None: ...
    class PrintStyles(java.lang.Enum['PrintFormatTable.PrintStyles']):
        TXT: typing.ClassVar['PrintFormatTable.PrintStyles'] = ...
        XML: typing.ClassVar['PrintFormatTable.PrintStyles'] = ...
        HTML: typing.ClassVar['PrintFormatTable.PrintStyles'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: typing.Union[java.lang.String, str]) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: typing.Union[java.lang.String, str]) -> 'PrintFormatTable.PrintStyles': ...
        @staticmethod
        def values() -> typing.List['PrintFormatTable.PrintStyles']: ...

class TiffComment:
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...

class UpgradeCheck:
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...

class XMLIndent:
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...
    @staticmethod
    def process(bufferedReader: java.io.BufferedReader, boolean: bool) -> None: ...

class XMLValidate:
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[java.lang.String]) -> None: ...
    @staticmethod
    def process(string: typing.Union[java.lang.String, str], bufferedReader: java.io.BufferedReader) -> None: ...
    @typing.overload
    @staticmethod
    def validate(bufferedReader: java.io.BufferedReader, string: typing.Union[java.lang.String, str]) -> bool: ...
    @typing.overload
    @staticmethod
    def validate(string: typing.Union[java.lang.String, str]) -> bool: ...
    @typing.overload
    @staticmethod
    def validate(stringArray: typing.List[java.lang.String]) -> typing.List[bool]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("loci.formats.tools")``.

    AmiraParameters: typing.Type[AmiraParameters]
    AsciiImage: typing.Type[AsciiImage]
    BioFormatsExtensionPrinter: typing.Type[BioFormatsExtensionPrinter]
    CacheConsole: typing.Type[CacheConsole]
    CommandLineTools: typing.Type[CommandLineTools]
    EditTiffG: typing.Type[EditTiffG]
    FakeImage: typing.Type[FakeImage]
    GenerateCache: typing.Type[GenerateCache]
    ImageConverter: typing.Type[ImageConverter]
    ImageFaker: typing.Type[ImageFaker]
    ImageInfo: typing.Type[ImageInfo]
    MakeTestOmeTiff: typing.Type[MakeTestOmeTiff]
    PrintDomains: typing.Type[PrintDomains]
    PrintFormatTable: typing.Type[PrintFormatTable]
    TiffComment: typing.Type[TiffComment]
    UpgradeCheck: typing.Type[UpgradeCheck]
    XMLIndent: typing.Type[XMLIndent]
    XMLValidate: typing.Type[XMLValidate]
