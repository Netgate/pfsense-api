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
        name (Union[Unset, str]):
        alias (Union[Unset, str]):
        device_id (Union[Unset, str]):
        device_type (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        address (Union[Unset, str]):
        address6 (Union[Unset, str]):
        primary_auth (Union[Unset, str]):
        auth (Union[Unset, ControlledDeviceAuth]):
        state (Union[Unset, str]): current device state: active, error, offline, rebooting, pending (pending auth)
        device_cert (Union[Unset, str]): recorded value of device certificate
        device_key (Union[Unset, str]): public key of device
        device_info (Union[Unset, ControlledDeviceInfo]): Additional information about the device
    """

    name: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    device_type: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    address: Union[Unset, str] = UNSET
    address6: Union[Unset, str] = UNSET
    primary_auth: Union[Unset, str] = UNSET
    auth: Union[Unset, "ControlledDeviceAuth"] = UNSET
    state: Union[Unset, str] = UNSET
    device_cert: Union[Unset, str] = UNSET
    device_key: Union[Unset, str] = UNSET
    device_info: Union[Unset, "ControlledDeviceInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        alias = self.alias

        device_id = self.device_id

        device_type = self.device_type

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        address = self.address

        address6 = self.address6

        primary_auth = self.primary_auth

        auth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        state = self.state

        device_cert = self.device_cert

        device_key = self.device_key

        device_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.device_info, Unset):
            device_info = self.device_info.to_dict()

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
        if state is not UNSET:
            field_dict["state"] = state
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
        name = d.pop("name", UNSET)

        alias = d.pop("alias", UNSET)

        device_id = d.pop("device_id", UNSET)

        device_type = d.pop("device_type", UNSET)

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

        state = d.pop("state", UNSET)

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
            device_id=device_id,
            device_type=device_type,
            tags=tags,
            address=address,
            address6=address6,
            primary_auth=primary_auth,
            auth=auth,
            state=state,
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
