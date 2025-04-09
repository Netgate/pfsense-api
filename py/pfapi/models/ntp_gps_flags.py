from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NtpGpsFlags")


@_attrs_define
class NtpGpsFlags:
    """
    Attributes:
        prefer_this_clock (Union[Unset, bool]):
        do_not_select_this_clock (Union[Unset, bool]):
        enable_pps_signal_processing (Union[Unset, bool]):
        enable_falling_edge_pps_signal_processing (Union[Unset, bool]):
        enable_kernel_pps_clock_disciple (Union[Unset, bool]):
        obscure_location_in_timestamp (Union[Unset, bool]):
        log_subsecond_received_timestamp (Union[Unset, bool]):
        display_extended_gps_status (Union[Unset, bool]):
    """

    prefer_this_clock: Union[Unset, bool] = UNSET
    do_not_select_this_clock: Union[Unset, bool] = UNSET
    enable_pps_signal_processing: Union[Unset, bool] = UNSET
    enable_falling_edge_pps_signal_processing: Union[Unset, bool] = UNSET
    enable_kernel_pps_clock_disciple: Union[Unset, bool] = UNSET
    obscure_location_in_timestamp: Union[Unset, bool] = UNSET
    log_subsecond_received_timestamp: Union[Unset, bool] = UNSET
    display_extended_gps_status: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prefer_this_clock = self.prefer_this_clock

        do_not_select_this_clock = self.do_not_select_this_clock

        enable_pps_signal_processing = self.enable_pps_signal_processing

        enable_falling_edge_pps_signal_processing = self.enable_falling_edge_pps_signal_processing

        enable_kernel_pps_clock_disciple = self.enable_kernel_pps_clock_disciple

        obscure_location_in_timestamp = self.obscure_location_in_timestamp

        log_subsecond_received_timestamp = self.log_subsecond_received_timestamp

        display_extended_gps_status = self.display_extended_gps_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prefer_this_clock is not UNSET:
            field_dict["prefer_this_clock"] = prefer_this_clock
        if do_not_select_this_clock is not UNSET:
            field_dict["do_not_select_this_clock"] = do_not_select_this_clock
        if enable_pps_signal_processing is not UNSET:
            field_dict["enable_pps_signal_processing"] = enable_pps_signal_processing
        if enable_falling_edge_pps_signal_processing is not UNSET:
            field_dict["enable_falling_edge_pps_signal_processing"] = enable_falling_edge_pps_signal_processing
        if enable_kernel_pps_clock_disciple is not UNSET:
            field_dict["enable_kernel_pps_clock_disciple"] = enable_kernel_pps_clock_disciple
        if obscure_location_in_timestamp is not UNSET:
            field_dict["obscure_location_in_timestamp"] = obscure_location_in_timestamp
        if log_subsecond_received_timestamp is not UNSET:
            field_dict["log_subsecond_received_timestamp"] = log_subsecond_received_timestamp
        if display_extended_gps_status is not UNSET:
            field_dict["display_extended_gps_status"] = display_extended_gps_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        prefer_this_clock = d.pop("prefer_this_clock", UNSET)

        do_not_select_this_clock = d.pop("do_not_select_this_clock", UNSET)

        enable_pps_signal_processing = d.pop("enable_pps_signal_processing", UNSET)

        enable_falling_edge_pps_signal_processing = d.pop("enable_falling_edge_pps_signal_processing", UNSET)

        enable_kernel_pps_clock_disciple = d.pop("enable_kernel_pps_clock_disciple", UNSET)

        obscure_location_in_timestamp = d.pop("obscure_location_in_timestamp", UNSET)

        log_subsecond_received_timestamp = d.pop("log_subsecond_received_timestamp", UNSET)

        display_extended_gps_status = d.pop("display_extended_gps_status", UNSET)

        ntp_gps_flags = cls(
            prefer_this_clock=prefer_this_clock,
            do_not_select_this_clock=do_not_select_this_clock,
            enable_pps_signal_processing=enable_pps_signal_processing,
            enable_falling_edge_pps_signal_processing=enable_falling_edge_pps_signal_processing,
            enable_kernel_pps_clock_disciple=enable_kernel_pps_clock_disciple,
            obscure_location_in_timestamp=obscure_location_in_timestamp,
            log_subsecond_received_timestamp=log_subsecond_received_timestamp,
            display_extended_gps_status=display_extended_gps_status,
        )

        ntp_gps_flags.additional_properties = d
        return ntp_gps_flags

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
