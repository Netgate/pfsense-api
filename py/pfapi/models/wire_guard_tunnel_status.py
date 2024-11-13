from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wg_tunnel import WGTunnel
    from ..models.wire_guard_peer_status import WireGuardPeerStatus


T = TypeVar("T", bound="WireGuardTunnelStatus")


@_attrs_define
class WireGuardTunnelStatus:
    """
    Attributes:
        private_key (Union[Unset, str]):
        public_key (Union[Unset, str]):
        listen_port (Union[Unset, str]):
        fwmark (Union[Unset, str]):
        status (Union[Unset, str]):
        transfer_rx (Union[Unset, int]):
        transfer_tx (Union[Unset, int]):
        inpkts (Union[Unset, int]):
        outpkts (Union[Unset, int]):
        mtu (Union[Unset, int]):
        config (Union[Unset, WGTunnel]): valid values:
            enabled = "yes", "no"
        peers (Union[Unset, List['WireGuardPeerStatus']]):
    """

    private_key: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    listen_port: Union[Unset, str] = UNSET
    fwmark: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    transfer_rx: Union[Unset, int] = UNSET
    transfer_tx: Union[Unset, int] = UNSET
    inpkts: Union[Unset, int] = UNSET
    outpkts: Union[Unset, int] = UNSET
    mtu: Union[Unset, int] = UNSET
    config: Union[Unset, "WGTunnel"] = UNSET
    peers: Union[Unset, List["WireGuardPeerStatus"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        private_key = self.private_key

        public_key = self.public_key

        listen_port = self.listen_port

        fwmark = self.fwmark

        status = self.status

        transfer_rx = self.transfer_rx

        transfer_tx = self.transfer_tx

        inpkts = self.inpkts

        outpkts = self.outpkts

        mtu = self.mtu

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        peers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.peers, Unset):
            peers = []
            for peers_item_data in self.peers:
                peers_item = peers_item_data.to_dict()
                peers.append(peers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if private_key is not UNSET:
            field_dict["private_key"] = private_key
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if listen_port is not UNSET:
            field_dict["listen_port"] = listen_port
        if fwmark is not UNSET:
            field_dict["fwmark"] = fwmark
        if status is not UNSET:
            field_dict["status"] = status
        if transfer_rx is not UNSET:
            field_dict["transfer_rx"] = transfer_rx
        if transfer_tx is not UNSET:
            field_dict["transfer_tx"] = transfer_tx
        if inpkts is not UNSET:
            field_dict["inpkts"] = inpkts
        if outpkts is not UNSET:
            field_dict["outpkts"] = outpkts
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if config is not UNSET:
            field_dict["config"] = config
        if peers is not UNSET:
            field_dict["peers"] = peers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wg_tunnel import WGTunnel
        from ..models.wire_guard_peer_status import WireGuardPeerStatus

        d = src_dict.copy()
        private_key = d.pop("private_key", UNSET)

        public_key = d.pop("public_key", UNSET)

        listen_port = d.pop("listen_port", UNSET)

        fwmark = d.pop("fwmark", UNSET)

        status = d.pop("status", UNSET)

        transfer_rx = d.pop("transfer_rx", UNSET)

        transfer_tx = d.pop("transfer_tx", UNSET)

        inpkts = d.pop("inpkts", UNSET)

        outpkts = d.pop("outpkts", UNSET)

        mtu = d.pop("mtu", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, WGTunnel]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = WGTunnel.from_dict(_config)

        peers = []
        _peers = d.pop("peers", UNSET)
        for peers_item_data in _peers or []:
            peers_item = WireGuardPeerStatus.from_dict(peers_item_data)

            peers.append(peers_item)

        wire_guard_tunnel_status = cls(
            private_key=private_key,
            public_key=public_key,
            listen_port=listen_port,
            fwmark=fwmark,
            status=status,
            transfer_rx=transfer_rx,
            transfer_tx=transfer_tx,
            inpkts=inpkts,
            outpkts=outpkts,
            mtu=mtu,
            config=config,
            peers=peers,
        )

        wire_guard_tunnel_status.additional_properties = d
        return wire_guard_tunnel_status

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
