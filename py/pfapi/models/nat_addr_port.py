from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NATAddrPort")


@_attrs_define
class NATAddrPort:
    """
    Attributes:
        address (Union[Unset, str]):
        network (Union[Unset, str]):
        port (Union[Unset, str]):
        any_ (Union[Unset, bool]):
    """

    address: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    any_: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address

        network = self.network

        port = self.port

        any_ = self.any_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if network is not UNSET:
            field_dict["network"] = network
        if port is not UNSET:
            field_dict["port"] = port
        if any_ is not UNSET:
            field_dict["any"] = any_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        network = d.pop("network", UNSET)

        port = d.pop("port", UNSET)

        any_ = d.pop("any", UNSET)

        nat_addr_port = cls(
            address=address,
            network=network,
            port=port,
            any_=any_,
        )

        nat_addr_port.additional_properties = d
        return nat_addr_port

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
