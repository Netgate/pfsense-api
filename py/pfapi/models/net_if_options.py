from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetIfOptions")


@_attrs_define
class NetIfOptions:
    """
    Attributes:
        blockbogons (bool | Unset):
        blockpriv (bool | Unset):
        mtu (int | Unset):
        mss (int | Unset):
        pcp (int | Unset):
        promisc (bool | Unset):
        member (str | Unset):
        mac (str | Unset):
        mediaopt (str | Unset):
        spoofmac (str | Unset):
        tag (int | Unset):
    """

    blockbogons: bool | Unset = UNSET
    blockpriv: bool | Unset = UNSET
    mtu: int | Unset = UNSET
    mss: int | Unset = UNSET
    pcp: int | Unset = UNSET
    promisc: bool | Unset = UNSET
    member: str | Unset = UNSET
    mac: str | Unset = UNSET
    mediaopt: str | Unset = UNSET
    spoofmac: str | Unset = UNSET
    tag: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blockbogons = self.blockbogons

        blockpriv = self.blockpriv

        mtu = self.mtu

        mss = self.mss

        pcp = self.pcp

        promisc = self.promisc

        member = self.member

        mac = self.mac

        mediaopt = self.mediaopt

        spoofmac = self.spoofmac

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blockbogons is not UNSET:
            field_dict["blockbogons"] = blockbogons
        if blockpriv is not UNSET:
            field_dict["blockpriv"] = blockpriv
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if mss is not UNSET:
            field_dict["mss"] = mss
        if pcp is not UNSET:
            field_dict["pcp"] = pcp
        if promisc is not UNSET:
            field_dict["promisc"] = promisc
        if member is not UNSET:
            field_dict["member"] = member
        if mac is not UNSET:
            field_dict["mac"] = mac
        if mediaopt is not UNSET:
            field_dict["mediaopt"] = mediaopt
        if spoofmac is not UNSET:
            field_dict["spoofmac"] = spoofmac
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blockbogons = d.pop("blockbogons", UNSET)

        blockpriv = d.pop("blockpriv", UNSET)

        mtu = d.pop("mtu", UNSET)

        mss = d.pop("mss", UNSET)

        pcp = d.pop("pcp", UNSET)

        promisc = d.pop("promisc", UNSET)

        member = d.pop("member", UNSET)

        mac = d.pop("mac", UNSET)

        mediaopt = d.pop("mediaopt", UNSET)

        spoofmac = d.pop("spoofmac", UNSET)

        tag = d.pop("tag", UNSET)

        net_if_options = cls(
            blockbogons=blockbogons,
            blockpriv=blockpriv,
            mtu=mtu,
            mss=mss,
            pcp=pcp,
            promisc=promisc,
            member=member,
            mac=mac,
            mediaopt=mediaopt,
            spoofmac=spoofmac,
            tag=tag,
        )

        net_if_options.additional_properties = d
        return net_if_options

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
