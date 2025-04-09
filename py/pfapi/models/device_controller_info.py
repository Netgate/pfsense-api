from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceControllerInfo")


@_attrs_define
class DeviceControllerInfo:
    """brief information about the controller managing the device

    Attributes:
        pubkey (Union[Unset, str]): base64 encoded public key of the controller
        vpn_ep_address (Union[Unset, str]): list of MIM VPN listening addresses of the controller
        vpn_addr (Union[Unset, str]): MIM vpn address
    """

    pubkey: Union[Unset, str] = UNSET
    vpn_ep_address: Union[Unset, str] = UNSET
    vpn_addr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pubkey = self.pubkey

        vpn_ep_address = self.vpn_ep_address

        vpn_addr = self.vpn_addr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if vpn_ep_address is not UNSET:
            field_dict["vpn_ep_address"] = vpn_ep_address
        if vpn_addr is not UNSET:
            field_dict["vpn_addr"] = vpn_addr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pubkey = d.pop("pubkey", UNSET)

        vpn_ep_address = d.pop("vpn_ep_address", UNSET)

        vpn_addr = d.pop("vpn_addr", UNSET)

        device_controller_info = cls(
            pubkey=pubkey,
            vpn_ep_address=vpn_ep_address,
            vpn_addr=vpn_addr,
        )

        device_controller_info.additional_properties = d
        return device_controller_info

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
