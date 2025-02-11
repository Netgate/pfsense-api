from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FWAddrPort")


@_attrs_define
class FWAddrPort:
    """
    Attributes:
        label (str):
        address (str):
        network (str):
        port (str):
        not_ (bool):
        alias_id (str):
        any_ (Union[Unset, bool]):
    """

    label: str
    address: str
    network: str
    port: str
    not_: bool
    alias_id: str
    any_: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        address = self.address

        network = self.network

        port = self.port

        not_ = self.not_

        alias_id = self.alias_id

        any_ = self.any_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "address": address,
                "network": network,
                "port": port,
                "not": not_,
                "alias_id": alias_id,
            }
        )
        if any_ is not UNSET:
            field_dict["any"] = any_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        address = d.pop("address")

        network = d.pop("network")

        port = d.pop("port")

        not_ = d.pop("not")

        alias_id = d.pop("alias_id")

        any_ = d.pop("any", UNSET)

        fw_addr_port = cls(
            label=label,
            address=address,
            network=network,
            port=port,
            not_=not_,
            alias_id=alias_id,
            any_=any_,
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
