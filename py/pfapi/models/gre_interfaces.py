from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gre_capable_interface import GRECapableInterface
    from ..models.gre_interface import GREInterface


T = TypeVar("T", bound="GREInterfaces")


@_attrs_define
class GREInterfaces:
    """
    Attributes:
        interfaces (Union[Unset, List['GREInterface']]):
        gre_capable_ifs (Union[Unset, List['GRECapableInterface']]):
    """

    interfaces: Union[Unset, List["GREInterface"]] = UNSET
    gre_capable_ifs: Union[Unset, List["GRECapableInterface"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        gre_capable_ifs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.gre_capable_ifs, Unset):
            gre_capable_ifs = []
            for gre_capable_ifs_item_data in self.gre_capable_ifs:
                gre_capable_ifs_item = gre_capable_ifs_item_data.to_dict()
                gre_capable_ifs.append(gre_capable_ifs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if gre_capable_ifs is not UNSET:
            field_dict["gre_capable_ifs"] = gre_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gre_capable_interface import GRECapableInterface
        from ..models.gre_interface import GREInterface

        d = src_dict.copy()
        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = GREInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        gre_capable_ifs = []
        _gre_capable_ifs = d.pop("gre_capable_ifs", UNSET)
        for gre_capable_ifs_item_data in _gre_capable_ifs or []:
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
