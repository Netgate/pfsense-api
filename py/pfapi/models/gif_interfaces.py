from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gif_capable_interface import GIFCapableInterface
    from ..models.gif_interface import GIFInterface


T = TypeVar("T", bound="GIFInterfaces")


@_attrs_define
class GIFInterfaces:
    """
    Attributes:
        interfaces (list[GIFInterface] | Unset):
        gif_capable_ifs (list[GIFCapableInterface] | Unset):
    """

    interfaces: list[GIFInterface] | Unset = UNSET
    gif_capable_ifs: list[GIFCapableInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        gif_capable_ifs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gif_capable_ifs, Unset):
            gif_capable_ifs = []
            for gif_capable_ifs_item_data in self.gif_capable_ifs:
                gif_capable_ifs_item = gif_capable_ifs_item_data.to_dict()
                gif_capable_ifs.append(gif_capable_ifs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if gif_capable_ifs is not UNSET:
            field_dict["gif_capable_ifs"] = gif_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gif_capable_interface import GIFCapableInterface
        from ..models.gif_interface import GIFInterface

        d = dict(src_dict)
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[GIFInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = GIFInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        _gif_capable_ifs = d.pop("gif_capable_ifs", UNSET)
        gif_capable_ifs: list[GIFCapableInterface] | Unset = UNSET
        if _gif_capable_ifs is not UNSET:
            gif_capable_ifs = []
            for gif_capable_ifs_item_data in _gif_capable_ifs:
                gif_capable_ifs_item = GIFCapableInterface.from_dict(gif_capable_ifs_item_data)

                gif_capable_ifs.append(gif_capable_ifs_item)

        gif_interfaces = cls(
            interfaces=interfaces,
            gif_capable_ifs=gif_capable_ifs,
        )

        gif_interfaces.additional_properties = d
        return gif_interfaces

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
