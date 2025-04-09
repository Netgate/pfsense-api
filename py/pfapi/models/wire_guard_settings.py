from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wg_config import WGConfig
    from ..models.wg_peers import WGPeers
    from ..models.wg_tunnels import WGTunnels


T = TypeVar("T", bound="WireGuardSettings")


@_attrs_define
class WireGuardSettings:
    """
    Attributes:
        config (Union[Unset, List['WGConfig']]):
        tunnels (Union[Unset, WGTunnels]):
        peers (Union[Unset, WGPeers]):
    """

    config: Union[Unset, List["WGConfig"]] = UNSET
    tunnels: Union[Unset, "WGTunnels"] = UNSET
    peers: Union[Unset, "WGPeers"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.config, Unset):
            config = []
            for config_item_data in self.config:
                config_item = config_item_data.to_dict()
                config.append(config_item)

        tunnels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tunnels, Unset):
            tunnels = self.tunnels.to_dict()

        peers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.peers, Unset):
            peers = self.peers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if tunnels is not UNSET:
            field_dict["tunnels"] = tunnels
        if peers is not UNSET:
            field_dict["peers"] = peers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wg_config import WGConfig
        from ..models.wg_peers import WGPeers
        from ..models.wg_tunnels import WGTunnels

        d = src_dict.copy()
        config = []
        _config = d.pop("config", UNSET)
        for config_item_data in _config or []:
            config_item = WGConfig.from_dict(config_item_data)

            config.append(config_item)

        _tunnels = d.pop("tunnels", UNSET)
        tunnels: Union[Unset, WGTunnels]
        if isinstance(_tunnels, Unset):
            tunnels = UNSET
        else:
            tunnels = WGTunnels.from_dict(_tunnels)

        _peers = d.pop("peers", UNSET)
        peers: Union[Unset, WGPeers]
        if isinstance(_peers, Unset):
            peers = UNSET
        else:
            peers = WGPeers.from_dict(_peers)

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
