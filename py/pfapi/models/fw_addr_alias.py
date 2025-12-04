from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FWAddrAlias")


@_attrs_define
class FWAddrAlias:
    """System or user-defined alias details about the network defined in FWAddrPort.network

    Attributes:
        alias_type (str): system, host, port, network, url
        label (str): alias label e.g. LAN__NETWORK, alias.name
        descr (str | Unset): description about the alias
        table (str | Unset): firewall table, if applicable
        values (list[str] | Unset):
        truncated (bool | Unset): indicates whether the value list is truncated
    """

    alias_type: str
    label: str
    descr: str | Unset = UNSET
    table: str | Unset = UNSET
    values: list[str] | Unset = UNSET
    truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias_type = self.alias_type

        label = self.label

        descr = self.descr

        table = self.table

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alias_type": alias_type,
                "label": label,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if table is not UNSET:
            field_dict["table"] = table
        if values is not UNSET:
            field_dict["values"] = values
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alias_type = d.pop("alias_type")

        label = d.pop("label")

        descr = d.pop("descr", UNSET)

        table = d.pop("table", UNSET)

        values = cast(list[str], d.pop("values", UNSET))

        truncated = d.pop("truncated", UNSET)

        fw_addr_alias = cls(
            alias_type=alias_type,
            label=label,
            descr=descr,
            table=table,
            values=values,
            truncated=truncated,
        )

        fw_addr_alias.additional_properties = d
        return fw_addr_alias

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
