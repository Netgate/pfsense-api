from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.threat_gate_user_defined_feed import ThreatGateUserDefinedFeed


T = TypeVar("T", bound="ThreatGateUserDefinedFeedArray")


@_attrs_define
class ThreatGateUserDefinedFeedArray:
    """
    Attributes:
        items (list[ThreatGateUserDefinedFeed] | Unset):
    """

    items: list[ThreatGateUserDefinedFeed] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.threat_gate_user_defined_feed import ThreatGateUserDefinedFeed

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[ThreatGateUserDefinedFeed] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = ThreatGateUserDefinedFeed.from_dict(items_item_data)

                items.append(items_item)

        threat_gate_user_defined_feed_array = cls(
            items=items,
        )

        threat_gate_user_defined_feed_array.additional_properties = d
        return threat_gate_user_defined_feed_array

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
