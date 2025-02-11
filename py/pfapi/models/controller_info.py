from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_vpn import DeviceVpn


T = TypeVar("T", bound="ControllerInfo")


@_attrs_define
class ControllerInfo:
    """
    Attributes:
        name (str):
        key (str):
        cert (str):
        vpn_listenaddr (str):
        vpn_address (str):
        vpn_pubkey (str):
        vpn_netkey (str):
        vpn_prefix (str):
        device_pubkey (str):
        device_vpn (DeviceVpn): The device's VPN settings
        tag (Union[Unset, str]):
        noise_secret (Union[Unset, str]):
    """

    name: str
    key: str
    cert: str
    vpn_listenaddr: str
    vpn_address: str
    vpn_pubkey: str
    vpn_netkey: str
    vpn_prefix: str
    device_pubkey: str
    device_vpn: "DeviceVpn"
    tag: Union[Unset, str] = UNSET
    noise_secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        key = self.key

        cert = self.cert

        vpn_listenaddr = self.vpn_listenaddr

        vpn_address = self.vpn_address

        vpn_pubkey = self.vpn_pubkey

        vpn_netkey = self.vpn_netkey

        vpn_prefix = self.vpn_prefix

        device_pubkey = self.device_pubkey

        device_vpn = self.device_vpn.to_dict()

        tag = self.tag

        noise_secret = self.noise_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "key": key,
                "cert": cert,
                "vpn_listenaddr": vpn_listenaddr,
                "vpn_address": vpn_address,
                "vpn_pubkey": vpn_pubkey,
                "vpn_netkey": vpn_netkey,
                "vpn_prefix": vpn_prefix,
                "device_pubkey": device_pubkey,
                "device_vpn": device_vpn,
            }
        )
        if tag is not UNSET:
            field_dict["tag"] = tag
        if noise_secret is not UNSET:
            field_dict["noise_secret"] = noise_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_vpn import DeviceVpn

        d = src_dict.copy()
        name = d.pop("name")

        key = d.pop("key")

        cert = d.pop("cert")

        vpn_listenaddr = d.pop("vpn_listenaddr")

        vpn_address = d.pop("vpn_address")

        vpn_pubkey = d.pop("vpn_pubkey")

        vpn_netkey = d.pop("vpn_netkey")

        vpn_prefix = d.pop("vpn_prefix")

        device_pubkey = d.pop("device_pubkey")

        device_vpn = DeviceVpn.from_dict(d.pop("device_vpn"))

        tag = d.pop("tag", UNSET)

        noise_secret = d.pop("noise_secret", UNSET)

        controller_info = cls(
            name=name,
            key=key,
            cert=cert,
            vpn_listenaddr=vpn_listenaddr,
            vpn_address=vpn_address,
            vpn_pubkey=vpn_pubkey,
            vpn_netkey=vpn_netkey,
            vpn_prefix=vpn_prefix,
            device_pubkey=device_pubkey,
            device_vpn=device_vpn,
            tag=tag,
            noise_secret=noise_secret,
        )

        controller_info.additional_properties = d
        return controller_info

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
