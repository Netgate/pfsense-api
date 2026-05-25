from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acme_validation_method_config import ACMEValidationMethodConfig


T = TypeVar("T", bound="ACMEDomain")


@_attrs_define
class ACMEDomain:
    """
    Attributes:
        name (str | Unset):
        enabled (bool | Unset):
        method (str | Unset):
        config (ACMEValidationMethodConfig | Unset):
    """

    name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    method: str | Unset = UNSET
    config: ACMEValidationMethodConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enabled = self.enabled

        method = self.method

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if method is not UNSET:
            field_dict["method"] = method
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acme_validation_method_config import ACMEValidationMethodConfig

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        method = d.pop("method", UNSET)

        _config = d.pop("config", UNSET)
        config: ACMEValidationMethodConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ACMEValidationMethodConfig.from_dict(_config)

        acme_domain = cls(
            name=name,
            enabled=enabled,
            method=method,
            config=config,
        )

        acme_domain.additional_properties = d
        return acme_domain

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
