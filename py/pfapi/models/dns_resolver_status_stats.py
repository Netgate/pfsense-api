from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DNSResolverStatusStats")


@_attrs_define
class DNSResolverStatusStats:
    """
    Attributes:
        server (str):
        zone (str):
        expired (bool):
        edns_lame_known (int):
        edns_version (int):
        probe_delay (int):
        lame_dnssec (int):
        lame_rec (int):
        lame_a (int):
        lame_other (int):
    """

    server: str
    zone: str
    expired: bool
    edns_lame_known: int
    edns_version: int
    probe_delay: int
    lame_dnssec: int
    lame_rec: int
    lame_a: int
    lame_other: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server = self.server

        zone = self.zone

        expired = self.expired

        edns_lame_known = self.edns_lame_known

        edns_version = self.edns_version

        probe_delay = self.probe_delay

        lame_dnssec = self.lame_dnssec

        lame_rec = self.lame_rec

        lame_a = self.lame_a

        lame_other = self.lame_other

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server": server,
                "zone": zone,
                "expired": expired,
                "edns_lame_known": edns_lame_known,
                "edns_version": edns_version,
                "probe_delay": probe_delay,
                "lame_dnssec": lame_dnssec,
                "lame_rec": lame_rec,
                "lame_a": lame_a,
                "lame_other": lame_other,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server = d.pop("server")

        zone = d.pop("zone")

        expired = d.pop("expired")

        edns_lame_known = d.pop("edns_lame_known")

        edns_version = d.pop("edns_version")

        probe_delay = d.pop("probe_delay")

        lame_dnssec = d.pop("lame_dnssec")

        lame_rec = d.pop("lame_rec")

        lame_a = d.pop("lame_a")

        lame_other = d.pop("lame_other")

        dns_resolver_status_stats = cls(
            server=server,
            zone=zone,
            expired=expired,
            edns_lame_known=edns_lame_known,
            edns_version=edns_version,
            probe_delay=probe_delay,
            lame_dnssec=lame_dnssec,
            lame_rec=lame_rec,
            lame_a=lame_a,
            lame_other=lame_other,
        )

        dns_resolver_status_stats.additional_properties = d
        return dns_resolver_status_stats

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
