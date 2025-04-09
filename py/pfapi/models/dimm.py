from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dimm")


@_attrs_define
class Dimm:
    """
    Attributes:
        slot (Union[Unset, str]):
        size (Union[Unset, int]):
        type (Union[Unset, str]):
    """

    slot: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        slot = self.slot

        size = self.size

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slot is not UNSET:
            field_dict["slot"] = slot
        if size is not UNSET:
            field_dict["size"] = size
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        slot = d.pop("slot", UNSET)

        size = d.pop("size", UNSET)

        type = d.pop("type", UNSET)

        dimm = cls(
            slot=slot,
            size=size,
            type=type,
        )

        dimm.additional_properties = d
        return dimm

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
