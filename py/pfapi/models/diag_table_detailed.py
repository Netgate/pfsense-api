from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagTableDetailed")


@_attrs_define
class DiagTableDetailed:
    """
    Attributes:
        table_name (Union[Unset, str]): name of table
        last_update (Union[Unset, str]): RFC3389/ISO-8601 timestamp of the latest data for the table if available
        avail_action (Union[Unset, str]): available action on the table
        action_descr (Union[Unset, str]): description of the action
        action_prompt (Union[Unset, str]): prompt to display to user before applying action
        entries (Union[Unset, List[str]]):
        entries_removable (Union[Unset, bool]): if each entry can be individually removed
    """

    table_name: Union[Unset, str] = UNSET
    last_update: Union[Unset, str] = UNSET
    avail_action: Union[Unset, str] = UNSET
    action_descr: Union[Unset, str] = UNSET
    action_prompt: Union[Unset, str] = UNSET
    entries: Union[Unset, List[str]] = UNSET
    entries_removable: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_name = self.table_name

        last_update = self.last_update

        avail_action = self.avail_action

        action_descr = self.action_descr

        action_prompt = self.action_prompt

        entries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = self.entries

        entries_removable = self.entries_removable

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        table_name = d.pop("table_name", UNSET)

        last_update = d.pop("last_update", UNSET)

        avail_action = d.pop("avail_action", UNSET)

        action_descr = d.pop("action_descr", UNSET)

        action_prompt = d.pop("action_prompt", UNSET)

        entries = cast(List[str], d.pop("entries", UNSET))

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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
