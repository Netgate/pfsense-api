from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coredns_configuration_groups import CorednsConfigurationGroups
    from ..models.rexdns_group import RexdnsGroup


T = TypeVar("T", bound="CorednsConfiguration")


@_attrs_define
class CorednsConfiguration:
    """
    Attributes:
        enabled (bool | Unset):
        high_security (bool | Unset):
        listen_port (str | Unset): PORT
        global_ruleset (RexdnsGroup | Unset):
        groups (CorednsConfigurationGroups | Unset):
    """

    enabled: bool | Unset = UNSET
    high_security: bool | Unset = UNSET
    listen_port: str | Unset = UNSET
    global_ruleset: RexdnsGroup | Unset = UNSET
    groups: CorednsConfigurationGroups | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        high_security = self.high_security

        listen_port = self.listen_port

        global_ruleset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_ruleset, Unset):
            global_ruleset = self.global_ruleset.to_dict()

        groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if high_security is not UNSET:
            field_dict["high_security"] = high_security
        if listen_port is not UNSET:
            field_dict["listen_port"] = listen_port
        if global_ruleset is not UNSET:
            field_dict["global_ruleset"] = global_ruleset
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coredns_configuration_groups import CorednsConfigurationGroups
        from ..models.rexdns_group import RexdnsGroup

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        high_security = d.pop("high_security", UNSET)

        listen_port = d.pop("listen_port", UNSET)

        _global_ruleset = d.pop("global_ruleset", UNSET)
        global_ruleset: RexdnsGroup | Unset
        if isinstance(_global_ruleset, Unset):
            global_ruleset = UNSET
        else:
            global_ruleset = RexdnsGroup.from_dict(_global_ruleset)

        _groups = d.pop("groups", UNSET)
        groups: CorednsConfigurationGroups | Unset
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = CorednsConfigurationGroups.from_dict(_groups)

        coredns_configuration = cls(
            enabled=enabled,
            high_security=high_security,
            listen_port=listen_port,
            global_ruleset=global_ruleset,
            groups=groups,
        )

        coredns_configuration.additional_properties = d
        return coredns_configuration

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
