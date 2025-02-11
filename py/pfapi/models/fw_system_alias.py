from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FWSystemAlias")


@_attrs_define
class FWSystemAlias:
    """
    Attributes:
        name (str):
        type (str):
        descr (str):
        address (str):
        url (str):
        table (str):
        if_ident (str):
        if_assigned_name (str):
        truncated (bool):
    """

    name: str
    type: str
    descr: str
    address: str
    url: str
    table: str
    if_ident: str
    if_assigned_name: str
    truncated: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        type = self.type

        descr = self.descr

        address = self.address

        url = self.url

        table = self.table

        if_ident = self.if_ident

        if_assigned_name = self.if_assigned_name

        truncated = self.truncated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
                "descr": descr,
                "address": address,
                "url": url,
                "table": table,
                "if_ident": if_ident,
                "if_assigned_name": if_assigned_name,
                "truncated": truncated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = d.pop("type")

        descr = d.pop("descr")

        address = d.pop("address")

        url = d.pop("url")

        table = d.pop("table")

        if_ident = d.pop("if_ident")

        if_assigned_name = d.pop("if_assigned_name")

        truncated = d.pop("truncated")

        fw_system_alias = cls(
            name=name,
            type=type,
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
