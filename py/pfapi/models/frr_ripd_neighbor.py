from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrRipdNeighbor")


@_attrs_define
class FrrRipdNeighbor:
    """
    Attributes:
        neighbor (str | Unset): (RIP Neighbors) RIP Neighbor IPv4 Address
        descr (str | Unset): (RIP Neighbors) Description
        id (str | Unset): (readonly) ID assigned to this entry
    """

    neighbor: str | Unset = UNSET
    descr: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        neighbor = self.neighbor

        descr = self.descr

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if neighbor is not UNSET:
            field_dict["neighbor"] = neighbor
        if descr is not UNSET:
            field_dict["descr"] = descr
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        neighbor = d.pop("neighbor", UNSET)

        descr = d.pop("descr", UNSET)

        id = d.pop("id", UNSET)

        frr_ripd_neighbor = cls(
            neighbor=neighbor,
            descr=descr,
            id=id,
        )

        frr_ripd_neighbor.additional_properties = d
        return frr_ripd_neighbor

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
