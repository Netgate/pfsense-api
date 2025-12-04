from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NtpPpsFlags")


@_attrs_define
class NtpPpsFlags:
    """
    Attributes:
        enable_falling_edge_pps_signal_processing (bool | Unset):
        enable_kernel_pps_clock_disciple (bool | Unset):
        record_a_timestamp_once_for_each_second (bool | Unset):
    """

    enable_falling_edge_pps_signal_processing: bool | Unset = UNSET
    enable_kernel_pps_clock_disciple: bool | Unset = UNSET
    record_a_timestamp_once_for_each_second: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_falling_edge_pps_signal_processing = self.enable_falling_edge_pps_signal_processing

        enable_kernel_pps_clock_disciple = self.enable_kernel_pps_clock_disciple

        record_a_timestamp_once_for_each_second = self.record_a_timestamp_once_for_each_second

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_falling_edge_pps_signal_processing is not UNSET:
            field_dict["enable_falling_edge_pps_signal_processing"] = enable_falling_edge_pps_signal_processing
        if enable_kernel_pps_clock_disciple is not UNSET:
            field_dict["enable_kernel_pps_clock_disciple"] = enable_kernel_pps_clock_disciple
        if record_a_timestamp_once_for_each_second is not UNSET:
            field_dict["record_a_timestamp_once_for_each_second"] = record_a_timestamp_once_for_each_second

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_falling_edge_pps_signal_processing = d.pop("enable_falling_edge_pps_signal_processing", UNSET)

        enable_kernel_pps_clock_disciple = d.pop("enable_kernel_pps_clock_disciple", UNSET)

        record_a_timestamp_once_for_each_second = d.pop("record_a_timestamp_once_for_each_second", UNSET)

        ntp_pps_flags = cls(
            enable_falling_edge_pps_signal_processing=enable_falling_edge_pps_signal_processing,
            enable_kernel_pps_clock_disciple=enable_kernel_pps_clock_disciple,
            record_a_timestamp_once_for_each_second=record_a_timestamp_once_for_each_second,
        )

        ntp_pps_flags.additional_properties = d
        return ntp_pps_flags

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
