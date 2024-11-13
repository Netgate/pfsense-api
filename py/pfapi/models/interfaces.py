from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interface import Interface


T = TypeVar("T", bound="Interfaces")


@_attrs_define
class Interfaces:
    """
    Attributes:
        interface (Union[Unset, List['Interface']]):
    """

    interface: Union[Unset, List["Interface"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interface: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interface, Unset):
            interface = []
            for interface_item_data in self.interface:
                interface_item = interface_item_data.to_dict()
                interface.append(interface_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface is not UNSET:
            field_dict["interface"] = interface

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interface import Interface

        d = src_dict.copy()
        interface = []
        _interface = d.pop("interface", UNSET)
        for interface_item_data in _interface or []:
            interface_item = Interface.from_dict(interface_item_data)

            interface.append(interface_item)

        interfaces = cls(
            interface=interface,
        )

        interfaces.additional_properties = d
        return interfaces

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
