from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DNSForwarderDomain")


@_attrs_define
class DNSForwarderDomain:
    """
    Attributes:
        domain (str):
        ip (str):
        descr (str):
        idx (int):
    """

    domain: str
    ip: str
    descr: str
    idx: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain = self.domain

        ip = self.ip

        descr = self.descr

        idx = self.idx

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "ip": ip,
                "descr": descr,
                "idx": idx,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        domain = d.pop("domain")

        ip = d.pop("ip")

        descr = d.pop("descr")

        idx = d.pop("idx")

        dns_forwarder_domain = cls(
            domain=domain,
            ip=ip,
            descr=descr,
            idx=idx,
        )

        dns_forwarder_domain.additional_properties = d
        return dns_forwarder_domain

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
