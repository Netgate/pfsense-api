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
        private_key (str):
        public_key (str):
        listen_port (str):
        fwmark (str):
        status (str):
        transfer_rx (int):
        transfer_tx (int):
        inpkts (int):
        outpkts (int):
        mtu (int):
        config (WGTunnel): valid values:
            enabled = "yes", "no"
        peers (Union[Unset, List['WireGuardPeerStatus']]):
    """

    private_key: str
    public_key: str
    listen_port: str
    fwmark: str
    status: str
    transfer_rx: int
    transfer_tx: int
    inpkts: int
    outpkts: int
    mtu: int
    config: "WGTunnel"
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

        config = self.config.to_dict()

        peers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.peers, Unset):
            peers = []
            for peers_item_data in self.peers:
                peers_item = peers_item_data.to_dict()
                peers.append(peers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "private_key": private_key,
                "public_key": public_key,
                "listen_port": listen_port,
                "fwmark": fwmark,
                "status": status,
                "transfer_rx": transfer_rx,
                "transfer_tx": transfer_tx,
                "inpkts": inpkts,
                "outpkts": outpkts,
                "mtu": mtu,
                "config": config,
            }
        )
        if peers is not UNSET:
            field_dict["peers"] = peers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wg_tunnel import WGTunnel
        from ..models.wire_guard_peer_status import WireGuardPeerStatus

        d = src_dict.copy()
        private_key = d.pop("private_key")

        public_key = d.pop("public_key")

        listen_port = d.pop("listen_port")

        fwmark = d.pop("fwmark")

        status = d.pop("status")

        transfer_rx = d.pop("transfer_rx")

        transfer_tx = d.pop("transfer_tx")

        inpkts = d.pop("inpkts")

        outpkts = d.pop("outpkts")

        mtu = d.pop("mtu")

        config = WGTunnel.from_dict(d.pop("config"))

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
