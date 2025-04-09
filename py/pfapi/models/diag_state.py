from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagState")


@_attrs_define
class DiagState:
    """
    Attributes:
        interface (Union[Unset, str]):
        proto (Union[Unset, str]):
        src (Union[Unset, str]):
        dst (Union[Unset, str]):
        display (Union[Unset, str]):
        state (Union[Unset, str]):
        packet (Union[Unset, str]):
        bytes_ (Union[Unset, str]):
    """

    interface: Union[Unset, str] = UNSET
    proto: Union[Unset, str] = UNSET
    src: Union[Unset, str] = UNSET
    dst: Union[Unset, str] = UNSET
    display: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    packet: Union[Unset, str] = UNSET
    bytes_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interface = self.interface

        proto = self.proto

        src = self.src

        dst = self.dst

        display = self.display

        state = self.state

        packet = self.packet

        bytes_ = self.bytes_

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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
