from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.arpmon_interface_state_macs import ArpmonInterfaceStateMacs


T = TypeVar("T", bound="ArpmonInterfaceState")


@_attrs_define
class ArpmonInterfaceState:
    """
    Attributes:
        monitoring (bool | Unset): interface is being monitored
        macs (ArpmonInterfaceStateMacs | Unset):
    """

    monitoring: bool | Unset = UNSET
    macs: ArpmonInterfaceStateMacs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitoring = self.monitoring

        macs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.macs, Unset):
            macs = self.macs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monitoring is not UNSET:
            field_dict["monitoring"] = monitoring
        if macs is not UNSET:
            field_dict["macs"] = macs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.arpmon_interface_state_macs import ArpmonInterfaceStateMacs

        d = dict(src_dict)
        monitoring = d.pop("monitoring", UNSET)

        _macs = d.pop("macs", UNSET)
        macs: ArpmonInterfaceStateMacs | Unset
        if isinstance(_macs, Unset):
            macs = UNSET
        else:
            macs = ArpmonInterfaceStateMacs.from_dict(_macs)

        arpmon_interface_state = cls(
            monitoring=monitoring,
            macs=macs,
        )

        arpmon_interface_state.additional_properties = d
        return arpmon_interface_state

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
