from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_high_availability_advance_config import DhcpHighAvailabilityAdvanceConfig


T = TypeVar("T", bound="DhcpHighAvailabilityConfig")


@_attrs_define
class DhcpHighAvailabilityConfig:
    """High-availability configuration for Kea DHCP service.

    Attributes:
        enable (bool):
        role (str | Unset): primary or standby
        local_name (str | Unset):
        local_address (str | Unset): address:port
        remote_name (str | Unset):
        remote_address (str | Unset): address:port
        advance_options (DhcpHighAvailabilityAdvanceConfig | Unset):
        enable_tls (bool | Unset):
        tls_server_cert_refid (str | Unset):
        enable_mutual_tls (bool | Unset):
        mutual_client_cert_refid (str | Unset):
        available_tls_server_certs (list[str] | Unset):
        available_mutual_client_certs (list[str] | Unset):
    """

    enable: bool
    role: str | Unset = UNSET
    local_name: str | Unset = UNSET
    local_address: str | Unset = UNSET
    remote_name: str | Unset = UNSET
    remote_address: str | Unset = UNSET
    advance_options: DhcpHighAvailabilityAdvanceConfig | Unset = UNSET
    enable_tls: bool | Unset = UNSET
    tls_server_cert_refid: str | Unset = UNSET
    enable_mutual_tls: bool | Unset = UNSET
    mutual_client_cert_refid: str | Unset = UNSET
    available_tls_server_certs: list[str] | Unset = UNSET
    available_mutual_client_certs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        role = self.role

        local_name = self.local_name

        local_address = self.local_address

        remote_name = self.remote_name

        remote_address = self.remote_address

        advance_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advance_options, Unset):
            advance_options = self.advance_options.to_dict()

        enable_tls = self.enable_tls

        tls_server_cert_refid = self.tls_server_cert_refid

        enable_mutual_tls = self.enable_mutual_tls

        mutual_client_cert_refid = self.mutual_client_cert_refid

        available_tls_server_certs: list[str] | Unset = UNSET
        if not isinstance(self.available_tls_server_certs, Unset):
            available_tls_server_certs = self.available_tls_server_certs

        available_mutual_client_certs: list[str] | Unset = UNSET
        if not isinstance(self.available_mutual_client_certs, Unset):
            available_mutual_client_certs = self.available_mutual_client_certs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if local_name is not UNSET:
            field_dict["local_name"] = local_name
        if local_address is not UNSET:
            field_dict["local_address"] = local_address
        if remote_name is not UNSET:
            field_dict["remote_name"] = remote_name
        if remote_address is not UNSET:
            field_dict["remote_address"] = remote_address
        if advance_options is not UNSET:
            field_dict["advance_options"] = advance_options
        if enable_tls is not UNSET:
            field_dict["enable_tls"] = enable_tls
        if tls_server_cert_refid is not UNSET:
            field_dict["tls_server_cert_refid"] = tls_server_cert_refid
        if enable_mutual_tls is not UNSET:
            field_dict["enable_mutual_tls"] = enable_mutual_tls
        if mutual_client_cert_refid is not UNSET:
            field_dict["mutual_client_cert_refid"] = mutual_client_cert_refid
        if available_tls_server_certs is not UNSET:
            field_dict["available_tls_server_certs"] = available_tls_server_certs
        if available_mutual_client_certs is not UNSET:
            field_dict["available_mutual_client_certs"] = available_mutual_client_certs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dhcp_high_availability_advance_config import DhcpHighAvailabilityAdvanceConfig

        d = dict(src_dict)
        enable = d.pop("enable")

        role = d.pop("role", UNSET)

        local_name = d.pop("local_name", UNSET)

        local_address = d.pop("local_address", UNSET)

        remote_name = d.pop("remote_name", UNSET)

        remote_address = d.pop("remote_address", UNSET)

        _advance_options = d.pop("advance_options", UNSET)
        advance_options: DhcpHighAvailabilityAdvanceConfig | Unset
        if isinstance(_advance_options, Unset):
            advance_options = UNSET
        else:
            advance_options = DhcpHighAvailabilityAdvanceConfig.from_dict(_advance_options)

        enable_tls = d.pop("enable_tls", UNSET)

        tls_server_cert_refid = d.pop("tls_server_cert_refid", UNSET)

        enable_mutual_tls = d.pop("enable_mutual_tls", UNSET)

        mutual_client_cert_refid = d.pop("mutual_client_cert_refid", UNSET)

        available_tls_server_certs = cast(list[str], d.pop("available_tls_server_certs", UNSET))

        available_mutual_client_certs = cast(list[str], d.pop("available_mutual_client_certs", UNSET))

        dhcp_high_availability_config = cls(
            enable=enable,
            role=role,
            local_name=local_name,
            local_address=local_address,
            remote_name=remote_name,
            remote_address=remote_address,
            advance_options=advance_options,
            enable_tls=enable_tls,
            tls_server_cert_refid=tls_server_cert_refid,
            enable_mutual_tls=enable_mutual_tls,
            mutual_client_cert_refid=mutual_client_cert_refid,
            available_tls_server_certs=available_tls_server_certs,
            available_mutual_client_certs=available_mutual_client_certs,
        )

        dhcp_high_availability_config.additional_properties = d
        return dhcp_high_availability_config

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
