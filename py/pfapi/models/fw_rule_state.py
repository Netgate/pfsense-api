from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FWRuleState")


@_attrs_define
class FWRuleState:
    """
    Attributes:
        id (str | Unset):
        tracker (str | Unset):
        label (str | Unset):
        evaluations (int | Unset):
        packets (int | Unset):
        bytes_ (int | Unset):
        states (int | Unset):
        pid (int | Unset):
        state_creations (int | Unset):
    """

    id: str | Unset = UNSET
    tracker: str | Unset = UNSET
    label: str | Unset = UNSET
    evaluations: int | Unset = UNSET
    packets: int | Unset = UNSET
    bytes_: int | Unset = UNSET
    states: int | Unset = UNSET
    pid: int | Unset = UNSET
    state_creations: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tracker = self.tracker

        label = self.label

        evaluations = self.evaluations

        packets = self.packets

        bytes_ = self.bytes_

        states = self.states

        pid = self.pid

        state_creations = self.state_creations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tracker is not UNSET:
            field_dict["tracker"] = tracker
        if label is not UNSET:
            field_dict["label"] = label
        if evaluations is not UNSET:
            field_dict["evaluations"] = evaluations
        if packets is not UNSET:
            field_dict["packets"] = packets
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if states is not UNSET:
            field_dict["states"] = states
        if pid is not UNSET:
            field_dict["pid"] = pid
        if state_creations is not UNSET:
            field_dict["state_creations"] = state_creations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tracker = d.pop("tracker", UNSET)

        label = d.pop("label", UNSET)

        evaluations = d.pop("evaluations", UNSET)

        packets = d.pop("packets", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        states = d.pop("states", UNSET)

        pid = d.pop("pid", UNSET)

        state_creations = d.pop("state_creations", UNSET)

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
