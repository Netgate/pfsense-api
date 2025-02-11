from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controlled_device_auth import ControlledDeviceAuth
    from ..models.controlled_device_info import ControlledDeviceInfo


T = TypeVar("T", bound="ControlledDevice")


@_attrs_define
class ControlledDevice:
    """Parameters for adding the device

    Attributes:
        name (str):
        alias (str):
        device_type (str):
        address (str):
        address6 (str):
        primary_auth (str):
        auth (ControlledDeviceAuth):
        state (str): current device state: active, error, offline, rebooting, pending (pending auth)
        device_id (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        device_cert (Union[Unset, str]): recorded value of device certificate
        device_key (Union[Unset, str]): public key of device
        device_info (Union[Unset, ControlledDeviceInfo]): Additional information about the device
    """

    name: str
    alias: str
    device_type: str
    address: str
    address6: str
    primary_auth: str
    auth: "ControlledDeviceAuth"
    state: str
    device_id: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    device_cert: Union[Unset, str] = UNSET
    device_key: Union[Unset, str] = UNSET
    device_info: Union[Unset, "ControlledDeviceInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        alias = self.alias

        device_type = self.device_type

        address = self.address

        address6 = self.address6

        primary_auth = self.primary_auth

        auth = self.auth.to_dict()

        state = self.state

        device_id = self.device_id

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        device_cert = self.device_cert

        device_key = self.device_key

        device_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.device_info, Unset):
            device_info = self.device_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "alias": alias,
                "device_type": device_type,
                "address": address,
                "address6": address6,
                "primary_auth": primary_auth,
                "auth": auth,
                "state": state,
            }
        )
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if device_cert is not UNSET:
            field_dict["device_cert"] = device_cert
        if device_key is not UNSET:
            field_dict["device_key"] = device_key
        if device_info is not UNSET:
            field_dict["device_info"] = device_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controlled_device_auth import ControlledDeviceAuth
        from ..models.controlled_device_info import ControlledDeviceInfo

        d = src_dict.copy()
        name = d.pop("name")

        alias = d.pop("alias")

        device_type = d.pop("device_type")

        address = d.pop("address")

        address6 = d.pop("address6")

        primary_auth = d.pop("primary_auth")

        auth = ControlledDeviceAuth.from_dict(d.pop("auth"))

        state = d.pop("state")

        device_id = d.pop("device_id", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        device_cert = d.pop("device_cert", UNSET)

        device_key = d.pop("device_key", UNSET)

        _device_info = d.pop("device_info", UNSET)
        device_info: Union[Unset, ControlledDeviceInfo]
        if isinstance(_device_info, Unset):
            device_info = UNSET
        else:
            device_info = ControlledDeviceInfo.from_dict(_device_info)

        controlled_device = cls(
            name=name,
            alias=alias,
            device_type=device_type,
            address=address,
            address6=address6,
            primary_auth=primary_auth,
            auth=auth,
            state=state,
            device_id=device_id,
            tags=tags,
            device_cert=device_cert,
            device_key=device_key,
            device_info=device_info,
        )

        controlled_device.additional_properties = d
        return controlled_device

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
