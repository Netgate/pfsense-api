from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_bgp_aspath import FrrBgpAspath


T = TypeVar("T", bound="FrrBgpAspathsList")


@_attrs_define
class FrrBgpAspathsList:
    """
    Attributes:
        bgpaspaths (list[FrrBgpAspath] | Unset):
    """

    bgpaspaths: list[FrrBgpAspath] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgpaspaths: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bgpaspaths, Unset):
            bgpaspaths = []
            for bgpaspaths_item_data in self.bgpaspaths:
                bgpaspaths_item = bgpaspaths_item_data.to_dict()
                bgpaspaths.append(bgpaspaths_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgpaspaths is not UNSET:
            field_dict["bgpaspaths"] = bgpaspaths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_bgp_aspath import FrrBgpAspath

        d = dict(src_dict)
        _bgpaspaths = d.pop("bgpaspaths", UNSET)
        bgpaspaths: list[FrrBgpAspath] | Unset = UNSET
        if _bgpaspaths is not UNSET:
            bgpaspaths = []
            for bgpaspaths_item_data in _bgpaspaths:
                bgpaspaths_item = FrrBgpAspath.from_dict(bgpaspaths_item_data)

                bgpaspaths.append(bgpaspaths_item)

        frr_bgp_aspaths_list = cls(
            bgpaspaths=bgpaspaths,
        )

        frr_bgp_aspaths_list.additional_properties = d
        return frr_bgp_aspaths_list

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
