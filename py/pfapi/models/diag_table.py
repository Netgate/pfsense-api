from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagTable")


@_attrs_define
class DiagTable:
    """
    Attributes:
        table_name (Union[Unset, str]): name of the table
        avail_action (Union[Unset, str]): available action on the table
        action_descr (Union[Unset, str]): description of the action
    """

    table_name: Union[Unset, str] = UNSET
    avail_action: Union[Unset, str] = UNSET
    action_descr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_name = self.table_name

        avail_action = self.avail_action

        action_descr = self.action_descr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if table_name is not UNSET:
            field_dict["table_name"] = table_name
        if avail_action is not UNSET:
            field_dict["avail_action"] = avail_action
        if action_descr is not UNSET:
            field_dict["action_descr"] = action_descr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        table_name = d.pop("table_name", UNSET)

        avail_action = d.pop("avail_action", UNSET)

        action_descr = d.pop("action_descr", UNSET)

        diag_table = cls(
            table_name=table_name,
            avail_action=avail_action,
            action_descr=action_descr,
        )

        diag_table.additional_properties = d
        return diag_table

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
