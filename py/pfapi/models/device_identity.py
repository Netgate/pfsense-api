from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
            name (str | Unset): name of device
            alias (str | Unset): another alias for the device
            device_type (str | Unset): device type, eg pfsense
            type_ (str | Unset): alias to device_type
            pubkey (str | Unset): public key identity of device
            address (str | Unset): device's API URL, e.g. https://0.0.0.0:8443
            vpn_pubkey (str | Unset): VPN public key
            vpn_address (str | Unset): MIM VPN address
            vpn_prefix (str | Unset): MIM VPN address subnet
            vpn_netkey (str | Unset): MIM VPN netkey
            vpn_listenaddr (str | Unset): MIM listening address:port
            tags (list[str] | Unset):
            devinfo (ControlledDeviceInfo | Unset): Additional information about the device
            controller_add (str | Unset): API command that can be used to add the device to the controller
    """

    name: str | Unset = UNSET
    alias: str | Unset = UNSET
    device_type: str | Unset = UNSET
    type_: str | Unset = UNSET
    pubkey: str | Unset = UNSET
    address: str | Unset = UNSET
    vpn_pubkey: str | Unset = UNSET
    vpn_address: str | Unset = UNSET
    vpn_prefix: str | Unset = UNSET
    vpn_netkey: str | Unset = UNSET
    vpn_listenaddr: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    devinfo: ControlledDeviceInfo | Unset = UNSET
    controller_add: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alias = self.alias

        device_type = self.device_type

        type_ = self.type_

        pubkey = self.pubkey

        address = self.address

        vpn_pubkey = self.vpn_pubkey

        vpn_address = self.vpn_address

        vpn_prefix = self.vpn_prefix

        vpn_netkey = self.vpn_netkey

        vpn_listenaddr = self.vpn_listenaddr

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        devinfo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.devinfo, Unset):
            devinfo = self.devinfo.to_dict()

        controller_add = self.controller_add

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if alias is not UNSET:
            field_dict["alias"] = alias
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if type_ is not UNSET:
            field_dict["type"] = type_
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.controlled_device_info import ControlledDeviceInfo

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        alias = d.pop("alias", UNSET)

        device_type = d.pop("device_type", UNSET)

        type_ = d.pop("type", UNSET)

        pubkey = d.pop("pubkey", UNSET)

        address = d.pop("address", UNSET)

        vpn_pubkey = d.pop("vpn_pubkey", UNSET)

        vpn_address = d.pop("vpn_address", UNSET)

        vpn_prefix = d.pop("vpn_prefix", UNSET)

        vpn_netkey = d.pop("vpn_netkey", UNSET)

        vpn_listenaddr = d.pop("vpn_listenaddr", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _devinfo = d.pop("devinfo", UNSET)
        devinfo: ControlledDeviceInfo | Unset
        if isinstance(_devinfo, Unset):
            devinfo = UNSET
        else:
            devinfo = ControlledDeviceInfo.from_dict(_devinfo)

        controller_add = d.pop("controller_add", UNSET)

        device_identity = cls(
            name=name,
            alias=alias,
            device_type=device_type,
            type_=type_,
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
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
