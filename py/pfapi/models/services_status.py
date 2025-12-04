from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicesStatus")


@_attrs_define
class ServicesStatus:
    """
    Attributes:
        name (str):
        description (str | Unset):
        vpnid (str | Unset): for openvpn service only
        mode (str | Unset): for openvpn service only
        zone (str | Unset): for captive portal service only
        enabled (bool | Unset):
        running (bool | Unset):
    """

    name: str
    description: str | Unset = UNSET
    vpnid: str | Unset = UNSET
    mode: str | Unset = UNSET
    zone: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    running: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        vpnid = self.vpnid

        mode = self.mode

        zone = self.zone

        enabled = self.enabled

        running = self.running

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if vpnid is not UNSET:
            field_dict["vpnid"] = vpnid
        if mode is not UNSET:
            field_dict["mode"] = mode
        if zone is not UNSET:
            field_dict["zone"] = zone
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if running is not UNSET:
            field_dict["running"] = running

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        vpnid = d.pop("vpnid", UNSET)

        mode = d.pop("mode", UNSET)

        zone = d.pop("zone", UNSET)

        enabled = d.pop("enabled", UNSET)

        running = d.pop("running", UNSET)

        services_status = cls(
            name=name,
            description=description,
            vpnid=vpnid,
            mode=mode,
            zone=zone,
            enabled=enabled,
            running=running,
        )

        services_status.additional_properties = d
        return services_status

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
