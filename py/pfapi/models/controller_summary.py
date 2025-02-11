from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControllerSummary")


@_attrs_define
class ControllerSummary:
    """Information provided to the remote device on how to connect to the
    controller using Netgard.

        Attributes:
            mode_active (bool):
            name (str):
            key (str):
            vpn_pubkey (str):
            vpn_listenaddr (str):
            vpn_address (str):
            vpn_prefix (str):
            vpn_netkey (str):
    """

    mode_active: bool
    name: str
    key: str
    vpn_pubkey: str
    vpn_listenaddr: str
    vpn_address: str
    vpn_prefix: str
    vpn_netkey: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mode_active = self.mode_active

        name = self.name

        key = self.key

        vpn_pubkey = self.vpn_pubkey

        vpn_listenaddr = self.vpn_listenaddr

        vpn_address = self.vpn_address

        vpn_prefix = self.vpn_prefix

        vpn_netkey = self.vpn_netkey

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode_active": mode_active,
                "name": name,
                "key": key,
                "vpn_pubkey": vpn_pubkey,
                "vpn_listenaddr": vpn_listenaddr,
                "vpn_address": vpn_address,
                "vpn_prefix": vpn_prefix,
                "vpn_netkey": vpn_netkey,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mode_active = d.pop("mode_active")

        name = d.pop("name")

        key = d.pop("key")

        vpn_pubkey = d.pop("vpn_pubkey")

        vpn_listenaddr = d.pop("vpn_listenaddr")

        vpn_address = d.pop("vpn_address")

        vpn_prefix = d.pop("vpn_prefix")

        vpn_netkey = d.pop("vpn_netkey")

        controller_summary = cls(
            mode_active=mode_active,
            name=name,
            key=key,
            vpn_pubkey=vpn_pubkey,
            vpn_listenaddr=vpn_listenaddr,
            vpn_address=vpn_address,
            vpn_prefix=vpn_prefix,
            vpn_netkey=vpn_netkey,
        )

        controller_summary.additional_properties = d
        return controller_summary

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
