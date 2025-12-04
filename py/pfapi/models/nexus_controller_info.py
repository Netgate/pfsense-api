from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NexusControllerInfo")


@_attrs_define
class NexusControllerInfo:
    """
    Attributes:
        addresses (list[str] | Unset):
        public_key (str | Unset):
        vpn_addr (str | Unset):
    """

    addresses: list[str] | Unset = UNSET
    public_key: str | Unset = UNSET
    vpn_addr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addresses: list[str] | Unset = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        public_key = self.public_key

        vpn_addr = self.vpn_addr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if vpn_addr is not UNSET:
            field_dict["vpn_addr"] = vpn_addr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        addresses = cast(list[str], d.pop("addresses", UNSET))

        public_key = d.pop("public_key", UNSET)

        vpn_addr = d.pop("vpn_addr", UNSET)

        nexus_controller_info = cls(
            addresses=addresses,
            public_key=public_key,
            vpn_addr=vpn_addr,
        )

        nexus_controller_info.additional_properties = d
        return nexus_controller_info

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
