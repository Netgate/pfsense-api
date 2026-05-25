from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyServerStat")


@_attrs_define
class HaproxyServerStat:
    """
    Attributes:
        pxname (str | Unset): Parent backend name
        svname (str | Unset): Server name
        status (str | Unset): Server status
        scur (int | Unset): Current sessions
    """

    pxname: str | Unset = UNSET
    svname: str | Unset = UNSET
    status: str | Unset = UNSET
    scur: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pxname = self.pxname

        svname = self.svname

        status = self.status

        scur = self.scur

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pxname is not UNSET:
            field_dict["pxname"] = pxname
        if svname is not UNSET:
            field_dict["svname"] = svname
        if status is not UNSET:
            field_dict["status"] = status
        if scur is not UNSET:
            field_dict["scur"] = scur

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pxname = d.pop("pxname", UNSET)

        svname = d.pop("svname", UNSET)

        status = d.pop("status", UNSET)

        scur = d.pop("scur", UNSET)

        haproxy_server_stat = cls(
            pxname=pxname,
            svname=svname,
            status=status,
            scur=scur,
        )

        haproxy_server_stat.additional_properties = d
        return haproxy_server_stat

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
