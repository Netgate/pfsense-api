from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitoringDataRequest")


@_attrs_define
class MonitoringDataRequest:
    """
    Attributes:
        scope (Union[Unset, str]):
        dataset (Union[Unset, str]):
        start_time_unix_seconds (Union[Unset, int]):
        end_time_unix_seconds (Union[Unset, int]):
        resolution_seconds (Union[Unset, int]):
    """

    scope: Union[Unset, str] = UNSET
    dataset: Union[Unset, str] = UNSET
    start_time_unix_seconds: Union[Unset, int] = UNSET
    end_time_unix_seconds: Union[Unset, int] = UNSET
    resolution_seconds: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scope = self.scope

        dataset = self.dataset

        start_time_unix_seconds = self.start_time_unix_seconds

        end_time_unix_seconds = self.end_time_unix_seconds

        resolution_seconds = self.resolution_seconds

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
