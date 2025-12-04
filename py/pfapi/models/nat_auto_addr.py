from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NATAutoAddr")


@_attrs_define
class NATAutoAddr:
    """
    Attributes:
        network (str | Unset):
        any_ (bool | Unset):
    """

    network: str | Unset = UNSET
    any_: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network

        any_ = self.any_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network is not UNSET:
            field_dict["network"] = network
        if any_ is not UNSET:
            field_dict["any"] = any_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network = d.pop("network", UNSET)

        any_ = d.pop("any", UNSET)

        nat_auto_addr = cls(
            network=network,
            any_=any_,
        )

        nat_auto_addr.additional_properties = d
        return nat_auto_addr

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
