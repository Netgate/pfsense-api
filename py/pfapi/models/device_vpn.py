from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceVpn")


@_attrs_define
class DeviceVpn:
    """The device's VPN settings

    Attributes:
        vpn_listenaddr (str | Unset):
        vpn_address (str | Unset):
        vpn_pubkey (str | Unset):
        vpn_netkey (str | Unset):
        vpn_prefix (str | Unset):
        vpn_state (str | Unset):
        vpn_conn_start (int | Unset):
        vpn_conn_stop (int | Unset):
        vpn_conn_attempt (int | Unset):
    """

    vpn_listenaddr: str | Unset = UNSET
    vpn_address: str | Unset = UNSET
    vpn_pubkey: str | Unset = UNSET
    vpn_netkey: str | Unset = UNSET
    vpn_prefix: str | Unset = UNSET
    vpn_state: str | Unset = UNSET
    vpn_conn_start: int | Unset = UNSET
    vpn_conn_stop: int | Unset = UNSET
    vpn_conn_attempt: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpn_listenaddr = self.vpn_listenaddr

        vpn_address = self.vpn_address

        vpn_pubkey = self.vpn_pubkey

        vpn_netkey = self.vpn_netkey

        vpn_prefix = self.vpn_prefix

        vpn_state = self.vpn_state

        vpn_conn_start = self.vpn_conn_start

        vpn_conn_stop = self.vpn_conn_stop

        vpn_conn_attempt = self.vpn_conn_attempt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpn_listenaddr is not UNSET:
            field_dict["vpn_listenaddr"] = vpn_listenaddr
        if vpn_address is not UNSET:
            field_dict["vpn_address"] = vpn_address
        if vpn_pubkey is not UNSET:
            field_dict["vpn_pubkey"] = vpn_pubkey
        if vpn_netkey is not UNSET:
            field_dict["vpn_netkey"] = vpn_netkey
        if vpn_prefix is not UNSET:
            field_dict["vpn_prefix"] = vpn_prefix
        if vpn_state is not UNSET:
            field_dict["vpn_state"] = vpn_state
        if vpn_conn_start is not UNSET:
            field_dict["vpn_conn_start"] = vpn_conn_start
        if vpn_conn_stop is not UNSET:
            field_dict["vpn_conn_stop"] = vpn_conn_stop
        if vpn_conn_attempt is not UNSET:
            field_dict["vpn_conn_attempt"] = vpn_conn_attempt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vpn_listenaddr = d.pop("vpn_listenaddr", UNSET)

        vpn_address = d.pop("vpn_address", UNSET)

        vpn_pubkey = d.pop("vpn_pubkey", UNSET)

        vpn_netkey = d.pop("vpn_netkey", UNSET)

        vpn_prefix = d.pop("vpn_prefix", UNSET)

        vpn_state = d.pop("vpn_state", UNSET)

        vpn_conn_start = d.pop("vpn_conn_start", UNSET)

        vpn_conn_stop = d.pop("vpn_conn_stop", UNSET)

        vpn_conn_attempt = d.pop("vpn_conn_attempt", UNSET)

        device_vpn = cls(
            vpn_listenaddr=vpn_listenaddr,
            vpn_address=vpn_address,
            vpn_pubkey=vpn_pubkey,
            vpn_netkey=vpn_netkey,
            vpn_prefix=vpn_prefix,
            vpn_state=vpn_state,
            vpn_conn_start=vpn_conn_start,
            vpn_conn_stop=vpn_conn_stop,
            vpn_conn_attempt=vpn_conn_attempt,
        )

        device_vpn.additional_properties = d
        return device_vpn

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
