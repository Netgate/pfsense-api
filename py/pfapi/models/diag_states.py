from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.diag_state import DiagState
    from ..models.simple_interface import SimpleInterface


T = TypeVar("T", bound="DiagStates")


@_attrs_define
class DiagStates:
    """
    Attributes:
        states (List['DiagState']):
        interfaces (List['SimpleInterface']):
    """

    states: List["DiagState"]
    interfaces: List["SimpleInterface"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        states = []
        for states_item_data in self.states:
            states_item = states_item_data.to_dict()
            states.append(states_item)

        interfaces = []
        for interfaces_item_data in self.interfaces:
            interfaces_item = interfaces_item_data.to_dict()
            interfaces.append(interfaces_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "states": states,
                "interfaces": interfaces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.diag_state import DiagState
        from ..models.simple_interface import SimpleInterface

        d = src_dict.copy()
        states = []
        _states = d.pop("states")
        for states_item_data in _states:
            states_item = DiagState.from_dict(states_item_data)

            states.append(states_item)

        interfaces = []
        _interfaces = d.pop("interfaces")
        for interfaces_item_data in _interfaces:
            interfaces_item = SimpleInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        diag_states = cls(
            states=states,
            interfaces=interfaces,
        )

        diag_states.additional_properties = d
        return diag_states

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
