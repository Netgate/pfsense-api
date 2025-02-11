from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HWDevice")


@_attrs_define
class HWDevice:
    """
    Attributes:
        name (str):
        location (str):
        type (str):
        vendor (str):
        class_ (str):
    """

    name: str
    location: str
    type: str
    vendor: str
    class_: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        location = self.location

        type = self.type

        vendor = self.vendor

        class_ = self.class_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "location": location,
                "type": type,
                "vendor": vendor,
                "class": class_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        location = d.pop("location")

        type = d.pop("type")

        vendor = d.pop("vendor")

        class_ = d.pop("class")

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
