from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wg_peer import WGPeer


T = TypeVar("T", bound="WireGuardPeerStatus")


@_attrs_define
class WireGuardPeerStatus:
    """
    Attributes:
        public_key (Union[Unset, str]):
        preshared_key (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        allowed_ips (Union[Unset, str]):
        latest_handshake (Union[Unset, str]):
        transfer_rx (Union[Unset, str]):
        transfer_tx (Union[Unset, str]):
        persistent_keepalive (Union[Unset, str]):
        config (Union[Unset, WGPeer]): valid values:
            enabled = "yes", "no"
    """

    public_key: Union[Unset, str] = UNSET
    preshared_key: Union[Unset, str] = UNSET
    endpoint: Union[Unset, str] = UNSET
    allowed_ips: Union[Unset, str] = UNSET
    latest_handshake: Union[Unset, str] = UNSET
    transfer_rx: Union[Unset, str] = UNSET
    transfer_tx: Union[Unset, str] = UNSET
    persistent_keepalive: Union[Unset, str] = UNSET
    config: Union[Unset, "WGPeer"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        public_key = self.public_key

        preshared_key = self.preshared_key

        endpoint = self.endpoint

        allowed_ips = self.allowed_ips

        latest_handshake = self.latest_handshake

        transfer_rx = self.transfer_rx

        transfer_tx = self.transfer_tx

        persistent_keepalive = self.persistent_keepalive

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if preshared_key is not UNSET:
            field_dict["preshared_key"] = preshared_key
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if allowed_ips is not UNSET:
            field_dict["allowed_ips"] = allowed_ips
        if latest_handshake is not UNSET:
            field_dict["latest_handshake"] = latest_handshake
        if transfer_rx is not UNSET:
            field_dict["transfer_rx"] = transfer_rx
        if transfer_tx is not UNSET:
            field_dict["transfer_tx"] = transfer_tx
        if persistent_keepalive is not UNSET:
            field_dict["persistent_keepalive"] = persistent_keepalive
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wg_peer import WGPeer

        d = src_dict.copy()
        public_key = d.pop("public_key", UNSET)

        preshared_key = d.pop("preshared_key", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        allowed_ips = d.pop("allowed_ips", UNSET)

        latest_handshake = d.pop("latest_handshake", UNSET)

        transfer_rx = d.pop("transfer_rx", UNSET)

        transfer_tx = d.pop("transfer_tx", UNSET)

        persistent_keepalive = d.pop("persistent_keepalive", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, WGPeer]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = WGPeer.from_dict(_config)

        wire_guard_peer_status = cls(
            public_key=public_key,
            preshared_key=preshared_key,
            endpoint=endpoint,
            allowed_ips=allowed_ips,
            latest_handshake=latest_handshake,
            transfer_rx=transfer_rx,
            transfer_tx=transfer_tx,
            persistent_keepalive=persistent_keepalive,
            config=config,
        )

        wire_guard_peer_status.additional_properties = d
        return wire_guard_peer_status

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
