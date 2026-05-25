from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_ospfd_areas_row import FrrOspfdAreasRow


T = TypeVar("T", bound="FrrOspfdArea")


@_attrs_define
class FrrOspfdArea:
    """
    Attributes:
        area (str | Unset): (Area Options) Area

            The ID for this area.
        descr (str | Unset): (Area Options) Description
        type_ (str | Unset): (Area Options) Area Type (none, stub, nosum, nssa, nssanosum)

            Defines how this area behaves
        defaultcost (str | Unset): (Area Options) Default Route Cost

            Cost applied to default route summary LSA messages sent to stub areas (0-16777215)
        shortcut (str | Unset): (Area Options) ABR Shortcut (default, enable, disable)

            Advertises the area as capable of using ABR shortcut behavior, if enabled in the OSPF Advanced Settings
        authtype (str | Unset): (Authentication) Authentication Type (, digest, simple)

            The type of OSPF authentication used by all routers in this area.
            This type must match all neighbors.

            Using Message Digest is the best practice as Simple Password authentication is weak.
        row (list[FrrOspfdAreasRow] | Unset):
        exportlist (str | Unset): (ABR Summary Route Filtering) Export List

            Uses this access list to filter summary route information transmitted to OSPF peers when acting as an ABR
        importlist (str | Unset): (ABR Summary Route Filtering) Import List

            Uses this access list to filter summary route information received from OSPF peers when acting as an ABR
        filterlist_out (str | Unset): (ABR Summary Route Filtering) Filter List (Out)

            Uses a prefix list to filter summary route information transmitted to OSPF peers when acting as an ABR
        filterlist_in (str | Unset): (ABR Summary Route Filtering) Filter List (In)

            Uses a prefix list to filter summary route information received from OSPF peers when acting as an ABR
        id (str | Unset): (readonly) ID
    """

    area: str | Unset = UNSET
    descr: str | Unset = UNSET
    type_: str | Unset = UNSET
    defaultcost: str | Unset = UNSET
    shortcut: str | Unset = UNSET
    authtype: str | Unset = UNSET
    row: list[FrrOspfdAreasRow] | Unset = UNSET
    exportlist: str | Unset = UNSET
    importlist: str | Unset = UNSET
    filterlist_out: str | Unset = UNSET
    filterlist_in: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area = self.area

        descr = self.descr

        type_ = self.type_

        defaultcost = self.defaultcost

        shortcut = self.shortcut

        authtype = self.authtype

        row: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        exportlist = self.exportlist

        importlist = self.importlist

        filterlist_out = self.filterlist_out

        filterlist_in = self.filterlist_in

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area is not UNSET:
            field_dict["area"] = area
        if descr is not UNSET:
            field_dict["descr"] = descr
        if type_ is not UNSET:
            field_dict["type"] = type_
        if defaultcost is not UNSET:
            field_dict["defaultcost"] = defaultcost
        if shortcut is not UNSET:
            field_dict["shortcut"] = shortcut
        if authtype is not UNSET:
            field_dict["authtype"] = authtype
        if row is not UNSET:
            field_dict["row"] = row
        if exportlist is not UNSET:
            field_dict["exportlist"] = exportlist
        if importlist is not UNSET:
            field_dict["importlist"] = importlist
        if filterlist_out is not UNSET:
            field_dict["filterlist_out"] = filterlist_out
        if filterlist_in is not UNSET:
            field_dict["filterlist_in"] = filterlist_in
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_ospfd_areas_row import FrrOspfdAreasRow

        d = dict(src_dict)
        area = d.pop("area", UNSET)

        descr = d.pop("descr", UNSET)

        type_ = d.pop("type", UNSET)

        defaultcost = d.pop("defaultcost", UNSET)

        shortcut = d.pop("shortcut", UNSET)

        authtype = d.pop("authtype", UNSET)

        _row = d.pop("row", UNSET)
        row: list[FrrOspfdAreasRow] | Unset = UNSET
        if _row is not UNSET:
            row = []
            for row_item_data in _row:
                row_item = FrrOspfdAreasRow.from_dict(row_item_data)

                row.append(row_item)

        exportlist = d.pop("exportlist", UNSET)

        importlist = d.pop("importlist", UNSET)

        filterlist_out = d.pop("filterlist_out", UNSET)

        filterlist_in = d.pop("filterlist_in", UNSET)

        id = d.pop("id", UNSET)

        frr_ospfd_area = cls(
            area=area,
            descr=descr,
            type_=type_,
            defaultcost=defaultcost,
            shortcut=shortcut,
            authtype=authtype,
            row=row,
            exportlist=exportlist,
            importlist=importlist,
            filterlist_out=filterlist_out,
            filterlist_in=filterlist_in,
            id=id,
        )

        frr_ospfd_area.additional_properties = d
        return frr_ospfd_area

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
