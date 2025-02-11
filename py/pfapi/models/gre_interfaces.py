from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.gre_capable_interface import GRECapableInterface
    from ..models.gre_interface import GREInterface


T = TypeVar("T", bound="GREInterfaces")


@_attrs_define
class GREInterfaces:
    """
    Attributes:
        interfaces (List['GREInterface']):
        gre_capable_ifs (List['GRECapableInterface']):
    """

    interfaces: List["GREInterface"]
    gre_capable_ifs: List["GRECapableInterface"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfaces = []
        for interfaces_item_data in self.interfaces:
            interfaces_item = interfaces_item_data.to_dict()
            interfaces.append(interfaces_item)

        gre_capable_ifs = []
        for gre_capable_ifs_item_data in self.gre_capable_ifs:
            gre_capable_ifs_item = gre_capable_ifs_item_data.to_dict()
            gre_capable_ifs.append(gre_capable_ifs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interfaces": interfaces,
                "gre_capable_ifs": gre_capable_ifs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gre_capable_interface import GRECapableInterface
        from ..models.gre_interface import GREInterface

        d = src_dict.copy()
        interfaces = []
        _interfaces = d.pop("interfaces")
        for interfaces_item_data in _interfaces:
            interfaces_item = GREInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        gre_capable_ifs = []
        _gre_capable_ifs = d.pop("gre_capable_ifs")
        for gre_capable_ifs_item_data in _gre_capable_ifs:
            gre_capable_ifs_item = GRECapableInterface.from_dict(gre_capable_ifs_item_data)

            gre_capable_ifs.append(gre_capable_ifs_item)

        gre_interfaces = cls(
            interfaces=interfaces,
            gre_capable_ifs=gre_capable_ifs,
        )

        gre_interfaces.additional_properties = d
        return gre_interfaces

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
