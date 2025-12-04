from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qin_q_interface import QinQInterface
    from ..models.vlan_capable_interface import VLANCapableInterface


T = TypeVar("T", bound="QinQInterfaces")


@_attrs_define
class QinQInterfaces:
    """
    Attributes:
        interfaces (list[QinQInterface] | Unset):
        vlan_capable_ifs (list[VLANCapableInterface] | Unset):
    """

    interfaces: list[QinQInterface] | Unset = UNSET
    vlan_capable_ifs: list[VLANCapableInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        vlan_capable_ifs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vlan_capable_ifs, Unset):
            vlan_capable_ifs = []
            for vlan_capable_ifs_item_data in self.vlan_capable_ifs:
                vlan_capable_ifs_item = vlan_capable_ifs_item_data.to_dict()
                vlan_capable_ifs.append(vlan_capable_ifs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if vlan_capable_ifs is not UNSET:
            field_dict["vlan_capable_ifs"] = vlan_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qin_q_interface import QinQInterface
        from ..models.vlan_capable_interface import VLANCapableInterface

        d = dict(src_dict)
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[QinQInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = QinQInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        _vlan_capable_ifs = d.pop("vlan_capable_ifs", UNSET)
        vlan_capable_ifs: list[VLANCapableInterface] | Unset = UNSET
        if _vlan_capable_ifs is not UNSET:
            vlan_capable_ifs = []
            for vlan_capable_ifs_item_data in _vlan_capable_ifs:
                vlan_capable_ifs_item = VLANCapableInterface.from_dict(vlan_capable_ifs_item_data)

                vlan_capable_ifs.append(vlan_capable_ifs_item)

        qin_q_interfaces = cls(
            interfaces=interfaces,
            vlan_capable_ifs=vlan_capable_ifs,
        )

        qin_q_interfaces.additional_properties = d
        return qin_q_interfaces

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
