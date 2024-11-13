from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSResolverStatusStats")


@_attrs_define
class DNSResolverStatusStats:
    """
    Attributes:
        server (Union[Unset, str]):
        zone (Union[Unset, str]):
        expired (Union[Unset, bool]):
        edns_lame_known (Union[Unset, int]):
        edns_version (Union[Unset, int]):
        probe_delay (Union[Unset, int]):
        lame_dnssec (Union[Unset, int]):
        lame_rec (Union[Unset, int]):
        lame_a (Union[Unset, int]):
        lame_other (Union[Unset, int]):
    """

    server: Union[Unset, str] = UNSET
    zone: Union[Unset, str] = UNSET
    expired: Union[Unset, bool] = UNSET
    edns_lame_known: Union[Unset, int] = UNSET
    edns_version: Union[Unset, int] = UNSET
    probe_delay: Union[Unset, int] = UNSET
    lame_dnssec: Union[Unset, int] = UNSET
    lame_rec: Union[Unset, int] = UNSET
    lame_a: Union[Unset, int] = UNSET
    lame_other: Union[Unset, int] = UNSET
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
        field_dict.update({})
        if server is not UNSET:
            field_dict["server"] = server
        if zone is not UNSET:
            field_dict["zone"] = zone
        if expired is not UNSET:
            field_dict["expired"] = expired
        if edns_lame_known is not UNSET:
            field_dict["edns_lame_known"] = edns_lame_known
        if edns_version is not UNSET:
            field_dict["edns_version"] = edns_version
        if probe_delay is not UNSET:
            field_dict["probe_delay"] = probe_delay
        if lame_dnssec is not UNSET:
            field_dict["lame_dnssec"] = lame_dnssec
        if lame_rec is not UNSET:
            field_dict["lame_rec"] = lame_rec
        if lame_a is not UNSET:
            field_dict["lame_a"] = lame_a
        if lame_other is not UNSET:
            field_dict["lame_other"] = lame_other

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server = d.pop("server", UNSET)

        zone = d.pop("zone", UNSET)

        expired = d.pop("expired", UNSET)

        edns_lame_known = d.pop("edns_lame_known", UNSET)

        edns_version = d.pop("edns_version", UNSET)

        probe_delay = d.pop("probe_delay", UNSET)

        lame_dnssec = d.pop("lame_dnssec", UNSET)

        lame_rec = d.pop("lame_rec", UNSET)

        lame_a = d.pop("lame_a", UNSET)

        lame_other = d.pop("lame_other", UNSET)

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
