from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagAuthTestRequest")


@_attrs_define
class DiagAuthTestRequest:
    """
    Attributes:
        authserver (str | Unset):
        username (str | Unset):
        password (str | Unset):
        debug (bool | Unset):
    """

    authserver: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    debug: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authserver = self.authserver

        username = self.username

        password = self.password

        debug = self.debug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authserver is not UNSET:
            field_dict["authserver"] = authserver
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authserver = d.pop("authserver", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        debug = d.pop("debug", UNSET)

        diag_auth_test_request = cls(
            authserver=authserver,
            username=username,
            password=password,
            debug=debug,
        )

        diag_auth_test_request.additional_properties = d
        return diag_auth_test_request

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
