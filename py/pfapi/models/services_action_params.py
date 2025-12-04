from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicesActionParams")


@_attrs_define
class ServicesActionParams:
    """valid values:
    action = "start", "stop", "restart"

        Attributes:
            service (str | Unset):
            action (str | Unset):
            vpnid (str | Unset):
            mode (str | Unset):
            zone (str | Unset):
    """

    service: str | Unset = UNSET
    action: str | Unset = UNSET
    vpnid: str | Unset = UNSET
    mode: str | Unset = UNSET
    zone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service = self.service

        action = self.action

        vpnid = self.vpnid

        mode = self.mode

        zone = self.zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service is not UNSET:
            field_dict["service"] = service
        if action is not UNSET:
            field_dict["action"] = action
        if vpnid is not UNSET:
            field_dict["vpnid"] = vpnid
        if mode is not UNSET:
            field_dict["mode"] = mode
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service = d.pop("service", UNSET)

        action = d.pop("action", UNSET)

        vpnid = d.pop("vpnid", UNSET)

        mode = d.pop("mode", UNSET)

        zone = d.pop("zone", UNSET)

        services_action_params = cls(
            service=service,
            action=action,
            vpnid=vpnid,
            mode=mode,
            zone=zone,
        )

        services_action_params.additional_properties = d
        return services_action_params

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
