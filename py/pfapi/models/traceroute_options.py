from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_value import TextValue


T = TypeVar("T", bound="TracerouteOptions")


@_attrs_define
class TracerouteOptions:
    """Values for traceroute command options

    Attributes:
        src (list[TextValue] | Unset):
        proto (list[str] | Unset):
    """

    src: list[TextValue] | Unset = UNSET
    proto: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.src, Unset):
            src = []
            for src_item_data in self.src:
                src_item = src_item_data.to_dict()
                src.append(src_item)

        proto: list[str] | Unset = UNSET
        if not isinstance(self.proto, Unset):
            proto = self.proto

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if src is not UNSET:
            field_dict["src"] = src
        if proto is not UNSET:
            field_dict["proto"] = proto

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _src = d.pop("src", UNSET)
        src: list[TextValue] | Unset = UNSET
        if _src is not UNSET:
            src = []
            for src_item_data in _src:
                src_item = TextValue.from_dict(src_item_data)

                src.append(src_item)

        proto = cast(list[str], d.pop("proto", UNSET))

        traceroute_options = cls(
            src=src,
            proto=proto,
        )

        traceroute_options.additional_properties = d
        return traceroute_options

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
