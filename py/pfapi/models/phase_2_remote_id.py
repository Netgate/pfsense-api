from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Phase2RemoteId")


@_attrs_define
class Phase2RemoteId:
    """
    Attributes:
        type_ (str | Unset):
        address (str | Unset):
        netbits (str | Unset):
    """

    type_: str | Unset = UNSET
    address: str | Unset = UNSET
    netbits: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        address = self.address

        netbits = self.netbits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if address is not UNSET:
            field_dict["address"] = address
        if netbits is not UNSET:
            field_dict["netbits"] = netbits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        address = d.pop("address", UNSET)

        netbits = d.pop("netbits", UNSET)

        phase_2_remote_id = cls(
            type_=type_,
            address=address,
            netbits=netbits,
        )

        phase_2_remote_id.additional_properties = d
        return phase_2_remote_id

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
