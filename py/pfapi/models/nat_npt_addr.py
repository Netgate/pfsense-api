from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NATNptAddr")


@_attrs_define
class NATNptAddr:
    """
    Attributes:
        address (Union[Unset, str]):
        not_ (Union[Unset, bool]):
        type (Union[Unset, str]):
    """

    address: Union[Unset, str] = UNSET
    not_: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address

        not_ = self.not_

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if not_ is not UNSET:
            field_dict["not"] = not_
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        not_ = d.pop("not", UNSET)

        type = d.pop("type", UNSET)

        nat_npt_addr = cls(
            address=address,
            not_=not_,
            type=type,
        )

        nat_npt_addr.additional_properties = d
        return nat_npt_addr

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
