from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.freeradiusinterface import Freeradiusinterface


T = TypeVar("T", bound="FreeradiusInterfacesList")


@_attrs_define
class FreeradiusInterfacesList:
    """
    Attributes:
        interfaces (list[Freeradiusinterface] | Unset):
    """

    interfaces: list[Freeradiusinterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.freeradiusinterface import Freeradiusinterface

        d = dict(src_dict)
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[Freeradiusinterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = Freeradiusinterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        freeradius_interfaces_list = cls(
            interfaces=interfaces,
        )

        freeradius_interfaces_list.additional_properties = d
        return freeradius_interfaces_list

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
