from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspDceUdp")


@_attrs_define
class SnortInspDceUdp:
    """
    Attributes:
        limit_alerts (bool | Unset): limit DCE alert to at most one per signature per flow; default true
        disable_defrag (bool | Unset): disable DCE/RPC defragmentation; default false
        max_frag_len (int | Unset): maximum fragment size for defragmentation { 1514:65535 }; default 65535
    """

    limit_alerts: bool | Unset = UNSET
    disable_defrag: bool | Unset = UNSET
    max_frag_len: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit_alerts = self.limit_alerts

        disable_defrag = self.disable_defrag

        max_frag_len = self.max_frag_len

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit_alerts is not UNSET:
            field_dict["limit_alerts"] = limit_alerts
        if disable_defrag is not UNSET:
            field_dict["disable_defrag"] = disable_defrag
        if max_frag_len is not UNSET:
            field_dict["max_frag_len"] = max_frag_len

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit_alerts = d.pop("limit_alerts", UNSET)

        disable_defrag = d.pop("disable_defrag", UNSET)

        max_frag_len = d.pop("max_frag_len", UNSET)

        snort_insp_dce_udp = cls(
            limit_alerts=limit_alerts,
            disable_defrag=disable_defrag,
            max_frag_len=max_frag_len,
        )

        snort_insp_dce_udp.additional_properties = d
        return snort_insp_dce_udp

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
