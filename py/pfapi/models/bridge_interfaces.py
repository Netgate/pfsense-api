from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bridge_capable_interface import BridgeCapableInterface
    from ..models.bridge_interface import BridgeInterface


T = TypeVar("T", bound="BridgeInterfaces")


@_attrs_define
class BridgeInterfaces:
    """
    Attributes:
        interfaces (List['BridgeInterface']):
        bridge_capable_ifs (List['BridgeCapableInterface']):
    """

    interfaces: List["BridgeInterface"]
    bridge_capable_ifs: List["BridgeCapableInterface"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfaces = []
        for interfaces_item_data in self.interfaces:
            interfaces_item = interfaces_item_data.to_dict()
            interfaces.append(interfaces_item)

        bridge_capable_ifs = []
        for bridge_capable_ifs_item_data in self.bridge_capable_ifs:
            bridge_capable_ifs_item = bridge_capable_ifs_item_data.to_dict()
            bridge_capable_ifs.append(bridge_capable_ifs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interfaces": interfaces,
                "bridge_capable_ifs": bridge_capable_ifs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bridge_capable_interface import BridgeCapableInterface
        from ..models.bridge_interface import BridgeInterface

        d = src_dict.copy()
        interfaces = []
        _interfaces = d.pop("interfaces")
        for interfaces_item_data in _interfaces:
            interfaces_item = BridgeInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        bridge_capable_ifs = []
        _bridge_capable_ifs = d.pop("bridge_capable_ifs")
        for bridge_capable_ifs_item_data in _bridge_capable_ifs:
            bridge_capable_ifs_item = BridgeCapableInterface.from_dict(bridge_capable_ifs_item_data)

            bridge_capable_ifs.append(bridge_capable_ifs_item)

        bridge_interfaces = cls(
            interfaces=interfaces,
            bridge_capable_ifs=bridge_capable_ifs,
        )

        bridge_interfaces.additional_properties = d
        return bridge_interfaces

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
