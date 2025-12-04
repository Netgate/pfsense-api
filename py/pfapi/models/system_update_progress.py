from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemUpdateProgress")


@_attrs_define
class SystemUpdateProgress:
    """
    Attributes:
        messages (list[str] | Unset):
        completed (int | Unset):
        started_timestamp (int | Unset):
        ended_timestamp (int | Unset):
        started_time (str | Unset):
        ended_time (str | Unset):
    """

    messages: list[str] | Unset = UNSET
    completed: int | Unset = UNSET
    started_timestamp: int | Unset = UNSET
    ended_timestamp: int | Unset = UNSET
    started_time: str | Unset = UNSET
    ended_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        messages: list[str] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages

        completed = self.completed

        started_timestamp = self.started_timestamp

        ended_timestamp = self.ended_timestamp

        started_time = self.started_time

        ended_time = self.ended_time

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        messages = cast(list[str], d.pop("messages", UNSET))

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
