import java.lang
import bioformats_jar._ome.units.quantity
import bioformats_jar._ome.units.unit
import typing



class UNITS:
    RADIAN: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    VOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    METRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    INCH: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    WATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KELVIN: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    SECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTAHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTAHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXAHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETAHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERAHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGAHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGAHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KILOHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HECTOHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECAHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECIHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CENTIHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MILLIHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NANOHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PICOHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FEMTOHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ATTOHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZEPTOHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOCTOHERTZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTAHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTAHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXAHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETAHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERAHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGAHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGAHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DAHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    AHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YHZ: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTAMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTAMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXAMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETAMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERAMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGAMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGAMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KILOMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HECTOMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECAMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECIMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CENTIMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MILLIMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NANOMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PICOMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FEMTOMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ATTOMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZEPTOMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOCTOMETRE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTAMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTAMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXAMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETAMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERAMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGAMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGAMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KILOMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HECTOMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECAMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    METER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECIMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CENTIMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MILLIMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NANOMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PICOMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FEMTOMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ATTOMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZEPTOMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOCTOMETER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ANGSTROM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    THOU: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    LINE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FOOT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YARD: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MILE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ASTRONOMICALUNIT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    LIGHTYEAR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PARSEC: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    POINT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PIXEL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    REFERENCEFRAME: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTAM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTAM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXAM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETAM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERAM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGAM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGAM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DAM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    M: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    AM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    LI: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    IN: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YD: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MI: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    UA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    LY: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PC: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTAWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTAWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXAWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETAWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERAWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGAWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGAWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KILOWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HECTOWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECAWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECIWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CENTIWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MILLIWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NANOWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PICOWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FEMTOWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ATTOWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZEPTOWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOCTOWATT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTAW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTAW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXAW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETAW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERAW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGAW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGAW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DAW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    W: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    AW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YW: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTAPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTAPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXAPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETAPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERAPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGAPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGAPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KILOPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HECTOPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECAPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECIPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CENTIPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MILLIPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NANOPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PICOPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FEMTOPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ATTOPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZEPTOPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOCTOPASCAL: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    BAR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGABAR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KILOBAR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECIBAR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CENTIBAR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MILLIBAR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ATMOSPHERE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PSI: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TORR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MILLITORR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MMHG: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTAPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTAPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXAPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETAPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERAPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGAPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGAPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DAPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    APA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YPA: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KBAR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DBAR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CBAR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MBAR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ATM: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MTORR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CELSIUS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    RANKINE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FAHRENHEIT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DEGREEC: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    K: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DEGREER: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DEGREEF: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTASECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTASECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXASECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETASECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERASECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGASECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGASECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KILOSECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HECTOSECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECASECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECISECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CENTISECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MILLISECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROSECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NANOSECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PICOSECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FEMTOSECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ATTOSECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZEPTOSECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOCTOSECOND: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MINUTE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HOUR: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DAY: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTAS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTAS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXAS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETAS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERAS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGAS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGAS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DAS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    S: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    AS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YS: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MIN: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    H: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    D: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTAVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTAVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXAVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETAVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERAVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGAVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGAVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KILOVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HECTOVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECAVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DECIVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CENTIVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MILLIVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NANOVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PICOVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FEMTOVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ATTOVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZEPTOVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOCTOVOLT: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YOTTAV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZETTAV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    EXAV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PETAV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    TERAV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GIGAV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MEGAV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    KV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    HV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DAV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    V: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    CV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    MICROV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    NV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    PV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    FV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    AV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    ZV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    YV: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DEGREE: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GRADIAN: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    DEG: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    RAD: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    GON: typing.ClassVar[bioformats_jar._ome.units.unit.Unit] = ...
    def __init__(self): ...
    _ATTO__T = typing.TypeVar('_ATTO__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def ATTO(unit: bioformats_jar._ome.units.unit.Unit[_ATTO__T]) -> bioformats_jar._ome.units.unit.Unit[_ATTO__T]: ...
    _CENTI__T = typing.TypeVar('_CENTI__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def CENTI(unit: bioformats_jar._ome.units.unit.Unit[_CENTI__T]) -> bioformats_jar._ome.units.unit.Unit[_CENTI__T]: ...
    _DECA__T = typing.TypeVar('_DECA__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def DECA(unit: bioformats_jar._ome.units.unit.Unit[_DECA__T]) -> bioformats_jar._ome.units.unit.Unit[_DECA__T]: ...
    _DECI__T = typing.TypeVar('_DECI__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def DECI(unit: bioformats_jar._ome.units.unit.Unit[_DECI__T]) -> bioformats_jar._ome.units.unit.Unit[_DECI__T]: ...
    _EXA__T = typing.TypeVar('_EXA__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def EXA(unit: bioformats_jar._ome.units.unit.Unit[_EXA__T]) -> bioformats_jar._ome.units.unit.Unit[_EXA__T]: ...
    _FEMTO__T = typing.TypeVar('_FEMTO__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def FEMTO(unit: bioformats_jar._ome.units.unit.Unit[_FEMTO__T]) -> bioformats_jar._ome.units.unit.Unit[_FEMTO__T]: ...
    _GIGA__T = typing.TypeVar('_GIGA__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def GIGA(unit: bioformats_jar._ome.units.unit.Unit[_GIGA__T]) -> bioformats_jar._ome.units.unit.Unit[_GIGA__T]: ...
    _HECTO__T = typing.TypeVar('_HECTO__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def HECTO(unit: bioformats_jar._ome.units.unit.Unit[_HECTO__T]) -> bioformats_jar._ome.units.unit.Unit[_HECTO__T]: ...
    _KILO__T = typing.TypeVar('_KILO__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def KILO(unit: bioformats_jar._ome.units.unit.Unit[_KILO__T]) -> bioformats_jar._ome.units.unit.Unit[_KILO__T]: ...
    _MEGA__T = typing.TypeVar('_MEGA__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def MEGA(unit: bioformats_jar._ome.units.unit.Unit[_MEGA__T]) -> bioformats_jar._ome.units.unit.Unit[_MEGA__T]: ...
    _MICRO__T = typing.TypeVar('_MICRO__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def MICRO(unit: bioformats_jar._ome.units.unit.Unit[_MICRO__T]) -> bioformats_jar._ome.units.unit.Unit[_MICRO__T]: ...
    _MILLI__T = typing.TypeVar('_MILLI__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def MILLI(unit: bioformats_jar._ome.units.unit.Unit[_MILLI__T]) -> bioformats_jar._ome.units.unit.Unit[_MILLI__T]: ...
    _NANO__T = typing.TypeVar('_NANO__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def NANO(unit: bioformats_jar._ome.units.unit.Unit[_NANO__T]) -> bioformats_jar._ome.units.unit.Unit[_NANO__T]: ...
    _PETA__T = typing.TypeVar('_PETA__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def PETA(unit: bioformats_jar._ome.units.unit.Unit[_PETA__T]) -> bioformats_jar._ome.units.unit.Unit[_PETA__T]: ...
    _PICO__T = typing.TypeVar('_PICO__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def PICO(unit: bioformats_jar._ome.units.unit.Unit[_PICO__T]) -> bioformats_jar._ome.units.unit.Unit[_PICO__T]: ...
    _TERA__T = typing.TypeVar('_TERA__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def TERA(unit: bioformats_jar._ome.units.unit.Unit[_TERA__T]) -> bioformats_jar._ome.units.unit.Unit[_TERA__T]: ...
    _YOCTO__T = typing.TypeVar('_YOCTO__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def YOCTO(unit: bioformats_jar._ome.units.unit.Unit[_YOCTO__T]) -> bioformats_jar._ome.units.unit.Unit[_YOCTO__T]: ...
    _YOTTA__T = typing.TypeVar('_YOTTA__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def YOTTA(unit: bioformats_jar._ome.units.unit.Unit[_YOTTA__T]) -> bioformats_jar._ome.units.unit.Unit[_YOTTA__T]: ...
    _ZEPTO__T = typing.TypeVar('_ZEPTO__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def ZEPTO(unit: bioformats_jar._ome.units.unit.Unit[_ZEPTO__T]) -> bioformats_jar._ome.units.unit.Unit[_ZEPTO__T]: ...
    _ZETTA__T = typing.TypeVar('_ZETTA__T', bound=ome.units.quantity.Quantity)  # <T>
    @staticmethod
    def ZETTA(unit: bioformats_jar._ome.units.unit.Unit[_ZETTA__T]) -> bioformats_jar._ome.units.unit.Unit[_ZETTA__T]: ...
    def getName(self) -> java.lang.String: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("ome.units")``.

    UNITS: typing.Type[UNITS]
    quantity: bioformats_jar._ome.units.quantity.__module_protocol__
    unit: bioformats_jar._ome.units.unit.__module_protocol__