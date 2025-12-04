from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_feature import LicenseFeature


T = TypeVar("T", bound="SysinfoLicense")


@_attrs_define
class SysinfoLicense:
    """
    Attributes:
        id (str | Unset): license identifier, if no value, then not licensed
        expiration (str | Unset): expiration time in RFC 3339 format
        expired (bool | Unset):
        features (list[LicenseFeature] | Unset):
    """

    id: str | Unset = UNSET
    expiration: str | Unset = UNSET
    expired: bool | Unset = UNSET
    features: list[LicenseFeature] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        expiration = self.expiration

        expired = self.expired

        features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.to_dict()
                features.append(features_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if expired is not UNSET:
            field_dict["expired"] = expired
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_feature import LicenseFeature

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        expiration = d.pop("expiration", UNSET)

        expired = d.pop("expired", UNSET)

        _features = d.pop("features", UNSET)
        features: list[LicenseFeature] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = LicenseFeature.from_dict(features_item_data)

                features.append(features_item)

        sysinfo_license = cls(
            id=id,
            expiration=expiration,
            expired=expired,
            features=features,
        )

        sysinfo_license.additional_properties = d
        return sysinfo_license

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
