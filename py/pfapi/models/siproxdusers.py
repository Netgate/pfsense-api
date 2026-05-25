from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Siproxdusers")


@_attrs_define
class Siproxdusers:
    """
    Attributes:
        username (str | Unset): Username

            Enter the username here.
        password (str | Unset): Password

            Enter the password here.
        description (str | Unset): Username Description

            Enter the description of the user here.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    username: str | Unset = UNSET
    password: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        description = self.description

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        siproxdusers = cls(
            username=username,
            password=password,
            description=description,
            id=id,
        )

        siproxdusers.additional_properties = d
        return siproxdusers

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
