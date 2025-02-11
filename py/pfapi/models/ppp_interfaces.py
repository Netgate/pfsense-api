from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ppp_capable_interfaces import PPPCapableInterfaces
    from ..models.ppp_interface import PPPInterface


T = TypeVar("T", bound="PPPInterfaces")


@_attrs_define
class PPPInterfaces:
    """
    Attributes:
        interfaces (List['PPPInterface']):
        ppp_capable_ifs (PPPCapableInterfaces):
    """

    interfaces: List["PPPInterface"]
    ppp_capable_ifs: "PPPCapableInterfaces"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfaces = []
        for interfaces_item_data in self.interfaces:
            interfaces_item = interfaces_item_data.to_dict()
            interfaces.append(interfaces_item)

        ppp_capable_ifs = self.ppp_capable_ifs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interfaces": interfaces,
                "ppp_capable_ifs": ppp_capable_ifs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ppp_capable_interfaces import PPPCapableInterfaces
        from ..models.ppp_interface import PPPInterface

        d = src_dict.copy()
        interfaces = []
        _interfaces = d.pop("interfaces")
        for interfaces_item_data in _interfaces:
            interfaces_item = PPPInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        ppp_capable_ifs = PPPCapableInterfaces.from_dict(d.pop("ppp_capable_ifs"))

        ppp_interfaces = cls(
            interfaces=interfaces,
            ppp_capable_ifs=ppp_capable_ifs,
        )

        ppp_interfaces.additional_properties = d
        return ppp_interfaces

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
