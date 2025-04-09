from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bridge_capable_interface import BridgeCapableInterface
    from ..models.bridge_interface import BridgeInterface


T = TypeVar("T", bound="BridgeInterfaces")


@_attrs_define
class BridgeInterfaces:
    """
    Attributes:
        interfaces (Union[Unset, List['BridgeInterface']]):
        bridge_capable_ifs (Union[Unset, List['BridgeCapableInterface']]):
    """

    interfaces: Union[Unset, List["BridgeInterface"]] = UNSET
    bridge_capable_ifs: Union[Unset, List["BridgeCapableInterface"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        bridge_capable_ifs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bridge_capable_ifs, Unset):
            bridge_capable_ifs = []
            for bridge_capable_ifs_item_data in self.bridge_capable_ifs:
                bridge_capable_ifs_item = bridge_capable_ifs_item_data.to_dict()
                bridge_capable_ifs.append(bridge_capable_ifs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if bridge_capable_ifs is not UNSET:
            field_dict["bridge_capable_ifs"] = bridge_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bridge_capable_interface import BridgeCapableInterface
        from ..models.bridge_interface import BridgeInterface

        d = src_dict.copy()
        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = BridgeInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        bridge_capable_ifs = []
        _bridge_capable_ifs = d.pop("bridge_capable_ifs", UNSET)
        for bridge_capable_ifs_item_data in _bridge_capable_ifs or []:
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
