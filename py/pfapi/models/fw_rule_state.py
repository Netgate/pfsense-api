from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FWRuleState")


@_attrs_define
class FWRuleState:
    """
    Attributes:
        id (str):
        tracker (str):
        label (str):
        evaluations (int):
        packets (int):
        bytes_ (int):
        states (int):
        pid (int):
        state_creations (int):
    """

    id: str
    tracker: str
    label: str
    evaluations: int
    packets: int
    bytes_: int
    states: int
    pid: int
    state_creations: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        tracker = self.tracker

        label = self.label

        evaluations = self.evaluations

        packets = self.packets

        bytes_ = self.bytes_

        states = self.states

        pid = self.pid

        state_creations = self.state_creations

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tracker": tracker,
                "label": label,
                "evaluations": evaluations,
                "packets": packets,
                "bytes": bytes_,
                "states": states,
                "pid": pid,
                "state_creations": state_creations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        tracker = d.pop("tracker")

        label = d.pop("label")

        evaluations = d.pop("evaluations")

        packets = d.pop("packets")

        bytes_ = d.pop("bytes")

        states = d.pop("states")

        pid = d.pop("pid")

        state_creations = d.pop("state_creations")

        fw_rule_state = cls(
            id=id,
            tracker=tracker,
            label=label,
            evaluations=evaluations,
            packets=packets,
            bytes_=bytes_,
            states=states,
            pid=pid,
            state_creations=state_creations,
        )

        fw_rule_state.additional_properties = d
        return fw_rule_state

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
