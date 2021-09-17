import java.lang
import bioformats_jar._ome.units.quantity
import bioformats_jar._ome.units.unit
import bioformats_jar._ome.xml.model.enums
import bioformats_jar._ome.xml.model.primitives
import typing



class IEnumerationHandler:
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class AcquisitionModeEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class ArcTypeEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class BinningEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class CompressionEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class ContrastMethodEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class CorrectionEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class DetectorTypeEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class DimensionOrderEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class ExperimentTypeEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class FilamentTypeEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class FillRuleEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class FilterTypeEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class FontFamilyEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class FontStyleEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class IlluminationTypeEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class ImmersionEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class LaserMediumEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class LaserTypeEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class MarkerEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class MediumEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class MicrobeamManipulationTypeEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class MicroscopeTypeEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class NamingConventionEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class PixelTypeEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class PulseEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...

class UnitsElectricPotentialEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    @staticmethod
    def getBaseUnit(unitsElectricPotential: bioformats_jar._ome.xml.model.enums.UnitsElectricPotential) -> bioformats_jar._ome.units.unit.Unit[bioformats_jar._ome.units.quantity.ElectricPotential]: ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    @typing.overload
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    @typing.overload
    def getEnumeration(self, electricPotential: bioformats_jar._ome.units.quantity.ElectricPotential) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    _getQuantity_0__T = typing.TypeVar('_getQuantity_0__T', bound=java.lang.Number)  # <T>
    _getQuantity_1__T = typing.TypeVar('_getQuantity_1__T', bound=ome.xml.model.primitives.PrimitiveNumber)  # <T>
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_0__T, unitsElectricPotential: bioformats_jar._ome.xml.model.enums.UnitsElectricPotential) -> bioformats_jar._ome.units.quantity.ElectricPotential: ...
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_1__T, unitsElectricPotential: bioformats_jar._ome.xml.model.enums.UnitsElectricPotential) -> bioformats_jar._ome.units.quantity.ElectricPotential: ...

class UnitsFrequencyEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    @staticmethod
    def getBaseUnit(unitsFrequency: bioformats_jar._ome.xml.model.enums.UnitsFrequency) -> bioformats_jar._ome.units.unit.Unit[bioformats_jar._ome.units.quantity.Frequency]: ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    @typing.overload
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    @typing.overload
    def getEnumeration(self, frequency: bioformats_jar._ome.units.quantity.Frequency) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    _getQuantity_0__T = typing.TypeVar('_getQuantity_0__T', bound=java.lang.Number)  # <T>
    _getQuantity_1__T = typing.TypeVar('_getQuantity_1__T', bound=ome.xml.model.primitives.PrimitiveNumber)  # <T>
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_0__T, unitsFrequency: bioformats_jar._ome.xml.model.enums.UnitsFrequency) -> bioformats_jar._ome.units.quantity.Frequency: ...
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_1__T, unitsFrequency: bioformats_jar._ome.xml.model.enums.UnitsFrequency) -> bioformats_jar._ome.units.quantity.Frequency: ...

class UnitsLengthEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    @staticmethod
    def getBaseUnit(unitsLength: bioformats_jar._ome.xml.model.enums.UnitsLength) -> bioformats_jar._ome.units.unit.Unit[bioformats_jar._ome.units.quantity.Length]: ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    @typing.overload
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    @typing.overload
    def getEnumeration(self, length: bioformats_jar._ome.units.quantity.Length) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    _getQuantity_0__T = typing.TypeVar('_getQuantity_0__T', bound=java.lang.Number)  # <T>
    _getQuantity_1__T = typing.TypeVar('_getQuantity_1__T', bound=ome.xml.model.primitives.PrimitiveNumber)  # <T>
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_0__T, unitsLength: bioformats_jar._ome.xml.model.enums.UnitsLength) -> bioformats_jar._ome.units.quantity.Length: ...
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_1__T, unitsLength: bioformats_jar._ome.xml.model.enums.UnitsLength) -> bioformats_jar._ome.units.quantity.Length: ...

class UnitsPowerEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    @staticmethod
    def getBaseUnit(unitsPower: bioformats_jar._ome.xml.model.enums.UnitsPower) -> bioformats_jar._ome.units.unit.Unit[bioformats_jar._ome.units.quantity.Power]: ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    @typing.overload
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    @typing.overload
    def getEnumeration(self, power: bioformats_jar._ome.units.quantity.Power) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    _getQuantity_0__T = typing.TypeVar('_getQuantity_0__T', bound=java.lang.Number)  # <T>
    _getQuantity_1__T = typing.TypeVar('_getQuantity_1__T', bound=ome.xml.model.primitives.PrimitiveNumber)  # <T>
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_0__T, unitsPower: bioformats_jar._ome.xml.model.enums.UnitsPower) -> bioformats_jar._ome.units.quantity.Power: ...
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_1__T, unitsPower: bioformats_jar._ome.xml.model.enums.UnitsPower) -> bioformats_jar._ome.units.quantity.Power: ...

class UnitsPressureEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    @staticmethod
    def getBaseUnit(unitsPressure: bioformats_jar._ome.xml.model.enums.UnitsPressure) -> bioformats_jar._ome.units.unit.Unit[bioformats_jar._ome.units.quantity.Pressure]: ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    @typing.overload
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    @typing.overload
    def getEnumeration(self, pressure: bioformats_jar._ome.units.quantity.Pressure) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    _getQuantity_0__T = typing.TypeVar('_getQuantity_0__T', bound=java.lang.Number)  # <T>
    _getQuantity_1__T = typing.TypeVar('_getQuantity_1__T', bound=ome.xml.model.primitives.PrimitiveNumber)  # <T>
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_0__T, unitsPressure: bioformats_jar._ome.xml.model.enums.UnitsPressure) -> bioformats_jar._ome.units.quantity.Pressure: ...
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_1__T, unitsPressure: bioformats_jar._ome.xml.model.enums.UnitsPressure) -> bioformats_jar._ome.units.quantity.Pressure: ...

class UnitsTemperatureEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    @staticmethod
    def getBaseUnit(unitsTemperature: bioformats_jar._ome.xml.model.enums.UnitsTemperature) -> bioformats_jar._ome.units.unit.Unit[bioformats_jar._ome.units.quantity.Temperature]: ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    @typing.overload
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    @typing.overload
    def getEnumeration(self, temperature: bioformats_jar._ome.units.quantity.Temperature) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    _getQuantity_0__T = typing.TypeVar('_getQuantity_0__T', bound=java.lang.Number)  # <T>
    _getQuantity_1__T = typing.TypeVar('_getQuantity_1__T', bound=ome.xml.model.primitives.PrimitiveNumber)  # <T>
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_0__T, unitsTemperature: bioformats_jar._ome.xml.model.enums.UnitsTemperature) -> bioformats_jar._ome.units.quantity.Temperature: ...
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_1__T, unitsTemperature: bioformats_jar._ome.xml.model.enums.UnitsTemperature) -> bioformats_jar._ome.units.quantity.Temperature: ...

class UnitsTimeEnumHandler(IEnumerationHandler):
    def __init__(self): ...
    @staticmethod
    def getBaseUnit(unitsTime: bioformats_jar._ome.xml.model.enums.UnitsTime) -> bioformats_jar._ome.units.unit.Unit[bioformats_jar._ome.units.quantity.Time]: ...
    def getEntity(self) -> typing.Type[bioformats_jar._ome.xml.model.enums.Enumeration]: ...
    @typing.overload
    def getEnumeration(self, string: typing.Union[java.lang.String, str]) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    @typing.overload
    def getEnumeration(self, time: bioformats_jar._ome.units.quantity.Time) -> bioformats_jar._ome.xml.model.enums.Enumeration: ...
    _getQuantity_0__T = typing.TypeVar('_getQuantity_0__T', bound=java.lang.Number)  # <T>
    _getQuantity_1__T = typing.TypeVar('_getQuantity_1__T', bound=ome.xml.model.primitives.PrimitiveNumber)  # <T>
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_0__T, unitsTime: bioformats_jar._ome.xml.model.enums.UnitsTime) -> bioformats_jar._ome.units.quantity.Time: ...
    @typing.overload
    @staticmethod
    def getQuantity(t: _getQuantity_1__T, unitsTime: bioformats_jar._ome.xml.model.enums.UnitsTime) -> bioformats_jar._ome.units.quantity.Time: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("ome.xml.model.enums.handlers")``.

    AcquisitionModeEnumHandler: typing.Type[AcquisitionModeEnumHandler]
    ArcTypeEnumHandler: typing.Type[ArcTypeEnumHandler]
    BinningEnumHandler: typing.Type[BinningEnumHandler]
    CompressionEnumHandler: typing.Type[CompressionEnumHandler]
    ContrastMethodEnumHandler: typing.Type[ContrastMethodEnumHandler]
    CorrectionEnumHandler: typing.Type[CorrectionEnumHandler]
    DetectorTypeEnumHandler: typing.Type[DetectorTypeEnumHandler]
    DimensionOrderEnumHandler: typing.Type[DimensionOrderEnumHandler]
    ExperimentTypeEnumHandler: typing.Type[ExperimentTypeEnumHandler]
    FilamentTypeEnumHandler: typing.Type[FilamentTypeEnumHandler]
    FillRuleEnumHandler: typing.Type[FillRuleEnumHandler]
    FilterTypeEnumHandler: typing.Type[FilterTypeEnumHandler]
    FontFamilyEnumHandler: typing.Type[FontFamilyEnumHandler]
    FontStyleEnumHandler: typing.Type[FontStyleEnumHandler]
    IEnumerationHandler: typing.Type[IEnumerationHandler]
    IlluminationTypeEnumHandler: typing.Type[IlluminationTypeEnumHandler]
    ImmersionEnumHandler: typing.Type[ImmersionEnumHandler]
    LaserMediumEnumHandler: typing.Type[LaserMediumEnumHandler]
    LaserTypeEnumHandler: typing.Type[LaserTypeEnumHandler]
    MarkerEnumHandler: typing.Type[MarkerEnumHandler]
    MediumEnumHandler: typing.Type[MediumEnumHandler]
    MicrobeamManipulationTypeEnumHandler: typing.Type[MicrobeamManipulationTypeEnumHandler]
    MicroscopeTypeEnumHandler: typing.Type[MicroscopeTypeEnumHandler]
    NamingConventionEnumHandler: typing.Type[NamingConventionEnumHandler]
    PixelTypeEnumHandler: typing.Type[PixelTypeEnumHandler]
    PulseEnumHandler: typing.Type[PulseEnumHandler]
    UnitsElectricPotentialEnumHandler: typing.Type[UnitsElectricPotentialEnumHandler]
    UnitsFrequencyEnumHandler: typing.Type[UnitsFrequencyEnumHandler]
    UnitsLengthEnumHandler: typing.Type[UnitsLengthEnumHandler]
    UnitsPowerEnumHandler: typing.Type[UnitsPowerEnumHandler]
    UnitsPressureEnumHandler: typing.Type[UnitsPressureEnumHandler]
    UnitsTemperatureEnumHandler: typing.Type[UnitsTemperatureEnumHandler]
    UnitsTimeEnumHandler: typing.Type[UnitsTimeEnumHandler]