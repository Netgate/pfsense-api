from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PacketCaptureRequest")


@_attrs_define
class PacketCaptureRequest:
    """valid values:
    action = "start", "stop"
    proto = "icmp", "icmp6", "tcp" , "udp", "arp", "carp", "esp", "pfsync", "ospf"
    detail = "full", "high", "medium", "normal"

        Attributes:
            action (Union[Unset, str]):
            host (Union[Unset, str]):
            interface (Union[Unset, str]):
            promiscuous (Union[Unset, bool]):
            count (Union[Unset, int]):
            snaplen (Union[Unset, int]):
            port (Union[Unset, str]):
            detail (Union[Unset, str]):
            fam (Union[Unset, str]):
            proto (Union[Unset, str]):
            dnsquery (Union[Unset, bool]):
    """

    action: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    promiscuous: Union[Unset, bool] = UNSET
    count: Union[Unset, int] = UNSET
    snaplen: Union[Unset, int] = UNSET
    port: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    fam: Union[Unset, str] = UNSET
    proto: Union[Unset, str] = UNSET
    dnsquery: Union[Unset, bool] = UNSET
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
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if host is not UNSET:
            field_dict["host"] = host
        if interface is not UNSET:
            field_dict["interface"] = interface
        if promiscuous is not UNSET:
            field_dict["promiscuous"] = promiscuous
        if count is not UNSET:
            field_dict["count"] = count
        if snaplen is not UNSET:
            field_dict["snaplen"] = snaplen
        if port is not UNSET:
            field_dict["port"] = port
        if detail is not UNSET:
            field_dict["detail"] = detail
        if fam is not UNSET:
            field_dict["fam"] = fam
        if proto is not UNSET:
            field_dict["proto"] = proto
        if dnsquery is not UNSET:
            field_dict["dnsquery"] = dnsquery

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = d.pop("action", UNSET)

        host = d.pop("host", UNSET)

        interface = d.pop("interface", UNSET)

        promiscuous = d.pop("promiscuous", UNSET)

        count = d.pop("count", UNSET)

        snaplen = d.pop("snaplen", UNSET)

        port = d.pop("port", UNSET)

        detail = d.pop("detail", UNSET)

        fam = d.pop("fam", UNSET)

        proto = d.pop("proto", UNSET)

        dnsquery = d.pop("dnsquery", UNSET)

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
