from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_generic import UserGeneric
    from ..models.user_group import UserGroup


T = TypeVar("T", bound="UsersConfigGeneric")


@_attrs_define
class UsersConfigGeneric:
    """Generic user for all platforms

    Attributes:
        users (list[UserGeneric] | Unset):
        groups (list[UserGroup] | Unset):
    """

    users: list[UserGeneric] | Unset = UNSET
    groups: list[UserGroup] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_generic import UserGeneric
        from ..models.user_group import UserGroup

        d = dict(src_dict)
        _users = d.pop("users", UNSET)
        users: list[UserGeneric] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = UserGeneric.from_dict(users_item_data)

                users.append(users_item)

        _groups = d.pop("groups", UNSET)
        groups: list[UserGroup] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = UserGroup.from_dict(groups_item_data)

                groups.append(groups_item)

        users_config_generic = cls(
            users=users,
            groups=groups,
        )

        users_config_generic.additional_properties = d
        return users_config_generic

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
