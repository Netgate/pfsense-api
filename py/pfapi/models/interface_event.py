from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InterfaceEvent")


@_attrs_define
class InterfaceEvent:
    """
    Attributes:
        name (str): name of interface device
        friendly_name (str): friendly name eg wan, lan
        state (str): current state change
        speed (int): speed change, Mbps
    """

    name: str
    friendly_name: str
    state: str
    speed: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        friendly_name = self.friendly_name

        state = self.state

        speed = self.speed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "friendly_name": friendly_name,
                "state": state,
                "speed": speed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        friendly_name = d.pop("friendly_name")

        state = d.pop("state")

        speed = d.pop("speed")

        interface_event = cls(
            name=name,
            friendly_name=friendly_name,
            state=state,
            speed=speed,
        )

        interface_event.additional_properties = d
        return interface_event

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
