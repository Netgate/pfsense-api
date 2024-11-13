from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControllerSummary")


@_attrs_define
class ControllerSummary:
    """Information provided to the remote device on how to connect to the
    controller using Netgard.

        Attributes:
            mode_active (Union[Unset, bool]):
            name (Union[Unset, str]):
            key (Union[Unset, str]):
            vpn_pubkey (Union[Unset, str]):
            vpn_listenaddr (Union[Unset, str]):
            vpn_address (Union[Unset, str]):
            vpn_prefix (Union[Unset, str]):
            vpn_netkey (Union[Unset, str]):
            vpn_listenaddr4 (Union[Unset, str]):
            vpn_listenaddr6 (Union[Unset, str]):
    """

    mode_active: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    vpn_pubkey: Union[Unset, str] = UNSET
    vpn_listenaddr: Union[Unset, str] = UNSET
    vpn_address: Union[Unset, str] = UNSET
    vpn_prefix: Union[Unset, str] = UNSET
    vpn_netkey: Union[Unset, str] = UNSET
    vpn_listenaddr4: Union[Unset, str] = UNSET
    vpn_listenaddr6: Union[Unset, str] = UNSET
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

        vpn_listenaddr4 = self.vpn_listenaddr4

        vpn_listenaddr6 = self.vpn_listenaddr6

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode_active is not UNSET:
            field_dict["mode_active"] = mode_active
        if name is not UNSET:
            field_dict["name"] = name
        if key is not UNSET:
            field_dict["key"] = key
        if vpn_pubkey is not UNSET:
            field_dict["vpn_pubkey"] = vpn_pubkey
        if vpn_listenaddr is not UNSET:
            field_dict["vpn_listenaddr"] = vpn_listenaddr
        if vpn_address is not UNSET:
            field_dict["vpn_address"] = vpn_address
        if vpn_prefix is not UNSET:
            field_dict["vpn_prefix"] = vpn_prefix
        if vpn_netkey is not UNSET:
            field_dict["vpn_netkey"] = vpn_netkey
        if vpn_listenaddr4 is not UNSET:
            field_dict["vpn_listenaddr4"] = vpn_listenaddr4
        if vpn_listenaddr6 is not UNSET:
            field_dict["vpn_listenaddr6"] = vpn_listenaddr6

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mode_active = d.pop("mode_active", UNSET)

        name = d.pop("name", UNSET)

        key = d.pop("key", UNSET)

        vpn_pubkey = d.pop("vpn_pubkey", UNSET)

        vpn_listenaddr = d.pop("vpn_listenaddr", UNSET)

        vpn_address = d.pop("vpn_address", UNSET)

        vpn_prefix = d.pop("vpn_prefix", UNSET)

        vpn_netkey = d.pop("vpn_netkey", UNSET)

        vpn_listenaddr4 = d.pop("vpn_listenaddr4", UNSET)

        vpn_listenaddr6 = d.pop("vpn_listenaddr6", UNSET)

        controller_summary = cls(
            mode_active=mode_active,
            name=name,
            key=key,
            vpn_pubkey=vpn_pubkey,
            vpn_listenaddr=vpn_listenaddr,
            vpn_address=vpn_address,
            vpn_prefix=vpn_prefix,
            vpn_netkey=vpn_netkey,
            vpn_listenaddr4=vpn_listenaddr4,
            vpn_listenaddr6=vpn_listenaddr6,
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
