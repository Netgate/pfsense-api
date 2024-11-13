from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_provider_setting import ServiceProviderSetting


T = TypeVar("T", bound="ProviderCountrySetting")


@_attrs_define
class ProviderCountrySetting:
    """
    Attributes:
        code (Union[Unset, str]):
        provider (Union[Unset, List['ServiceProviderSetting']]):
    """

    code: Union[Unset, str] = UNSET
    provider: Union[Unset, List["ServiceProviderSetting"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        provider: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.provider, Unset):
            provider = []
            for provider_item_data in self.provider:
                provider_item = provider_item_data.to_dict()
                provider.append(provider_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_provider_setting import ServiceProviderSetting

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        provider = []
        _provider = d.pop("provider", UNSET)
        for provider_item_data in _provider or []:
            provider_item = ServiceProviderSetting.from_dict(provider_item_data)

            provider.append(provider_item)

        provider_country_setting = cls(
            code=code,
            provider=provider,
        )

        provider_country_setting.additional_properties = d
        return provider_country_setting

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
