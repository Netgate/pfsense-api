from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspPacketCapture")


@_attrs_define
class SnortInspPacketCapture:
    """
    Attributes:
        enable (bool | Unset): state of packet capturing; default false
        filter_ (str | Unset): bpf filter to use for packet capturing
        group (int | Unset): group filter to use for packet capturing { -1:32767 }; default -1
        tenants (str | Unset): comma-separated tenants filter to use for packet capturing
        check_inner_pkt (bool | Unset): apply filter on inner packet headers; default true
        capture_path (str | Unset): directory path to capture pcaps
        max_packet_count (int | Unset): cap the number of packets per thread { 0:max32 }; default 0
    """

    enable: bool | Unset = UNSET
    filter_: str | Unset = UNSET
    group: int | Unset = UNSET
    tenants: str | Unset = UNSET
    check_inner_pkt: bool | Unset = UNSET
    capture_path: str | Unset = UNSET
    max_packet_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        filter_ = self.filter_

        group = self.group

        tenants = self.tenants

        check_inner_pkt = self.check_inner_pkt

        capture_path = self.capture_path

        max_packet_count = self.max_packet_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if group is not UNSET:
            field_dict["group"] = group
        if tenants is not UNSET:
            field_dict["tenants"] = tenants
        if check_inner_pkt is not UNSET:
            field_dict["check_inner_pkt"] = check_inner_pkt
        if capture_path is not UNSET:
            field_dict["capture_path"] = capture_path
        if max_packet_count is not UNSET:
            field_dict["max_packet_count"] = max_packet_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        filter_ = d.pop("filter", UNSET)

        group = d.pop("group", UNSET)

        tenants = d.pop("tenants", UNSET)

        check_inner_pkt = d.pop("check_inner_pkt", UNSET)

        capture_path = d.pop("capture_path", UNSET)

        max_packet_count = d.pop("max_packet_count", UNSET)

        snort_insp_packet_capture = cls(
            enable=enable,
            filter_=filter_,
            group=group,
            tenants=tenants,
            check_inner_pkt=check_inner_pkt,
            capture_path=capture_path,
            max_packet_count=max_packet_count,
        )

        snort_insp_packet_capture.additional_properties = d
        return snort_insp_packet_capture

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
