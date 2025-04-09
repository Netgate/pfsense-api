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
        name (Union[Unset, str]):
        alias (Union[Unset, str]):
        device_id (Union[Unset, str]):
        device_type (Union[Unset, str]): defeault pfsense
        device_key (Union[Unset, str]): public key of device
        tags (Union[Unset, List[str]]):
        address (Union[Unset, str]):
        address6 (Union[Unset, str]):
        primary_auth (Union[Unset, str]):
        auth (Union[Unset, ControlledDeviceAuth]):
        controller (Union[Unset, DeviceControllerInfo]): brief information about the controller managing the device
        mim_path (Union[Unset, List[str]]):
        mim_depth (Union[Unset, int]): how many hops to reach device. 0 = this sytem, 1 = direct hop, etc
        mim_devices (Union[Unset, int]): if this device is a controller, how many devices are being managed by it
        state (Union[Unset, str]): current device state: active, error, offline, rebooting, pending (pending auth)
        device_cert (Union[Unset, str]): recorded value of device certificate
        sys_info (Union[Unset, ControlledDeviceInfo]): Additional information about the device
    """

    name: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    device_type: Union[Unset, str] = UNSET
    device_key: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    address: Union[Unset, str] = UNSET
    address6: Union[Unset, str] = UNSET
    primary_auth: Union[Unset, str] = UNSET
    auth: Union[Unset, "ControlledDeviceAuth"] = UNSET
    controller: Union[Unset, "DeviceControllerInfo"] = UNSET
    mim_path: Union[Unset, List[str]] = UNSET
    mim_depth: Union[Unset, int] = UNSET
    mim_devices: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    device_cert: Union[Unset, str] = UNSET
    sys_info: Union[Unset, "ControlledDeviceInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        alias = self.alias

        device_id = self.device_id

        device_type = self.device_type

        device_key = self.device_key

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        address = self.address

        address6 = self.address6

        primary_auth = self.primary_auth

        auth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        controller: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.controller, Unset):
            controller = self.controller.to_dict()

        mim_path: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mim_path, Unset):
            mim_path = self.mim_path

        mim_depth = self.mim_depth

        mim_devices = self.mim_devices

        state = self.state

        device_cert = self.device_cert

        sys_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sys_info, Unset):
            sys_info = self.sys_info.to_dict()

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controlled_device_auth import ControlledDeviceAuth
        from ..models.controlled_device_info import ControlledDeviceInfo
        from ..models.device_controller_info import DeviceControllerInfo

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        alias = d.pop("alias", UNSET)

        device_id = d.pop("device_id", UNSET)

        device_type = d.pop("device_type", UNSET)

        device_key = d.pop("device_key", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        address = d.pop("address", UNSET)

        address6 = d.pop("address6", UNSET)

        primary_auth = d.pop("primary_auth", UNSET)

        _auth = d.pop("auth", UNSET)
        auth: Union[Unset, ControlledDeviceAuth]
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = ControlledDeviceAuth.from_dict(_auth)

        _controller = d.pop("controller", UNSET)
        controller: Union[Unset, DeviceControllerInfo]
        if isinstance(_controller, Unset):
            controller = UNSET
        else:
            controller = DeviceControllerInfo.from_dict(_controller)

        mim_path = cast(List[str], d.pop("mim_path", UNSET))

        mim_depth = d.pop("mim_depth", UNSET)

        mim_devices = d.pop("mim_devices", UNSET)

        state = d.pop("state", UNSET)

        device_cert = d.pop("device_cert", UNSET)

        _sys_info = d.pop("sys_info", UNSET)
        sys_info: Union[Unset, ControlledDeviceInfo]
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
