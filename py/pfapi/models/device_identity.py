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
    * vpn_address:     Netgard VPN address
    * vpn_prefix:      Netgard VPN address subnet
    * vpn_netkey:      Netgard VPN netkey
    * vpn_listenaddr:  Netgard listening address:port
    * devinfo:         summary of device information
    * tags:            Optional tags assigned to device

    * controller_add:  curl command that can be used to add the device to the controller.

        Attributes:
            name (Union[Unset, str]):
            alias (Union[Unset, str]):
            type (Union[Unset, str]):
            pubkey (Union[Unset, str]):
            address (Union[Unset, str]):
            vpn_pubkey (Union[Unset, str]):
            vpn_address (Union[Unset, str]):
            vpn_prefix (Union[Unset, str]):
            vpn_netkey (Union[Unset, str]):
            vpn_listenaddr (Union[Unset, str]):
            controller_add (Union[Unset, str]):
            devinfo (Union[Unset, ControlledDeviceInfo]): Additional information about the device
            tags (Union[Unset, List[str]]):
            vpn_listenaddr4 (Union[Unset, str]):
            vpn_listenaddr6 (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    pubkey: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    vpn_pubkey: Union[Unset, str] = UNSET
    vpn_address: Union[Unset, str] = UNSET
    vpn_prefix: Union[Unset, str] = UNSET
    vpn_netkey: Union[Unset, str] = UNSET
    vpn_listenaddr: Union[Unset, str] = UNSET
    controller_add: Union[Unset, str] = UNSET
    devinfo: Union[Unset, "ControlledDeviceInfo"] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    vpn_listenaddr4: Union[Unset, str] = UNSET
    vpn_listenaddr6: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        alias = self.alias

        type = self.type

        pubkey = self.pubkey

        address = self.address

        vpn_pubkey = self.vpn_pubkey

        vpn_address = self.vpn_address

        vpn_prefix = self.vpn_prefix

        vpn_netkey = self.vpn_netkey

        vpn_listenaddr = self.vpn_listenaddr

        controller_add = self.controller_add

        devinfo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.devinfo, Unset):
            devinfo = self.devinfo.to_dict()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        vpn_listenaddr4 = self.vpn_listenaddr4

        vpn_listenaddr6 = self.vpn_listenaddr6

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if alias is not UNSET:
            field_dict["alias"] = alias
        if type is not UNSET:
            field_dict["type"] = type
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if address is not UNSET:
            field_dict["address"] = address
        if vpn_pubkey is not UNSET:
            field_dict["vpn_pubkey"] = vpn_pubkey
        if vpn_address is not UNSET:
            field_dict["vpn_address"] = vpn_address
        if vpn_prefix is not UNSET:
            field_dict["vpn_prefix"] = vpn_prefix
        if vpn_netkey is not UNSET:
            field_dict["vpn_netkey"] = vpn_netkey
        if vpn_listenaddr is not UNSET:
            field_dict["vpn_listenaddr"] = vpn_listenaddr
        if controller_add is not UNSET:
            field_dict["controller_add"] = controller_add
        if devinfo is not UNSET:
            field_dict["devinfo"] = devinfo
        if tags is not UNSET:
            field_dict["tags"] = tags
        if vpn_listenaddr4 is not UNSET:
            field_dict["vpn_listenaddr4"] = vpn_listenaddr4
        if vpn_listenaddr6 is not UNSET:
            field_dict["vpn_listenaddr6"] = vpn_listenaddr6

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controlled_device_info import ControlledDeviceInfo

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        alias = d.pop("alias", UNSET)

        type = d.pop("type", UNSET)

        pubkey = d.pop("pubkey", UNSET)

        address = d.pop("address", UNSET)

        vpn_pubkey = d.pop("vpn_pubkey", UNSET)

        vpn_address = d.pop("vpn_address", UNSET)

        vpn_prefix = d.pop("vpn_prefix", UNSET)

        vpn_netkey = d.pop("vpn_netkey", UNSET)

        vpn_listenaddr = d.pop("vpn_listenaddr", UNSET)

        controller_add = d.pop("controller_add", UNSET)

        _devinfo = d.pop("devinfo", UNSET)
        devinfo: Union[Unset, ControlledDeviceInfo]
        if isinstance(_devinfo, Unset):
            devinfo = UNSET
        else:
            devinfo = ControlledDeviceInfo.from_dict(_devinfo)

        tags = cast(List[str], d.pop("tags", UNSET))

        vpn_listenaddr4 = d.pop("vpn_listenaddr4", UNSET)

        vpn_listenaddr6 = d.pop("vpn_listenaddr6", UNSET)

        device_identity = cls(
            name=name,
            alias=alias,
            type=type,
            pubkey=pubkey,
            address=address,
            vpn_pubkey=vpn_pubkey,
            vpn_address=vpn_address,
            vpn_prefix=vpn_prefix,
            vpn_netkey=vpn_netkey,
            vpn_listenaddr=vpn_listenaddr,
            controller_add=controller_add,
            devinfo=devinfo,
            tags=tags,
            vpn_listenaddr4=vpn_listenaddr4,
            vpn_listenaddr6=vpn_listenaddr6,
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
