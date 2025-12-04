from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitoringDataRequest")


@_attrs_define
class MonitoringDataRequest:
    """
    Attributes:
        scope (str | Unset):
        dataset (str | Unset):
        start_time_unix_seconds (int | Unset):
        end_time_unix_seconds (int | Unset):
        resolution_seconds (int | Unset):
    """

    scope: str | Unset = UNSET
    dataset: str | Unset = UNSET
    start_time_unix_seconds: int | Unset = UNSET
    end_time_unix_seconds: int | Unset = UNSET
    resolution_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope = self.scope

        dataset = self.dataset

        start_time_unix_seconds = self.start_time_unix_seconds

        end_time_unix_seconds = self.end_time_unix_seconds

        resolution_seconds = self.resolution_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if dataset is not UNSET:
            field_dict["dataset"] = dataset
        if start_time_unix_seconds is not UNSET:
            field_dict["start_time_unix_seconds"] = start_time_unix_seconds
        if end_time_unix_seconds is not UNSET:
            field_dict["end_time_unix_seconds"] = end_time_unix_seconds
        if resolution_seconds is not UNSET:
            field_dict["resolution_seconds"] = resolution_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scope = d.pop("scope", UNSET)

        dataset = d.pop("dataset", UNSET)

        start_time_unix_seconds = d.pop("start_time_unix_seconds", UNSET)

        end_time_unix_seconds = d.pop("end_time_unix_seconds", UNSET)

        resolution_seconds = d.pop("resolution_seconds", UNSET)

        monitoring_data_request = cls(
            scope=scope,
            dataset=dataset,
            start_time_unix_seconds=start_time_unix_seconds,
            end_time_unix_seconds=end_time_unix_seconds,
            resolution_seconds=resolution_seconds,
        )

        monitoring_data_request.additional_properties = d
        return monitoring_data_request

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
