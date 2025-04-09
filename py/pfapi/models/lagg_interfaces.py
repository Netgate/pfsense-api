from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lagg_capable_interfaces import LAGGCapableInterfaces
    from ..models.lagg_interface import LAGGInterface


T = TypeVar("T", bound="LAGGInterfaces")


@_attrs_define
class LAGGInterfaces:
    """
    Attributes:
        interfaces (Union[Unset, List['LAGGInterface']]):
        lagg_capable_ifs (Union[Unset, LAGGCapableInterfaces]):
    """

    interfaces: Union[Unset, List["LAGGInterface"]] = UNSET
    lagg_capable_ifs: Union[Unset, "LAGGCapableInterfaces"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        lagg_capable_ifs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lagg_capable_ifs, Unset):
            lagg_capable_ifs = self.lagg_capable_ifs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if lagg_capable_ifs is not UNSET:
            field_dict["lagg_capable_ifs"] = lagg_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lagg_capable_interfaces import LAGGCapableInterfaces
        from ..models.lagg_interface import LAGGInterface

        d = src_dict.copy()
        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = LAGGInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        _lagg_capable_ifs = d.pop("lagg_capable_ifs", UNSET)
        lagg_capable_ifs: Union[Unset, LAGGCapableInterfaces]
        if isinstance(_lagg_capable_ifs, Unset):
            lagg_capable_ifs = UNSET
        else:
            lagg_capable_ifs = LAGGCapableInterfaces.from_dict(_lagg_capable_ifs)

        lagg_interfaces = cls(
            interfaces=interfaces,
            lagg_capable_ifs=lagg_capable_ifs,
        )

        lagg_interfaces.additional_properties = d
        return lagg_interfaces

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
