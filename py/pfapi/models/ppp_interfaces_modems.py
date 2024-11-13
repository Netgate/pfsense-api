from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ppp_interface import PPPInterface


T = TypeVar("T", bound="PPPInterfacesModems")


@_attrs_define
class PPPInterfacesModems:
    """
    Attributes:
        interfaces (Union[Unset, List['PPPInterface']]):
        modems (Union[Unset, List[str]]):
    """

    interfaces: Union[Unset, List["PPPInterface"]] = UNSET
    modems: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        modems: Union[Unset, List[str]] = UNSET
        if not isinstance(self.modems, Unset):
            modems = self.modems

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if modems is not UNSET:
            field_dict["modems"] = modems

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ppp_interface import PPPInterface

        d = src_dict.copy()
        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = PPPInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        modems = cast(List[str], d.pop("modems", UNSET))

        ppp_interfaces_modems = cls(
            interfaces=interfaces,
            modems=modems,
        )

        ppp_interfaces_modems.additional_properties = d
        return ppp_interfaces_modems

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
