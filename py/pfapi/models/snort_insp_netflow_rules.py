from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspNetflowRules")


@_attrs_define
class SnortInspNetflowRules:
    """
    Attributes:
        device_ip (str | Unset): restrict the NetFlow devices from which Snort will analyze packets
        exclude (bool | Unset): exclude the NetFlow records that match this rule; default false
        zones (str | Unset): generate events only for NetFlow packets that originate from these zones
        networks (str | Unset): generate events for NetFlow records that contain an initiator or responder IP from these
            networks
        create_host (bool | Unset): generate a new host event; default false
        create_service (bool | Unset): generate a new or changed service event; default false
    """

    device_ip: str | Unset = UNSET
    exclude: bool | Unset = UNSET
    zones: str | Unset = UNSET
    networks: str | Unset = UNSET
    create_host: bool | Unset = UNSET
    create_service: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_ip = self.device_ip

        exclude = self.exclude

        zones = self.zones

        networks = self.networks

        create_host = self.create_host

        create_service = self.create_service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_ip is not UNSET:
            field_dict["device_ip"] = device_ip
        if exclude is not UNSET:
            field_dict["exclude"] = exclude
        if zones is not UNSET:
            field_dict["zones"] = zones
        if networks is not UNSET:
            field_dict["networks"] = networks
        if create_host is not UNSET:
            field_dict["create_host"] = create_host
        if create_service is not UNSET:
            field_dict["create_service"] = create_service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_ip = d.pop("device_ip", UNSET)

        exclude = d.pop("exclude", UNSET)

        zones = d.pop("zones", UNSET)

        networks = d.pop("networks", UNSET)

        create_host = d.pop("create_host", UNSET)

        create_service = d.pop("create_service", UNSET)

        snort_insp_netflow_rules = cls(
            device_ip=device_ip,
            exclude=exclude,
            zones=zones,
            networks=networks,
            create_host=create_host,
            create_service=create_service,
        )

        snort_insp_netflow_rules.additional_properties = d
        return snort_insp_netflow_rules

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
