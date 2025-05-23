from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NATAutoAddr")


@_attrs_define
class NATAutoAddr:
    """
    Attributes:
        network (Union[Unset, str]):
        any_ (Union[Unset, bool]):
    """

    network: Union[Unset, str] = UNSET
    any_: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        network = self.network

        any_ = self.any_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network is not UNSET:
            field_dict["network"] = network
        if any_ is not UNSET:
            field_dict["any"] = any_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        network = d.pop("network", UNSET)

        any_ = d.pop("any", UNSET)

        nat_auto_addr = cls(
            network=network,
            any_=any_,
        )

        nat_auto_addr.additional_properties = d
        return nat_auto_addr

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
