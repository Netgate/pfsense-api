from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeviceVpn")


@_attrs_define
class DeviceVpn:
    """The device's VPN settings

    Attributes:
        vpn_listenaddr (str):
        vpn_address (str):
        vpn_pubkey (str):
        vpn_netkey (str):
        vpn_prefix (str):
        vpn_state (str):
        vpn_conn_start (int):
        vpn_conn_stop (int):
        vpn_conn_attempt (int):
    """

    vpn_listenaddr: str
    vpn_address: str
    vpn_pubkey: str
    vpn_netkey: str
    vpn_prefix: str
    vpn_state: str
    vpn_conn_start: int
    vpn_conn_stop: int
    vpn_conn_attempt: int
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
        field_dict.update(
            {
                "vpn_listenaddr": vpn_listenaddr,
                "vpn_address": vpn_address,
                "vpn_pubkey": vpn_pubkey,
                "vpn_netkey": vpn_netkey,
                "vpn_prefix": vpn_prefix,
                "vpn_state": vpn_state,
                "vpn_conn_start": vpn_conn_start,
                "vpn_conn_stop": vpn_conn_stop,
                "vpn_conn_attempt": vpn_conn_attempt,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vpn_listenaddr = d.pop("vpn_listenaddr")

        vpn_address = d.pop("vpn_address")

        vpn_pubkey = d.pop("vpn_pubkey")

        vpn_netkey = d.pop("vpn_netkey")

        vpn_prefix = d.pop("vpn_prefix")

        vpn_state = d.pop("vpn_state")

        vpn_conn_start = d.pop("vpn_conn_start")

        vpn_conn_stop = d.pop("vpn_conn_stop")

        vpn_conn_attempt = d.pop("vpn_conn_attempt")

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
