from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_ospfd_neighbor import FrrOspfdNeighbor


T = TypeVar("T", bound="FrrOspfdNeighborsList")


@_attrs_define
class FrrOspfdNeighborsList:
    """
    Attributes:
        ospfdneighbors (list[FrrOspfdNeighbor] | Unset):
    """

    ospfdneighbors: list[FrrOspfdNeighbor] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ospfdneighbors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ospfdneighbors, Unset):
            ospfdneighbors = []
            for ospfdneighbors_item_data in self.ospfdneighbors:
                ospfdneighbors_item = ospfdneighbors_item_data.to_dict()
                ospfdneighbors.append(ospfdneighbors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ospfdneighbors is not UNSET:
            field_dict["ospfdneighbors"] = ospfdneighbors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_ospfd_neighbor import FrrOspfdNeighbor

        d = dict(src_dict)
        _ospfdneighbors = d.pop("ospfdneighbors", UNSET)
        ospfdneighbors: list[FrrOspfdNeighbor] | Unset = UNSET
        if _ospfdneighbors is not UNSET:
            ospfdneighbors = []
            for ospfdneighbors_item_data in _ospfdneighbors:
                ospfdneighbors_item = FrrOspfdNeighbor.from_dict(ospfdneighbors_item_data)

                ospfdneighbors.append(ospfdneighbors_item)

        frr_ospfd_neighbors_list = cls(
            ospfdneighbors=ospfdneighbors,
        )

        frr_ospfd_neighbors_list.additional_properties = d
        return frr_ospfd_neighbors_list

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
