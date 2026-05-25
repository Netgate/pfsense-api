from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.haproxy_stick_table import HaproxyStickTable


T = TypeVar("T", bound="HaproxyStickTableList")


@_attrs_define
class HaproxyStickTableList:
    """
    Attributes:
        tables (list[HaproxyStickTable] | Unset):
    """

    tables: list[HaproxyStickTable] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()
                tables.append(tables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tables is not UNSET:
            field_dict["tables"] = tables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.haproxy_stick_table import HaproxyStickTable

        d = dict(src_dict)
        _tables = d.pop("tables", UNSET)
        tables: list[HaproxyStickTable] | Unset = UNSET
        if _tables is not UNSET:
            tables = []
            for tables_item_data in _tables:
                tables_item = HaproxyStickTable.from_dict(tables_item_data)

                tables.append(tables_item)

        haproxy_stick_table_list = cls(
            tables=tables,
        )

        haproxy_stick_table_list.additional_properties = d
        return haproxy_stick_table_list

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
