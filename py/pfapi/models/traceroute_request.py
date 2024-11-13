from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TracerouteRequest")


@_attrs_define
class TracerouteRequest:
    """
    Attributes:
        host (Union[Unset, str]):
        hops (Union[Unset, int]):
        icmp (Union[Unset, bool]):
        proto (Union[Unset, str]):
        rev (Union[Unset, bool]):
        src (Union[Unset, str]):
    """

    host: Union[Unset, str] = UNSET
    hops: Union[Unset, int] = UNSET
    icmp: Union[Unset, bool] = UNSET
    proto: Union[Unset, str] = UNSET
    rev: Union[Unset, bool] = UNSET
    src: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host

        hops = self.hops

        icmp = self.icmp

        proto = self.proto

        rev = self.rev

        src = self.src

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if hops is not UNSET:
            field_dict["hops"] = hops
        if icmp is not UNSET:
            field_dict["icmp"] = icmp
        if proto is not UNSET:
            field_dict["proto"] = proto
        if rev is not UNSET:
            field_dict["rev"] = rev
        if src is not UNSET:
            field_dict["src"] = src

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host", UNSET)

        hops = d.pop("hops", UNSET)

        icmp = d.pop("icmp", UNSET)

        proto = d.pop("proto", UNSET)

        rev = d.pop("rev", UNSET)

        src = d.pop("src", UNSET)

        traceroute_request = cls(
            host=host,
            hops=hops,
            icmp=icmp,
            proto=proto,
            rev=rev,
            src=src,
        )

        traceroute_request.additional_properties = d
        return traceroute_request

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
