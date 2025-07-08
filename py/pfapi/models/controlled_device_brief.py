from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControlledDeviceBrief")


@_attrs_define
class ControlledDeviceBrief:
    """
    Attributes:
        device_id (Union[Unset, str]):
        alias (Union[Unset, str]):
        name (Union[Unset, str]):
        addresses (Union[Unset, List[str]]):
    """

    device_id: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    addresses: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_id = self.device_id

        alias = self.alias

        name = self.name

        addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if alias is not UNSET:
            field_dict["alias"] = alias
        if name is not UNSET:
            field_dict["name"] = name
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("device_id", UNSET)

        alias = d.pop("alias", UNSET)

        name = d.pop("name", UNSET)

        addresses = cast(List[str], d.pop("addresses", UNSET))

        controlled_device_brief = cls(
            device_id=device_id,
            alias=alias,
            name=name,
            addresses=addresses,
        )

        controlled_device_brief.additional_properties = d
        return controlled_device_brief

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
