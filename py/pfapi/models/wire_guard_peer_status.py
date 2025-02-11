from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.wg_peer import WGPeer


T = TypeVar("T", bound="WireGuardPeerStatus")


@_attrs_define
class WireGuardPeerStatus:
    """
    Attributes:
        public_key (str):
        preshared_key (str):
        endpoint (str):
        allowed_ips (str):
        latest_handshake (str):
        transfer_rx (str):
        transfer_tx (str):
        persistent_keepalive (str):
        config (WGPeer): valid values:
            enabled = "yes", "no"
    """

    public_key: str
    preshared_key: str
    endpoint: str
    allowed_ips: str
    latest_handshake: str
    transfer_rx: str
    transfer_tx: str
    persistent_keepalive: str
    config: "WGPeer"
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

        config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_key": public_key,
                "preshared_key": preshared_key,
                "endpoint": endpoint,
                "allowed_ips": allowed_ips,
                "latest_handshake": latest_handshake,
                "transfer_rx": transfer_rx,
                "transfer_tx": transfer_tx,
                "persistent_keepalive": persistent_keepalive,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wg_peer import WGPeer

        d = src_dict.copy()
        public_key = d.pop("public_key")

        preshared_key = d.pop("preshared_key")

        endpoint = d.pop("endpoint")

        allowed_ips = d.pop("allowed_ips")

        latest_handshake = d.pop("latest_handshake")

        transfer_rx = d.pop("transfer_rx")

        transfer_tx = d.pop("transfer_tx")

        persistent_keepalive = d.pop("persistent_keepalive")

        config = WGPeer.from_dict(d.pop("config"))

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
