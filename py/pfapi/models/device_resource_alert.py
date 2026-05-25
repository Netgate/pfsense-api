from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_alert import ResourceAlert


T = TypeVar("T", bound="DeviceResourceAlert")


@_attrs_define
class DeviceResourceAlert:
    """Alert from a controlled device that one or more system resources have
    crossed their high-usage thresholds. Forwarded to the event queue when
    the controller receives a resource_alert via /devevt.

        Attributes:
            device_key (str | Unset): public key of source device
            hostname (str | Unset): hostname of source device, if known
            alert (ResourceAlert | Unset): One or more high-resource-usage conditions that crossed their thresholds
    """

    device_key: str | Unset = UNSET
    hostname: str | Unset = UNSET
    alert: ResourceAlert | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_key = self.device_key

        hostname = self.hostname

        alert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_key is not UNSET:
            field_dict["device_key"] = device_key
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if alert is not UNSET:
            field_dict["alert"] = alert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_alert import ResourceAlert

        d = dict(src_dict)
        device_key = d.pop("device_key", UNSET)

        hostname = d.pop("hostname", UNSET)

        _alert = d.pop("alert", UNSET)
        alert: ResourceAlert | Unset
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = ResourceAlert.from_dict(_alert)

        device_resource_alert = cls(
            device_key=device_key,
            hostname=hostname,
            alert=alert,
        )

        device_resource_alert.additional_properties = d
        return device_resource_alert

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
