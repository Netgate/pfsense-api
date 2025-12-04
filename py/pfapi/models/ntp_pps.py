from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ntp_pps_flags import NtpPpsFlags


T = TypeVar("T", bound="NtpPps")


@_attrs_define
class NtpPps:
    """
    Attributes:
        port (str):
        fudge1 (float | Unset):
        stratum (int | Unset): 0-16
        ppsminpoll (str | Unset): Empty for default, "omit" or number ranged from 3 to 17 based on pfsense specific
            approach
        ppsmaxpoll (str | Unset): Empty for default, "omit" or number ranged from 3 to 17 based on pfsense specific
            approach
        pps_flags (NtpPpsFlags | Unset):
        refid (str | Unset):
    """

    port: str
    fudge1: float | Unset = UNSET
    stratum: int | Unset = UNSET
    ppsminpoll: str | Unset = UNSET
    ppsmaxpoll: str | Unset = UNSET
    pps_flags: NtpPpsFlags | Unset = UNSET
    refid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        fudge1 = self.fudge1

        stratum = self.stratum

        ppsminpoll = self.ppsminpoll

        ppsmaxpoll = self.ppsmaxpoll

        pps_flags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pps_flags, Unset):
            pps_flags = self.pps_flags.to_dict()

        refid = self.refid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
            }
        )
        if fudge1 is not UNSET:
            field_dict["fudge1"] = fudge1
        if stratum is not UNSET:
            field_dict["stratum"] = stratum
        if ppsminpoll is not UNSET:
            field_dict["ppsminpoll"] = ppsminpoll
        if ppsmaxpoll is not UNSET:
            field_dict["ppsmaxpoll"] = ppsmaxpoll
        if pps_flags is not UNSET:
            field_dict["pps_flags"] = pps_flags
        if refid is not UNSET:
            field_dict["refid"] = refid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ntp_pps_flags import NtpPpsFlags

        d = dict(src_dict)
        port = d.pop("port")

        fudge1 = d.pop("fudge1", UNSET)

        stratum = d.pop("stratum", UNSET)

        ppsminpoll = d.pop("ppsminpoll", UNSET)

        ppsmaxpoll = d.pop("ppsmaxpoll", UNSET)

        _pps_flags = d.pop("pps_flags", UNSET)
        pps_flags: NtpPpsFlags | Unset
        if isinstance(_pps_flags, Unset):
            pps_flags = UNSET
        else:
            pps_flags = NtpPpsFlags.from_dict(_pps_flags)

        refid = d.pop("refid", UNSET)

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
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
