import java.lang
import java.util
import bioformats_jar._loci
import bioformats_jar._loci.poi.hssf.record
import typing



class AreaReference:
    def __init__(self, string: typing.Union[java.lang.String, str]): ...
    def getCells(self) -> typing.List['CellReference']: ...
    def getDim(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class CellReference:
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, string: typing.Union[java.lang.String, str]): ...
    def getCol(self) -> int: ...
    def getRow(self) -> int: ...
    def getSheetName(self) -> java.lang.String: ...
    def isColAbsolute(self) -> bool: ...
    def isRowAbsolute(self) -> bool: ...
    def toString(self) -> java.lang.String: ...

class PaneInformation:
    PANE_LOWER_RIGHT: typing.ClassVar[int] = ...
    PANE_UPPER_RIGHT: typing.ClassVar[int] = ...
    PANE_LOWER_LEFT: typing.ClassVar[int] = ...
    PANE_UPPER_LEFT: typing.ClassVar[int] = ...
    def __init__(self, short: int, short2: int, short3: int, short4: int, byte: int, boolean: bool): ...
    def getActivePane(self) -> int: ...
    def getHorizontalSplitPosition(self) -> int: ...
    def getHorizontalSplitTopRow(self) -> int: ...
    def getVerticalSplitLeftColumn(self) -> int: ...
    def getVerticalSplitPosition(self) -> int: ...
    def isFreezePane(self) -> bool: ...

class RKUtil:
    @staticmethod
    def decodeNumber(int: int) -> float: ...

class RangeAddress:
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, int4: int): ...
    @typing.overload
    def __init__(self, string: typing.Union[java.lang.String, str]): ...
    def get26Sys(self, string: typing.Union[java.lang.String, str]) -> int: ...
    def getAddress(self) -> java.lang.String: ...
    def getCharPart(self, string: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    def getDigitPart(self, string: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    def getFromCell(self) -> java.lang.String: ...
    def getHeight(self) -> int: ...
    def getRange(self) -> java.lang.String: ...
    def getSheetName(self) -> java.lang.String: ...
    def getToCell(self) -> java.lang.String: ...
    def getWidth(self) -> int: ...
    def getXPosition(self, string: typing.Union[java.lang.String, str]) -> int: ...
    def getYPosition(self, string: typing.Union[java.lang.String, str]) -> int: ...
    def hasCell(self) -> bool: ...
    def hasRange(self) -> bool: ...
    def hasSheetName(self) -> bool: ...
    def isCellOk(self, string: typing.Union[java.lang.String, str]) -> bool: ...
    @typing.overload
    def isSheetNameOk(self) -> bool: ...
    @typing.overload
    @staticmethod
    def isSheetNameOk(string: typing.Union[java.lang.String, str]) -> bool: ...
    def numTo26Sys(self, int: int) -> java.lang.String: ...
    def removeString(self, string: typing.Union[java.lang.String, str], string2: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    def replaceString(self, string: typing.Union[java.lang.String, str], string2: typing.Union[java.lang.String, str], string3: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    def setSize(self, int: int, int2: int) -> None: ...

class Region(java.lang.Comparable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int, short: int, int2: int, short2: int): ...
    @typing.overload
    def __init__(self, mergedRegion: bioformats_jar._loci.poi.hssf.record.MergeCellsRecord.MergedRegion): ...
    @typing.overload
    def compareTo(self, object: typing.Any) -> int: ...
    @typing.overload
    def compareTo(self, region: 'Region') -> int: ...
    def contains(self, int: int, short: int) -> bool: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def equals(self, region: 'Region') -> bool: ...
    def getArea(self) -> int: ...
    def getColumnFrom(self) -> int: ...
    def getColumnTo(self) -> int: ...
    def getRowFrom(self) -> int: ...
    def getRowTo(self) -> int: ...
    def setColumnFrom(self, short: int) -> None: ...
    def setColumnTo(self, short: int) -> None: ...
    def setRowFrom(self, int: int) -> None: ...
    def setRowTo(self, int: int) -> None: ...

class SheetReferences:
    def __init__(self): ...
    def addSheetReference(self, string: typing.Union[java.lang.String, str], int: int) -> None: ...
    def getSheetName(self, int: int) -> java.lang.String: ...

class HSSFColor:
    def __init__(self): ...
    def getHexString(self) -> java.lang.String: ...
    def getIndex(self) -> int: ...
    @staticmethod
    def getIndexHash() -> java.util.Hashtable: ...
    def getTriplet(self) -> typing.List[int]: ...
    @staticmethod
    def getTripletHash() -> java.util.Hashtable: ...
    class AQUA(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class AUTOMATIC(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        @staticmethod
        def getInstance() -> 'HSSFColor': ...
        def getTriplet(self) -> typing.List[int]: ...
    class BLACK(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class BLUE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        index2: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class BLUE_GREY(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class BRIGHT_GREEN(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        index2: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class BROWN(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class CORAL(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class CORNFLOWER_BLUE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class DARK_BLUE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        index2: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class DARK_GREEN(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class DARK_RED(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        index2: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class DARK_TEAL(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class DARK_YELLOW(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class GOLD(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class GREEN(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class GREY_25_PERCENT(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class GREY_40_PERCENT(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class GREY_50_PERCENT(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class GREY_80_PERCENT(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class INDIGO(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class LAVENDER(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class LEMON_CHIFFON(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class LIGHT_BLUE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class LIGHT_CORNFLOWER_BLUE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class LIGHT_GREEN(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class LIGHT_ORANGE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class LIGHT_TURQUOISE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        index2: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class LIGHT_YELLOW(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class LIME(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class MAROON(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class OLIVE_GREEN(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class ORANGE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class ORCHID(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class PALE_BLUE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class PINK(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        index2: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class PLUM(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        index2: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class RED(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class ROSE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class ROYAL_BLUE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class SEA_GREEN(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class SKY_BLUE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class TAN(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class TEAL(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        index2: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class TURQUOISE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        index2: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class VIOLET(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        index2: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class WHITE(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...
    class YELLOW(loci.poi.hssf.util.HSSFColor):
        index: typing.ClassVar[int] = ...
        index2: typing.ClassVar[int] = ...
        triplet: typing.ClassVar[typing.List[int]] = ...
        hexString: typing.ClassVar[java.lang.String] = ...
        def __init__(self): ...
        def getHexString(self) -> java.lang.String: ...
        def getIndex(self) -> int: ...
        def getTriplet(self) -> typing.List[int]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("loci.poi.hssf.util")``.

    AreaReference: typing.Type[AreaReference]
    CellReference: typing.Type[CellReference]
    HSSFColor: typing.Type[HSSFColor]
    PaneInformation: typing.Type[PaneInformation]
    RKUtil: typing.Type[RKUtil]
    RangeAddress: typing.Type[RangeAddress]
    Region: typing.Type[Region]
    SheetReferences: typing.Type[SheetReferences]
