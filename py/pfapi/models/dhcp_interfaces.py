from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interface_label_to_name import InterfaceLabelToName


T = TypeVar("T", bound="DhcpInterfaces")


@_attrs_define
class DhcpInterfaces:
    """
    Attributes:
        entries (list[InterfaceLabelToName] | Unset):
    """

    entries: list[InterfaceLabelToName] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interface_label_to_name import InterfaceLabelToName

        d = dict(src_dict)
        _entries = d.pop("entries", UNSET)
        entries: list[InterfaceLabelToName] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = InterfaceLabelToName.from_dict(entries_item_data)

                entries.append(entries_item)

        dhcp_interfaces = cls(
            entries=entries,
        )

        dhcp_interfaces.additional_properties = d
        return dhcp_interfaces

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
