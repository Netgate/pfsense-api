from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DiagState")


@_attrs_define
class DiagState:
    """
    Attributes:
        interface (str):
        proto (str):
        src (str):
        dst (str):
        display (str):
        state (str):
        packet (str):
        bytes_ (str):
    """

    interface: str
    proto: str
    src: str
    dst: str
    display: str
    state: str
    packet: str
    bytes_: str
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
        field_dict.update(
            {
                "interface": interface,
                "proto": proto,
                "src": src,
                "dst": dst,
                "display": display,
                "state": state,
                "packet": packet,
                "bytes": bytes_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interface = d.pop("interface")

        proto = d.pop("proto")

        src = d.pop("src")

        dst = d.pop("dst")

        display = d.pop("display")

        state = d.pop("state")

        packet = d.pop("packet")

        bytes_ = d.pop("bytes")

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
