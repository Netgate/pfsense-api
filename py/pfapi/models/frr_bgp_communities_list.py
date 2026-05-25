from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_bgp_community import FrrBgpCommunity


T = TypeVar("T", bound="FrrBgpCommunitiesList")


@_attrs_define
class FrrBgpCommunitiesList:
    """
    Attributes:
        bgpcommunities (list[FrrBgpCommunity] | Unset):
    """

    bgpcommunities: list[FrrBgpCommunity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgpcommunities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bgpcommunities, Unset):
            bgpcommunities = []
            for bgpcommunities_item_data in self.bgpcommunities:
                bgpcommunities_item = bgpcommunities_item_data.to_dict()
                bgpcommunities.append(bgpcommunities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgpcommunities is not UNSET:
            field_dict["bgpcommunities"] = bgpcommunities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_bgp_community import FrrBgpCommunity

        d = dict(src_dict)
        _bgpcommunities = d.pop("bgpcommunities", UNSET)
        bgpcommunities: list[FrrBgpCommunity] | Unset = UNSET
        if _bgpcommunities is not UNSET:
            bgpcommunities = []
            for bgpcommunities_item_data in _bgpcommunities:
                bgpcommunities_item = FrrBgpCommunity.from_dict(bgpcommunities_item_data)

                bgpcommunities.append(bgpcommunities_item)

        frr_bgp_communities_list = cls(
            bgpcommunities=bgpcommunities,
        )

        frr_bgp_communities_list.additional_properties = d
        return frr_bgp_communities_list

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
