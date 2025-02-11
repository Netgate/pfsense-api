from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Dhcpv6StaticMapping")


@_attrs_define
class Dhcpv6StaticMapping:
    """
    Attributes:
        id (str):
        backend (str):
        duid (str):
        ipv6_address (str):
        hostname (str):
        description (str):
        early_dns_reg (str):
    """

    id: str
    backend: str
    duid: str
    ipv6_address: str
    hostname: str
    description: str
    early_dns_reg: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        backend = self.backend

        duid = self.duid

        ipv6_address = self.ipv6_address

        hostname = self.hostname

        description = self.description

        early_dns_reg = self.early_dns_reg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "backend": backend,
                "duid": duid,
                "ipv6_address": ipv6_address,
                "hostname": hostname,
                "description": description,
                "early_dns_reg": early_dns_reg,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        backend = d.pop("backend")

        duid = d.pop("duid")

        ipv6_address = d.pop("ipv6_address")

        hostname = d.pop("hostname")

        description = d.pop("description")

        early_dns_reg = d.pop("early_dns_reg")

        dhcpv_6_static_mapping = cls(
            id=id,
            backend=backend,
            duid=duid,
            ipv6_address=ipv6_address,
            hostname=hostname,
            description=description,
            early_dns_reg=early_dns_reg,
        )

        dhcpv_6_static_mapping.additional_properties = d
        return dhcpv_6_static_mapping

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
