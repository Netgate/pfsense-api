from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortIpsStateRule")


@_attrs_define
class SnortIpsStateRule:
    """
    Attributes:
        action (str | Unset):
        gid (str | Unset):
        sid (str | Unset):
        enable (bool | Unset):
    """

    action: str | Unset = UNSET
    gid: str | Unset = UNSET
    sid: str | Unset = UNSET
    enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        gid = self.gid

        sid = self.sid

        enable = self.enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if gid is not UNSET:
            field_dict["gid"] = gid
        if sid is not UNSET:
            field_dict["sid"] = sid
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        gid = d.pop("gid", UNSET)

        sid = d.pop("sid", UNSET)

        enable = d.pop("enable", UNSET)

        snort_ips_state_rule = cls(
            action=action,
            gid=gid,
            sid=sid,
            enable=enable,
        )

        snort_ips_state_rule.additional_properties = d
        return snort_ips_state_rule

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
