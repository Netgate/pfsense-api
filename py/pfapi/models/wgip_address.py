from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WGIPAddress")


@_attrs_define
class WGIPAddress:
    """
    Attributes:
        address (Union[Unset, str]):
        mask (Union[Unset, str]):
        descr (Union[Unset, str]):
    """

    address: Union[Unset, str] = UNSET
    mask: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address

        mask = self.mask

        descr = self.descr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if mask is not UNSET:
            field_dict["mask"] = mask
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        mask = d.pop("mask", UNSET)

        descr = d.pop("descr", UNSET)

        wgip_address = cls(
            address=address,
            mask=mask,
            descr=descr,
        )

        wgip_address.additional_properties = d
        return wgip_address

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