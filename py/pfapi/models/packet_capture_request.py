from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PacketCaptureRequest")


@_attrs_define
class PacketCaptureRequest:
    """valid values:
    action = "start", "stop"
    proto = "icmp", "icmp6", "tcp" , "udp", "arp", "carp", "esp", "pfsync", "ospf"
    detail = "full", "high", "medium", "normal"

        Attributes:
            action (str):
            host (str):
            interface (str):
            promiscuous (bool):
            count (int):
            snaplen (int):
            port (str):
            detail (str):
            fam (str):
            proto (str):
            dnsquery (bool):
    """

    action: str
    host: str
    interface: str
    promiscuous: bool
    count: int
    snaplen: int
    port: str
    detail: str
    fam: str
    proto: str
    dnsquery: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action

        host = self.host

        interface = self.interface

        promiscuous = self.promiscuous

        count = self.count

        snaplen = self.snaplen

        port = self.port

        detail = self.detail

        fam = self.fam

        proto = self.proto

        dnsquery = self.dnsquery

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "host": host,
                "interface": interface,
                "promiscuous": promiscuous,
                "count": count,
                "snaplen": snaplen,
                "port": port,
                "detail": detail,
                "fam": fam,
                "proto": proto,
                "dnsquery": dnsquery,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = d.pop("action")

        host = d.pop("host")

        interface = d.pop("interface")

        promiscuous = d.pop("promiscuous")

        count = d.pop("count")

        snaplen = d.pop("snaplen")

        port = d.pop("port")

        detail = d.pop("detail")

        fam = d.pop("fam")

        proto = d.pop("proto")

        dnsquery = d.pop("dnsquery")

        packet_capture_request = cls(
            action=action,
            host=host,
            interface=interface,
            promiscuous=promiscuous,
            count=count,
            snaplen=snaplen,
            port=port,
            detail=detail,
            fam=fam,
            proto=proto,
            dnsquery=dnsquery,
        )

        packet_capture_request.additional_properties = d
        return packet_capture_request

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
