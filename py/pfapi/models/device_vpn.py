from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceVpn")


@_attrs_define
class DeviceVpn:
    """The device's VPN settings

    Attributes:
        vpn_listenaddr (Union[Unset, str]):
        vpn_address (Union[Unset, str]):
        vpn_pubkey (Union[Unset, str]):
        vpn_netkey (Union[Unset, str]):
        vpn_prefix (Union[Unset, str]):
        vpn_state (Union[Unset, str]):
        vpn_conn_start (Union[Unset, int]):
        vpn_conn_stop (Union[Unset, int]):
        vpn_conn_attempt (Union[Unset, int]):
    """

    vpn_listenaddr: Union[Unset, str] = UNSET
    vpn_address: Union[Unset, str] = UNSET
    vpn_pubkey: Union[Unset, str] = UNSET
    vpn_netkey: Union[Unset, str] = UNSET
    vpn_prefix: Union[Unset, str] = UNSET
    vpn_state: Union[Unset, str] = UNSET
    vpn_conn_start: Union[Unset, int] = UNSET
    vpn_conn_stop: Union[Unset, int] = UNSET
    vpn_conn_attempt: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vpn_listenaddr = self.vpn_listenaddr

        vpn_address = self.vpn_address

        vpn_pubkey = self.vpn_pubkey

        vpn_netkey = self.vpn_netkey

        vpn_prefix = self.vpn_prefix

        vpn_state = self.vpn_state

        vpn_conn_start = self.vpn_conn_start

        vpn_conn_stop = self.vpn_conn_stop

        vpn_conn_attempt = self.vpn_conn_attempt

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
