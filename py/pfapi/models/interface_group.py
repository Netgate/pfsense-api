from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceGroup")


@_attrs_define
class InterfaceGroup:
    """
    Attributes:
        members (list[str] | Unset):
        descr (str | Unset):
        ifname (str | Unset): interface group name
    """

    members: list[str] | Unset = UNSET
    descr: str | Unset = UNSET
    ifname: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        members: list[str] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        descr = self.descr

        ifname = self.ifname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if members is not UNSET:
            field_dict["members"] = members
        if descr is not UNSET:
            field_dict["descr"] = descr
        if ifname is not UNSET:
            field_dict["ifname"] = ifname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        members = cast(list[str], d.pop("members", UNSET))

        descr = d.pop("descr", UNSET)

        ifname = d.pop("ifname", UNSET)

        interface_group = cls(
            members=members,
            descr=descr,
            ifname=ifname,
        )

        interface_group.additional_properties = d
        return interface_group

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
