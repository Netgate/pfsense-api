from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_value import TextValue


T = TypeVar("T", bound="ValidPingOptions")


@_attrs_define
class ValidPingOptions:
    """
    Attributes:
        source_addresses (list[TextValue] | Unset):
        max_count (int | Unset):
        max_wait_sec (int | Unset):
    """

    source_addresses: list[TextValue] | Unset = UNSET
    max_count: int | Unset = UNSET
    max_wait_sec: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.source_addresses, Unset):
            source_addresses = []
            for source_addresses_item_data in self.source_addresses:
                source_addresses_item = source_addresses_item_data.to_dict()
                source_addresses.append(source_addresses_item)

        max_count = self.max_count

        max_wait_sec = self.max_wait_sec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_addresses is not UNSET:
            field_dict["source_addresses"] = source_addresses
        if max_count is not UNSET:
            field_dict["max_count"] = max_count
        if max_wait_sec is not UNSET:
            field_dict["max_wait_sec"] = max_wait_sec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _source_addresses = d.pop("source_addresses", UNSET)
        source_addresses: list[TextValue] | Unset = UNSET
        if _source_addresses is not UNSET:
            source_addresses = []
            for source_addresses_item_data in _source_addresses:
                source_addresses_item = TextValue.from_dict(source_addresses_item_data)

                source_addresses.append(source_addresses_item)

        max_count = d.pop("max_count", UNSET)

        max_wait_sec = d.pop("max_wait_sec", UNSET)

        valid_ping_options = cls(
            source_addresses=source_addresses,
            max_count=max_count,
            max_wait_sec=max_wait_sec,
        )

        valid_ping_options.additional_properties = d
        return valid_ping_options

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
