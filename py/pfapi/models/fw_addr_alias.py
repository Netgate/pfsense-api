from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FWAddrAlias")


@_attrs_define
class FWAddrAlias:
    """System or user-defined alias details about the network defined in FWAddrPort.network

    Attributes:
        alias_type (Union[Unset, str]):
        label (Union[Unset, str]):
        descr (Union[Unset, str]):
        table (Union[Unset, str]):
        values (Union[Unset, List[str]]):
    """

    alias_type: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    table: Union[Unset, str] = UNSET
    values: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alias_type = self.alias_type

        label = self.label

        descr = self.descr

        table = self.table

        values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias_type is not UNSET:
            field_dict["alias_type"] = alias_type
        if label is not UNSET:
            field_dict["label"] = label
        if descr is not UNSET:
            field_dict["descr"] = descr
        if table is not UNSET:
            field_dict["table"] = table
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alias_type = d.pop("alias_type", UNSET)

        label = d.pop("label", UNSET)

        descr = d.pop("descr", UNSET)

        table = d.pop("table", UNSET)

        values = cast(List[str], d.pop("values", UNSET))

        fw_addr_alias = cls(
            alias_type=alias_type,
            label=label,
            descr=descr,
            table=table,
            values=values,
        )

        fw_addr_alias.additional_properties = d
        return fw_addr_alias

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
