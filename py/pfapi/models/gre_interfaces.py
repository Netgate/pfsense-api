from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gre_capable_interface import GRECapableInterface
    from ..models.gre_interface import GREInterface


T = TypeVar("T", bound="GREInterfaces")


@_attrs_define
class GREInterfaces:
    """
    Attributes:
        interfaces (list[GREInterface] | Unset):
        gre_capable_ifs (list[GRECapableInterface] | Unset):
    """

    interfaces: list[GREInterface] | Unset = UNSET
    gre_capable_ifs: list[GRECapableInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        gre_capable_ifs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gre_capable_ifs, Unset):
            gre_capable_ifs = []
            for gre_capable_ifs_item_data in self.gre_capable_ifs:
                gre_capable_ifs_item = gre_capable_ifs_item_data.to_dict()
                gre_capable_ifs.append(gre_capable_ifs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if gre_capable_ifs is not UNSET:
            field_dict["gre_capable_ifs"] = gre_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gre_capable_interface import GRECapableInterface
        from ..models.gre_interface import GREInterface

        d = dict(src_dict)
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[GREInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = GREInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        _gre_capable_ifs = d.pop("gre_capable_ifs", UNSET)
        gre_capable_ifs: list[GRECapableInterface] | Unset = UNSET
        if _gre_capable_ifs is not UNSET:
            gre_capable_ifs = []
            for gre_capable_ifs_item_data in _gre_capable_ifs:
                gre_capable_ifs_item = GRECapableInterface.from_dict(gre_capable_ifs_item_data)

                gre_capable_ifs.append(gre_capable_ifs_item)

        gre_interfaces = cls(
            interfaces=interfaces,
            gre_capable_ifs=gre_capable_ifs,
        )

        gre_interfaces.additional_properties = d
        return gre_interfaces

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
