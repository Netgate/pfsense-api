from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
            enable (bool):
            keep_conf (bool):
            resolve_interval (str):
            resolve_interval_track (bool):
            interface_group (str):
            hide_secrets (bool):
            hide_peers (bool):
    """

    enable: bool
    keep_conf: bool
    resolve_interval: str
    resolve_interval_track: bool
    interface_group: str
    hide_secrets: bool
    hide_peers: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        keep_conf = self.keep_conf

        resolve_interval = self.resolve_interval

        resolve_interval_track = self.resolve_interval_track

        interface_group = self.interface_group

        hide_secrets = self.hide_secrets

        hide_peers = self.hide_peers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "keep_conf": keep_conf,
                "resolve_interval": resolve_interval,
                "resolve_interval_track": resolve_interval_track,
                "interface_group": interface_group,
                "hide_secrets": hide_secrets,
                "hide_peers": hide_peers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable")

        keep_conf = d.pop("keep_conf")

        resolve_interval = d.pop("resolve_interval")

        resolve_interval_track = d.pop("resolve_interval_track")

        interface_group = d.pop("interface_group")

        hide_secrets = d.pop("hide_secrets")

        hide_peers = d.pop("hide_peers")

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
