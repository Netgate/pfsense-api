from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrRow")


@_attrs_define
class FrrRow:
    """
    Attributes:
        acceptfilter (str | Unset): Do Not Accept

            Accept Filter
        nullroute (str | Unset): Null Route

            Redistribute rules.
        routevalue (str | Unset): Subnet
        routetarget (str | Unset): Static Route Target

            Target for an FRR static route
    """

    acceptfilter: str | Unset = UNSET
    nullroute: str | Unset = UNSET
    routevalue: str | Unset = UNSET
    routetarget: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acceptfilter = self.acceptfilter

        nullroute = self.nullroute

        routevalue = self.routevalue

        routetarget = self.routetarget

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acceptfilter is not UNSET:
            field_dict["acceptfilter"] = acceptfilter
        if nullroute is not UNSET:
            field_dict["nullroute"] = nullroute
        if routevalue is not UNSET:
            field_dict["routevalue"] = routevalue
        if routetarget is not UNSET:
            field_dict["routetarget"] = routetarget

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acceptfilter = d.pop("acceptfilter", UNSET)

        nullroute = d.pop("nullroute", UNSET)

        routevalue = d.pop("routevalue", UNSET)

        routetarget = d.pop("routetarget", UNSET)

        frr_row = cls(
            acceptfilter=acceptfilter,
            nullroute=nullroute,
            routevalue=routevalue,
            routetarget=routetarget,
        )

        frr_row.additional_properties = d
        return frr_row

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
