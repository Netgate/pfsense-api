from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controlled_device_auth import ControlledDeviceAuth
    from ..models.controlled_device_info import ControlledDeviceInfo
    from ..models.device_controller_info import DeviceControllerInfo


T = TypeVar("T", bound="ControlledDeviceDetailed")


@_attrs_define
class ControlledDeviceDetailed:
    """Detailed information about the controlled device

    Attributes:
        name (str | Unset):
        alias (str | Unset):
        device_id (str | Unset):
        device_type (str | Unset): defeault pfsense
        device_key (str | Unset): public key of device
        tags (list[str] | Unset):
        address (str | Unset):
        address6 (str | Unset):
        gateways (list[str] | Unset):
        primary_auth (str | Unset):
        auth (ControlledDeviceAuth | Unset):
        controller (DeviceControllerInfo | Unset): brief information about the controller managing the device
        mim_path (list[str] | Unset):
        mim_depth (int | Unset): how many hops to reach device. 0 = this sytem, 1 = direct hop, etc
        mim_devices (int | Unset): if this device is a controller, how many devices are being managed by it
        state (str | Unset): current device state: active, error, offline, rebooting, pending (pending auth)
        device_cert (str | Unset): recorded value of device certificate
        sys_info (ControlledDeviceInfo | Unset): Additional information about the device
    """

    name: str | Unset = UNSET
    alias: str | Unset = UNSET
    device_id: str | Unset = UNSET
    device_type: str | Unset = UNSET
    device_key: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    address: str | Unset = UNSET
    address6: str | Unset = UNSET
    gateways: list[str] | Unset = UNSET
    primary_auth: str | Unset = UNSET
    auth: ControlledDeviceAuth | Unset = UNSET
    controller: DeviceControllerInfo | Unset = UNSET
    mim_path: list[str] | Unset = UNSET
    mim_depth: int | Unset = UNSET
    mim_devices: int | Unset = UNSET
    state: str | Unset = UNSET
    device_cert: str | Unset = UNSET
    sys_info: ControlledDeviceInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alias = self.alias

        device_id = self.device_id

        device_type = self.device_type

        device_key = self.device_key

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        address = self.address

        address6 = self.address6

        gateways: list[str] | Unset = UNSET
        if not isinstance(self.gateways, Unset):
            gateways = self.gateways

        primary_auth = self.primary_auth

        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        controller: dict[str, Any] | Unset = UNSET
        if not isinstance(self.controller, Unset):
            controller = self.controller.to_dict()

        mim_path: list[str] | Unset = UNSET
        if not isinstance(self.mim_path, Unset):
            mim_path = self.mim_path

        mim_depth = self.mim_depth

        mim_devices = self.mim_devices

        state = self.state

        device_cert = self.device_cert

        sys_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sys_info, Unset):
            sys_info = self.sys_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if alias is not UNSET:
            field_dict["alias"] = alias
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if device_key is not UNSET:
            field_dict["device_key"] = device_key
        if tags is not UNSET:
            field_dict["tags"] = tags
        if address is not UNSET:
            field_dict["address"] = address
        if address6 is not UNSET:
            field_dict["address6"] = address6
        if gateways is not UNSET:
            field_dict["gateways"] = gateways
        if primary_auth is not UNSET:
            field_dict["primary_auth"] = primary_auth
        if auth is not UNSET:
            field_dict["auth"] = auth
        if controller is not UNSET:
            field_dict["controller"] = controller
        if mim_path is not UNSET:
            field_dict["mim_path"] = mim_path
        if mim_depth is not UNSET:
            field_dict["mim_depth"] = mim_depth
        if mim_devices is not UNSET:
            field_dict["mim_devices"] = mim_devices
        if state is not UNSET:
            field_dict["state"] = state
        if device_cert is not UNSET:
            field_dict["device_cert"] = device_cert
        if sys_info is not UNSET:
            field_dict["sys_info"] = sys_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.controlled_device_auth import ControlledDeviceAuth
        from ..models.controlled_device_info import ControlledDeviceInfo
        from ..models.device_controller_info import DeviceControllerInfo

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        alias = d.pop("alias", UNSET)

        device_id = d.pop("device_id", UNSET)

        device_type = d.pop("device_type", UNSET)

        device_key = d.pop("device_key", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        address = d.pop("address", UNSET)

        address6 = d.pop("address6", UNSET)

        gateways = cast(list[str], d.pop("gateways", UNSET))

        primary_auth = d.pop("primary_auth", UNSET)

        _auth = d.pop("auth", UNSET)
        auth: ControlledDeviceAuth | Unset
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = ControlledDeviceAuth.from_dict(_auth)

        _controller = d.pop("controller", UNSET)
        controller: DeviceControllerInfo | Unset
        if isinstance(_controller, Unset):
            controller = UNSET
        else:
            controller = DeviceControllerInfo.from_dict(_controller)

        mim_path = cast(list[str], d.pop("mim_path", UNSET))

        mim_depth = d.pop("mim_depth", UNSET)

        mim_devices = d.pop("mim_devices", UNSET)

        state = d.pop("state", UNSET)

        device_cert = d.pop("device_cert", UNSET)

        _sys_info = d.pop("sys_info", UNSET)
        sys_info: ControlledDeviceInfo | Unset
        if isinstance(_sys_info, Unset):
            sys_info = UNSET
        else:
            sys_info = ControlledDeviceInfo.from_dict(_sys_info)

        controlled_device_detailed = cls(
            name=name,
            alias=alias,
            device_id=device_id,
            device_type=device_type,
            device_key=device_key,
            tags=tags,
            address=address,
            address6=address6,
            gateways=gateways,
            primary_auth=primary_auth,
            auth=auth,
            controller=controller,
            mim_path=mim_path,
            mim_depth=mim_depth,
            mim_devices=mim_devices,
            state=state,
            device_cert=device_cert,
            sys_info=sys_info,
        )

        controlled_device_detailed.additional_properties = d
        return controlled_device_detailed

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
