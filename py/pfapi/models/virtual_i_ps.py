from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simple_interface import SimpleInterface
    from ..models.virtual_ip import VirtualIP


T = TypeVar("T", bound="VirtualIPs")


@_attrs_define
class VirtualIPs:
    """
    Attributes:
        virtualips (Union[Unset, List['VirtualIP']]):
        interfaces (Union[Unset, List['SimpleInterface']]):
    """

    virtualips: Union[Unset, List["VirtualIP"]] = UNSET
    interfaces: Union[Unset, List["SimpleInterface"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        virtualips: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.virtualips, Unset):
            virtualips = []
            for virtualips_item_data in self.virtualips:
                virtualips_item = virtualips_item_data.to_dict()
                virtualips.append(virtualips_item)

        interfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if virtualips is not UNSET:
            field_dict["virtualips"] = virtualips
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.simple_interface import SimpleInterface
        from ..models.virtual_ip import VirtualIP

        d = src_dict.copy()
        virtualips = []
        _virtualips = d.pop("virtualips", UNSET)
        for virtualips_item_data in _virtualips or []:
            virtualips_item = VirtualIP.from_dict(virtualips_item_data)

            virtualips.append(virtualips_item)

        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = SimpleInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        virtual_i_ps = cls(
            virtualips=virtualips,
            interfaces=interfaces,
        )

        virtual_i_ps.additional_properties = d
        return virtual_i_ps

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
