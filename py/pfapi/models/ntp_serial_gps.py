from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ntp_gps_flags import NtpGpsFlags


T = TypeVar("T", bound="NtpSerialGps")


@_attrs_define
class NtpSerialGps:
    """
    Attributes:
        type (Union[Unset, str]): Default | Custom | Generic | Garmin | MediaTek | SiRF | U-Blox | SureGPS
        port (Union[Unset, str]):
        speed (Union[Unset, str]):
        autobaudinit (Union[Unset, bool]):
        nmea (Union[Unset, int]): 0 | 1 | 2 | 4 | 8 or sum of them if multi selected
        fudge1 (Union[Unset, float]):
        fudge2 (Union[Unset, float]):
        stratum (Union[Unset, int]): 0-16
        gpsminpoll (Union[Unset, str]): Empty for default, "omit" or number ranged from 3 to 17 based on pfsense
            specific approach
        gpsmaxpoll (Union[Unset, str]): Empty for default, "omit" or number ranged from 3 to 17 based on pfsense
            specific approach
        ntp_gps_flags (Union[Unset, NtpGpsFlags]):
        refid (Union[Unset, str]):
        initcmd (Union[Unset, str]):
        autocorrect_initcmd (Union[Unset, bool]):
    """

    type: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    speed: Union[Unset, str] = UNSET
    autobaudinit: Union[Unset, bool] = UNSET
    nmea: Union[Unset, int] = UNSET
    fudge1: Union[Unset, float] = UNSET
    fudge2: Union[Unset, float] = UNSET
    stratum: Union[Unset, int] = UNSET
    gpsminpoll: Union[Unset, str] = UNSET
    gpsmaxpoll: Union[Unset, str] = UNSET
    ntp_gps_flags: Union[Unset, "NtpGpsFlags"] = UNSET
    refid: Union[Unset, str] = UNSET
    initcmd: Union[Unset, str] = UNSET
    autocorrect_initcmd: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        port = self.port

        speed = self.speed

        autobaudinit = self.autobaudinit

        nmea = self.nmea

        fudge1 = self.fudge1

        fudge2 = self.fudge2

        stratum = self.stratum

        gpsminpoll = self.gpsminpoll

        gpsmaxpoll = self.gpsmaxpoll

        ntp_gps_flags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ntp_gps_flags, Unset):
            ntp_gps_flags = self.ntp_gps_flags.to_dict()

        refid = self.refid

        initcmd = self.initcmd

        autocorrect_initcmd = self.autocorrect_initcmd

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if port is not UNSET:
            field_dict["port"] = port
        if speed is not UNSET:
            field_dict["speed"] = speed
        if autobaudinit is not UNSET:
            field_dict["autobaudinit"] = autobaudinit
        if nmea is not UNSET:
            field_dict["nmea"] = nmea
        if fudge1 is not UNSET:
            field_dict["fudge1"] = fudge1
        if fudge2 is not UNSET:
            field_dict["fudge2"] = fudge2
        if stratum is not UNSET:
            field_dict["stratum"] = stratum
        if gpsminpoll is not UNSET:
            field_dict["gpsminpoll"] = gpsminpoll
        if gpsmaxpoll is not UNSET:
            field_dict["gpsmaxpoll"] = gpsmaxpoll
        if ntp_gps_flags is not UNSET:
            field_dict["ntp_gps_flags"] = ntp_gps_flags
        if refid is not UNSET:
            field_dict["refid"] = refid
        if initcmd is not UNSET:
            field_dict["initcmd"] = initcmd
        if autocorrect_initcmd is not UNSET:
            field_dict["autocorrect_initcmd"] = autocorrect_initcmd

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ntp_gps_flags import NtpGpsFlags

        d = src_dict.copy()
        type = d.pop("type", UNSET)

        port = d.pop("port", UNSET)

        speed = d.pop("speed", UNSET)

        autobaudinit = d.pop("autobaudinit", UNSET)

        nmea = d.pop("nmea", UNSET)

        fudge1 = d.pop("fudge1", UNSET)

        fudge2 = d.pop("fudge2", UNSET)

        stratum = d.pop("stratum", UNSET)

        gpsminpoll = d.pop("gpsminpoll", UNSET)

        gpsmaxpoll = d.pop("gpsmaxpoll", UNSET)

        _ntp_gps_flags = d.pop("ntp_gps_flags", UNSET)
        ntp_gps_flags: Union[Unset, NtpGpsFlags]
        if isinstance(_ntp_gps_flags, Unset):
            ntp_gps_flags = UNSET
        else:
            ntp_gps_flags = NtpGpsFlags.from_dict(_ntp_gps_flags)

        refid = d.pop("refid", UNSET)

        initcmd = d.pop("initcmd", UNSET)

        autocorrect_initcmd = d.pop("autocorrect_initcmd", UNSET)

        ntp_serial_gps = cls(
            type=type,
            port=port,
            speed=speed,
            autobaudinit=autobaudinit,
            nmea=nmea,
            fudge1=fudge1,
            fudge2=fudge2,
            stratum=stratum,
            gpsminpoll=gpsminpoll,
            gpsmaxpoll=gpsmaxpoll,
            ntp_gps_flags=ntp_gps_flags,
            refid=refid,
            initcmd=initcmd,
            autocorrect_initcmd=autocorrect_initcmd,
        )

        ntp_serial_gps.additional_properties = d
        return ntp_serial_gps

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
