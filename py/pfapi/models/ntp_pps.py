from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ntp_pps_flags import NtpPpsFlags


T = TypeVar("T", bound="NtpPps")


@_attrs_define
class NtpPps:
    """
    Attributes:
        port (str):
        fudge1 (float):
        stratum (int):
        ppsminpoll (str):
        ppsmaxpoll (str):
        pps_flags (NtpPpsFlags):
        refid (str):
    """

    port: str
    fudge1: float
    stratum: int
    ppsminpoll: str
    ppsmaxpoll: str
    pps_flags: "NtpPpsFlags"
    refid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        port = self.port

        fudge1 = self.fudge1

        stratum = self.stratum

        ppsminpoll = self.ppsminpoll

        ppsmaxpoll = self.ppsmaxpoll

        pps_flags = self.pps_flags.to_dict()

        refid = self.refid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
                "fudge1": fudge1,
                "stratum": stratum,
                "ppsminpoll": ppsminpoll,
                "ppsmaxpoll": ppsmaxpoll,
                "pps_flags": pps_flags,
                "refid": refid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ntp_pps_flags import NtpPpsFlags

        d = src_dict.copy()
        port = d.pop("port")

        fudge1 = d.pop("fudge1")

        stratum = d.pop("stratum")

        ppsminpoll = d.pop("ppsminpoll")

        ppsmaxpoll = d.pop("ppsmaxpoll")

        pps_flags = NtpPpsFlags.from_dict(d.pop("pps_flags"))

        refid = d.pop("refid")

        ntp_pps = cls(
            port=port,
            fudge1=fudge1,
            stratum=stratum,
            ppsminpoll=ppsminpoll,
            ppsmaxpoll=ppsmaxpoll,
            pps_flags=pps_flags,
            refid=refid,
        )

        ntp_pps.additional_properties = d
        return ntp_pps

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
