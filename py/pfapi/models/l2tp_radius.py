from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="L2TPRadius")


@_attrs_define
class L2TPRadius:
    """
    Attributes:
        server (str):
        secret (str):
        enable (bool | Unset):
        accounting (bool | Unset):
        radiusissueips (bool | Unset):
    """

    server: str
    secret: str
    enable: bool | Unset = UNSET
    accounting: bool | Unset = UNSET
    radiusissueips: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server = self.server

        secret = self.secret

        enable = self.enable

        accounting = self.accounting

        radiusissueips = self.radiusissueips

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server": server,
                "secret": secret,
            }
        )
        if enable is not UNSET:
            field_dict["enable"] = enable
        if accounting is not UNSET:
            field_dict["accounting"] = accounting
        if radiusissueips is not UNSET:
            field_dict["radiusissueips"] = radiusissueips

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server = d.pop("server")

        secret = d.pop("secret")

        enable = d.pop("enable", UNSET)

        accounting = d.pop("accounting", UNSET)

        radiusissueips = d.pop("radiusissueips", UNSET)

        l2tp_radius = cls(
            server=server,
            secret=secret,
            enable=enable,
            accounting=accounting,
            radiusissueips=radiusissueips,
        )

        l2tp_radius.additional_properties = d
        return l2tp_radius

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
