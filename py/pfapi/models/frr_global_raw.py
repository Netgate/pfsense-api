from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_global_tcp_md_5_peer import FrrGlobalTcpMd5Peer


T = TypeVar("T", bound="FrrGlobalRaw")


@_attrs_define
class FrrGlobalRaw:
    """
    Attributes:
        tcp_md5_peers (list[FrrGlobalTcpMd5Peer] | Unset):
        frr (str | Unset): (RAW Configuration Files) SAVED frr.conf

            Note: If a configuration is placed in this box and saved, the GUI settings (in all other tabs) will be
            overridden with the contents of this box.
            To get back the GUI configuration save this form below once with empty input fields.
        frrrunning (str | Unset): (RAW Configuration Files) RUNNING frr.conf

            Note: This is the CURRENT RUNNING CONFIG from "/var/etc/frr/frr.conf".
    """

    tcp_md5_peers: list[FrrGlobalTcpMd5Peer] | Unset = UNSET
    frr: str | Unset = UNSET
    frrrunning: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tcp_md5_peers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tcp_md5_peers, Unset):
            tcp_md5_peers = []
            for tcp_md5_peers_item_data in self.tcp_md5_peers:
                tcp_md5_peers_item = tcp_md5_peers_item_data.to_dict()
                tcp_md5_peers.append(tcp_md5_peers_item)

        frr = self.frr

        frrrunning = self.frrrunning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tcp_md5_peers is not UNSET:
            field_dict["tcp_md5_peers"] = tcp_md5_peers
        if frr is not UNSET:
            field_dict["frr"] = frr
        if frrrunning is not UNSET:
            field_dict["frrrunning"] = frrrunning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_global_tcp_md_5_peer import FrrGlobalTcpMd5Peer

        d = dict(src_dict)
        _tcp_md5_peers = d.pop("tcp_md5_peers", UNSET)
        tcp_md5_peers: list[FrrGlobalTcpMd5Peer] | Unset = UNSET
        if _tcp_md5_peers is not UNSET:
            tcp_md5_peers = []
            for tcp_md5_peers_item_data in _tcp_md5_peers:
                tcp_md5_peers_item = FrrGlobalTcpMd5Peer.from_dict(tcp_md5_peers_item_data)

                tcp_md5_peers.append(tcp_md5_peers_item)

        frr = d.pop("frr", UNSET)

        frrrunning = d.pop("frrrunning", UNSET)

        frr_global_raw = cls(
            tcp_md5_peers=tcp_md5_peers,
            frr=frr,
            frrrunning=frrrunning,
        )

        frr_global_raw.additional_properties = d
        return frr_global_raw

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
