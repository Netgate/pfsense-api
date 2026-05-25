from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrOspfdRow")


@_attrs_define
class FrrOspfdRow:
    """
    Attributes:
        routevalue (str | Unset): OSPF Subnet
        routearea (str | Unset): Area ID
    """

    routevalue: str | Unset = UNSET
    routearea: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        routevalue = self.routevalue

        routearea = self.routearea

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if routevalue is not UNSET:
            field_dict["routevalue"] = routevalue
        if routearea is not UNSET:
            field_dict["routearea"] = routearea

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        routevalue = d.pop("routevalue", UNSET)

        routearea = d.pop("routearea", UNSET)

        frr_ospfd_row = cls(
            routevalue=routevalue,
            routearea=routearea,
        )

        frr_ospfd_row.additional_properties = d
        return frr_ospfd_row

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
