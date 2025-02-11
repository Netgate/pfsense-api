from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MonitoringDatasetInfo")


@_attrs_define
class MonitoringDatasetInfo:
    """
    Attributes:
        scope (str):
        dataset (str):
        earliest_data_time (int):
    """

    scope: str
    dataset: str
    earliest_data_time: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scope = self.scope

        dataset = self.dataset

        earliest_data_time = self.earliest_data_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scope": scope,
                "dataset": dataset,
                "earliest_data_time": earliest_data_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scope = d.pop("scope")

        dataset = d.pop("dataset")

        earliest_data_time = d.pop("earliest_data_time")

        monitoring_dataset_info = cls(
            scope=scope,
            dataset=dataset,
            earliest_data_time=earliest_data_time,
        )

        monitoring_dataset_info.additional_properties = d
        return monitoring_dataset_info

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
