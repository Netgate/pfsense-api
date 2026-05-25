from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.arpmon_timed_address import ArpmonTimedAddress


T = TypeVar("T", bound="ArpmonMacState")


@_attrs_define
class ArpmonMacState:
    """
    Attributes:
        mac (str | Unset): MAC address of advertiser
        ip4_addresses (list[ArpmonTimedAddress] | Unset):
        ip6_addresses (list[ArpmonTimedAddress] | Unset):
    """

    mac: str | Unset = UNSET
    ip4_addresses: list[ArpmonTimedAddress] | Unset = UNSET
    ip6_addresses: list[ArpmonTimedAddress] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        ip4_addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ip4_addresses, Unset):
            ip4_addresses = []
            for ip4_addresses_item_data in self.ip4_addresses:
                ip4_addresses_item = ip4_addresses_item_data.to_dict()
                ip4_addresses.append(ip4_addresses_item)

        ip6_addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ip6_addresses, Unset):
            ip6_addresses = []
            for ip6_addresses_item_data in self.ip6_addresses:
                ip6_addresses_item = ip6_addresses_item_data.to_dict()
                ip6_addresses.append(ip6_addresses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ip4_addresses is not UNSET:
            field_dict["ip4_addresses"] = ip4_addresses
        if ip6_addresses is not UNSET:
            field_dict["ip6_addresses"] = ip6_addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.arpmon_timed_address import ArpmonTimedAddress

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        _ip4_addresses = d.pop("ip4_addresses", UNSET)
        ip4_addresses: list[ArpmonTimedAddress] | Unset = UNSET
        if _ip4_addresses is not UNSET:
            ip4_addresses = []
            for ip4_addresses_item_data in _ip4_addresses:
                ip4_addresses_item = ArpmonTimedAddress.from_dict(ip4_addresses_item_data)

                ip4_addresses.append(ip4_addresses_item)

        _ip6_addresses = d.pop("ip6_addresses", UNSET)
        ip6_addresses: list[ArpmonTimedAddress] | Unset = UNSET
        if _ip6_addresses is not UNSET:
            ip6_addresses = []
            for ip6_addresses_item_data in _ip6_addresses:
                ip6_addresses_item = ArpmonTimedAddress.from_dict(ip6_addresses_item_data)

                ip6_addresses.append(ip6_addresses_item)

        arpmon_mac_state = cls(
            mac=mac,
            ip4_addresses=ip4_addresses,
            ip6_addresses=ip6_addresses,
        )

        arpmon_mac_state.additional_properties = d
        return arpmon_mac_state

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
