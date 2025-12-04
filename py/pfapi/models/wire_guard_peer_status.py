from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        public_key (str | Unset):
        preshared_key (str | Unset):
        endpoint (str | Unset):
        allowed_ips (str | Unset):
        latest_handshake (str | Unset):
        transfer_rx (str | Unset):
        transfer_tx (str | Unset):
        persistent_keepalive (str | Unset):
        config (WGPeer | Unset): valid values:
            enabled = "yes", "no"
    """

    public_key: str | Unset = UNSET
    preshared_key: str | Unset = UNSET
    endpoint: str | Unset = UNSET
    allowed_ips: str | Unset = UNSET
    latest_handshake: str | Unset = UNSET
    transfer_rx: str | Unset = UNSET
    transfer_tx: str | Unset = UNSET
    persistent_keepalive: str | Unset = UNSET
    config: WGPeer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        preshared_key = self.preshared_key

        endpoint = self.endpoint

        allowed_ips = self.allowed_ips

        latest_handshake = self.latest_handshake

        transfer_rx = self.transfer_rx

        transfer_tx = self.transfer_tx

        persistent_keepalive = self.persistent_keepalive

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wg_peer import WGPeer

        d = dict(src_dict)
        public_key = d.pop("public_key", UNSET)

        preshared_key = d.pop("preshared_key", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        allowed_ips = d.pop("allowed_ips", UNSET)

        latest_handshake = d.pop("latest_handshake", UNSET)

        transfer_rx = d.pop("transfer_rx", UNSET)

        transfer_tx = d.pop("transfer_tx", UNSET)

        persistent_keepalive = d.pop("persistent_keepalive", UNSET)

        _config = d.pop("config", UNSET)
        config: WGPeer | Unset
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
