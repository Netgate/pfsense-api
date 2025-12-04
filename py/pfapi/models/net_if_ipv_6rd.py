from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetIfIpv6RD")


@_attrs_define
class NetIfIpv6RD:
    """
    Attributes:
        prefix_6rd (str | Unset):
        gateway_6rd (str | Unset):
        track6_prefix_id_hex (str | Unset):
        prefix_6rd_v4plen (str | Unset):
        track6_interface (str | Unset):
    """

    prefix_6rd: str | Unset = UNSET
    gateway_6rd: str | Unset = UNSET
    track6_prefix_id_hex: str | Unset = UNSET
    prefix_6rd_v4plen: str | Unset = UNSET
    track6_interface: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prefix_6rd = self.prefix_6rd

        gateway_6rd = self.gateway_6rd

        track6_prefix_id_hex = self.track6_prefix_id_hex

        prefix_6rd_v4plen = self.prefix_6rd_v4plen

        track6_interface = self.track6_interface

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prefix_6rd is not UNSET:
            field_dict["prefix_6rd"] = prefix_6rd
        if gateway_6rd is not UNSET:
            field_dict["gateway_6rd"] = gateway_6rd
        if track6_prefix_id_hex is not UNSET:
            field_dict["track6_prefix_id_hex"] = track6_prefix_id_hex
        if prefix_6rd_v4plen is not UNSET:
            field_dict["prefix_6rd_v4plen"] = prefix_6rd_v4plen
        if track6_interface is not UNSET:
            field_dict["track6_interface"] = track6_interface

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prefix_6rd = d.pop("prefix_6rd", UNSET)

        gateway_6rd = d.pop("gateway_6rd", UNSET)

        track6_prefix_id_hex = d.pop("track6_prefix_id_hex", UNSET)

        prefix_6rd_v4plen = d.pop("prefix_6rd_v4plen", UNSET)

        track6_interface = d.pop("track6_interface", UNSET)

        net_if_ipv_6rd = cls(
            prefix_6rd=prefix_6rd,
            gateway_6rd=gateway_6rd,
            track6_prefix_id_hex=track6_prefix_id_hex,
            prefix_6rd_v4plen=prefix_6rd_v4plen,
            track6_interface=track6_interface,
        )

        net_if_ipv_6rd.additional_properties = d
        return net_if_ipv_6rd

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
