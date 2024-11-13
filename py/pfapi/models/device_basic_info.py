from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceBasicInfo")


@_attrs_define
class DeviceBasicInfo:
    """
    Attributes:
        name (Union[Unset, str]):
        device_id (Union[Unset, str]):
        device_type (Union[Unset, str]):
        os_type (Union[Unset, str]):
        os_version (Union[Unset, str]):
        address (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    device_type: Union[Unset, str] = UNSET
    os_type: Union[Unset, str] = UNSET
    os_version: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        device_id = self.device_id

        device_type = self.device_type

        os_type = self.os_type

        os_version = self.os_version

        address = self.address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if os_type is not UNSET:
            field_dict["os_type"] = os_type
        if os_version is not UNSET:
            field_dict["os_version"] = os_version
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        device_id = d.pop("device_id", UNSET)

        device_type = d.pop("device_type", UNSET)

        os_type = d.pop("os_type", UNSET)

        os_version = d.pop("os_version", UNSET)

        address = d.pop("address", UNSET)

        device_basic_info = cls(
            name=name,
            device_id=device_id,
            device_type=device_type,
            os_type=os_type,
            os_version=os_version,
            address=address,
        )

        device_basic_info.additional_properties = d
        return device_basic_info

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
