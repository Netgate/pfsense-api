from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceEvent")


@_attrs_define
class InterfaceEvent:
    """
    Attributes:
        name (Union[Unset, str]): name of interface device
        friendly_name (Union[Unset, str]): friendly name eg wan, lan
        state (Union[Unset, str]): current state change
        speed (Union[Unset, int]): speed change, Mbps
    """

    name: Union[Unset, str] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    speed: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        friendly_name = self.friendly_name

        state = self.state

        speed = self.speed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if friendly_name is not UNSET:
            field_dict["friendly_name"] = friendly_name
        if state is not UNSET:
            field_dict["state"] = state
        if speed is not UNSET:
            field_dict["speed"] = speed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        friendly_name = d.pop("friendly_name", UNSET)

        state = d.pop("state", UNSET)

        speed = d.pop("speed", UNSET)

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
