from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NATAddrPort")


@_attrs_define
class NATAddrPort:
    """
    Attributes:
        address (str | Unset):
        type_ (str | Unset):
        port (str | Unset):
        not_ (bool | Unset):
    """

    address: str | Unset = UNSET
    type_: str | Unset = UNSET
    port: str | Unset = UNSET
    not_: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        type_ = self.type_

        port = self.port

        not_ = self.not_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if type_ is not UNSET:
            field_dict["type"] = type_
        if port is not UNSET:
            field_dict["port"] = port
        if not_ is not UNSET:
            field_dict["not"] = not_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        type_ = d.pop("type", UNSET)

        port = d.pop("port", UNSET)

        not_ = d.pop("not", UNSET)

        nat_addr_port = cls(
            address=address,
            type_=type_,
            port=port,
            not_=not_,
        )

        nat_addr_port.additional_properties = d
        return nat_addr_port

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
