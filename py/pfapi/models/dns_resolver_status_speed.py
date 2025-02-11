from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DNSResolverStatusSpeed")


@_attrs_define
class DNSResolverStatusSpeed:
    """
    Attributes:
        server (str):
        zone (str):
        ttl (int):
        expired (bool):
        ping (int):
        var (int):
        rtt (int):
        rto (int):
        timeout_a (int):
        timeout_aaaa (int):
        timeout_other (int):
    """

    server: str
    zone: str
    ttl: int
    expired: bool
    ping: int
    var: int
    rtt: int
    rto: int
    timeout_a: int
    timeout_aaaa: int
    timeout_other: int
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
        field_dict.update(
            {
                "server": server,
                "zone": zone,
                "ttl": ttl,
                "expired": expired,
                "ping": ping,
                "var": var,
                "rtt": rtt,
                "rto": rto,
                "timeout_a": timeout_a,
                "timeout_aaaa": timeout_aaaa,
                "timeout_other": timeout_other,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server = d.pop("server")

        zone = d.pop("zone")

        ttl = d.pop("ttl")

        expired = d.pop("expired")

        ping = d.pop("ping")

        var = d.pop("var")

        rtt = d.pop("rtt")

        rto = d.pop("rto")

        timeout_a = d.pop("timeout_a")

        timeout_aaaa = d.pop("timeout_aaaa")

        timeout_other = d.pop("timeout_other")

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
