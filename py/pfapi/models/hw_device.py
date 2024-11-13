from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HWDevice")


@_attrs_define
class HWDevice:
    """
    Attributes:
        name (Union[Unset, str]):
        location (Union[Unset, str]):
        type (Union[Unset, str]):
        vendor (Union[Unset, str]):
        class_ (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    class_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        location = self.location

        type = self.type

        vendor = self.vendor

        class_ = self.class_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if location is not UNSET:
            field_dict["location"] = location
        if type is not UNSET:
            field_dict["type"] = type
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if class_ is not UNSET:
            field_dict["class"] = class_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        location = d.pop("location", UNSET)

        type = d.pop("type", UNSET)

        vendor = d.pop("vendor", UNSET)

        class_ = d.pop("class", UNSET)

        hw_device = cls(
            name=name,
            location=location,
            type=type,
            vendor=vendor,
            class_=class_,
        )

        hw_device.additional_properties = d
        return hw_device

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
