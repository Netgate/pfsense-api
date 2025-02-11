from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ArpTableEntry")


@_attrs_define
class ArpTableEntry:
    """
    Attributes:
        ip (str):
        mac (str):
        interface (str):
        expires (str):
        type (str):
        dnsresolve (str):
    """

    ip: str
    mac: str
    interface: str
    expires: str
    type: str
    dnsresolve: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ip = self.ip

        mac = self.mac

        interface = self.interface

        expires = self.expires

        type = self.type

        dnsresolve = self.dnsresolve

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip": ip,
                "mac": mac,
                "interface": interface,
                "expires": expires,
                "type": type,
                "dnsresolve": dnsresolve,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip = d.pop("ip")

        mac = d.pop("mac")

        interface = d.pop("interface")

        expires = d.pop("expires")

        type = d.pop("type")

        dnsresolve = d.pop("dnsresolve")

        arp_table_entry = cls(
            ip=ip,
            mac=mac,
            interface=interface,
            expires=expires,
            type=type,
            dnsresolve=dnsresolve,
        )

        arp_table_entry.additional_properties = d
        return arp_table_entry

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
