from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lagg_capable_interfaces import LAGGCapableInterfaces
    from ..models.lagg_interface import LAGGInterface


T = TypeVar("T", bound="LAGGInterfaces")


@_attrs_define
class LAGGInterfaces:
    """
    Attributes:
        interfaces (list[LAGGInterface] | Unset):
        lagg_capable_ifs (LAGGCapableInterfaces | Unset):
    """

    interfaces: list[LAGGInterface] | Unset = UNSET
    lagg_capable_ifs: LAGGCapableInterfaces | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        lagg_capable_ifs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lagg_capable_ifs, Unset):
            lagg_capable_ifs = self.lagg_capable_ifs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if lagg_capable_ifs is not UNSET:
            field_dict["lagg_capable_ifs"] = lagg_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lagg_capable_interfaces import LAGGCapableInterfaces
        from ..models.lagg_interface import LAGGInterface

        d = dict(src_dict)
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[LAGGInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = LAGGInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        _lagg_capable_ifs = d.pop("lagg_capable_ifs", UNSET)
        lagg_capable_ifs: LAGGCapableInterfaces | Unset
        if isinstance(_lagg_capable_ifs, Unset):
            lagg_capable_ifs = UNSET
        else:
            lagg_capable_ifs = LAGGCapableInterfaces.from_dict(_lagg_capable_ifs)

        lagg_interfaces = cls(
            interfaces=interfaces,
            lagg_capable_ifs=lagg_capable_ifs,
        )

        lagg_interfaces.additional_properties = d
        return lagg_interfaces

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
