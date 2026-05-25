from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrOspf6DRow")


@_attrs_define
class FrrOspf6DRow:
    """
    Attributes:
        routevalue (str | Unset): Subnet to Route
        routearea (str | Unset): Area ID
        routecost (str | Unset): Cost
    """

    routevalue: str | Unset = UNSET
    routearea: str | Unset = UNSET
    routecost: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        routevalue = self.routevalue

        routearea = self.routearea

        routecost = self.routecost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if routevalue is not UNSET:
            field_dict["routevalue"] = routevalue
        if routearea is not UNSET:
            field_dict["routearea"] = routearea
        if routecost is not UNSET:
            field_dict["routecost"] = routecost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        routevalue = d.pop("routevalue", UNSET)

        routearea = d.pop("routearea", UNSET)

        routecost = d.pop("routecost", UNSET)

        frr_ospf_6d_row = cls(
            routevalue=routevalue,
            routearea=routearea,
            routecost=routecost,
        )

        frr_ospf_6d_row.additional_properties = d
        return frr_ospf_6d_row

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
