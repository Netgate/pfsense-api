from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserGroup")


@_attrs_define
class UserGroup:
    """
    Attributes:
        name (str | Unset):
        description (str | Unset):
        scope (str | Unset):
        gid (int | Unset):
        members (list[int] | Unset):
        privs (list[str] | Unset):
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    scope: str | Unset = UNSET
    gid: int | Unset = UNSET
    members: list[int] | Unset = UNSET
    privs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        scope = self.scope

        gid = self.gid

        members: list[int] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        privs: list[str] | Unset = UNSET
        if not isinstance(self.privs, Unset):
            privs = self.privs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if scope is not UNSET:
            field_dict["scope"] = scope
        if gid is not UNSET:
            field_dict["gid"] = gid
        if members is not UNSET:
            field_dict["members"] = members
        if privs is not UNSET:
            field_dict["privs"] = privs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        scope = d.pop("scope", UNSET)

        gid = d.pop("gid", UNSET)

        members = cast(list[int], d.pop("members", UNSET))

        privs = cast(list[str], d.pop("privs", UNSET))

        user_group = cls(
            name=name,
            description=description,
            scope=scope,
            gid=gid,
            members=members,
            privs=privs,
        )

        user_group.additional_properties = d
        return user_group

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
