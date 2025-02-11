from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controlled_device_info import ControlledDeviceInfo


T = TypeVar("T", bound="DeviceIdentity")


@_attrs_define
class DeviceIdentity:
    """Fields:
    * name:            name of device
    * alias:           another alias for the device
    * type:            device type
    * pubkey:          public key identity of device
    * address:         device's API URL, e.g. https://0.0.0.0:8443
    * vpn_pubkey:      VPN public key
    * vpn_address:     MIM VPN address
    * vpn_prefix:      MIM VPN address subnet
    * vpn_netkey:      MIM VPN netkey
    * vpn_listenaddr:  MIM listening address:port
    * devinfo:         summary of device information
    * tags:            Optional tags assigned to device

    * controller_add:  curl command that can be used to add the device to the controller.

        Attributes:
            name (str): name of device
            alias (str): another alias for the device
            device_type (str): device type, eg pfsense
            type (str): alias to device_type
            pubkey (str): public key identity of device
            address (str): device's API URL, e.g. https://0.0.0.0:8443
            vpn_pubkey (str): VPN public key
            vpn_address (str): MIM VPN address
            vpn_prefix (str): MIM VPN address subnet
            vpn_netkey (str): MIM VPN netkey
            vpn_listenaddr (str): MIM listening address:port
            tags (List[str]):
            devinfo (Union[Unset, ControlledDeviceInfo]): Additional information about the device
            controller_add (Union[Unset, str]): API command that can be used to add the device to the controller
    """

    name: str
    alias: str
    device_type: str
    type: str
    pubkey: str
    address: str
    vpn_pubkey: str
    vpn_address: str
    vpn_prefix: str
    vpn_netkey: str
    vpn_listenaddr: str
    tags: List[str]
    devinfo: Union[Unset, "ControlledDeviceInfo"] = UNSET
    controller_add: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        alias = self.alias

        device_type = self.device_type

        type = self.type

        pubkey = self.pubkey

        address = self.address

        vpn_pubkey = self.vpn_pubkey

        vpn_address = self.vpn_address

        vpn_prefix = self.vpn_prefix

        vpn_netkey = self.vpn_netkey

        vpn_listenaddr = self.vpn_listenaddr

        tags = self.tags

        devinfo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.devinfo, Unset):
            devinfo = self.devinfo.to_dict()

        controller_add = self.controller_add

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "alias": alias,
                "device_type": device_type,
                "type": type,
                "pubkey": pubkey,
                "address": address,
                "vpn_pubkey": vpn_pubkey,
                "vpn_address": vpn_address,
                "vpn_prefix": vpn_prefix,
                "vpn_netkey": vpn_netkey,
                "vpn_listenaddr": vpn_listenaddr,
                "tags": tags,
            }
        )
        if devinfo is not UNSET:
            field_dict["devinfo"] = devinfo
        if controller_add is not UNSET:
            field_dict["controller_add"] = controller_add

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controlled_device_info import ControlledDeviceInfo

        d = src_dict.copy()
        name = d.pop("name")

        alias = d.pop("alias")

        device_type = d.pop("device_type")

        type = d.pop("type")

        pubkey = d.pop("pubkey")

        address = d.pop("address")

        vpn_pubkey = d.pop("vpn_pubkey")

        vpn_address = d.pop("vpn_address")

        vpn_prefix = d.pop("vpn_prefix")

        vpn_netkey = d.pop("vpn_netkey")

        vpn_listenaddr = d.pop("vpn_listenaddr")

        tags = cast(List[str], d.pop("tags"))

        _devinfo = d.pop("devinfo", UNSET)
        devinfo: Union[Unset, ControlledDeviceInfo]
        if isinstance(_devinfo, Unset):
            devinfo = UNSET
        else:
            devinfo = ControlledDeviceInfo.from_dict(_devinfo)

        controller_add = d.pop("controller_add", UNSET)

        device_identity = cls(
            name=name,
            alias=alias,
            device_type=device_type,
            type=type,
            pubkey=pubkey,
            address=address,
            vpn_pubkey=vpn_pubkey,
            vpn_address=vpn_address,
            vpn_prefix=vpn_prefix,
            vpn_netkey=vpn_netkey,
            vpn_listenaddr=vpn_listenaddr,
            tags=tags,
            devinfo=devinfo,
            controller_add=controller_add,
        )

        device_identity.additional_properties = d
        return device_identity

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
