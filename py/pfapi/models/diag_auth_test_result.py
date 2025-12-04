from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagAuthTestResult")


@_attrs_define
class DiagAuthTestResult:
    """
    Attributes:
        authtype (str | Unset):
        groups (list[str] | Unset):
        authenticated (bool | Unset):
    """

    authtype: str | Unset = UNSET
    groups: list[str] | Unset = UNSET
    authenticated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authtype = self.authtype

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        authenticated = self.authenticated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authtype is not UNSET:
            field_dict["authtype"] = authtype
        if groups is not UNSET:
            field_dict["groups"] = groups
        if authenticated is not UNSET:
            field_dict["authenticated"] = authenticated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authtype = d.pop("authtype", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))

        authenticated = d.pop("authenticated", UNSET)

        diag_auth_test_result = cls(
            authtype=authtype,
            groups=groups,
            authenticated=authenticated,
        )

        diag_auth_test_result.additional_properties = d
        return diag_auth_test_result

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
