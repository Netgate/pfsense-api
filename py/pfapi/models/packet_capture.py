from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pcap_interface import PcapInterface


T = TypeVar("T", bound="PacketCapture")


@_attrs_define
class PacketCapture:
    """
    Attributes:
        filename (str | Unset):
        capture (str | Unset):
        starttime (str | Unset):
        endtime (str | Unset):
        running (bool | Unset):
        command (str | Unset):
        interfaces (list[PcapInterface] | Unset):
    """

    filename: str | Unset = UNSET
    capture: str | Unset = UNSET
    starttime: str | Unset = UNSET
    endtime: str | Unset = UNSET
    running: bool | Unset = UNSET
    command: str | Unset = UNSET
    interfaces: list[PcapInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        capture = self.capture

        starttime = self.starttime

        endtime = self.endtime

        running = self.running

        command = self.command

        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filename is not UNSET:
            field_dict["filename"] = filename
        if capture is not UNSET:
            field_dict["capture"] = capture
        if starttime is not UNSET:
            field_dict["starttime"] = starttime
        if endtime is not UNSET:
            field_dict["endtime"] = endtime
        if running is not UNSET:
            field_dict["running"] = running
        if command is not UNSET:
            field_dict["command"] = command
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pcap_interface import PcapInterface

        d = dict(src_dict)
        filename = d.pop("filename", UNSET)

        capture = d.pop("capture", UNSET)

        starttime = d.pop("starttime", UNSET)

        endtime = d.pop("endtime", UNSET)

        running = d.pop("running", UNSET)

        command = d.pop("command", UNSET)

        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[PcapInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = PcapInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        packet_capture = cls(
            filename=filename,
            capture=capture,
            starttime=starttime,
            endtime=endtime,
            running=running,
            command=command,
            interfaces=interfaces,
        )

        packet_capture.additional_properties = d
        return packet_capture

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
