from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptiveElement")


@_attrs_define
class CaptiveElement:
    """
    Attributes:
        name (Union[Unset, str]):
        size (Union[Unset, str]):
        nocontent (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    nocontent: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        size = self.size

        nocontent = self.nocontent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if nocontent is not UNSET:
            field_dict["nocontent"] = nocontent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        nocontent = d.pop("nocontent", UNSET)

        captive_element = cls(
            name=name,
            size=size,
            nocontent=nocontent,
        )

        captive_element.additional_properties = d
        return captive_element

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
