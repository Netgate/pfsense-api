from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagTableDetailed")


@_attrs_define
class DiagTableDetailed:
    """
    Attributes:
        table_name (str | Unset): name of table
        last_update (str | Unset): RFC3389/ISO-8601 timestamp of the latest data for the table if available
        avail_action (str | Unset): available action on the table
        action_descr (str | Unset): description of the action
        action_prompt (str | Unset): prompt to display to user before applying action
        entries (list[str] | Unset):
        entries_removable (bool | Unset): if each entry can be individually removed
    """

    table_name: str | Unset = UNSET
    last_update: str | Unset = UNSET
    avail_action: str | Unset = UNSET
    action_descr: str | Unset = UNSET
    action_prompt: str | Unset = UNSET
    entries: list[str] | Unset = UNSET
    entries_removable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table_name = self.table_name

        last_update = self.last_update

        avail_action = self.avail_action

        action_descr = self.action_descr

        action_prompt = self.action_prompt

        entries: list[str] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = self.entries

        entries_removable = self.entries_removable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if table_name is not UNSET:
            field_dict["table_name"] = table_name
        if last_update is not UNSET:
            field_dict["last_update"] = last_update
        if avail_action is not UNSET:
            field_dict["avail_action"] = avail_action
        if action_descr is not UNSET:
            field_dict["action_descr"] = action_descr
        if action_prompt is not UNSET:
            field_dict["action_prompt"] = action_prompt
        if entries is not UNSET:
            field_dict["entries"] = entries
        if entries_removable is not UNSET:
            field_dict["entries_removable"] = entries_removable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        table_name = d.pop("table_name", UNSET)

        last_update = d.pop("last_update", UNSET)

        avail_action = d.pop("avail_action", UNSET)

        action_descr = d.pop("action_descr", UNSET)

        action_prompt = d.pop("action_prompt", UNSET)

        entries = cast(list[str], d.pop("entries", UNSET))

        entries_removable = d.pop("entries_removable", UNSET)

        diag_table_detailed = cls(
            table_name=table_name,
            last_update=last_update,
            avail_action=avail_action,
            action_descr=action_descr,
            action_prompt=action_prompt,
            entries=entries,
            entries_removable=entries_removable,
        )

        diag_table_detailed.additional_properties = d
        return diag_table_detailed

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
