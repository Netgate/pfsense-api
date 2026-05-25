from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspDceTcp")


@_attrs_define
class SnortInspDceTcp:
    """
    Attributes:
        limit_alerts (bool | Unset): limit DCE alert to at most one per signature per flow; default true
        disable_defrag (bool | Unset): disable DCE/RPC defragmentation; default false
        max_frag_len (int | Unset): maximum fragment size for defragmentation { 1514:65535 }; default 65535
        reassemble_threshold (int | Unset): minimum bytes received before performing reassembly { 0:65535 }; default 0
        policy (str | Unset): target based policy to use { Win2000 | WinXP | WinVista | Win2003 | Win2008 | Win7 | Samba
            | Samba-3.0.37 | Samba-3.0.22 | Samba-3.0.20 }; default WinXP
    """

    limit_alerts: bool | Unset = UNSET
    disable_defrag: bool | Unset = UNSET
    max_frag_len: int | Unset = UNSET
    reassemble_threshold: int | Unset = UNSET
    policy: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit_alerts = self.limit_alerts

        disable_defrag = self.disable_defrag

        max_frag_len = self.max_frag_len

        reassemble_threshold = self.reassemble_threshold

        policy = self.policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit_alerts is not UNSET:
            field_dict["limit_alerts"] = limit_alerts
        if disable_defrag is not UNSET:
            field_dict["disable_defrag"] = disable_defrag
        if max_frag_len is not UNSET:
            field_dict["max_frag_len"] = max_frag_len
        if reassemble_threshold is not UNSET:
            field_dict["reassemble_threshold"] = reassemble_threshold
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit_alerts = d.pop("limit_alerts", UNSET)

        disable_defrag = d.pop("disable_defrag", UNSET)

        max_frag_len = d.pop("max_frag_len", UNSET)

        reassemble_threshold = d.pop("reassemble_threshold", UNSET)

        policy = d.pop("policy", UNSET)

        snort_insp_dce_tcp = cls(
            limit_alerts=limit_alerts,
            disable_defrag=disable_defrag,
            max_frag_len=max_frag_len,
            reassemble_threshold=reassemble_threshold,
            policy=policy,
        )

        snort_insp_dce_tcp.additional_properties = d
        return snort_insp_dce_tcp

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
