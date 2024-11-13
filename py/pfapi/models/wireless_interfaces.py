from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wireless_addl import WirelessAddl
    from ..models.wireless_interface import WirelessInterface


T = TypeVar("T", bound="WirelessInterfaces")


@_attrs_define
class WirelessInterfaces:
    """
    Attributes:
        interfaces (Union[Unset, List['WirelessInterface']]):
        interfaces_clone (Union[Unset, List['WirelessAddl']]):
    """

    interfaces: Union[Unset, List["WirelessInterface"]] = UNSET
    interfaces_clone: Union[Unset, List["WirelessAddl"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        interfaces_clone: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces_clone, Unset):
            interfaces_clone = []
            for interfaces_clone_item_data in self.interfaces_clone:
                interfaces_clone_item = interfaces_clone_item_data.to_dict()
                interfaces_clone.append(interfaces_clone_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if interfaces_clone is not UNSET:
            field_dict["interfacesClone"] = interfaces_clone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wireless_addl import WirelessAddl
        from ..models.wireless_interface import WirelessInterface

        d = src_dict.copy()
        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = WirelessInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        interfaces_clone = []
        _interfaces_clone = d.pop("interfacesClone", UNSET)
        for interfaces_clone_item_data in _interfaces_clone or []:
            interfaces_clone_item = WirelessAddl.from_dict(interfaces_clone_item_data)

            interfaces_clone.append(interfaces_clone_item)

        wireless_interfaces = cls(
            interfaces=interfaces,
            interfaces_clone=interfaces_clone,
        )

        wireless_interfaces.additional_properties = d
        return wireless_interfaces

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
