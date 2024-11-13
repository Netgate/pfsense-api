from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSResolverStatusSpeed")


@_attrs_define
class DNSResolverStatusSpeed:
    """
    Attributes:
        server (Union[Unset, str]):
        zone (Union[Unset, str]):
        ttl (Union[Unset, int]):
        expired (Union[Unset, bool]):
        ping (Union[Unset, int]):
        var (Union[Unset, int]):
        rtt (Union[Unset, int]):
        rto (Union[Unset, int]):
        timeout_a (Union[Unset, int]):
        timeout_aaaa (Union[Unset, int]):
        timeout_other (Union[Unset, int]):
    """

    server: Union[Unset, str] = UNSET
    zone: Union[Unset, str] = UNSET
    ttl: Union[Unset, int] = UNSET
    expired: Union[Unset, bool] = UNSET
    ping: Union[Unset, int] = UNSET
    var: Union[Unset, int] = UNSET
    rtt: Union[Unset, int] = UNSET
    rto: Union[Unset, int] = UNSET
    timeout_a: Union[Unset, int] = UNSET
    timeout_aaaa: Union[Unset, int] = UNSET
    timeout_other: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server = self.server

        zone = self.zone

        ttl = self.ttl

        expired = self.expired

        ping = self.ping

        var = self.var

        rtt = self.rtt

        rto = self.rto

        timeout_a = self.timeout_a

        timeout_aaaa = self.timeout_aaaa

        timeout_other = self.timeout_other

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server is not UNSET:
            field_dict["server"] = server
        if zone is not UNSET:
            field_dict["zone"] = zone
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if expired is not UNSET:
            field_dict["expired"] = expired
        if ping is not UNSET:
            field_dict["ping"] = ping
        if var is not UNSET:
            field_dict["var"] = var
        if rtt is not UNSET:
            field_dict["rtt"] = rtt
        if rto is not UNSET:
            field_dict["rto"] = rto
        if timeout_a is not UNSET:
            field_dict["timeout_a"] = timeout_a
        if timeout_aaaa is not UNSET:
            field_dict["timeout_aaaa"] = timeout_aaaa
        if timeout_other is not UNSET:
            field_dict["timeout_other"] = timeout_other

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server = d.pop("server", UNSET)

        zone = d.pop("zone", UNSET)

        ttl = d.pop("ttl", UNSET)

        expired = d.pop("expired", UNSET)

        ping = d.pop("ping", UNSET)

        var = d.pop("var", UNSET)

        rtt = d.pop("rtt", UNSET)

        rto = d.pop("rto", UNSET)

        timeout_a = d.pop("timeout_a", UNSET)

        timeout_aaaa = d.pop("timeout_aaaa", UNSET)

        timeout_other = d.pop("timeout_other", UNSET)

        dns_resolver_status_speed = cls(
            server=server,
            zone=zone,
            ttl=ttl,
            expired=expired,
            ping=ping,
            var=var,
            rtt=rtt,
            rto=rto,
            timeout_a=timeout_a,
            timeout_aaaa=timeout_aaaa,
            timeout_other=timeout_other,
        )

        dns_resolver_status_speed.additional_properties = d
        return dns_resolver_status_speed

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
