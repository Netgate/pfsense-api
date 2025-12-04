from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagAuthServerList")


@_attrs_define
class DiagAuthServerList:
    """
    Attributes:
        servers (list[str] | Unset):
        authtype (str | Unset):
    """

    servers: list[str] | Unset = UNSET
    authtype: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        servers: list[str] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = self.servers

        authtype = self.authtype

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if servers is not UNSET:
            field_dict["servers"] = servers
        if authtype is not UNSET:
            field_dict["authtype"] = authtype

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        servers = cast(list[str], d.pop("servers", UNSET))

        authtype = d.pop("authtype", UNSET)

        diag_auth_server_list = cls(
            servers=servers,
            authtype=authtype,
        )

        diag_auth_server_list.additional_properties = d
        return diag_auth_server_list

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
