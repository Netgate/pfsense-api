from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        provider (ServiceProviderSetting | Unset):
    """

    provider: ServiceProviderSetting | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_provider_setting import ServiceProviderSetting

        d = dict(src_dict)
        _provider = d.pop("provider", UNSET)
        provider: ServiceProviderSetting | Unset
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
