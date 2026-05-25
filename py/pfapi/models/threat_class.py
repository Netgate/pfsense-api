from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThreatClass")


@_attrs_define
class ThreatClass:
    """
    Attributes:
        countries (list[str] | Unset):
        asns (list[str] | Unset):
        categories (list[str] | Unset):
    """

    countries: list[str] | Unset = UNSET
    asns: list[str] | Unset = UNSET
    categories: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        countries: list[str] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        asns: list[str] | Unset = UNSET
        if not isinstance(self.asns, Unset):
            asns = self.asns

        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if countries is not UNSET:
            field_dict["countries"] = countries
        if asns is not UNSET:
            field_dict["asns"] = asns
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        countries = cast(list[str], d.pop("countries", UNSET))

        asns = cast(list[str], d.pop("asns", UNSET))

        categories = cast(list[str], d.pop("categories", UNSET))

        threat_class = cls(
            countries=countries,
            asns=asns,
            categories=categories,
        )

        threat_class.additional_properties = d
        return threat_class

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
