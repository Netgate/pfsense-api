from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FWSystemAlias")


@_attrs_define
class FWSystemAlias:
    """
    Attributes:
        name (Union[Unset, str]):
        type (Union[Unset, str]):
        descr (Union[Unset, str]):
        address (Union[Unset, str]):
        url (Union[Unset, str]):
        table (Union[Unset, str]):
        if_ident (Union[Unset, str]):
        if_assigned_name (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    table: Union[Unset, str] = UNSET
    if_ident: Union[Unset, str] = UNSET
    if_assigned_name: Union[Unset, str] = UNSET
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        descr = d.pop("descr", UNSET)

        address = d.pop("address", UNSET)

        url = d.pop("url", UNSET)

        table = d.pop("table", UNSET)

        if_ident = d.pop("if_ident", UNSET)

        if_assigned_name = d.pop("if_assigned_name", UNSET)

        fw_system_alias = cls(
            name=name,
            type=type,
            descr=descr,
            address=address,
            url=url,
            table=table,
            if_ident=if_ident,
            if_assigned_name=if_assigned_name,
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
