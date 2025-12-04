from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dhcp_global_settings_ipv_6_duid_type import DhcpGlobalSettingsIpv6DuidType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpGlobalSettings")


@_attrs_define
class DhcpGlobalSettings:
    """
    Attributes:
        backend (str | Unset):
        radvd_debug (bool | Unset):
        dhcp6_debug (bool | Unset):
        address_release (bool | Unset):
        ignore_isc_warn (bool | Unset):
        ipv6_duid_type (DhcpGlobalSettingsIpv6DuidType | Unset): A DHCPv6 Unique Identifier (DUID) is used by the
            firewall when requesting an IPv6 address.

            By default, the firewall automatically creates a dynamic DUID-LLT which is not saved
            in the firewall configuration. To ensure that the same DUID is retained by the firewall
            at all times, enter a DUID in this section. The new DUID will take effect after a
            reboot or when the WAN interface(s) are reconfigured by the firewall.

            If the firewall is configured to use a RAM disk for state (such as /var), the best
            practice is to store a DUID here; otherwise, the DUID will change on each reboot.

            When setting the config, if duid type is 0/raw and no value for ipv6_duid_raw is provided,
            then the DUID will be removed from the firewall configuration.
        ipv6_duid_raw (str | Unset):
        ipv6_duid_llt_time (str | Unset):
        ipv6_duid_llt_ll (str | Unset):
        ipv6_duid_en_en (str | Unset):
        ipv6_duid_en_id (str | Unset):
        ipv6_duid_ll (str | Unset):
        ipv6_duid_uuid (str | Unset):
    """

    backend: str | Unset = UNSET
    radvd_debug: bool | Unset = UNSET
    dhcp6_debug: bool | Unset = UNSET
    address_release: bool | Unset = UNSET
    ignore_isc_warn: bool | Unset = UNSET
    ipv6_duid_type: DhcpGlobalSettingsIpv6DuidType | Unset = UNSET
    ipv6_duid_raw: str | Unset = UNSET
    ipv6_duid_llt_time: str | Unset = UNSET
    ipv6_duid_llt_ll: str | Unset = UNSET
    ipv6_duid_en_en: str | Unset = UNSET
    ipv6_duid_en_id: str | Unset = UNSET
    ipv6_duid_ll: str | Unset = UNSET
    ipv6_duid_uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backend = self.backend

        radvd_debug = self.radvd_debug

        dhcp6_debug = self.dhcp6_debug

        address_release = self.address_release

        ignore_isc_warn = self.ignore_isc_warn

        ipv6_duid_type: str | Unset = UNSET
        if not isinstance(self.ipv6_duid_type, Unset):
            ipv6_duid_type = self.ipv6_duid_type.value

        ipv6_duid_raw = self.ipv6_duid_raw

        ipv6_duid_llt_time = self.ipv6_duid_llt_time

        ipv6_duid_llt_ll = self.ipv6_duid_llt_ll

        ipv6_duid_en_en = self.ipv6_duid_en_en

        ipv6_duid_en_id = self.ipv6_duid_en_id

        ipv6_duid_ll = self.ipv6_duid_ll

        ipv6_duid_uuid = self.ipv6_duid_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backend is not UNSET:
            field_dict["backend"] = backend
        if radvd_debug is not UNSET:
            field_dict["radvd_debug"] = radvd_debug
        if dhcp6_debug is not UNSET:
            field_dict["dhcp6_debug"] = dhcp6_debug
        if address_release is not UNSET:
            field_dict["address_release"] = address_release
        if ignore_isc_warn is not UNSET:
            field_dict["ignore_isc_warn"] = ignore_isc_warn
        if ipv6_duid_type is not UNSET:
            field_dict["ipv6_duid_type"] = ipv6_duid_type
        if ipv6_duid_raw is not UNSET:
            field_dict["ipv6_duid_raw"] = ipv6_duid_raw
        if ipv6_duid_llt_time is not UNSET:
            field_dict["ipv6_duid_llt_time"] = ipv6_duid_llt_time
        if ipv6_duid_llt_ll is not UNSET:
            field_dict["ipv6_duid_llt_ll"] = ipv6_duid_llt_ll
        if ipv6_duid_en_en is not UNSET:
            field_dict["ipv6_duid_en_en"] = ipv6_duid_en_en
        if ipv6_duid_en_id is not UNSET:
            field_dict["ipv6_duid_en_id"] = ipv6_duid_en_id
        if ipv6_duid_ll is not UNSET:
            field_dict["ipv6_duid_ll"] = ipv6_duid_ll
        if ipv6_duid_uuid is not UNSET:
            field_dict["ipv6_duid_uuid"] = ipv6_duid_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backend = d.pop("backend", UNSET)

        radvd_debug = d.pop("radvd_debug", UNSET)

        dhcp6_debug = d.pop("dhcp6_debug", UNSET)

        address_release = d.pop("address_release", UNSET)

        ignore_isc_warn = d.pop("ignore_isc_warn", UNSET)

        _ipv6_duid_type = d.pop("ipv6_duid_type", UNSET)
        ipv6_duid_type: DhcpGlobalSettingsIpv6DuidType | Unset
        if isinstance(_ipv6_duid_type, Unset):
            ipv6_duid_type = UNSET
        else:
            ipv6_duid_type = DhcpGlobalSettingsIpv6DuidType(_ipv6_duid_type)

        ipv6_duid_raw = d.pop("ipv6_duid_raw", UNSET)

        ipv6_duid_llt_time = d.pop("ipv6_duid_llt_time", UNSET)

        ipv6_duid_llt_ll = d.pop("ipv6_duid_llt_ll", UNSET)

        ipv6_duid_en_en = d.pop("ipv6_duid_en_en", UNSET)

        ipv6_duid_en_id = d.pop("ipv6_duid_en_id", UNSET)

        ipv6_duid_ll = d.pop("ipv6_duid_ll", UNSET)

        ipv6_duid_uuid = d.pop("ipv6_duid_uuid", UNSET)

        dhcp_global_settings = cls(
            backend=backend,
            radvd_debug=radvd_debug,
            dhcp6_debug=dhcp6_debug,
            address_release=address_release,
            ignore_isc_warn=ignore_isc_warn,
            ipv6_duid_type=ipv6_duid_type,
            ipv6_duid_raw=ipv6_duid_raw,
            ipv6_duid_llt_time=ipv6_duid_llt_time,
            ipv6_duid_llt_ll=ipv6_duid_llt_ll,
            ipv6_duid_en_en=ipv6_duid_en_en,
            ipv6_duid_en_id=ipv6_duid_en_id,
            ipv6_duid_ll=ipv6_duid_ll,
            ipv6_duid_uuid=ipv6_duid_uuid,
        )

        dhcp_global_settings.additional_properties = d
        return dhcp_global_settings

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
