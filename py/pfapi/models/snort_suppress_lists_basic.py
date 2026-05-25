from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_suppress_list_basic import SnortSuppressListBasic


T = TypeVar("T", bound="SnortSuppressListsBasic")


@_attrs_define
class SnortSuppressListsBasic:
    """
    Attributes:
        suppress_lists (list[SnortSuppressListBasic] | Unset):
    """

    suppress_lists: list[SnortSuppressListBasic] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suppress_lists: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.suppress_lists, Unset):
            suppress_lists = []
            for suppress_lists_item_data in self.suppress_lists:
                suppress_lists_item = suppress_lists_item_data.to_dict()
                suppress_lists.append(suppress_lists_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if suppress_lists is not UNSET:
            field_dict["suppress_lists"] = suppress_lists

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_suppress_list_basic import SnortSuppressListBasic

        d = dict(src_dict)
        _suppress_lists = d.pop("suppress_lists", UNSET)
        suppress_lists: list[SnortSuppressListBasic] | Unset = UNSET
        if _suppress_lists is not UNSET:
            suppress_lists = []
            for suppress_lists_item_data in _suppress_lists:
                suppress_lists_item = SnortSuppressListBasic.from_dict(suppress_lists_item_data)

                suppress_lists.append(suppress_lists_item)

        snort_suppress_lists_basic = cls(
            suppress_lists=suppress_lists,
        )

        snort_suppress_lists_basic.additional_properties = d
        return snort_suppress_lists_basic

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
