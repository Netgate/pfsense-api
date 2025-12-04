from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitoringDatasetInfo")


@_attrs_define
class MonitoringDatasetInfo:
    """
    Attributes:
        scope (str | Unset):
        dataset (str | Unset):
        earliest_data_time (int | Unset):
    """

    scope: str | Unset = UNSET
    dataset: str | Unset = UNSET
    earliest_data_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope = self.scope

        dataset = self.dataset

        earliest_data_time = self.earliest_data_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if dataset is not UNSET:
            field_dict["dataset"] = dataset
        if earliest_data_time is not UNSET:
            field_dict["earliest_data_time"] = earliest_data_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scope = d.pop("scope", UNSET)

        dataset = d.pop("dataset", UNSET)

        earliest_data_time = d.pop("earliest_data_time", UNSET)

        monitoring_dataset_info = cls(
            scope=scope,
            dataset=dataset,
            earliest_data_time=earliest_data_time,
        )

        monitoring_dataset_info.additional_properties = d
        return monitoring_dataset_info

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
