from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspStreamTcpQueueLimit")


@_attrs_define
class SnortInspStreamTcpQueueLimit:
    """
    Attributes:
        max_bytes (int | Unset): don’t queue more than given bytes per session and direction, 0 = unlimited { 0:max32 };
            default 4194304
        max_segments (int | Unset): don’t queue more than given segments per session and direction, 0 = unlimited {
            0:max32 }; default 3072
        asymmetric_ids_flush_threshold (int | Unset): max bytes queued on asymmetric flow before flush in IDS mode {
            1:max31 }; default 3145728
    """

    max_bytes: int | Unset = UNSET
    max_segments: int | Unset = UNSET
    asymmetric_ids_flush_threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_bytes = self.max_bytes

        max_segments = self.max_segments

        asymmetric_ids_flush_threshold = self.asymmetric_ids_flush_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_bytes is not UNSET:
            field_dict["max_bytes"] = max_bytes
        if max_segments is not UNSET:
            field_dict["max_segments"] = max_segments
        if asymmetric_ids_flush_threshold is not UNSET:
            field_dict["asymmetric_ids_flush_threshold"] = asymmetric_ids_flush_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_bytes = d.pop("max_bytes", UNSET)

        max_segments = d.pop("max_segments", UNSET)

        asymmetric_ids_flush_threshold = d.pop("asymmetric_ids_flush_threshold", UNSET)

        snort_insp_stream_tcp_queue_limit = cls(
            max_bytes=max_bytes,
            max_segments=max_segments,
            asymmetric_ids_flush_threshold=asymmetric_ids_flush_threshold,
        )

        snort_insp_stream_tcp_queue_limit.additional_properties = d
        return snort_insp_stream_tcp_queue_limit

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
