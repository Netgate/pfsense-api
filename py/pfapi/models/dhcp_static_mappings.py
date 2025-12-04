from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_static_mapping import DhcpStaticMapping
    from ..models.dhcpv_6_static_mapping import Dhcpv6StaticMapping


T = TypeVar("T", bound="DhcpStaticMappings")


@_attrs_define
class DhcpStaticMappings:
    """
    Attributes:
        entries (list[DhcpStaticMapping] | Unset):
        entriesv6 (list[Dhcpv6StaticMapping] | Unset):
    """

    entries: list[DhcpStaticMapping] | Unset = UNSET
    entriesv6: list[Dhcpv6StaticMapping] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        entriesv6: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entriesv6, Unset):
            entriesv6 = []
            for entriesv6_item_data in self.entriesv6:
                entriesv6_item = entriesv6_item_data.to_dict()
                entriesv6.append(entriesv6_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if entriesv6 is not UNSET:
            field_dict["entriesv6"] = entriesv6

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dhcp_static_mapping import DhcpStaticMapping
        from ..models.dhcpv_6_static_mapping import Dhcpv6StaticMapping

        d = dict(src_dict)
        _entries = d.pop("entries", UNSET)
        entries: list[DhcpStaticMapping] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = DhcpStaticMapping.from_dict(entries_item_data)

                entries.append(entries_item)

        _entriesv6 = d.pop("entriesv6", UNSET)
        entriesv6: list[Dhcpv6StaticMapping] | Unset = UNSET
        if _entriesv6 is not UNSET:
            entriesv6 = []
            for entriesv6_item_data in _entriesv6:
                entriesv6_item = Dhcpv6StaticMapping.from_dict(entriesv6_item_data)

                entriesv6.append(entriesv6_item)

        dhcp_static_mappings = cls(
            entries=entries,
            entriesv6=entriesv6,
        )

        dhcp_static_mappings.additional_properties = d
        return dhcp_static_mappings

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
