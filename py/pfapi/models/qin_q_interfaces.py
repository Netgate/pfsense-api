from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qin_q_interface import QinQInterface
    from ..models.vlan_capable_interface import VLANCapableInterface


T = TypeVar("T", bound="QinQInterfaces")


@_attrs_define
class QinQInterfaces:
    """
    Attributes:
        interfaces (List['QinQInterface']):
        vlan_capable_ifs (List['VLANCapableInterface']):
    """

    interfaces: List["QinQInterface"]
    vlan_capable_ifs: List["VLANCapableInterface"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfaces = []
        for interfaces_item_data in self.interfaces:
            interfaces_item = interfaces_item_data.to_dict()
            interfaces.append(interfaces_item)

        vlan_capable_ifs = []
        for vlan_capable_ifs_item_data in self.vlan_capable_ifs:
            vlan_capable_ifs_item = vlan_capable_ifs_item_data.to_dict()
            vlan_capable_ifs.append(vlan_capable_ifs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interfaces": interfaces,
                "vlan_capable_ifs": vlan_capable_ifs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.qin_q_interface import QinQInterface
        from ..models.vlan_capable_interface import VLANCapableInterface

        d = src_dict.copy()
        interfaces = []
        _interfaces = d.pop("interfaces")
        for interfaces_item_data in _interfaces:
            interfaces_item = QinQInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        vlan_capable_ifs = []
        _vlan_capable_ifs = d.pop("vlan_capable_ifs")
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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
