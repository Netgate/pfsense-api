from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_ripd_neighbor import FrrRipdNeighbor


T = TypeVar("T", bound="FrrRipdNeighborsList")


@_attrs_define
class FrrRipdNeighborsList:
    """
    Attributes:
        ripdneighbors (list[FrrRipdNeighbor] | Unset):
    """

    ripdneighbors: list[FrrRipdNeighbor] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ripdneighbors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ripdneighbors, Unset):
            ripdneighbors = []
            for ripdneighbors_item_data in self.ripdneighbors:
                ripdneighbors_item = ripdneighbors_item_data.to_dict()
                ripdneighbors.append(ripdneighbors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ripdneighbors is not UNSET:
            field_dict["ripdneighbors"] = ripdneighbors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_ripd_neighbor import FrrRipdNeighbor

        d = dict(src_dict)
        _ripdneighbors = d.pop("ripdneighbors", UNSET)
        ripdneighbors: list[FrrRipdNeighbor] | Unset = UNSET
        if _ripdneighbors is not UNSET:
            ripdneighbors = []
            for ripdneighbors_item_data in _ripdneighbors:
                ripdneighbors_item = FrrRipdNeighbor.from_dict(ripdneighbors_item_data)

                ripdneighbors.append(ripdneighbors_item)

        frr_ripd_neighbors_list = cls(
            ripdneighbors=ripdneighbors,
        )

        frr_ripd_neighbors_list.additional_properties = d
        return frr_ripd_neighbors_list

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
