from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        country (Union[Unset, ProviderCountrySetting]):
    """

    country: Union[Unset, "ProviderCountrySetting"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        country: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.provider_country_setting import ProviderCountrySetting

        d = src_dict.copy()
        _country = d.pop("country", UNSET)
        country: Union[Unset, ProviderCountrySetting]
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
