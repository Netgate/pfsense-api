from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ppp_capable_interface import PPPCapableInterface


T = TypeVar("T", bound="PPPCapableInterfaces")


@_attrs_define
class PPPCapableInterfaces:
    """
    Attributes:
        serials (List['PPPCapableInterface']):
        interfaces (List['PPPCapableInterface']):
    """

    serials: List["PPPCapableInterface"]
    interfaces: List["PPPCapableInterface"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        serials = []
        for serials_item_data in self.serials:
            serials_item = serials_item_data.to_dict()
            serials.append(serials_item)

        interfaces = []
        for interfaces_item_data in self.interfaces:
            interfaces_item = interfaces_item_data.to_dict()
            interfaces.append(interfaces_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serials": serials,
                "interfaces": interfaces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ppp_capable_interface import PPPCapableInterface

        d = src_dict.copy()
        serials = []
        _serials = d.pop("serials")
        for serials_item_data in _serials:
            serials_item = PPPCapableInterface.from_dict(serials_item_data)

            serials.append(serials_item)

        interfaces = []
        _interfaces = d.pop("interfaces")
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
