from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceAlertCondition")


@_attrs_define
class ResourceAlertCondition:
    """
    Attributes:
        resource (str | Unset): cpu, memory, disk
        path (str | Unset): mount path of filesystem for disk alerts
        threshold (int | Unset): threshold percentage that was crossed
        value (int | Unset): current value percentage
        duration_s (int | Unset): how long the condition has been continuously triggered
    """

    resource: str | Unset = UNSET
    path: str | Unset = UNSET
    threshold: int | Unset = UNSET
    value: int | Unset = UNSET
    duration_s: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource

        path = self.path

        threshold = self.threshold

        value = self.value

        duration_s = self.duration_s

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource is not UNSET:
            field_dict["resource"] = resource
        if path is not UNSET:
            field_dict["path"] = path
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if value is not UNSET:
            field_dict["value"] = value
        if duration_s is not UNSET:
            field_dict["duration_s"] = duration_s

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource = d.pop("resource", UNSET)

        path = d.pop("path", UNSET)

        threshold = d.pop("threshold", UNSET)

        value = d.pop("value", UNSET)

        duration_s = d.pop("duration_s", UNSET)

        resource_alert_condition = cls(
            resource=resource,
            path=path,
            threshold=threshold,
            value=value,
            duration_s=duration_s,
        )

        resource_alert_condition.additional_properties = d
        return resource_alert_condition

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
