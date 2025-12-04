from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diag_state import DiagState
    from ..models.simple_interface import SimpleInterface


T = TypeVar("T", bound="DiagStates")


@_attrs_define
class DiagStates:
    """
    Attributes:
        states (list[DiagState] | Unset):
        interfaces (list[SimpleInterface] | Unset):
        msg (str | Unset): warnings or other info
    """

    states: list[DiagState] | Unset = UNSET
    interfaces: list[SimpleInterface] | Unset = UNSET
    msg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.states, Unset):
            states = []
            for states_item_data in self.states:
                states_item = states_item_data.to_dict()
                states.append(states_item)

        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        msg = self.msg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if states is not UNSET:
            field_dict["states"] = states
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if msg is not UNSET:
            field_dict["msg"] = msg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diag_state import DiagState
        from ..models.simple_interface import SimpleInterface

        d = dict(src_dict)
        _states = d.pop("states", UNSET)
        states: list[DiagState] | Unset = UNSET
        if _states is not UNSET:
            states = []
            for states_item_data in _states:
                states_item = DiagState.from_dict(states_item_data)

                states.append(states_item)

        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[SimpleInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = SimpleInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        msg = d.pop("msg", UNSET)

        diag_states = cls(
            states=states,
            interfaces=interfaces,
            msg=msg,
        )

        diag_states.additional_properties = d
        return diag_states

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
