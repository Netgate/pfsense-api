from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagState")


@_attrs_define
class DiagState:
    """
    Attributes:
        interface (str | Unset):
        proto (str | Unset):
        src (str | Unset):
        dst (str | Unset):
        display (str | Unset):
        state (str | Unset):
        packet (str | Unset):
        bytes_ (str | Unset):
    """

    interface: str | Unset = UNSET
    proto: str | Unset = UNSET
    src: str | Unset = UNSET
    dst: str | Unset = UNSET
    display: str | Unset = UNSET
    state: str | Unset = UNSET
    packet: str | Unset = UNSET
    bytes_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        proto = self.proto

        src = self.src

        dst = self.dst

        display = self.display

        state = self.state

        packet = self.packet

        bytes_ = self.bytes_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface is not UNSET:
            field_dict["interface"] = interface
        if proto is not UNSET:
            field_dict["proto"] = proto
        if src is not UNSET:
            field_dict["src"] = src
        if dst is not UNSET:
            field_dict["dst"] = dst
        if display is not UNSET:
            field_dict["display"] = display
        if state is not UNSET:
            field_dict["state"] = state
        if packet is not UNSET:
            field_dict["packet"] = packet
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interface = d.pop("interface", UNSET)

        proto = d.pop("proto", UNSET)

        src = d.pop("src", UNSET)

        dst = d.pop("dst", UNSET)

        display = d.pop("display", UNSET)

        state = d.pop("state", UNSET)

        packet = d.pop("packet", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        diag_state = cls(
            interface=interface,
            proto=proto,
            src=src,
            dst=dst,
            display=display,
            state=state,
            packet=packet,
            bytes_=bytes_,
        )

        diag_state.additional_properties = d
        return diag_state

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
