from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FWAddrPort")


@_attrs_define
class FWAddrPort:
    """
    Attributes:
        label (str): read-only; label to display to user
        address (Union[Unset, str]): single address, subnet or an alias (FWAlias)
        network (Union[Unset, str]): system aliases: interface name (e.g. opt1), interface address "opt1ip", or firewall
            "self"
        port (Union[Unset, str]):
        not_ (Union[Unset, bool]):
        any_ (Union[Unset, bool]):
        alias_id (Union[Unset, str]):
    """

    label: str
    address: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    not_: Union[Unset, bool] = UNSET
    any_: Union[Unset, bool] = UNSET
    alias_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        address = self.address

        network = self.network

        port = self.port

        not_ = self.not_

        any_ = self.any_

        alias_id = self.alias_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if network is not UNSET:
            field_dict["network"] = network
        if port is not UNSET:
            field_dict["port"] = port
        if not_ is not UNSET:
            field_dict["not"] = not_
        if any_ is not UNSET:
            field_dict["any"] = any_
        if alias_id is not UNSET:
            field_dict["alias_id"] = alias_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        address = d.pop("address", UNSET)

        network = d.pop("network", UNSET)

        port = d.pop("port", UNSET)

        not_ = d.pop("not", UNSET)

        any_ = d.pop("any", UNSET)

        alias_id = d.pop("alias_id", UNSET)

        fw_addr_port = cls(
            label=label,
            address=address,
            network=network,
            port=port,
            not_=not_,
            any_=any_,
            alias_id=alias_id,
        )

        fw_addr_port.additional_properties = d
        return fw_addr_port

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
