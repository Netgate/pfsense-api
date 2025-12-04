from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptiveAllowedIP")


@_attrs_define
class CaptiveAllowedIP:
    """
    Attributes:
        ip (str):
        sn (str | Unset):
        descr (str | Unset):
        dir_ (str | Unset):
        bw_up (str | Unset):
        bw_down (str | Unset):
    """

    ip: str
    sn: str | Unset = UNSET
    descr: str | Unset = UNSET
    dir_: str | Unset = UNSET
    bw_up: str | Unset = UNSET
    bw_down: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip = self.ip

        sn = self.sn

        descr = self.descr

        dir_ = self.dir_

        bw_up = self.bw_up

        bw_down = self.bw_down

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip": ip,
            }
        )
        if sn is not UNSET:
            field_dict["sn"] = sn
        if descr is not UNSET:
            field_dict["descr"] = descr
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if bw_up is not UNSET:
            field_dict["bw_up"] = bw_up
        if bw_down is not UNSET:
            field_dict["bw_down"] = bw_down

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ip = d.pop("ip")

        sn = d.pop("sn", UNSET)

        descr = d.pop("descr", UNSET)

        dir_ = d.pop("dir", UNSET)

        bw_up = d.pop("bw_up", UNSET)

        bw_down = d.pop("bw_down", UNSET)

        captive_allowed_ip = cls(
            ip=ip,
            sn=sn,
            descr=descr,
            dir_=dir_,
            bw_up=bw_up,
            bw_down=bw_down,
        )

        captive_allowed_ip.additional_properties = d
        return captive_allowed_ip

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
