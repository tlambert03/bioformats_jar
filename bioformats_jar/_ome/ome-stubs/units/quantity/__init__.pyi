import _jpype
import java.lang
import bioformats_jar._ome.units.unit
import typing



class Quantity:
    def __init__(self): ...
    def unit(self) -> bioformats_jar._ome.units.unit.Unit['Quantity']: ...
    def value(self) -> java.lang.Number: ...

class Angle(Quantity, java.lang.Comparable['Angle']):
    def __init__(self, number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], unit: bioformats_jar._ome.units.unit.Unit['Angle']): ...
    def compareTo(self, angle: 'Angle') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def unit(self) -> bioformats_jar._ome.units.unit.Unit['Angle']: ...
    @typing.overload
    def value(self) -> java.lang.Number: ...
    @typing.overload
    def value(self, unit: bioformats_jar._ome.units.unit.Unit['Angle']) -> java.lang.Number: ...

class ElectricPotential(Quantity, java.lang.Comparable['ElectricPotential']):
    def __init__(self, number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], unit: bioformats_jar._ome.units.unit.Unit['ElectricPotential']): ...
    def compareTo(self, electricPotential: 'ElectricPotential') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def unit(self) -> bioformats_jar._ome.units.unit.Unit['ElectricPotential']: ...
    @typing.overload
    def value(self) -> java.lang.Number: ...
    @typing.overload
    def value(self, unit: bioformats_jar._ome.units.unit.Unit['ElectricPotential']) -> java.lang.Number: ...

class Frequency(Quantity, java.lang.Comparable['Frequency']):
    def __init__(self, number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], unit: bioformats_jar._ome.units.unit.Unit['Frequency']): ...
    def compareTo(self, frequency: 'Frequency') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def unit(self) -> bioformats_jar._ome.units.unit.Unit['Frequency']: ...
    @typing.overload
    def value(self) -> java.lang.Number: ...
    @typing.overload
    def value(self, unit: bioformats_jar._ome.units.unit.Unit['Frequency']) -> java.lang.Number: ...

class Length(Quantity, java.lang.Comparable['Length']):
    def __init__(self, number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], unit: bioformats_jar._ome.units.unit.Unit['Length']): ...
    def compareTo(self, length: 'Length') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def unit(self) -> bioformats_jar._ome.units.unit.Unit['Length']: ...
    @typing.overload
    def value(self) -> java.lang.Number: ...
    @typing.overload
    def value(self, unit: bioformats_jar._ome.units.unit.Unit['Length']) -> java.lang.Number: ...

class Power(Quantity, java.lang.Comparable['Power']):
    def __init__(self, number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], unit: bioformats_jar._ome.units.unit.Unit['Power']): ...
    def compareTo(self, power: 'Power') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def unit(self) -> bioformats_jar._ome.units.unit.Unit['Power']: ...
    @typing.overload
    def value(self) -> java.lang.Number: ...
    @typing.overload
    def value(self, unit: bioformats_jar._ome.units.unit.Unit['Power']) -> java.lang.Number: ...

class Pressure(Quantity, java.lang.Comparable['Pressure']):
    def __init__(self, number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], unit: bioformats_jar._ome.units.unit.Unit['Pressure']): ...
    def compareTo(self, pressure: 'Pressure') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def unit(self) -> bioformats_jar._ome.units.unit.Unit['Pressure']: ...
    @typing.overload
    def value(self) -> java.lang.Number: ...
    @typing.overload
    def value(self, unit: bioformats_jar._ome.units.unit.Unit['Pressure']) -> java.lang.Number: ...

class Temperature(Quantity, java.lang.Comparable['Temperature']):
    def __init__(self, number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], unit: bioformats_jar._ome.units.unit.Unit['Temperature']): ...
    def compareTo(self, temperature: 'Temperature') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def unit(self) -> bioformats_jar._ome.units.unit.Unit['Temperature']: ...
    @typing.overload
    def value(self) -> java.lang.Number: ...
    @typing.overload
    def value(self, unit: bioformats_jar._ome.units.unit.Unit['Temperature']) -> java.lang.Number: ...

class Time(Quantity, java.lang.Comparable['Time']):
    def __init__(self, number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], unit: bioformats_jar._ome.units.unit.Unit['Time']): ...
    def compareTo(self, time: 'Time') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def unit(self) -> bioformats_jar._ome.units.unit.Unit['Time']: ...
    @typing.overload
    def value(self) -> java.lang.Number: ...
    @typing.overload
    def value(self, unit: bioformats_jar._ome.units.unit.Unit['Time']) -> java.lang.Number: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("ome.units.quantity")``.

    Angle: typing.Type[Angle]
    ElectricPotential: typing.Type[ElectricPotential]
    Frequency: typing.Type[Frequency]
    Length: typing.Type[Length]
    Power: typing.Type[Power]
    Pressure: typing.Type[Pressure]
    Quantity: typing.Type[Quantity]
    Temperature: typing.Type[Temperature]
    Time: typing.Type[Time]