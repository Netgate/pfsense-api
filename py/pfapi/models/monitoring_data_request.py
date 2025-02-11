from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MonitoringDataRequest")


@_attrs_define
class MonitoringDataRequest:
    """
    Attributes:
        scope (str):
        dataset (str):
        start_time_unix_seconds (int):
        end_time_unix_seconds (int):
        resolution_seconds (int):
    """

    scope: str
    dataset: str
    start_time_unix_seconds: int
    end_time_unix_seconds: int
    resolution_seconds: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scope = self.scope

        dataset = self.dataset

        start_time_unix_seconds = self.start_time_unix_seconds

        end_time_unix_seconds = self.end_time_unix_seconds

        resolution_seconds = self.resolution_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scope": scope,
                "dataset": dataset,
                "start_time_unix_seconds": start_time_unix_seconds,
                "end_time_unix_seconds": end_time_unix_seconds,
                "resolution_seconds": resolution_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scope = d.pop("scope")

        dataset = d.pop("dataset")

        start_time_unix_seconds = d.pop("start_time_unix_seconds")

        end_time_unix_seconds = d.pop("end_time_unix_seconds")

        resolution_seconds = d.pop("resolution_seconds")

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
