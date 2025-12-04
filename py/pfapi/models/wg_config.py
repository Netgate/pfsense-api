from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WGConfig")


@_attrs_define
class WGConfig:
    """valid values:
    enable = "on", "off"
    keep_conf = "yes", "no"
    resolve_interval_track = "yes", "no"
    interface_group = "all", "unassigned", "none"
    hide_secrets = "yes", "no"
    hide_peers = "yes", "no"

        Attributes:
            enable (bool | Unset):
            keep_conf (bool | Unset):
            resolve_interval (str | Unset):
            resolve_interval_track (bool | Unset):
            interface_group (str | Unset):
            hide_secrets (bool | Unset):
            hide_peers (bool | Unset):
    """

    enable: bool | Unset = UNSET
    keep_conf: bool | Unset = UNSET
    resolve_interval: str | Unset = UNSET
    resolve_interval_track: bool | Unset = UNSET
    interface_group: str | Unset = UNSET
    hide_secrets: bool | Unset = UNSET
    hide_peers: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        keep_conf = self.keep_conf

        resolve_interval = self.resolve_interval

        resolve_interval_track = self.resolve_interval_track

        interface_group = self.interface_group

        hide_secrets = self.hide_secrets

        hide_peers = self.hide_peers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if keep_conf is not UNSET:
            field_dict["keep_conf"] = keep_conf
        if resolve_interval is not UNSET:
            field_dict["resolve_interval"] = resolve_interval
        if resolve_interval_track is not UNSET:
            field_dict["resolve_interval_track"] = resolve_interval_track
        if interface_group is not UNSET:
            field_dict["interface_group"] = interface_group
        if hide_secrets is not UNSET:
            field_dict["hide_secrets"] = hide_secrets
        if hide_peers is not UNSET:
            field_dict["hide_peers"] = hide_peers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        keep_conf = d.pop("keep_conf", UNSET)

        resolve_interval = d.pop("resolve_interval", UNSET)

        resolve_interval_track = d.pop("resolve_interval_track", UNSET)

        interface_group = d.pop("interface_group", UNSET)

        hide_secrets = d.pop("hide_secrets", UNSET)

        hide_peers = d.pop("hide_peers", UNSET)

        wg_config = cls(
            enable=enable,
            keep_conf=keep_conf,
            resolve_interval=resolve_interval,
            resolve_interval_track=resolve_interval_track,
            interface_group=interface_group,
            hide_secrets=hide_secrets,
            hide_peers=hide_peers,
        )

        wg_config.additional_properties = d
        return wg_config

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
