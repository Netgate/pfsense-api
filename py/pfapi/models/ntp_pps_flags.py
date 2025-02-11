from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NtpPpsFlags")


@_attrs_define
class NtpPpsFlags:
    """
    Attributes:
        enable_falling_edge_pps_signal_processing (bool):
        enable_kernel_pps_clock_disciple (bool):
        record_a_timestamp_once_for_each_second (bool):
    """

    enable_falling_edge_pps_signal_processing: bool
    enable_kernel_pps_clock_disciple: bool
    record_a_timestamp_once_for_each_second: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable_falling_edge_pps_signal_processing = self.enable_falling_edge_pps_signal_processing

        enable_kernel_pps_clock_disciple = self.enable_kernel_pps_clock_disciple

        record_a_timestamp_once_for_each_second = self.record_a_timestamp_once_for_each_second

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable_falling_edge_pps_signal_processing": enable_falling_edge_pps_signal_processing,
                "enable_kernel_pps_clock_disciple": enable_kernel_pps_clock_disciple,
                "record_a_timestamp_once_for_each_second": record_a_timestamp_once_for_each_second,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable_falling_edge_pps_signal_processing = d.pop("enable_falling_edge_pps_signal_processing")

        enable_kernel_pps_clock_disciple = d.pop("enable_kernel_pps_clock_disciple")

        record_a_timestamp_once_for_each_second = d.pop("record_a_timestamp_once_for_each_second")

        ntp_pps_flags = cls(
            enable_falling_edge_pps_signal_processing=enable_falling_edge_pps_signal_processing,
            enable_kernel_pps_clock_disciple=enable_kernel_pps_clock_disciple,
            record_a_timestamp_once_for_each_second=record_a_timestamp_once_for_each_second,
        )

        ntp_pps_flags.additional_properties = d
        return ntp_pps_flags

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
