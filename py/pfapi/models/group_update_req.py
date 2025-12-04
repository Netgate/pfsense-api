from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupUpdateReq")


@_attrs_define
class GroupUpdateReq:
    """
    Attributes:
        description (str | Unset):
        scope (str | Unset): local or remote (if non-system)
        gid (int | Unset):
        members (list[int] | Unset):
        remove_members (list[int] | Unset):
        privs (list[str] | Unset):
    """

    description: str | Unset = UNSET
    scope: str | Unset = UNSET
    gid: int | Unset = UNSET
    members: list[int] | Unset = UNSET
    remove_members: list[int] | Unset = UNSET
    privs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        scope = self.scope

        gid = self.gid

        members: list[int] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        remove_members: list[int] | Unset = UNSET
        if not isinstance(self.remove_members, Unset):
            remove_members = self.remove_members

        privs: list[str] | Unset = UNSET
        if not isinstance(self.privs, Unset):
            privs = self.privs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if scope is not UNSET:
            field_dict["scope"] = scope
        if gid is not UNSET:
            field_dict["gid"] = gid
        if members is not UNSET:
            field_dict["members"] = members
        if remove_members is not UNSET:
            field_dict["remove_members"] = remove_members
        if privs is not UNSET:
            field_dict["privs"] = privs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        scope = d.pop("scope", UNSET)

        gid = d.pop("gid", UNSET)

        members = cast(list[int], d.pop("members", UNSET))

        remove_members = cast(list[int], d.pop("remove_members", UNSET))

        privs = cast(list[str], d.pop("privs", UNSET))

        group_update_req = cls(
            description=description,
            scope=scope,
            gid=gid,
            members=members,
            remove_members=remove_members,
            privs=privs,
        )

        group_update_req.additional_properties = d
        return group_update_req

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
