from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.captive_portal_config import CaptivePortalConfig
    from ..models.service_certificate import ServiceCertificate
    from ..models.voucher import Voucher


T = TypeVar("T", bound="CaptivePortalInfo")


@_attrs_define
class CaptivePortalInfo:
    """
    Attributes:
        config (CaptivePortalConfig | Unset):
        interfaces (list[str] | Unset):
        certificates (list[ServiceCertificate] | Unset):
        vouch (Voucher | Unset):
    """

    config: CaptivePortalConfig | Unset = UNSET
    interfaces: list[str] | Unset = UNSET
    certificates: list[ServiceCertificate] | Unset = UNSET
    vouch: Voucher | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        interfaces: list[str] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        certificates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.certificates, Unset):
            certificates = []
            for certificates_item_data in self.certificates:
                certificates_item = certificates_item_data.to_dict()
                certificates.append(certificates_item)

        vouch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vouch, Unset):
            vouch = self.vouch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if certificates is not UNSET:
            field_dict["certificates"] = certificates
        if vouch is not UNSET:
            field_dict["vouch"] = vouch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.captive_portal_config import CaptivePortalConfig
        from ..models.service_certificate import ServiceCertificate
        from ..models.voucher import Voucher

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: CaptivePortalConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = CaptivePortalConfig.from_dict(_config)

        interfaces = cast(list[str], d.pop("interfaces", UNSET))

        _certificates = d.pop("certificates", UNSET)
        certificates: list[ServiceCertificate] | Unset = UNSET
        if _certificates is not UNSET:
            certificates = []
            for certificates_item_data in _certificates:
                certificates_item = ServiceCertificate.from_dict(certificates_item_data)

                certificates.append(certificates_item)

        _vouch = d.pop("vouch", UNSET)
        vouch: Voucher | Unset
        if isinstance(_vouch, Unset):
            vouch = UNSET
        else:
            vouch = Voucher.from_dict(_vouch)

        captive_portal_info = cls(
            config=config,
            interfaces=interfaces,
            certificates=certificates,
            vouch=vouch,
        )

        captive_portal_info.additional_properties = d
        return captive_portal_info

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
