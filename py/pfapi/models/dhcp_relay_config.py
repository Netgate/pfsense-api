from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_value import TextValue


T = TypeVar("T", bound="DhcpRelayConfig")


@_attrs_define
class DhcpRelayConfig:
    """
    Attributes:
        enable (bool | Unset):
        interfaces (list[str] | Unset):
        carp_status_vip (str | Unset):
        append_circuit_agent_ids (bool | Unset):
        upstream_servers (list[str] | Unset):
        carp_status_vip_entries (list[TextValue] | Unset):
        interfaces_entries (list[TextValue] | Unset):
    """

    enable: bool | Unset = UNSET
    interfaces: list[str] | Unset = UNSET
    carp_status_vip: str | Unset = UNSET
    append_circuit_agent_ids: bool | Unset = UNSET
    upstream_servers: list[str] | Unset = UNSET
    carp_status_vip_entries: list[TextValue] | Unset = UNSET
    interfaces_entries: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        interfaces: list[str] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        carp_status_vip = self.carp_status_vip

        append_circuit_agent_ids = self.append_circuit_agent_ids

        upstream_servers: list[str] | Unset = UNSET
        if not isinstance(self.upstream_servers, Unset):
            upstream_servers = self.upstream_servers

        carp_status_vip_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.carp_status_vip_entries, Unset):
            carp_status_vip_entries = []
            for carp_status_vip_entries_item_data in self.carp_status_vip_entries:
                carp_status_vip_entries_item = carp_status_vip_entries_item_data.to_dict()
                carp_status_vip_entries.append(carp_status_vip_entries_item)

        interfaces_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces_entries, Unset):
            interfaces_entries = []
            for interfaces_entries_item_data in self.interfaces_entries:
                interfaces_entries_item = interfaces_entries_item_data.to_dict()
                interfaces_entries.append(interfaces_entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if carp_status_vip is not UNSET:
            field_dict["carp_status_vip"] = carp_status_vip
        if append_circuit_agent_ids is not UNSET:
            field_dict["append_circuit_agent_ids"] = append_circuit_agent_ids
        if upstream_servers is not UNSET:
            field_dict["upstream_servers"] = upstream_servers
        if carp_status_vip_entries is not UNSET:
            field_dict["carp_status_vip_entries"] = carp_status_vip_entries
        if interfaces_entries is not UNSET:
            field_dict["interfaces_entries"] = interfaces_entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_value import TextValue

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        interfaces = cast(list[str], d.pop("interfaces", UNSET))

        carp_status_vip = d.pop("carp_status_vip", UNSET)

        append_circuit_agent_ids = d.pop("append_circuit_agent_ids", UNSET)

        upstream_servers = cast(list[str], d.pop("upstream_servers", UNSET))

        _carp_status_vip_entries = d.pop("carp_status_vip_entries", UNSET)
        carp_status_vip_entries: list[TextValue] | Unset = UNSET
        if _carp_status_vip_entries is not UNSET:
            carp_status_vip_entries = []
            for carp_status_vip_entries_item_data in _carp_status_vip_entries:
                carp_status_vip_entries_item = TextValue.from_dict(carp_status_vip_entries_item_data)

                carp_status_vip_entries.append(carp_status_vip_entries_item)

        _interfaces_entries = d.pop("interfaces_entries", UNSET)
        interfaces_entries: list[TextValue] | Unset = UNSET
        if _interfaces_entries is not UNSET:
            interfaces_entries = []
            for interfaces_entries_item_data in _interfaces_entries:
                interfaces_entries_item = TextValue.from_dict(interfaces_entries_item_data)

                interfaces_entries.append(interfaces_entries_item)

        dhcp_relay_config = cls(
            enable=enable,
            interfaces=interfaces,
            carp_status_vip=carp_status_vip,
            append_circuit_agent_ids=append_circuit_agent_ids,
            upstream_servers=upstream_servers,
            carp_status_vip_entries=carp_status_vip_entries,
            interfaces_entries=interfaces_entries,
        )

        dhcp_relay_config.additional_properties = d
        return dhcp_relay_config

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
