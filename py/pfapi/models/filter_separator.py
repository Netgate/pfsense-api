from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterSeparator")


@_attrs_define
class FilterSeparator:
    """
    Attributes:
        id (Union[Unset, str]):
        row (Union[Unset, str]):
        text (Union[Unset, str]):
        color (Union[Unset, str]):
        if_ (Union[Unset, str]): interface name
    """

    id: Union[Unset, str] = UNSET
    row: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    if_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        row = self.row

        text = self.text

        color = self.color

        if_ = self.if_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if row is not UNSET:
            field_dict["row"] = row
        if text is not UNSET:
            field_dict["text"] = text
        if color is not UNSET:
            field_dict["color"] = color
        if if_ is not UNSET:
            field_dict["if"] = if_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        row = d.pop("row", UNSET)

        text = d.pop("text", UNSET)

        color = d.pop("color", UNSET)

        if_ = d.pop("if", UNSET)

        filter_separator = cls(
            id=id,
            row=row,
            text=text,
            color=color,
            if_=if_,
        )

        filter_separator.additional_properties = d
        return filter_separator

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
