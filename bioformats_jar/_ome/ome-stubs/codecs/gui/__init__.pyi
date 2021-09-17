import java.awt.color
import java.awt.image
import java.lang
import typing



class AWTImageTools:
    @typing.overload
    @staticmethod
    def constructImage(int: int, int2: int, int3: int, int4: int, boolean: bool, boolean2: bool, dataBuffer: java.awt.image.DataBuffer) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def constructImage(int: int, int2: int, int3: int, int4: int, boolean: bool, boolean2: bool, dataBuffer: java.awt.image.DataBuffer, colorModel: java.awt.image.ColorModel) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def getBytes(bufferedImage: java.awt.image.BufferedImage, boolean: bool) -> typing.List[int]: ...
    @typing.overload
    @staticmethod
    def getBytes(bufferedImage: java.awt.image.BufferedImage) -> typing.List[typing.List[int]]: ...
    @typing.overload
    @staticmethod
    def getBytes(writableRaster: java.awt.image.WritableRaster) -> typing.List[typing.List[int]]: ...
    @typing.overload
    @staticmethod
    def getBytes(writableRaster: java.awt.image.WritableRaster, int: int, int2: int, int3: int, int4: int) -> typing.List[typing.List[int]]: ...
    @typing.overload
    @staticmethod
    def getDoubles(bufferedImage: java.awt.image.BufferedImage) -> typing.List[typing.List[float]]: ...
    @typing.overload
    @staticmethod
    def getDoubles(writableRaster: java.awt.image.WritableRaster) -> typing.List[typing.List[float]]: ...
    @typing.overload
    @staticmethod
    def getDoubles(writableRaster: java.awt.image.WritableRaster, int: int, int2: int, int3: int, int4: int) -> typing.List[typing.List[float]]: ...
    @typing.overload
    @staticmethod
    def getFloats(bufferedImage: java.awt.image.BufferedImage) -> typing.List[typing.List[float]]: ...
    @typing.overload
    @staticmethod
    def getFloats(writableRaster: java.awt.image.WritableRaster) -> typing.List[typing.List[float]]: ...
    @typing.overload
    @staticmethod
    def getFloats(writableRaster: java.awt.image.WritableRaster, int: int, int2: int, int3: int, int4: int) -> typing.List[typing.List[float]]: ...
    @typing.overload
    @staticmethod
    def getInts(bufferedImage: java.awt.image.BufferedImage) -> typing.List[typing.List[int]]: ...
    @typing.overload
    @staticmethod
    def getInts(writableRaster: java.awt.image.WritableRaster) -> typing.List[typing.List[int]]: ...
    @typing.overload
    @staticmethod
    def getInts(writableRaster: java.awt.image.WritableRaster, int: int, int2: int, int3: int, int4: int) -> typing.List[typing.List[int]]: ...
    @typing.overload
    @staticmethod
    def getPixelBytes(bufferedImage: java.awt.image.BufferedImage, boolean: bool) -> typing.List[typing.List[int]]: ...
    @typing.overload
    @staticmethod
    def getPixelBytes(bufferedImage: java.awt.image.BufferedImage, boolean: bool, int: int, int2: int, int3: int, int4: int) -> typing.List[typing.List[int]]: ...
    @typing.overload
    @staticmethod
    def getPixelBytes(writableRaster: java.awt.image.WritableRaster, boolean: bool) -> typing.List[typing.List[int]]: ...
    @typing.overload
    @staticmethod
    def getPixelBytes(writableRaster: java.awt.image.WritableRaster, boolean: bool, int: int, int2: int, int3: int, int4: int) -> typing.List[typing.List[int]]: ...
    @typing.overload
    @staticmethod
    def getPixels(bufferedImage: java.awt.image.BufferedImage) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def getPixels(bufferedImage: java.awt.image.BufferedImage, int: int, int2: int, int3: int, int4: int) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def getPixels(writableRaster: java.awt.image.WritableRaster) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def getPixels(writableRaster: java.awt.image.WritableRaster, int: int, int2: int, int3: int, int4: int) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def getShorts(bufferedImage: java.awt.image.BufferedImage) -> typing.List[typing.List[int]]: ...
    @typing.overload
    @staticmethod
    def getShorts(writableRaster: java.awt.image.WritableRaster) -> typing.List[typing.List[int]]: ...
    @typing.overload
    @staticmethod
    def getShorts(writableRaster: java.awt.image.WritableRaster, int: int, int2: int, int3: int, int4: int) -> typing.List[typing.List[int]]: ...
    @staticmethod
    def makeColorModel(int: int, int2: int) -> java.awt.image.ColorModel: ...
    @staticmethod
    def makeColorSpace(int: int) -> java.awt.color.ColorSpace: ...
    @typing.overload
    @staticmethod
    def makeImage(byteArray: typing.List[int], int: int, int2: int, boolean: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(byteArray: typing.List[int], int: int, int2: int, int3: int, boolean: bool, boolean2: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(byteArray: typing.List[int], int: int, int2: int, int3: int, boolean: bool, int4: int, boolean2: bool, boolean3: bool, boolean4: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(byteArray: typing.List[typing.List[int]], int: int, int2: int, boolean: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(byteArray: typing.List[typing.List[int]], int: int, int2: int, int3: int, boolean: bool, boolean2: bool, boolean3: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(doubleArray: typing.List[float], int: int, int2: int) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(doubleArray: typing.List[float], int: int, int2: int, int3: int, boolean: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(doubleArray: typing.List[typing.List[float]], int: int, int2: int) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(floatArray: typing.List[float], int: int, int2: int) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(floatArray: typing.List[float], int: int, int2: int, int3: int, boolean: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(floatArray: typing.List[typing.List[float]], int: int, int2: int) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(intArray: typing.List[int], int2: int, int3: int, boolean: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(intArray: typing.List[int], int2: int, int3: int, int4: int, boolean: bool, boolean2: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(intArray: typing.List[typing.List[int]], int2: int, int3: int, boolean: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(shortArray: typing.List[int], int: int, int2: int, boolean: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(shortArray: typing.List[int], int: int, int2: int, int3: int, boolean: bool, boolean2: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeImage(shortArray: typing.List[typing.List[int]], int: int, int2: int, boolean: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeRGBImage(byteArray: typing.List[int], int: int, int2: int, int3: int, boolean: bool) -> java.awt.image.BufferedImage: ...
    @typing.overload
    @staticmethod
    def makeRGBImage(byteArray: typing.List[typing.List[int]], int: int, int2: int) -> java.awt.image.BufferedImage: ...

class SignedByteBuffer(java.awt.image.DataBuffer):
    @typing.overload
    def __init__(self, byteArray: typing.List[int], int: int): ...
    @typing.overload
    def __init__(self, byteArray: typing.List[typing.List[int]], int: int): ...
    @typing.overload
    def getData(self) -> typing.List[int]: ...
    @typing.overload
    def getData(self, int: int) -> typing.List[int]: ...
    @typing.overload
    def getElem(self, int: int) -> int: ...
    @typing.overload
    def getElem(self, int: int, int2: int) -> int: ...
    @typing.overload
    def setElem(self, int: int, int2: int) -> None: ...
    @typing.overload
    def setElem(self, int: int, int2: int, int3: int) -> None: ...

class SignedShortBuffer(java.awt.image.DataBuffer):
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, shortArray: typing.List[int], int: int): ...
    @typing.overload
    def __init__(self, shortArray: typing.List[int], int: int, int2: int): ...
    @typing.overload
    def __init__(self, shortArray: typing.List[typing.List[int]], int: int): ...
    @typing.overload
    def __init__(self, shortArray: typing.List[typing.List[int]], int: int, intArray: typing.List[int]): ...
    @typing.overload
    def getData(self) -> typing.List[int]: ...
    @typing.overload
    def getData(self, int: int) -> typing.List[int]: ...
    @typing.overload
    def getElem(self, int: int) -> int: ...
    @typing.overload
    def getElem(self, int: int, int2: int) -> int: ...
    @typing.overload
    def setElem(self, int: int, int2: int) -> None: ...
    @typing.overload
    def setElem(self, int: int, int2: int, int3: int) -> None: ...

class TwoChannelColorSpace(java.awt.color.ColorSpace):
    CS_2C: typing.ClassVar[int] = ...
    def fromCIEXYZ(self, floatArray: typing.List[float]) -> typing.List[float]: ...
    def fromRGB(self, floatArray: typing.List[float]) -> typing.List[float]: ...
    @staticmethod
    def getInstance(int: int) -> java.awt.color.ColorSpace: ...
    def getName(self, int: int) -> java.lang.String: ...
    def getNumComponents(self) -> int: ...
    def getType(self) -> int: ...
    def isCS_sRGB(self) -> bool: ...
    def toCIEXYZ(self, floatArray: typing.List[float]) -> typing.List[float]: ...
    def toRGB(self, floatArray: typing.List[float]) -> typing.List[float]: ...

class UnsignedIntBuffer(java.awt.image.DataBuffer):
    @typing.overload
    def __init__(self, intArray: typing.List[int], int2: int): ...
    @typing.overload
    def __init__(self, intArray: typing.List[typing.List[int]], int2: int): ...
    @typing.overload
    def getData(self) -> typing.List[int]: ...
    @typing.overload
    def getData(self, int: int) -> typing.List[int]: ...
    @typing.overload
    def getElem(self, int: int) -> int: ...
    @typing.overload
    def getElem(self, int: int, int2: int) -> int: ...
    @typing.overload
    def getElemDouble(self, int: int) -> float: ...
    @typing.overload
    def getElemDouble(self, int: int, int2: int) -> float: ...
    @typing.overload
    def getElemFloat(self, int: int) -> float: ...
    @typing.overload
    def getElemFloat(self, int: int, int2: int) -> float: ...
    @typing.overload
    def setElem(self, int: int, int2: int) -> None: ...
    @typing.overload
    def setElem(self, int: int, int2: int, int3: int) -> None: ...
    @typing.overload
    def setElemDouble(self, int: int, double: float) -> None: ...
    @typing.overload
    def setElemDouble(self, int: int, int2: int, double: float) -> None: ...
    @typing.overload
    def setElemFloat(self, int: int, float: float) -> None: ...
    @typing.overload
    def setElemFloat(self, int: int, int2: int, float: float) -> None: ...

class UnsignedIntColorModel(java.awt.image.ColorModel):
    def __init__(self, int: int, int2: int, int3: int): ...
    def createCompatibleWritableRaster(self, int: int, int2: int) -> java.awt.image.WritableRaster: ...
    @typing.overload
    def getAlpha(self, int: int) -> int: ...
    @typing.overload
    def getAlpha(self, object: typing.Any) -> int: ...
    @typing.overload
    def getBlue(self, int: int) -> int: ...
    @typing.overload
    def getBlue(self, object: typing.Any) -> int: ...
    @typing.overload
    def getDataElements(self, floatArray: typing.List[float], int: int, object: typing.Any) -> typing.Any: ...
    @typing.overload
    def getDataElements(self, intArray: typing.List[int], int2: int, object: typing.Any) -> typing.Any: ...
    @typing.overload
    def getDataElements(self, int: int, object: typing.Any) -> typing.Any: ...
    @typing.overload
    def getGreen(self, int: int) -> int: ...
    @typing.overload
    def getGreen(self, object: typing.Any) -> int: ...
    @typing.overload
    def getRed(self, int: int) -> int: ...
    @typing.overload
    def getRed(self, object: typing.Any) -> int: ...
    def isCompatibleRaster(self, raster: java.awt.image.Raster) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("ome.codecs.gui")``.

    AWTImageTools: typing.Type[AWTImageTools]
    SignedByteBuffer: typing.Type[SignedByteBuffer]
    SignedShortBuffer: typing.Type[SignedShortBuffer]
    TwoChannelColorSpace: typing.Type[TwoChannelColorSpace]
    UnsignedIntBuffer: typing.Type[UnsignedIntBuffer]
    UnsignedIntColorModel: typing.Type[UnsignedIntColorModel]