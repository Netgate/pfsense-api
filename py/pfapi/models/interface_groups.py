from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.if_group_capable_interface import IfGroupCapableInterface
    from ..models.interface_group import InterfaceGroup


T = TypeVar("T", bound="InterfaceGroups")


@_attrs_define
class InterfaceGroups:
    """
    Attributes:
        groups (Union[Unset, List['InterfaceGroup']]):
        groups_capable_ifs (Union[Unset, List['IfGroupCapableInterface']]):
    """

    groups: Union[Unset, List["InterfaceGroup"]] = UNSET
    groups_capable_ifs: Union[Unset, List["IfGroupCapableInterface"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        groups_capable_ifs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups_capable_ifs, Unset):
            groups_capable_ifs = []
            for groups_capable_ifs_item_data in self.groups_capable_ifs:
                groups_capable_ifs_item = groups_capable_ifs_item_data.to_dict()
                groups_capable_ifs.append(groups_capable_ifs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if groups_capable_ifs is not UNSET:
            field_dict["groups_capable_ifs"] = groups_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.if_group_capable_interface import IfGroupCapableInterface
        from ..models.interface_group import InterfaceGroup

        d = src_dict.copy()
        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = InterfaceGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        groups_capable_ifs = []
        _groups_capable_ifs = d.pop("groups_capable_ifs", UNSET)
        for groups_capable_ifs_item_data in _groups_capable_ifs or []:
            groups_capable_ifs_item = IfGroupCapableInterface.from_dict(groups_capable_ifs_item_data)

            groups_capable_ifs.append(groups_capable_ifs_item)

        interface_groups = cls(
            groups=groups,
            groups_capable_ifs=groups_capable_ifs,
        )

        interface_groups.additional_properties = d
        return interface_groups

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
