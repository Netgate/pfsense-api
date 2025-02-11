from typing import Any, Dict, List, Type, TypeVar, Union, cast

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
        descr (str): description about the alias
        table (str): firewall table, if applicable
        values (List[str]):
        truncated (Union[Unset, bool]): indicates whether the value list is truncated
    """

    alias_type: str
    label: str
    descr: str
    table: str
    values: List[str]
    truncated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alias_type = self.alias_type

        label = self.label

        descr = self.descr

        table = self.table

        values = self.values

        truncated = self.truncated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alias_type": alias_type,
                "label": label,
                "descr": descr,
                "table": table,
                "values": values,
            }
        )
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alias_type = d.pop("alias_type")

        label = d.pop("label")

        descr = d.pop("descr")

        table = d.pop("table")

        values = cast(List[str], d.pop("values"))

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
