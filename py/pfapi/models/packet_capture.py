from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pcap_interface import PcapInterface


T = TypeVar("T", bound="PacketCapture")


@_attrs_define
class PacketCapture:
    """
    Attributes:
        capture (str):
        starttime (str):
        endtime (str):
        running (bool):
        interfaces (List['PcapInterface']):
    """

    capture: str
    starttime: str
    endtime: str
    running: bool
    interfaces: List["PcapInterface"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        capture = self.capture

        starttime = self.starttime

        endtime = self.endtime

        running = self.running

        interfaces = []
        for interfaces_item_data in self.interfaces:
            interfaces_item = interfaces_item_data.to_dict()
            interfaces.append(interfaces_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "capture": capture,
                "starttime": starttime,
                "endtime": endtime,
                "running": running,
                "interfaces": interfaces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pcap_interface import PcapInterface

        d = src_dict.copy()
        capture = d.pop("capture")

        starttime = d.pop("starttime")

        endtime = d.pop("endtime")

        running = d.pop("running")

        interfaces = []
        _interfaces = d.pop("interfaces")
        for interfaces_item_data in _interfaces:
            interfaces_item = PcapInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        packet_capture = cls(
            capture=capture,
            starttime=starttime,
            endtime=endtime,
            running=running,
            interfaces=interfaces,
        )

        packet_capture.additional_properties = d
        return packet_capture

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
