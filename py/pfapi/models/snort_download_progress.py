from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortDownloadProgress")


@_attrs_define
class SnortDownloadProgress:
    """
    Attributes:
        completed (bool | Unset): download completed
        start_ts (int | Unset): millisecond timestamp of when download request started
        end_ts (int | Unset): millisecond timetamp of when download ended
        errors (str | Unset): error messages from download
        messages (str | Unset): messages from download
        percent (float | Unset):
        state (str | Unset): state of download - running, idle (enabled), stopped, suspended (disabled)
    """

    completed: bool | Unset = UNSET
    start_ts: int | Unset = UNSET
    end_ts: int | Unset = UNSET
    errors: str | Unset = UNSET
    messages: str | Unset = UNSET
    percent: float | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completed = self.completed

        start_ts = self.start_ts

        end_ts = self.end_ts

        errors = self.errors

        messages = self.messages

        percent = self.percent

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed is not UNSET:
            field_dict["completed"] = completed
        if start_ts is not UNSET:
            field_dict["start_ts"] = start_ts
        if end_ts is not UNSET:
            field_dict["end_ts"] = end_ts
        if errors is not UNSET:
            field_dict["errors"] = errors
        if messages is not UNSET:
            field_dict["messages"] = messages
        if percent is not UNSET:
            field_dict["percent"] = percent
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        completed = d.pop("completed", UNSET)

        start_ts = d.pop("start_ts", UNSET)

        end_ts = d.pop("end_ts", UNSET)

        errors = d.pop("errors", UNSET)

        messages = d.pop("messages", UNSET)

        percent = d.pop("percent", UNSET)

        state = d.pop("state", UNSET)

        snort_download_progress = cls(
            completed=completed,
            start_ts=start_ts,
            end_ts=end_ts,
            errors=errors,
            messages=messages,
            percent=percent,
            state=state,
        )

        snort_download_progress.additional_properties = d
        return snort_download_progress

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
