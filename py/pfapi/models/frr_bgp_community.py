from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_bgp_communities_row import FrrBgpCommunitiesRow


T = TypeVar("T", bound="FrrBgpCommunity")


@_attrs_define
class FrrBgpCommunity:
    """
    Attributes:
        name (str | Unset): Name

            The name of this BGP Community.

            Use 1-99 for a standard community list (AS:VAL pairs),
            100-500 for an expanded community list (Regular Expression Matching),
            or enter a text name combined with the selected type.
        descr (str | Unset): Description
        listtype (str | Unset): Community List Type (standard, expanded)

            Type of Community List to specify, which controls how the list operates. The selected type must match the Name
            appropriately.
        row (list[FrrBgpCommunitiesRow] | Unset):
        id (str | Unset): (readonly) ID assigned to this entry
    """

    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    listtype: str | Unset = UNSET
    row: list[FrrBgpCommunitiesRow] | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descr = self.descr

        listtype = self.listtype

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
        if listtype is not UNSET:
            field_dict["listtype"] = listtype
        if row is not UNSET:
            field_dict["row"] = row
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_bgp_communities_row import FrrBgpCommunitiesRow

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        listtype = d.pop("listtype", UNSET)

        _row = d.pop("row", UNSET)
        row: list[FrrBgpCommunitiesRow] | Unset = UNSET
        if _row is not UNSET:
            row = []
            for row_item_data in _row:
                row_item = FrrBgpCommunitiesRow.from_dict(row_item_data)

                row.append(row_item)

        id = d.pop("id", UNSET)

        frr_bgp_community = cls(
            name=name,
            descr=descr,
            listtype=listtype,
            row=row,
            id=id,
        )

        frr_bgp_community.additional_properties = d
        return frr_bgp_community

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
