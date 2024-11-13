from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        capture (Union[Unset, str]):
        starttime (Union[Unset, str]):
        endtime (Union[Unset, str]):
        running (Union[Unset, bool]):
        interfaces (Union[Unset, List['PcapInterface']]):
    """

    capture: Union[Unset, str] = UNSET
    starttime: Union[Unset, str] = UNSET
    endtime: Union[Unset, str] = UNSET
    running: Union[Unset, bool] = UNSET
    interfaces: Union[Unset, List["PcapInterface"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        capture = self.capture

        starttime = self.starttime

        endtime = self.endtime

        running = self.running

        interfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capture is not UNSET:
            field_dict["capture"] = capture
        if starttime is not UNSET:
            field_dict["starttime"] = starttime
        if endtime is not UNSET:
            field_dict["endtime"] = endtime
        if running is not UNSET:
            field_dict["running"] = running
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pcap_interface import PcapInterface

        d = src_dict.copy()
        capture = d.pop("capture", UNSET)

        starttime = d.pop("starttime", UNSET)

        endtime = d.pop("endtime", UNSET)

        running = d.pop("running", UNSET)

        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
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
