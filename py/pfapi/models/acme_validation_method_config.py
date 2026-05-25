from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acme_validation_method_config_additional import ACMEValidationMethodConfigAdditional
    from ..models.acme_validation_method_config_credentials import ACMEValidationMethodConfigCredentials


T = TypeVar("T", bound="ACMEValidationMethodConfig")


@_attrs_define
class ACMEValidationMethodConfig:
    """
    Attributes:
        credentials (ACMEValidationMethodConfigCredentials | Unset):
        additional (ACMEValidationMethodConfigAdditional | Unset):
    """

    credentials: ACMEValidationMethodConfigCredentials | Unset = UNSET
    additional: ACMEValidationMethodConfigAdditional | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        additional: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional, Unset):
            additional = self.additional.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if additional is not UNSET:
            field_dict["additional"] = additional

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acme_validation_method_config_additional import ACMEValidationMethodConfigAdditional
        from ..models.acme_validation_method_config_credentials import ACMEValidationMethodConfigCredentials

        d = dict(src_dict)
        _credentials = d.pop("credentials", UNSET)
        credentials: ACMEValidationMethodConfigCredentials | Unset
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = ACMEValidationMethodConfigCredentials.from_dict(_credentials)

        _additional = d.pop("additional", UNSET)
        additional: ACMEValidationMethodConfigAdditional | Unset
        if isinstance(_additional, Unset):
            additional = UNSET
        else:
            additional = ACMEValidationMethodConfigAdditional.from_dict(_additional)

        acme_validation_method_config = cls(
            credentials=credentials,
            additional=additional,
        )

        acme_validation_method_config.additional_properties = d
        return acme_validation_method_config

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
