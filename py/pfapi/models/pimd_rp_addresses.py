from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pimd_rp_address import PimdRpAddress


T = TypeVar("T", bound="PimdRpAddresses")


@_attrs_define
class PimdRpAddresses:
    """
    Attributes:
        addresses (list[PimdRpAddress] | Unset):
    """

    addresses: list[PimdRpAddress] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pimd_rp_address import PimdRpAddress

        d = dict(src_dict)
        _addresses = d.pop("addresses", UNSET)
        addresses: list[PimdRpAddress] | Unset = UNSET
        if _addresses is not UNSET:
            addresses = []
            for addresses_item_data in _addresses:
                addresses_item = PimdRpAddress.from_dict(addresses_item_data)

                addresses.append(addresses_item)

        pimd_rp_addresses = cls(
            addresses=addresses,
        )

        pimd_rp_addresses.additional_properties = d
        return pimd_rp_addresses

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
