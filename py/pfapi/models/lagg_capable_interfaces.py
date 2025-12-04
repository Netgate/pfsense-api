from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lagg_capable_interface import LAGGCapableInterface


T = TypeVar("T", bound="LAGGCapableInterfaces")


@_attrs_define
class LAGGCapableInterfaces:
    """
    Attributes:
        capable_ifs (list[LAGGCapableInterface] | Unset):
        lagg_members (list[LAGGCapableInterface] | Unset):
    """

    capable_ifs: list[LAGGCapableInterface] | Unset = UNSET
    lagg_members: list[LAGGCapableInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capable_ifs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.capable_ifs, Unset):
            capable_ifs = []
            for capable_ifs_item_data in self.capable_ifs:
                capable_ifs_item = capable_ifs_item_data.to_dict()
                capable_ifs.append(capable_ifs_item)

        lagg_members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lagg_members, Unset):
            lagg_members = []
            for lagg_members_item_data in self.lagg_members:
                lagg_members_item = lagg_members_item_data.to_dict()
                lagg_members.append(lagg_members_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capable_ifs is not UNSET:
            field_dict["capable_ifs"] = capable_ifs
        if lagg_members is not UNSET:
            field_dict["lagg_members"] = lagg_members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lagg_capable_interface import LAGGCapableInterface

        d = dict(src_dict)
        _capable_ifs = d.pop("capable_ifs", UNSET)
        capable_ifs: list[LAGGCapableInterface] | Unset = UNSET
        if _capable_ifs is not UNSET:
            capable_ifs = []
            for capable_ifs_item_data in _capable_ifs:
                capable_ifs_item = LAGGCapableInterface.from_dict(capable_ifs_item_data)

                capable_ifs.append(capable_ifs_item)

        _lagg_members = d.pop("lagg_members", UNSET)
        lagg_members: list[LAGGCapableInterface] | Unset = UNSET
        if _lagg_members is not UNSET:
            lagg_members = []
            for lagg_members_item_data in _lagg_members:
                lagg_members_item = LAGGCapableInterface.from_dict(lagg_members_item_data)

                lagg_members.append(lagg_members_item)

        lagg_capable_interfaces = cls(
            capable_ifs=capable_ifs,
            lagg_members=lagg_members,
        )

        lagg_capable_interfaces.additional_properties = d
        return lagg_capable_interfaces

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
