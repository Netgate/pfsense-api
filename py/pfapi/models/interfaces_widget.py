from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InterfacesWidget")


@_attrs_define
class InterfacesWidget:
    """
    Attributes:
        name (str):
        ip (str):
        status (str):
        speed (str):
    """

    name: str
    ip: str
    status: str
    speed: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        ip = self.ip

        status = self.status

        speed = self.speed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "ip": ip,
                "status": status,
                "speed": speed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        ip = d.pop("ip")

        status = d.pop("status")

        speed = d.pop("speed")

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
