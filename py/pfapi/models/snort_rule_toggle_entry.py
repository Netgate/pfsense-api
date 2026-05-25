from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortRuleToggleEntry")


@_attrs_define
class SnortRuleToggleEntry:
    """
    Attributes:
        gid (str | Unset):
        sid (str | Unset):
        enable (bool | Unset): enable or disable
        suppress (bool | Unset): suppress alerting of the rule
        reset_entry (bool | Unset): reset this toggle to the rule's default (deleted from config)
    """

    gid: str | Unset = UNSET
    sid: str | Unset = UNSET
    enable: bool | Unset = UNSET
    suppress: bool | Unset = UNSET
    reset_entry: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gid = self.gid

        sid = self.sid

        enable = self.enable

        suppress = self.suppress

        reset_entry = self.reset_entry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gid is not UNSET:
            field_dict["gid"] = gid
        if sid is not UNSET:
            field_dict["sid"] = sid
        if enable is not UNSET:
            field_dict["enable"] = enable
        if suppress is not UNSET:
            field_dict["suppress"] = suppress
        if reset_entry is not UNSET:
            field_dict["reset_entry"] = reset_entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gid = d.pop("gid", UNSET)

        sid = d.pop("sid", UNSET)

        enable = d.pop("enable", UNSET)

        suppress = d.pop("suppress", UNSET)

        reset_entry = d.pop("reset_entry", UNSET)

        snort_rule_toggle_entry = cls(
            gid=gid,
            sid=sid,
            enable=enable,
            suppress=suppress,
            reset_entry=reset_entry,
        )

        snort_rule_toggle_entry.additional_properties = d
        return snort_rule_toggle_entry

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
