from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ntp_gps_flags import NtpGpsFlags


T = TypeVar("T", bound="NtpSerialGps")


@_attrs_define
class NtpSerialGps:
    """
    Attributes:
        type (str):
        port (str):
        speed (str):
        autobaudinit (bool):
        nmea (int):
        fudge1 (float):
        fudge2 (float):
        stratum (int):
        gpsminpoll (str):
        gpsmaxpoll (str):
        ntp_gps_flags (NtpGpsFlags):
        refid (str):
        initcmd (str):
        autocorrect_initcmd (bool):
    """

    type: str
    port: str
    speed: str
    autobaudinit: bool
    nmea: int
    fudge1: float
    fudge2: float
    stratum: int
    gpsminpoll: str
    gpsmaxpoll: str
    ntp_gps_flags: "NtpGpsFlags"
    refid: str
    initcmd: str
    autocorrect_initcmd: bool
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

        ntp_gps_flags = self.ntp_gps_flags.to_dict()

        refid = self.refid

        initcmd = self.initcmd

        autocorrect_initcmd = self.autocorrect_initcmd

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "port": port,
                "speed": speed,
                "autobaudinit": autobaudinit,
                "nmea": nmea,
                "fudge1": fudge1,
                "fudge2": fudge2,
                "stratum": stratum,
                "gpsminpoll": gpsminpoll,
                "gpsmaxpoll": gpsmaxpoll,
                "ntp_gps_flags": ntp_gps_flags,
                "refid": refid,
                "initcmd": initcmd,
                "autocorrect_initcmd": autocorrect_initcmd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ntp_gps_flags import NtpGpsFlags

        d = src_dict.copy()
        type = d.pop("type")

        port = d.pop("port")

        speed = d.pop("speed")

        autobaudinit = d.pop("autobaudinit")

        nmea = d.pop("nmea")

        fudge1 = d.pop("fudge1")

        fudge2 = d.pop("fudge2")

        stratum = d.pop("stratum")

        gpsminpoll = d.pop("gpsminpoll")

        gpsmaxpoll = d.pop("gpsmaxpoll")

        ntp_gps_flags = NtpGpsFlags.from_dict(d.pop("ntp_gps_flags"))

        refid = d.pop("refid")

        initcmd = d.pop("initcmd")

        autocorrect_initcmd = d.pop("autocorrect_initcmd")

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
