from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_country_setting import ProviderCountrySetting


T = TypeVar("T", bound="ServiceProviders")


@_attrs_define
class ServiceProviders:
    """
    Attributes:
        countries (list[ProviderCountrySetting] | Unset):
    """

    countries: list[ProviderCountrySetting] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        countries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = []
            for countries_item_data in self.countries:
                countries_item = countries_item_data.to_dict()
                countries.append(countries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if countries is not UNSET:
            field_dict["countries"] = countries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_country_setting import ProviderCountrySetting

        d = dict(src_dict)
        _countries = d.pop("countries", UNSET)
        countries: list[ProviderCountrySetting] | Unset = UNSET
        if _countries is not UNSET:
            countries = []
            for countries_item_data in _countries:
                countries_item = ProviderCountrySetting.from_dict(countries_item_data)

                countries.append(countries_item)

        service_providers = cls(
            countries=countries,
        )

        service_providers.additional_properties = d
        return service_providers

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
