from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        groups (list[InterfaceGroup] | Unset):
        groups_capable_ifs (list[IfGroupCapableInterface] | Unset):
    """

    groups: list[InterfaceGroup] | Unset = UNSET
    groups_capable_ifs: list[IfGroupCapableInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        groups_capable_ifs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups_capable_ifs, Unset):
            groups_capable_ifs = []
            for groups_capable_ifs_item_data in self.groups_capable_ifs:
                groups_capable_ifs_item = groups_capable_ifs_item_data.to_dict()
                groups_capable_ifs.append(groups_capable_ifs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if groups_capable_ifs is not UNSET:
            field_dict["groups_capable_ifs"] = groups_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.if_group_capable_interface import IfGroupCapableInterface
        from ..models.interface_group import InterfaceGroup

        d = dict(src_dict)
        _groups = d.pop("groups", UNSET)
        groups: list[InterfaceGroup] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = InterfaceGroup.from_dict(groups_item_data)

                groups.append(groups_item)

        _groups_capable_ifs = d.pop("groups_capable_ifs", UNSET)
        groups_capable_ifs: list[IfGroupCapableInterface] | Unset = UNSET
        if _groups_capable_ifs is not UNSET:
            groups_capable_ifs = []
            for groups_capable_ifs_item_data in _groups_capable_ifs:
                groups_capable_ifs_item = IfGroupCapableInterface.from_dict(groups_capable_ifs_item_data)

                groups_capable_ifs.append(groups_capable_ifs_item)

        interface_groups = cls(
            groups=groups,
            groups_capable_ifs=groups_capable_ifs,
        )

        interface_groups.additional_properties = d
        return interface_groups

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
