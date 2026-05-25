from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrGlobalTcpMd5Peer")


@_attrs_define
class FrrGlobalTcpMd5Peer:
    """
    Attributes:
        tcpsigsrc (str | Unset): Local Source Address
        tcpsigdst (str | Unset): Remote Peer Address
        tcpsigpw (str | Unset): MD5 Password
        tcpsigbidir (str | Unset): Bidirectional SA
    """

    tcpsigsrc: str | Unset = UNSET
    tcpsigdst: str | Unset = UNSET
    tcpsigpw: str | Unset = UNSET
    tcpsigbidir: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tcpsigsrc = self.tcpsigsrc

        tcpsigdst = self.tcpsigdst

        tcpsigpw = self.tcpsigpw

        tcpsigbidir = self.tcpsigbidir

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tcpsigsrc is not UNSET:
            field_dict["tcpsigsrc"] = tcpsigsrc
        if tcpsigdst is not UNSET:
            field_dict["tcpsigdst"] = tcpsigdst
        if tcpsigpw is not UNSET:
            field_dict["tcpsigpw"] = tcpsigpw
        if tcpsigbidir is not UNSET:
            field_dict["tcpsigbidir"] = tcpsigbidir

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tcpsigsrc = d.pop("tcpsigsrc", UNSET)

        tcpsigdst = d.pop("tcpsigdst", UNSET)

        tcpsigpw = d.pop("tcpsigpw", UNSET)

        tcpsigbidir = d.pop("tcpsigbidir", UNSET)

        frr_global_tcp_md_5_peer = cls(
            tcpsigsrc=tcpsigsrc,
            tcpsigdst=tcpsigdst,
            tcpsigpw=tcpsigpw,
            tcpsigbidir=tcpsigbidir,
        )

        frr_global_tcp_md_5_peer.additional_properties = d
        return frr_global_tcp_md_5_peer

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
