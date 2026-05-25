from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_bfd_profile import FrrBfdProfile


T = TypeVar("T", bound="FrrBfdProfilesList")


@_attrs_define
class FrrBfdProfilesList:
    """
    Attributes:
        bfdprofiles (list[FrrBfdProfile] | Unset):
    """

    bfdprofiles: list[FrrBfdProfile] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bfdprofiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bfdprofiles, Unset):
            bfdprofiles = []
            for bfdprofiles_item_data in self.bfdprofiles:
                bfdprofiles_item = bfdprofiles_item_data.to_dict()
                bfdprofiles.append(bfdprofiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bfdprofiles is not UNSET:
            field_dict["bfdprofiles"] = bfdprofiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_bfd_profile import FrrBfdProfile

        d = dict(src_dict)
        _bfdprofiles = d.pop("bfdprofiles", UNSET)
        bfdprofiles: list[FrrBfdProfile] | Unset = UNSET
        if _bfdprofiles is not UNSET:
            bfdprofiles = []
            for bfdprofiles_item_data in _bfdprofiles:
                bfdprofiles_item = FrrBfdProfile.from_dict(bfdprofiles_item_data)

                bfdprofiles.append(bfdprofiles_item)

        frr_bfd_profiles_list = cls(
            bfdprofiles=bfdprofiles,
        )

        frr_bfd_profiles_list.additional_properties = d
        return frr_bfd_profiles_list

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
