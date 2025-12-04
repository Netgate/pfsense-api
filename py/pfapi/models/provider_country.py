from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_country_setting import ProviderCountrySetting


T = TypeVar("T", bound="ProviderCountry")


@_attrs_define
class ProviderCountry:
    """
    Attributes:
        country (ProviderCountrySetting | Unset):
    """

    country: ProviderCountrySetting | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_country_setting import ProviderCountrySetting

        d = dict(src_dict)
        _country = d.pop("country", UNSET)
        country: ProviderCountrySetting | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = ProviderCountrySetting.from_dict(_country)

        provider_country = cls(
            country=country,
        )

        provider_country.additional_properties = d
        return provider_country

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
