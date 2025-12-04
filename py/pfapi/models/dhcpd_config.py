from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_global_settings import DhcpGlobalSettings
    from ..models.dhcp_service_config import DhcpServiceConfig


T = TypeVar("T", bound="DhcpdConfig")


@_attrs_define
class DhcpdConfig:
    """
    Attributes:
        service (DhcpGlobalSettings | Unset):
        dhcpd (DhcpServiceConfig | Unset): Per IP version DHCP service setting
        dhcpdv6 (DhcpServiceConfig | Unset): Per IP version DHCP service setting
    """

    service: DhcpGlobalSettings | Unset = UNSET
    dhcpd: DhcpServiceConfig | Unset = UNSET
    dhcpdv6: DhcpServiceConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.to_dict()

        dhcpd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcpd, Unset):
            dhcpd = self.dhcpd.to_dict()

        dhcpdv6: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcpdv6, Unset):
            dhcpdv6 = self.dhcpdv6.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service is not UNSET:
            field_dict["service"] = service
        if dhcpd is not UNSET:
            field_dict["dhcpd"] = dhcpd
        if dhcpdv6 is not UNSET:
            field_dict["dhcpdv6"] = dhcpdv6

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dhcp_global_settings import DhcpGlobalSettings
        from ..models.dhcp_service_config import DhcpServiceConfig

        d = dict(src_dict)
        _service = d.pop("service", UNSET)
        service: DhcpGlobalSettings | Unset
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = DhcpGlobalSettings.from_dict(_service)

        _dhcpd = d.pop("dhcpd", UNSET)
        dhcpd: DhcpServiceConfig | Unset
        if isinstance(_dhcpd, Unset):
            dhcpd = UNSET
        else:
            dhcpd = DhcpServiceConfig.from_dict(_dhcpd)

        _dhcpdv6 = d.pop("dhcpdv6", UNSET)
        dhcpdv6: DhcpServiceConfig | Unset
        if isinstance(_dhcpdv6, Unset):
            dhcpdv6 = UNSET
        else:
            dhcpdv6 = DhcpServiceConfig.from_dict(_dhcpdv6)

        dhcpd_config = cls(
            service=service,
            dhcpd=dhcpd,
            dhcpdv6=dhcpdv6,
        )

        dhcpd_config.additional_properties = d
        return dhcpd_config

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
