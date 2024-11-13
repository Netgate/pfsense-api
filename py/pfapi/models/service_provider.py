from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_provider_setting import ServiceProviderSetting


T = TypeVar("T", bound="ServiceProvider")


@_attrs_define
class ServiceProvider:
    """
    Attributes:
        provider (Union[Unset, ServiceProviderSetting]):
    """

    provider: Union[Unset, "ServiceProviderSetting"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_provider_setting import ServiceProviderSetting

        d = src_dict.copy()
        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, ServiceProviderSetting]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ServiceProviderSetting.from_dict(_provider)

        service_provider = cls(
            provider=provider,
        )

        service_provider.additional_properties = d
        return service_provider

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
