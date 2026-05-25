from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_daemon_status_states import FrrDaemonStatusStates


T = TypeVar("T", bound="FrrDaemonStatus")


@_attrs_define
class FrrDaemonStatus:
    """
    Attributes:
        name (str | Unset): daemon name (zebra, mgmtd, staticd, bgpd, ospfd, ospf6d, ripd, bfdd)
        running (bool | Unset): true if the daemon process is currently running
        states (FrrDaemonStatusStates | Unset):
    """

    name: str | Unset = UNSET
    running: bool | Unset = UNSET
    states: FrrDaemonStatusStates | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        running = self.running

        states: dict[str, Any] | Unset = UNSET
        if not isinstance(self.states, Unset):
            states = self.states.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if running is not UNSET:
            field_dict["running"] = running
        if states is not UNSET:
            field_dict["states"] = states

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_daemon_status_states import FrrDaemonStatusStates

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        running = d.pop("running", UNSET)

        _states = d.pop("states", UNSET)
        states: FrrDaemonStatusStates | Unset
        if isinstance(_states, Unset):
            states = UNSET
        else:
            states = FrrDaemonStatusStates.from_dict(_states)

        frr_daemon_status = cls(
            name=name,
            running=running,
            states=states,
        )

        frr_daemon_status.additional_properties = d
        return frr_daemon_status

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
