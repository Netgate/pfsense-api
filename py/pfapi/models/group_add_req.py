from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupAddReq")


@_attrs_define
class GroupAddReq:
    """
    Attributes:
        name (str):
        scope (str):
        description (str | Unset):
        gid (int | Unset):
        members (list[int] | Unset):
        privs (list[str] | Unset):
    """

    name: str
    scope: str
    description: str | Unset = UNSET
    gid: int | Unset = UNSET
    members: list[int] | Unset = UNSET
    privs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scope = self.scope

        description = self.description

        gid = self.gid

        members: list[int] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        privs: list[str] | Unset = UNSET
        if not isinstance(self.privs, Unset):
            privs = self.privs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "scope": scope,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
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
        name = d.pop("name")

        scope = d.pop("scope")

        description = d.pop("description", UNSET)

        gid = d.pop("gid", UNSET)

        members = cast(list[int], d.pop("members", UNSET))

        privs = cast(list[str], d.pop("privs", UNSET))

        group_add_req = cls(
            name=name,
            scope=scope,
            description=description,
            gid=gid,
            members=members,
            privs=privs,
        )

        group_add_req.additional_properties = d
        return group_add_req

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
