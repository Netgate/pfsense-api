from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.wg_config import WGConfig
    from ..models.wg_peers import WGPeers
    from ..models.wg_tunnels import WGTunnels


T = TypeVar("T", bound="WireGuardSettings")


@_attrs_define
class WireGuardSettings:
    """
    Attributes:
        config (List['WGConfig']):
        tunnels (WGTunnels):
        peers (WGPeers):
    """

    config: List["WGConfig"]
    tunnels: "WGTunnels"
    peers: "WGPeers"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config = []
        for config_item_data in self.config:
            config_item = config_item_data.to_dict()
            config.append(config_item)

        tunnels = self.tunnels.to_dict()

        peers = self.peers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "tunnels": tunnels,
                "peers": peers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wg_config import WGConfig
        from ..models.wg_peers import WGPeers
        from ..models.wg_tunnels import WGTunnels

        d = src_dict.copy()
        config = []
        _config = d.pop("config")
        for config_item_data in _config:
            config_item = WGConfig.from_dict(config_item_data)

            config.append(config_item)

        tunnels = WGTunnels.from_dict(d.pop("tunnels"))

        peers = WGPeers.from_dict(d.pop("peers"))

        wire_guard_settings = cls(
            config=config,
            tunnels=tunnels,
            peers=peers,
        )

        wire_guard_settings.additional_properties = d
        return wire_guard_settings

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
