from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_firewall_interfaces_interface_mappings import FWFirewallInterfacesInterfaceMappings
    from ..models.fw_firewall_interfaces_traffic_sources import FWFirewallInterfacesTrafficSources


T = TypeVar("T", bound="FWFirewallInterfaces")


@_attrs_define
class FWFirewallInterfaces:
    """
    Attributes:
        interfaces (list[str] | Unset):
        wan (str | Unset):
        lan (str | Unset):
        ethernet (bool | Unset): ethernet filter is enabled
        interface_mappings (FWFirewallInterfacesInterfaceMappings | Unset):
        traffic_sources (FWFirewallInterfacesTrafficSources | Unset):
    """

    interfaces: list[str] | Unset = UNSET
    wan: str | Unset = UNSET
    lan: str | Unset = UNSET
    ethernet: bool | Unset = UNSET
    interface_mappings: FWFirewallInterfacesInterfaceMappings | Unset = UNSET
    traffic_sources: FWFirewallInterfacesTrafficSources | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: list[str] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        wan = self.wan

        lan = self.lan

        ethernet = self.ethernet

        interface_mappings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interface_mappings, Unset):
            interface_mappings = self.interface_mappings.to_dict()

        traffic_sources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic_sources, Unset):
            traffic_sources = self.traffic_sources.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if wan is not UNSET:
            field_dict["wan"] = wan
        if lan is not UNSET:
            field_dict["lan"] = lan
        if ethernet is not UNSET:
            field_dict["ethernet"] = ethernet
        if interface_mappings is not UNSET:
            field_dict["interface_mappings"] = interface_mappings
        if traffic_sources is not UNSET:
            field_dict["traffic_sources"] = traffic_sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fw_firewall_interfaces_interface_mappings import FWFirewallInterfacesInterfaceMappings
        from ..models.fw_firewall_interfaces_traffic_sources import FWFirewallInterfacesTrafficSources

        d = dict(src_dict)
        interfaces = cast(list[str], d.pop("interfaces", UNSET))

        wan = d.pop("wan", UNSET)

        lan = d.pop("lan", UNSET)

        ethernet = d.pop("ethernet", UNSET)

        _interface_mappings = d.pop("interface_mappings", UNSET)
        interface_mappings: FWFirewallInterfacesInterfaceMappings | Unset
        if isinstance(_interface_mappings, Unset):
            interface_mappings = UNSET
        else:
            interface_mappings = FWFirewallInterfacesInterfaceMappings.from_dict(_interface_mappings)

        _traffic_sources = d.pop("traffic_sources", UNSET)
        traffic_sources: FWFirewallInterfacesTrafficSources | Unset
        if isinstance(_traffic_sources, Unset):
            traffic_sources = UNSET
        else:
            traffic_sources = FWFirewallInterfacesTrafficSources.from_dict(_traffic_sources)

        fw_firewall_interfaces = cls(
            interfaces=interfaces,
            wan=wan,
            lan=lan,
            ethernet=ethernet,
            interface_mappings=interface_mappings,
            traffic_sources=traffic_sources,
        )

        fw_firewall_interfaces.additional_properties = d
        return fw_firewall_interfaces

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
