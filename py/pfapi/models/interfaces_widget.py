from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfacesWidget")


@_attrs_define
class InterfacesWidget:
    """
    Attributes:
        name (Union[Unset, str]):
        ip (Union[Unset, str]):
        status (Union[Unset, str]):
        speed (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    speed: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        ip = self.ip

        status = self.status

        speed = self.speed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if status is not UNSET:
            field_dict["status"] = status
        if speed is not UNSET:
            field_dict["speed"] = speed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        status = d.pop("status", UNSET)

        speed = d.pop("speed", UNSET)

        interfaces_widget = cls(
            name=name,
            ip=ip,
            status=status,
            speed=speed,
        )

        interfaces_widget.additional_properties = d
        return interfaces_widget

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
