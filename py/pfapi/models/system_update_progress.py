from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SystemUpdateProgress")


@_attrs_define
class SystemUpdateProgress:
    """
    Attributes:
        messages (List[str]):
        completed (int):
        started_timestamp (int):
        ended_timestamp (int):
        started_time (str):
        ended_time (str):
    """

    messages: List[str]
    completed: int
    started_timestamp: int
    ended_timestamp: int
    started_time: str
    ended_time: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        messages = self.messages

        completed = self.completed

        started_timestamp = self.started_timestamp

        ended_timestamp = self.ended_timestamp

        started_time = self.started_time

        ended_time = self.ended_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
                "completed": completed,
                "started_timestamp": started_timestamp,
                "ended_timestamp": ended_timestamp,
                "started_time": started_time,
                "ended_time": ended_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        messages = cast(List[str], d.pop("messages"))

        completed = d.pop("completed")

        started_timestamp = d.pop("started_timestamp")

        ended_timestamp = d.pop("ended_timestamp")

        started_time = d.pop("started_time")

        ended_time = d.pop("ended_time")

        system_update_progress = cls(
            messages=messages,
            completed=completed,
            started_timestamp=started_timestamp,
            ended_timestamp=ended_timestamp,
            started_time=started_time,
            ended_time=ended_time,
        )

        system_update_progress.additional_properties = d
        return system_update_progress

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
