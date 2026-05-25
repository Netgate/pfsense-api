from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_pass_list import SnortPassList


T = TypeVar("T", bound="SnortPassLists")


@_attrs_define
class SnortPassLists:
    """
    Attributes:
        pass_lists (list[SnortPassList] | Unset):
    """

    pass_lists: list[SnortPassList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pass_lists: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pass_lists, Unset):
            pass_lists = []
            for pass_lists_item_data in self.pass_lists:
                pass_lists_item = pass_lists_item_data.to_dict()
                pass_lists.append(pass_lists_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pass_lists is not UNSET:
            field_dict["pass_lists"] = pass_lists

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_pass_list import SnortPassList

        d = dict(src_dict)
        _pass_lists = d.pop("pass_lists", UNSET)
        pass_lists: list[SnortPassList] | Unset = UNSET
        if _pass_lists is not UNSET:
            pass_lists = []
            for pass_lists_item_data in _pass_lists:
                pass_lists_item = SnortPassList.from_dict(pass_lists_item_data)

                pass_lists.append(pass_lists_item)

        snort_pass_lists = cls(
            pass_lists=pass_lists,
        )

        snort_pass_lists.additional_properties = d
        return snort_pass_lists

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
