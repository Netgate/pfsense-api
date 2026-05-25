from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyFrontendStat")


@_attrs_define
class HaproxyFrontendStat:
    """
    Attributes:
        pxname (str | Unset): Frontend proxy name
        status (str | Unset): Frontend status
        scur (int | Unset): Current sessions
        slim (int | Unset): Session limit
    """

    pxname: str | Unset = UNSET
    status: str | Unset = UNSET
    scur: int | Unset = UNSET
    slim: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pxname = self.pxname

        status = self.status

        scur = self.scur

        slim = self.slim

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pxname is not UNSET:
            field_dict["pxname"] = pxname
        if status is not UNSET:
            field_dict["status"] = status
        if scur is not UNSET:
            field_dict["scur"] = scur
        if slim is not UNSET:
            field_dict["slim"] = slim

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pxname = d.pop("pxname", UNSET)

        status = d.pop("status", UNSET)

        scur = d.pop("scur", UNSET)

        slim = d.pop("slim", UNSET)

        haproxy_frontend_stat = cls(
            pxname=pxname,
            status=status,
            scur=scur,
            slim=slim,
        )

        haproxy_frontend_stat.additional_properties = d
        return haproxy_frontend_stat

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
