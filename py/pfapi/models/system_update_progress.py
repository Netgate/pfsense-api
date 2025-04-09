from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemUpdateProgress")


@_attrs_define
class SystemUpdateProgress:
    """
    Attributes:
        messages (Union[Unset, List[str]]):
        completed (Union[Unset, int]):
        started_timestamp (Union[Unset, int]):
        ended_timestamp (Union[Unset, int]):
        started_time (Union[Unset, str]):
        ended_time (Union[Unset, str]):
    """

    messages: Union[Unset, List[str]] = UNSET
    completed: Union[Unset, int] = UNSET
    started_timestamp: Union[Unset, int] = UNSET
    ended_timestamp: Union[Unset, int] = UNSET
    started_time: Union[Unset, str] = UNSET
    ended_time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        messages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages

        completed = self.completed

        started_timestamp = self.started_timestamp

        ended_timestamp = self.ended_timestamp

        started_time = self.started_time

        ended_time = self.ended_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if messages is not UNSET:
            field_dict["messages"] = messages
        if completed is not UNSET:
            field_dict["completed"] = completed
        if started_timestamp is not UNSET:
            field_dict["started_timestamp"] = started_timestamp
        if ended_timestamp is not UNSET:
            field_dict["ended_timestamp"] = ended_timestamp
        if started_time is not UNSET:
            field_dict["started_time"] = started_time
        if ended_time is not UNSET:
            field_dict["ended_time"] = ended_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        messages = cast(List[str], d.pop("messages", UNSET))

        completed = d.pop("completed", UNSET)

        started_timestamp = d.pop("started_timestamp", UNSET)

        ended_timestamp = d.pop("ended_timestamp", UNSET)

        started_time = d.pop("started_time", UNSET)

        ended_time = d.pop("ended_time", UNSET)

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
