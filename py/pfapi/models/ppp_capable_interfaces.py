from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ppp_capable_interface import PPPCapableInterface


T = TypeVar("T", bound="PPPCapableInterfaces")


@_attrs_define
class PPPCapableInterfaces:
    """
    Attributes:
        serials (list[PPPCapableInterface] | Unset):
        interfaces (list[PPPCapableInterface] | Unset):
    """

    serials: list[PPPCapableInterface] | Unset = UNSET
    interfaces: list[PPPCapableInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        serials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.serials, Unset):
            serials = []
            for serials_item_data in self.serials:
                serials_item = serials_item_data.to_dict()
                serials.append(serials_item)

        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if serials is not UNSET:
            field_dict["serials"] = serials
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ppp_capable_interface import PPPCapableInterface

        d = dict(src_dict)
        _serials = d.pop("serials", UNSET)
        serials: list[PPPCapableInterface] | Unset = UNSET
        if _serials is not UNSET:
            serials = []
            for serials_item_data in _serials:
                serials_item = PPPCapableInterface.from_dict(serials_item_data)

                serials.append(serials_item)

        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[PPPCapableInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = PPPCapableInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        ppp_capable_interfaces = cls(
            serials=serials,
            interfaces=interfaces,
        )

        ppp_capable_interfaces.additional_properties = d
        return ppp_capable_interfaces

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
