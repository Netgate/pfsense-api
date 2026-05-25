from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArpingRequest")


@_attrs_define
class ArpingRequest:
    """
    Attributes:
        destination (str | Unset): Address of the destination host
        count (int | Unset): Number of pings to send and listen for
        iface (str | Unset): Interface friendly name
    """

    destination: str | Unset = UNSET
    count: int | Unset = UNSET
    iface: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination = self.destination

        count = self.count

        iface = self.iface

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if count is not UNSET:
            field_dict["count"] = count
        if iface is not UNSET:
            field_dict["iface"] = iface

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination = d.pop("destination", UNSET)

        count = d.pop("count", UNSET)

        iface = d.pop("iface", UNSET)

        arping_request = cls(
            destination=destination,
            count=count,
            iface=iface,
        )

        arping_request.additional_properties = d
        return arping_request

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
