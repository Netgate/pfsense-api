from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminLoginSession")


@_attrs_define
class AdminLoginSession:
    """
    Attributes:
        identity (str | Unset): username@address
        at (int | Unset): millisecond timestamp when login started
        at_str (str | Unset): timestamp in RFC 3339 format
    """

    identity: str | Unset = UNSET
    at: int | Unset = UNSET
    at_str: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identity = self.identity

        at = self.at

        at_str = self.at_str

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identity is not UNSET:
            field_dict["identity"] = identity
        if at is not UNSET:
            field_dict["at"] = at
        if at_str is not UNSET:
            field_dict["at_str"] = at_str

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity = d.pop("identity", UNSET)

        at = d.pop("at", UNSET)

        at_str = d.pop("at_str", UNSET)

        admin_login_session = cls(
            identity=identity,
            at=at,
            at_str=at_str,
        )

        admin_login_session.additional_properties = d
        return admin_login_session

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
