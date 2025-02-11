from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NDPEntry")


@_attrs_define
class NDPEntry:
    """
    Attributes:
        ipv6 (str):
        mac (str):
        iface (str):
        hostname (str):
        exp (str):
        status (str):
        flags (str):
    """

    ipv6: str
    mac: str
    iface: str
    hostname: str
    exp: str
    status: str
    flags: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ipv6 = self.ipv6

        mac = self.mac

        iface = self.iface

        hostname = self.hostname

        exp = self.exp

        status = self.status

        flags = self.flags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipv6": ipv6,
                "mac": mac,
                "iface": iface,
                "hostname": hostname,
                "exp": exp,
                "status": status,
                "flags": flags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ipv6 = d.pop("ipv6")

        mac = d.pop("mac")

        iface = d.pop("iface")

        hostname = d.pop("hostname")

        exp = d.pop("exp")

        status = d.pop("status")

        flags = d.pop("flags")

        ndp_entry = cls(
            ipv6=ipv6,
            mac=mac,
            iface=iface,
            hostname=hostname,
            exp=exp,
            status=status,
            flags=flags,
        )

        ndp_entry.additional_properties = d
        return ndp_entry

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
