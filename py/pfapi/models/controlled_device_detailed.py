from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        name (str):
        alias (str):
        device_id (str):
        device_key (str): public key of device
        address (str):
        address6 (str):
        primary_auth (str):
        auth (ControlledDeviceAuth):
        mim_depth (int): how many hops to reach device. 0 = this sytem, 1 = direct hop, etc
        mim_devices (int): if this device is a controller, how many devices are being managed by it
        state (str): current device state: active, error, offline, rebooting, pending (pending auth)
        sys_info (ControlledDeviceInfo): Additional information about the device
        device_type (Union[Unset, str]): defeault pfsense
        tags (Union[Unset, List[str]]):
        controller (Union[Unset, DeviceControllerInfo]): brief information about the controller managing the device
        device_cert (Union[Unset, str]): recorded value of device certificate
    """

    name: str
    alias: str
    device_id: str
    device_key: str
    address: str
    address6: str
    primary_auth: str
    auth: "ControlledDeviceAuth"
    mim_depth: int
    mim_devices: int
    state: str
    sys_info: "ControlledDeviceInfo"
    device_type: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    controller: Union[Unset, "DeviceControllerInfo"] = UNSET
    device_cert: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        alias = self.alias

        device_id = self.device_id

        device_key = self.device_key

        address = self.address

        address6 = self.address6

        primary_auth = self.primary_auth

        auth = self.auth.to_dict()

        mim_depth = self.mim_depth

        mim_devices = self.mim_devices

        state = self.state

        sys_info = self.sys_info.to_dict()

        device_type = self.device_type

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        controller: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.controller, Unset):
            controller = self.controller.to_dict()

        device_cert = self.device_cert

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "alias": alias,
                "device_id": device_id,
                "device_key": device_key,
                "address": address,
                "address6": address6,
                "primary_auth": primary_auth,
                "auth": auth,
                "mim_depth": mim_depth,
                "mim_devices": mim_devices,
                "state": state,
                "sys_info": sys_info,
            }
        )
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if tags is not UNSET:
            field_dict["tags"] = tags
        if controller is not UNSET:
            field_dict["controller"] = controller
        if device_cert is not UNSET:
            field_dict["device_cert"] = device_cert

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controlled_device_auth import ControlledDeviceAuth
        from ..models.controlled_device_info import ControlledDeviceInfo
        from ..models.device_controller_info import DeviceControllerInfo

        d = src_dict.copy()
        name = d.pop("name")

        alias = d.pop("alias")

        device_id = d.pop("device_id")

        device_key = d.pop("device_key")

        address = d.pop("address")

        address6 = d.pop("address6")

        primary_auth = d.pop("primary_auth")

        auth = ControlledDeviceAuth.from_dict(d.pop("auth"))

        mim_depth = d.pop("mim_depth")

        mim_devices = d.pop("mim_devices")

        state = d.pop("state")

        sys_info = ControlledDeviceInfo.from_dict(d.pop("sys_info"))

        device_type = d.pop("device_type", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        _controller = d.pop("controller", UNSET)
        controller: Union[Unset, DeviceControllerInfo]
        if isinstance(_controller, Unset):
            controller = UNSET
        else:
            controller = DeviceControllerInfo.from_dict(_controller)

        device_cert = d.pop("device_cert", UNSET)

        controlled_device_detailed = cls(
            name=name,
            alias=alias,
            device_id=device_id,
            device_key=device_key,
            address=address,
            address6=address6,
            primary_auth=primary_auth,
            auth=auth,
            mim_depth=mim_depth,
            mim_devices=mim_devices,
            state=state,
            sys_info=sys_info,
            device_type=device_type,
            tags=tags,
            controller=controller,
            device_cert=device_cert,
        )

        controlled_device_detailed.additional_properties = d
        return controlled_device_detailed

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
