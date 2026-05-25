from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspFileLog")


@_attrs_define
class SnortInspFileLog:
    """
    Attributes:
        log_pkt_time (bool | Unset): log the packet time when event generated; default true
        log_sys_time (bool | Unset): log the system time when event generated; default false
    """

    log_pkt_time: bool | Unset = UNSET
    log_sys_time: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        log_pkt_time = self.log_pkt_time

        log_sys_time = self.log_sys_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if log_pkt_time is not UNSET:
            field_dict["log_pkt_time"] = log_pkt_time
        if log_sys_time is not UNSET:
            field_dict["log_sys_time"] = log_sys_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        log_pkt_time = d.pop("log_pkt_time", UNSET)

        log_sys_time = d.pop("log_sys_time", UNSET)

        snort_insp_file_log = cls(
            log_pkt_time=log_pkt_time,
            log_sys_time=log_sys_time,
        )

        snort_insp_file_log.additional_properties = d
        return snort_insp_file_log

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
