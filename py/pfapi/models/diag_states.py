from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        states (Union[Unset, List['DiagState']]):
        interfaces (Union[Unset, List['SimpleInterface']]):
        msg (Union[Unset, str]): warnings or other info
    """

    states: Union[Unset, List["DiagState"]] = UNSET
    interfaces: Union[Unset, List["SimpleInterface"]] = UNSET
    msg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        states: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.states, Unset):
            states = []
            for states_item_data in self.states:
                states_item = states_item_data.to_dict()
                states.append(states_item)

        interfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        msg = self.msg

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.diag_state import DiagState
        from ..models.simple_interface import SimpleInterface

        d = src_dict.copy()
        states = []
        _states = d.pop("states", UNSET)
        for states_item_data in _states or []:
            states_item = DiagState.from_dict(states_item_data)

            states.append(states_item)

        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
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
