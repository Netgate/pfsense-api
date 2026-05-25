from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspHttp2Inspect")


@_attrs_define
class SnortInspHttp2Inspect:
    """
    Attributes:
        concurrent_streams_limit (int | Unset): Maximum number of concurrent streams allowed in a single HTTP/2 flow {
            100:1000 }; default 100
        settings_max_frame_size (int | Unset): Maximum allowed value for settings frame SETTINGS_MAX_FRAME_SIZE {
            16384:16777215 }; default 16777215
    """

    concurrent_streams_limit: int | Unset = UNSET
    settings_max_frame_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        concurrent_streams_limit = self.concurrent_streams_limit

        settings_max_frame_size = self.settings_max_frame_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if concurrent_streams_limit is not UNSET:
            field_dict["concurrent_streams_limit"] = concurrent_streams_limit
        if settings_max_frame_size is not UNSET:
            field_dict["settings_max_frame_size"] = settings_max_frame_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        concurrent_streams_limit = d.pop("concurrent_streams_limit", UNSET)

        settings_max_frame_size = d.pop("settings_max_frame_size", UNSET)

        snort_insp_http_2_inspect = cls(
            concurrent_streams_limit=concurrent_streams_limit,
            settings_max_frame_size=settings_max_frame_size,
        )

        snort_insp_http_2_inspect.additional_properties = d
        return snort_insp_http_2_inspect

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
