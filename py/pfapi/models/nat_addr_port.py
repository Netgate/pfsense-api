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
        type (Union[Unset, str]):
        port (Union[Unset, str]):
        not_ (Union[Unset, bool]):
    """

    address: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    not_: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address

        type = self.type

        port = self.port

        not_ = self.not_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if type is not UNSET:
            field_dict["type"] = type
        if port is not UNSET:
            field_dict["port"] = port
        if not_ is not UNSET:
            field_dict["not"] = not_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        type = d.pop("type", UNSET)

        port = d.pop("port", UNSET)

        not_ = d.pop("not", UNSET)

        nat_addr_port = cls(
            address=address,
            type=type,
            port=port,
            not_=not_,
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
