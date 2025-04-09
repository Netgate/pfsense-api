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
            name (Union[Unset, str]): name of device
            alias (Union[Unset, str]): another alias for the device
            device_type (Union[Unset, str]): device type, eg pfsense
            type (Union[Unset, str]): alias to device_type
            pubkey (Union[Unset, str]): public key identity of device
            address (Union[Unset, str]): device's API URL, e.g. https://0.0.0.0:8443
            vpn_pubkey (Union[Unset, str]): VPN public key
            vpn_address (Union[Unset, str]): MIM VPN address
            vpn_prefix (Union[Unset, str]): MIM VPN address subnet
            vpn_netkey (Union[Unset, str]): MIM VPN netkey
            vpn_listenaddr (Union[Unset, str]): MIM listening address:port
            tags (Union[Unset, List[str]]):
            devinfo (Union[Unset, ControlledDeviceInfo]): Additional information about the device
            controller_add (Union[Unset, str]): API command that can be used to add the device to the controller
    """

    name: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    device_type: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    pubkey: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    vpn_pubkey: Union[Unset, str] = UNSET
    vpn_address: Union[Unset, str] = UNSET
    vpn_prefix: Union[Unset, str] = UNSET
    vpn_netkey: Union[Unset, str] = UNSET
    vpn_listenaddr: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
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

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        devinfo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.devinfo, Unset):
            devinfo = self.devinfo.to_dict()

        controller_add = self.controller_add

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if alias is not UNSET:
            field_dict["alias"] = alias
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
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
        if tags is not UNSET:
            field_dict["tags"] = tags
        if devinfo is not UNSET:
            field_dict["devinfo"] = devinfo
        if controller_add is not UNSET:
            field_dict["controller_add"] = controller_add

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controlled_device_info import ControlledDeviceInfo

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        alias = d.pop("alias", UNSET)

        device_type = d.pop("device_type", UNSET)

        type = d.pop("type", UNSET)

        pubkey = d.pop("pubkey", UNSET)

        address = d.pop("address", UNSET)

        vpn_pubkey = d.pop("vpn_pubkey", UNSET)

        vpn_address = d.pop("vpn_address", UNSET)

        vpn_prefix = d.pop("vpn_prefix", UNSET)

        vpn_netkey = d.pop("vpn_netkey", UNSET)

        vpn_listenaddr = d.pop("vpn_listenaddr", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

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
