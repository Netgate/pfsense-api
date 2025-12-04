from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteRecord")


@_attrs_define
class RouteRecord:
    """
    Attributes:
        dest (str | Unset):
        gw (str | Unset):
        flags (str | Unset):
        uses (str | Unset):
        mtu (str | Unset):
        interface (str | Unset):
        exp (str | Unset):
    """

    dest: str | Unset = UNSET
    gw: str | Unset = UNSET
    flags: str | Unset = UNSET
    uses: str | Unset = UNSET
    mtu: str | Unset = UNSET
    interface: str | Unset = UNSET
    exp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dest = self.dest

        gw = self.gw

        flags = self.flags

        uses = self.uses

        mtu = self.mtu

        interface = self.interface

        exp = self.exp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dest is not UNSET:
            field_dict["dest"] = dest
        if gw is not UNSET:
            field_dict["gw"] = gw
        if flags is not UNSET:
            field_dict["flags"] = flags
        if uses is not UNSET:
            field_dict["uses"] = uses
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if interface is not UNSET:
            field_dict["interface"] = interface
        if exp is not UNSET:
            field_dict["exp"] = exp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dest = d.pop("dest", UNSET)

        gw = d.pop("gw", UNSET)

        flags = d.pop("flags", UNSET)

        uses = d.pop("uses", UNSET)

        mtu = d.pop("mtu", UNSET)

        interface = d.pop("interface", UNSET)

        exp = d.pop("exp", UNSET)

        route_record = cls(
            dest=dest,
            gw=gw,
            flags=flags,
            uses=uses,
            mtu=mtu,
            interface=interface,
            exp=exp,
        )

        route_record.additional_properties = d
        return route_record

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
