from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyAcl")


@_attrs_define
class HaproxyAcl:
    """
    Attributes:
        name (str | Unset): ACL Name

            Name of the ACL condition. Referenced by actions to determine when they apply.
        expression (str | Unset): Expression Type

            Type of comparison to perform. Valid values:
            host_starts_with, host_ends_with, host_matches, host_regex, host_contains,
            path_starts_with, path_ends_with, path_matches, path_regex, path_contains, path_dir,
            url_parameter,
            ssl_sni_matches, ssl_sni_contains, ssl_sni_starts_with, ssl_sni_ends_with, ssl_sni_regex,
            ssl_c_verify_code, ssl_c_verify, ssl_c_i_dn, ssl_c_s_dn,
            source_ip, backendservercount, traffic_is_http, traffic_is_ssl,
            custom, nbsrv, nbsrv_backend
        value (str | Unset): Value

            Pattern or value to match against. Interpretation depends on expression type.
        casesensitive (bool | Unset): Case Sensitive

            Enable case-sensitive matching for this ACL.
        not_flag (bool | Unset): Negate

            Negate the ACL match condition (logical NOT).
    """

    name: str | Unset = UNSET
    expression: str | Unset = UNSET
    value: str | Unset = UNSET
    casesensitive: bool | Unset = UNSET
    not_flag: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        expression = self.expression

        value = self.value

        casesensitive = self.casesensitive

        not_flag = self.not_flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if expression is not UNSET:
            field_dict["expression"] = expression
        if value is not UNSET:
            field_dict["value"] = value
        if casesensitive is not UNSET:
            field_dict["casesensitive"] = casesensitive
        if not_flag is not UNSET:
            field_dict["not_flag"] = not_flag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        expression = d.pop("expression", UNSET)

        value = d.pop("value", UNSET)

        casesensitive = d.pop("casesensitive", UNSET)

        not_flag = d.pop("not_flag", UNSET)

        haproxy_acl = cls(
            name=name,
            expression=expression,
            value=value,
            casesensitive=casesensitive,
            not_flag=not_flag,
        )

        haproxy_acl.additional_properties = d
        return haproxy_acl

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
