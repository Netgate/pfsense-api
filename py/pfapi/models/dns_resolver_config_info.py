from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_resolver_config import DNSResolverConfig
    from ..models.dns_resolver_config_info_interfaces import DNSResolverConfigInfoInterfaces
    from ..models.service_certificate import ServiceCertificate


T = TypeVar("T", bound="DNSResolverConfigInfo")


@_attrs_define
class DNSResolverConfigInfo:
    """
    Attributes:
        config (DNSResolverConfig | Unset):
        interfaces (DNSResolverConfigInfoInterfaces | Unset):
        certs (list[ServiceCertificate] | Unset):
        scripts (list[str] | Unset):
    """

    config: DNSResolverConfig | Unset = UNSET
    interfaces: DNSResolverConfigInfoInterfaces | Unset = UNSET
    certs: list[ServiceCertificate] | Unset = UNSET
    scripts: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        interfaces: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces.to_dict()

        certs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.certs, Unset):
            certs = []
            for certs_item_data in self.certs:
                certs_item = certs_item_data.to_dict()
                certs.append(certs_item)

        scripts: list[str] | Unset = UNSET
        if not isinstance(self.scripts, Unset):
            scripts = self.scripts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if certs is not UNSET:
            field_dict["certs"] = certs
        if scripts is not UNSET:
            field_dict["scripts"] = scripts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_resolver_config import DNSResolverConfig
        from ..models.dns_resolver_config_info_interfaces import DNSResolverConfigInfoInterfaces
        from ..models.service_certificate import ServiceCertificate

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: DNSResolverConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = DNSResolverConfig.from_dict(_config)

        _interfaces = d.pop("interfaces", UNSET)
        interfaces: DNSResolverConfigInfoInterfaces | Unset
        if isinstance(_interfaces, Unset):
            interfaces = UNSET
        else:
            interfaces = DNSResolverConfigInfoInterfaces.from_dict(_interfaces)

        _certs = d.pop("certs", UNSET)
        certs: list[ServiceCertificate] | Unset = UNSET
        if _certs is not UNSET:
            certs = []
            for certs_item_data in _certs:
                certs_item = ServiceCertificate.from_dict(certs_item_data)

                certs.append(certs_item)

        scripts = cast(list[str], d.pop("scripts", UNSET))

        dns_resolver_config_info = cls(
            config=config,
            interfaces=interfaces,
            certs=certs,
            scripts=scripts,
        )

        dns_resolver_config_info.additional_properties = d
        return dns_resolver_config_info

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
