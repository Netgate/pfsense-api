from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ppp_capable_interfaces import PPPCapableInterfaces
    from ..models.ppp_interface import PPPInterface


T = TypeVar("T", bound="PPPInterfaces")


@_attrs_define
class PPPInterfaces:
    """
    Attributes:
        interfaces (list[PPPInterface] | Unset):
        ppp_capable_ifs (PPPCapableInterfaces | Unset):
    """

    interfaces: list[PPPInterface] | Unset = UNSET
    ppp_capable_ifs: PPPCapableInterfaces | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        ppp_capable_ifs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ppp_capable_ifs, Unset):
            ppp_capable_ifs = self.ppp_capable_ifs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if ppp_capable_ifs is not UNSET:
            field_dict["ppp_capable_ifs"] = ppp_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ppp_capable_interfaces import PPPCapableInterfaces
        from ..models.ppp_interface import PPPInterface

        d = dict(src_dict)
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[PPPInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = PPPInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        _ppp_capable_ifs = d.pop("ppp_capable_ifs", UNSET)
        ppp_capable_ifs: PPPCapableInterfaces | Unset
        if isinstance(_ppp_capable_ifs, Unset):
            ppp_capable_ifs = UNSET
        else:
            ppp_capable_ifs = PPPCapableInterfaces.from_dict(_ppp_capable_ifs)

        ppp_interfaces = cls(
            interfaces=interfaces,
            ppp_capable_ifs=ppp_capable_ifs,
        )

        ppp_interfaces.additional_properties = d
        return ppp_interfaces

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
