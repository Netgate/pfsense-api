from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSForwarderDomain")


@_attrs_define
class DNSForwarderDomain:
    """
    Attributes:
        domain (str):
        ip (str):
        source_ip (str):
        descr (str | Unset):
        idx (int | Unset):
    """

    domain: str
    ip: str
    source_ip: str
    descr: str | Unset = UNSET
    idx: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        ip = self.ip

        source_ip = self.source_ip

        descr = self.descr

        idx = self.idx

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "ip": ip,
                "source_ip": source_ip,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if idx is not UNSET:
            field_dict["idx"] = idx

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        ip = d.pop("ip")

        source_ip = d.pop("source_ip")

        descr = d.pop("descr", UNSET)

        idx = d.pop("idx", UNSET)

        dns_forwarder_domain = cls(
            domain=domain,
            ip=ip,
            source_ip=source_ip,
            descr=descr,
            idx=idx,
        )

        dns_forwarder_domain.additional_properties = d
        return dns_forwarder_domain

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
