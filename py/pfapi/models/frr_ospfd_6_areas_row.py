from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrOspfd6AreasRow")


@_attrs_define
class FrrOspfd6AreasRow:
    """
    Attributes:
        rangeprefix (str | Unset): Prefix
        rangenotadvertise (str | Unset): Do Not Advertise
        rangecost (str | Unset): Cost (0-16777215)
        id (str | Unset): (readonly) ID assigned to this entry
    """

    rangeprefix: str | Unset = UNSET
    rangenotadvertise: str | Unset = UNSET
    rangecost: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rangeprefix = self.rangeprefix

        rangenotadvertise = self.rangenotadvertise

        rangecost = self.rangecost

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rangeprefix is not UNSET:
            field_dict["rangeprefix"] = rangeprefix
        if rangenotadvertise is not UNSET:
            field_dict["rangenotadvertise"] = rangenotadvertise
        if rangecost is not UNSET:
            field_dict["rangecost"] = rangecost
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rangeprefix = d.pop("rangeprefix", UNSET)

        rangenotadvertise = d.pop("rangenotadvertise", UNSET)

        rangecost = d.pop("rangecost", UNSET)

        id = d.pop("id", UNSET)

        frr_ospfd_6_areas_row = cls(
            rangeprefix=rangeprefix,
            rangenotadvertise=rangenotadvertise,
            rangecost=rangecost,
            id=id,
        )

        frr_ospfd_6_areas_row.additional_properties = d
        return frr_ospfd_6_areas_row

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
