from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IfGroupCapableInterface")


@_attrs_define
class IfGroupCapableInterface:
    """
    Attributes:
        if_device (Union[Unset, str]):
        if_identity (Union[Unset, str]):
        if_assigned_name (Union[Unset, str]):
    """

    if_device: Union[Unset, str] = UNSET
    if_identity: Union[Unset, str] = UNSET
    if_assigned_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if_device = self.if_device

        if_identity = self.if_identity

        if_assigned_name = self.if_assigned_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if if_device is not UNSET:
            field_dict["if_device"] = if_device
        if if_identity is not UNSET:
            field_dict["if_identity"] = if_identity
        if if_assigned_name is not UNSET:
            field_dict["if_assigned_name"] = if_assigned_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        if_device = d.pop("if_device", UNSET)

        if_identity = d.pop("if_identity", UNSET)

        if_assigned_name = d.pop("if_assigned_name", UNSET)

        if_group_capable_interface = cls(
            if_device=if_device,
            if_identity=if_identity,
            if_assigned_name=if_assigned_name,
        )

        if_group_capable_interface.additional_properties = d
        return if_group_capable_interface

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
