from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortRule")


@_attrs_define
class SnortRule:
    """
    Attributes:
        action (str | Unset): alert, block, drop, log, pass, react, reject, rewrite
        gid (str | Unset): generator id
        sid (str | Unset): signature id
        proto (str | Unset): protocol
        src (str | Unset): source address
        src_port (str | Unset): source port
        dst (str | Unset): destination address
        dst_port (str | Unset): destination port
        msg (str | Unset): message/information about the rule
        rawrule (str | Unset): original rule definition
        orig_disabled (bool | Unset): disabled in original ruleset
        user_disabled (bool | Unset): user explicitly disabled
        ips_enabled (bool | Unset): IPS policy enabled, only available in per-interface config
        user_override (str | Unset): user override of IPS policy (enable or disable)
        cat (str | Unset): category (file) of rule
        ruleset (str | Unset): name of ruleset containing the rule
    """

    action: str | Unset = UNSET
    gid: str | Unset = UNSET
    sid: str | Unset = UNSET
    proto: str | Unset = UNSET
    src: str | Unset = UNSET
    src_port: str | Unset = UNSET
    dst: str | Unset = UNSET
    dst_port: str | Unset = UNSET
    msg: str | Unset = UNSET
    rawrule: str | Unset = UNSET
    orig_disabled: bool | Unset = UNSET
    user_disabled: bool | Unset = UNSET
    ips_enabled: bool | Unset = UNSET
    user_override: str | Unset = UNSET
    cat: str | Unset = UNSET
    ruleset: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        gid = self.gid

        sid = self.sid

        proto = self.proto

        src = self.src

        src_port = self.src_port

        dst = self.dst

        dst_port = self.dst_port

        msg = self.msg

        rawrule = self.rawrule

        orig_disabled = self.orig_disabled

        user_disabled = self.user_disabled

        ips_enabled = self.ips_enabled

        user_override = self.user_override

        cat = self.cat

        ruleset = self.ruleset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if gid is not UNSET:
            field_dict["gid"] = gid
        if sid is not UNSET:
            field_dict["sid"] = sid
        if proto is not UNSET:
            field_dict["proto"] = proto
        if src is not UNSET:
            field_dict["src"] = src
        if src_port is not UNSET:
            field_dict["src_port"] = src_port
        if dst is not UNSET:
            field_dict["dst"] = dst
        if dst_port is not UNSET:
            field_dict["dst_port"] = dst_port
        if msg is not UNSET:
            field_dict["msg"] = msg
        if rawrule is not UNSET:
            field_dict["rawrule"] = rawrule
        if orig_disabled is not UNSET:
            field_dict["orig_disabled"] = orig_disabled
        if user_disabled is not UNSET:
            field_dict["user_disabled"] = user_disabled
        if ips_enabled is not UNSET:
            field_dict["ips_enabled"] = ips_enabled
        if user_override is not UNSET:
            field_dict["user_override"] = user_override
        if cat is not UNSET:
            field_dict["cat"] = cat
        if ruleset is not UNSET:
            field_dict["ruleset"] = ruleset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        gid = d.pop("gid", UNSET)

        sid = d.pop("sid", UNSET)

        proto = d.pop("proto", UNSET)

        src = d.pop("src", UNSET)

        src_port = d.pop("src_port", UNSET)

        dst = d.pop("dst", UNSET)

        dst_port = d.pop("dst_port", UNSET)

        msg = d.pop("msg", UNSET)

        rawrule = d.pop("rawrule", UNSET)

        orig_disabled = d.pop("orig_disabled", UNSET)

        user_disabled = d.pop("user_disabled", UNSET)

        ips_enabled = d.pop("ips_enabled", UNSET)

        user_override = d.pop("user_override", UNSET)

        cat = d.pop("cat", UNSET)

        ruleset = d.pop("ruleset", UNSET)

        snort_rule = cls(
            action=action,
            gid=gid,
            sid=sid,
            proto=proto,
            src=src,
            src_port=src_port,
            dst=dst,
            dst_port=dst_port,
            msg=msg,
            rawrule=rawrule,
            orig_disabled=orig_disabled,
            user_disabled=user_disabled,
            ips_enabled=ips_enabled,
            user_override=user_override,
            cat=cat,
            ruleset=ruleset,
        )

        snort_rule.additional_properties = d
        return snort_rule

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
