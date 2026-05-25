from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspStreamTcpSmallSegments")


@_attrs_define
class SnortInspStreamTcpSmallSegments:
    """
    Attributes:
        count (int | Unset): number of consecutive (in the received order) TCP small segments considered to be excessive
            (129:12) { 0:2048 }; default 0
        maximum_size (int | Unset): minimum bytes for a TCP segment not to be considered small (129:12) { 0:2048 };
            default 0
    """

    count: int | Unset = UNSET
    maximum_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        maximum_size = self.maximum_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if maximum_size is not UNSET:
            field_dict["maximum_size"] = maximum_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        maximum_size = d.pop("maximum_size", UNSET)

        snort_insp_stream_tcp_small_segments = cls(
            count=count,
            maximum_size=maximum_size,
        )

        snort_insp_stream_tcp_small_segments.additional_properties = d
        return snort_insp_stream_tcp_small_segments

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
