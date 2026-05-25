from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_bgp_aspaths_row import FrrBgpAspathsRow


T = TypeVar("T", bound="FrrBgpAspath")


@_attrs_define
class FrrBgpAspath:
    """
    Attributes:
        name (str | Unset): Name

            The name of this AS Path List.
        descr (str | Unset): Description
        row (list[FrrBgpAspathsRow] | Unset):
        id (str | Unset): (readonly) ID assigned to this entry
    """

    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    row: list[FrrBgpAspathsRow] | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descr = self.descr

        row: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if row is not UNSET:
            field_dict["row"] = row
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_bgp_aspaths_row import FrrBgpAspathsRow

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        _row = d.pop("row", UNSET)
        row: list[FrrBgpAspathsRow] | Unset = UNSET
        if _row is not UNSET:
            row = []
            for row_item_data in _row:
                row_item = FrrBgpAspathsRow.from_dict(row_item_data)

                row.append(row_item)

        id = d.pop("id", UNSET)

        frr_bgp_aspath = cls(
            name=name,
            descr=descr,
            row=row,
            id=id,
        )

        frr_bgp_aspath.additional_properties = d
        return frr_bgp_aspath

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
