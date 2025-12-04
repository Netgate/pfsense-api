from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FWSystemAlias")


@_attrs_define
class FWSystemAlias:
    """
    Attributes:
        name (str):
        type_ (str):
        descr (str | Unset):
        address (str | Unset): space separated list of addresses
        url (str | Unset):
        table (str | Unset): name of firewall table applicable to this alias
        if_ident (str | Unset): interface identity
        if_assigned_name (str | Unset): interface assigned name
        truncated (bool | Unset):
    """

    name: str
    type_: str
    descr: str | Unset = UNSET
    address: str | Unset = UNSET
    url: str | Unset = UNSET
    table: str | Unset = UNSET
    if_ident: str | Unset = UNSET
    if_assigned_name: str | Unset = UNSET
    truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        descr = self.descr

        address = self.address

        url = self.url

        table = self.table

        if_ident = self.if_ident

        if_assigned_name = self.if_assigned_name

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if address is not UNSET:
            field_dict["address"] = address
        if url is not UNSET:
            field_dict["url"] = url
        if table is not UNSET:
            field_dict["table"] = table
        if if_ident is not UNSET:
            field_dict["if_ident"] = if_ident
        if if_assigned_name is not UNSET:
            field_dict["if_assigned_name"] = if_assigned_name
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        descr = d.pop("descr", UNSET)

        address = d.pop("address", UNSET)

        url = d.pop("url", UNSET)

        table = d.pop("table", UNSET)

        if_ident = d.pop("if_ident", UNSET)

        if_assigned_name = d.pop("if_assigned_name", UNSET)

        truncated = d.pop("truncated", UNSET)

        fw_system_alias = cls(
            name=name,
            type_=type_,
            descr=descr,
            address=address,
            url=url,
            table=table,
            if_ident=if_ident,
            if_assigned_name=if_assigned_name,
            truncated=truncated,
        )

        fw_system_alias.additional_properties = d
        return fw_system_alias

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
