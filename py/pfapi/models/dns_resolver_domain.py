from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSResolverDomain")


@_attrs_define
class DNSResolverDomain:
    """
    Attributes:
        domain (str):
        ip (str):
        descr (Union[Unset, str]):
        forward_tls_upstream (Union[Unset, bool]):
        tls_hostname (Union[Unset, str]):
        idx (Union[Unset, int]):
    """

    domain: str
    ip: str
    descr: Union[Unset, str] = UNSET
    forward_tls_upstream: Union[Unset, bool] = UNSET
    tls_hostname: Union[Unset, str] = UNSET
    idx: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain = self.domain

        ip = self.ip

        descr = self.descr

        forward_tls_upstream = self.forward_tls_upstream

        tls_hostname = self.tls_hostname

        idx = self.idx

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "ip": ip,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if forward_tls_upstream is not UNSET:
            field_dict["forward_tls_upstream"] = forward_tls_upstream
        if tls_hostname is not UNSET:
            field_dict["tls_hostname"] = tls_hostname
        if idx is not UNSET:
            field_dict["idx"] = idx

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        domain = d.pop("domain")

        ip = d.pop("ip")

        descr = d.pop("descr", UNSET)

        forward_tls_upstream = d.pop("forward_tls_upstream", UNSET)

        tls_hostname = d.pop("tls_hostname", UNSET)

        idx = d.pop("idx", UNSET)

        dns_resolver_domain = cls(
            domain=domain,
            ip=ip,
            descr=descr,
            forward_tls_upstream=forward_tls_upstream,
            tls_hostname=tls_hostname,
            idx=idx,
        )

        dns_resolver_domain.additional_properties = d
        return dns_resolver_domain

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
