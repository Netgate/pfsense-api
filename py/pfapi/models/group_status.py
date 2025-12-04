from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tier import Tier


T = TypeVar("T", bound="GroupStatus")


@_attrs_define
class GroupStatus:
    """
    Attributes:
        name (str | Unset):
        descr (str | Unset):
        tier1 (list[Tier] | Unset):
        tier2 (list[Tier] | Unset):
        tier3 (list[Tier] | Unset):
        tier4 (list[Tier] | Unset):
        tier5 (list[Tier] | Unset):
    """

    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    tier1: list[Tier] | Unset = UNSET
    tier2: list[Tier] | Unset = UNSET
    tier3: list[Tier] | Unset = UNSET
    tier4: list[Tier] | Unset = UNSET
    tier5: list[Tier] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descr = self.descr

        tier1: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tier1, Unset):
            tier1 = []
            for tier1_item_data in self.tier1:
                tier1_item = tier1_item_data.to_dict()
                tier1.append(tier1_item)

        tier2: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tier2, Unset):
            tier2 = []
            for tier2_item_data in self.tier2:
                tier2_item = tier2_item_data.to_dict()
                tier2.append(tier2_item)

        tier3: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tier3, Unset):
            tier3 = []
            for tier3_item_data in self.tier3:
                tier3_item = tier3_item_data.to_dict()
                tier3.append(tier3_item)

        tier4: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tier4, Unset):
            tier4 = []
            for tier4_item_data in self.tier4:
                tier4_item = tier4_item_data.to_dict()
                tier4.append(tier4_item)

        tier5: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tier5, Unset):
            tier5 = []
            for tier5_item_data in self.tier5:
                tier5_item = tier5_item_data.to_dict()
                tier5.append(tier5_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if tier1 is not UNSET:
            field_dict["tier1"] = tier1
        if tier2 is not UNSET:
            field_dict["tier2"] = tier2
        if tier3 is not UNSET:
            field_dict["tier3"] = tier3
        if tier4 is not UNSET:
            field_dict["tier4"] = tier4
        if tier5 is not UNSET:
            field_dict["tier5"] = tier5

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tier import Tier

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        _tier1 = d.pop("tier1", UNSET)
        tier1: list[Tier] | Unset = UNSET
        if _tier1 is not UNSET:
            tier1 = []
            for tier1_item_data in _tier1:
                tier1_item = Tier.from_dict(tier1_item_data)

                tier1.append(tier1_item)

        _tier2 = d.pop("tier2", UNSET)
        tier2: list[Tier] | Unset = UNSET
        if _tier2 is not UNSET:
            tier2 = []
            for tier2_item_data in _tier2:
                tier2_item = Tier.from_dict(tier2_item_data)

                tier2.append(tier2_item)

        _tier3 = d.pop("tier3", UNSET)
        tier3: list[Tier] | Unset = UNSET
        if _tier3 is not UNSET:
            tier3 = []
            for tier3_item_data in _tier3:
                tier3_item = Tier.from_dict(tier3_item_data)

                tier3.append(tier3_item)

        _tier4 = d.pop("tier4", UNSET)
        tier4: list[Tier] | Unset = UNSET
        if _tier4 is not UNSET:
            tier4 = []
            for tier4_item_data in _tier4:
                tier4_item = Tier.from_dict(tier4_item_data)

                tier4.append(tier4_item)

        _tier5 = d.pop("tier5", UNSET)
        tier5: list[Tier] | Unset = UNSET
        if _tier5 is not UNSET:
            tier5 = []
            for tier5_item_data in _tier5:
                tier5_item = Tier.from_dict(tier5_item_data)

                tier5.append(tier5_item)

        group_status = cls(
            name=name,
            descr=descr,
            tier1=tier1,
            tier2=tier2,
            tier3=tier3,
            tier4=tier4,
            tier5=tier5,
        )

        group_status.additional_properties = d
        return group_status

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
