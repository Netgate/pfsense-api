from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControlledDeviceAuth")


@_attrs_define
class ControlledDeviceAuth:
    """
    Attributes:
        vpn_pubkey (Union[Unset, str]):
        vpn_address (Union[Unset, str]):
        vpn_listenaddr (Union[Unset, str]):
        cert (Union[Unset, str]):
        vpn_listenaddr4 (Union[Unset, str]):
        vpn_listenaddr6 (Union[Unset, str]):
    """

    vpn_pubkey: Union[Unset, str] = UNSET
    vpn_address: Union[Unset, str] = UNSET
    vpn_listenaddr: Union[Unset, str] = UNSET
    cert: Union[Unset, str] = UNSET
    vpn_listenaddr4: Union[Unset, str] = UNSET
    vpn_listenaddr6: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vpn_pubkey = self.vpn_pubkey

        vpn_address = self.vpn_address

        vpn_listenaddr = self.vpn_listenaddr

        cert = self.cert

        vpn_listenaddr4 = self.vpn_listenaddr4

        vpn_listenaddr6 = self.vpn_listenaddr6

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpn_pubkey is not UNSET:
            field_dict["vpn_pubkey"] = vpn_pubkey
        if vpn_address is not UNSET:
            field_dict["vpn_address"] = vpn_address
        if vpn_listenaddr is not UNSET:
            field_dict["vpn_listenaddr"] = vpn_listenaddr
        if cert is not UNSET:
            field_dict["cert"] = cert
        if vpn_listenaddr4 is not UNSET:
            field_dict["vpn_listenaddr4"] = vpn_listenaddr4
        if vpn_listenaddr6 is not UNSET:
            field_dict["vpn_listenaddr6"] = vpn_listenaddr6

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vpn_pubkey = d.pop("vpn_pubkey", UNSET)

        vpn_address = d.pop("vpn_address", UNSET)

        vpn_listenaddr = d.pop("vpn_listenaddr", UNSET)

        cert = d.pop("cert", UNSET)

        vpn_listenaddr4 = d.pop("vpn_listenaddr4", UNSET)

        vpn_listenaddr6 = d.pop("vpn_listenaddr6", UNSET)

        controlled_device_auth = cls(
            vpn_pubkey=vpn_pubkey,
            vpn_address=vpn_address,
            vpn_listenaddr=vpn_listenaddr,
            cert=cert,
            vpn_listenaddr4=vpn_listenaddr4,
            vpn_listenaddr6=vpn_listenaddr6,
        )

        controlled_device_auth.additional_properties = d
        return controlled_device_auth

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
