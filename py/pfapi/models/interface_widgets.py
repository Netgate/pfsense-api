from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interfaces_widget import InterfacesWidget


T = TypeVar("T", bound="InterfaceWidgets")


@_attrs_define
class InterfaceWidgets:
    """
    Attributes:
        interfaces (Union[Unset, List['InterfacesWidget']]):
    """

    interfaces: Union[Unset, List["InterfacesWidget"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interfaces_widget import InterfacesWidget

        d = src_dict.copy()
        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = InterfacesWidget.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        interface_widgets = cls(
            interfaces=interfaces,
        )

        interface_widgets.additional_properties = d
        return interface_widgets

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