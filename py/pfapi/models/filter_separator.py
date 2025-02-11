from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FilterSeparator")


@_attrs_define
class FilterSeparator:
    """
    Attributes:
        row (str):
        id (str):
        text (str):
        color (str):
        if_ (str):
    """

    row: str
    id: str
    text: str
    color: str
    if_: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        row = self.row

        id = self.id

        text = self.text

        color = self.color

        if_ = self.if_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "row": row,
                "id": id,
                "text": text,
                "color": color,
                "if": if_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        row = d.pop("row")

        id = d.pop("id")

        text = d.pop("text")

        color = d.pop("color")

        if_ = d.pop("if")

        filter_separator = cls(
            row=row,
            id=id,
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
