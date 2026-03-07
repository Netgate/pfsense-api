from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_value import TextValue


T = TypeVar("T", bound="IPSecExportSettings")


@_attrs_define
class IPSecExportSettings:
    """
    Attributes:
        mobile_p1_exist (bool | Unset): is mobile phase 1 in the ipsec config
        mobile_p2_exist (bool | Unset): is mobile phase 2 in the ipsec config
        mobile_p2_is_tunnel (bool | Unset): are all mobile phase 2 in tunnel mode
        mobile_p1_descr (str | Unset):
        mobile_p1_authmethod (str | Unset): only support eap authmethod for windows
        system_hostname (str | Unset):
        server_addresses (list[str] | Unset):
        vpnclients (list[TextValue] | Unset):
    """

    mobile_p1_exist: bool | Unset = UNSET
    mobile_p2_exist: bool | Unset = UNSET
    mobile_p2_is_tunnel: bool | Unset = UNSET
    mobile_p1_descr: str | Unset = UNSET
    mobile_p1_authmethod: str | Unset = UNSET
    system_hostname: str | Unset = UNSET
    server_addresses: list[str] | Unset = UNSET
    vpnclients: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mobile_p1_exist = self.mobile_p1_exist

        mobile_p2_exist = self.mobile_p2_exist

        mobile_p2_is_tunnel = self.mobile_p2_is_tunnel

        mobile_p1_descr = self.mobile_p1_descr

        mobile_p1_authmethod = self.mobile_p1_authmethod

        system_hostname = self.system_hostname

        server_addresses: list[str] | Unset = UNSET
        if not isinstance(self.server_addresses, Unset):
            server_addresses = self.server_addresses

        vpnclients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vpnclients, Unset):
            vpnclients = []
            for vpnclients_item_data in self.vpnclients:
                vpnclients_item = vpnclients_item_data.to_dict()
                vpnclients.append(vpnclients_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mobile_p1_exist is not UNSET:
            field_dict["mobile_p1_exist"] = mobile_p1_exist
        if mobile_p2_exist is not UNSET:
            field_dict["mobile_p2_exist"] = mobile_p2_exist
        if mobile_p2_is_tunnel is not UNSET:
            field_dict["mobile_p2_is_tunnel"] = mobile_p2_is_tunnel
        if mobile_p1_descr is not UNSET:
            field_dict["mobile_p1_descr"] = mobile_p1_descr
        if mobile_p1_authmethod is not UNSET:
            field_dict["mobile_p1_authmethod"] = mobile_p1_authmethod
        if system_hostname is not UNSET:
            field_dict["system_hostname"] = system_hostname
        if server_addresses is not UNSET:
            field_dict["server_addresses"] = server_addresses
        if vpnclients is not UNSET:
            field_dict["vpnclients"] = vpnclients

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_value import TextValue

        d = dict(src_dict)
        mobile_p1_exist = d.pop("mobile_p1_exist", UNSET)

        mobile_p2_exist = d.pop("mobile_p2_exist", UNSET)

        mobile_p2_is_tunnel = d.pop("mobile_p2_is_tunnel", UNSET)

        mobile_p1_descr = d.pop("mobile_p1_descr", UNSET)

        mobile_p1_authmethod = d.pop("mobile_p1_authmethod", UNSET)

        system_hostname = d.pop("system_hostname", UNSET)

        server_addresses = cast(list[str], d.pop("server_addresses", UNSET))

        _vpnclients = d.pop("vpnclients", UNSET)
        vpnclients: list[TextValue] | Unset = UNSET
        if _vpnclients is not UNSET:
            vpnclients = []
            for vpnclients_item_data in _vpnclients:
                vpnclients_item = TextValue.from_dict(vpnclients_item_data)

                vpnclients.append(vpnclients_item)

        ip_sec_export_settings = cls(
            mobile_p1_exist=mobile_p1_exist,
            mobile_p2_exist=mobile_p2_exist,
            mobile_p2_is_tunnel=mobile_p2_is_tunnel,
            mobile_p1_descr=mobile_p1_descr,
            mobile_p1_authmethod=mobile_p1_authmethod,
            system_hostname=system_hostname,
            server_addresses=server_addresses,
            vpnclients=vpnclients,
        )

        ip_sec_export_settings.additional_properties = d
        return ip_sec_export_settings

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
