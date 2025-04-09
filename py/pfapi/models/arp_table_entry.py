from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArpTableEntry")


@_attrs_define
class ArpTableEntry:
    """
    Attributes:
        ip (Union[Unset, str]):
        mac (Union[Unset, str]):
        interface (Union[Unset, str]):
        expires (Union[Unset, str]):
        type (Union[Unset, str]):
        dnsresolve (Union[Unset, str]):
    """

    ip: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    expires: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    dnsresolve: Union[Unset, str] = UNSET
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
        field_dict.update({})
        if ip is not UNSET:
            field_dict["ip"] = ip
        if mac is not UNSET:
            field_dict["mac"] = mac
        if interface is not UNSET:
            field_dict["interface"] = interface
        if expires is not UNSET:
            field_dict["expires"] = expires
        if type is not UNSET:
            field_dict["type"] = type
        if dnsresolve is not UNSET:
            field_dict["dnsresolve"] = dnsresolve

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip = d.pop("ip", UNSET)

        mac = d.pop("mac", UNSET)

        interface = d.pop("interface", UNSET)

        expires = d.pop("expires", UNSET)

        type = d.pop("type", UNSET)

        dnsresolve = d.pop("dnsresolve", UNSET)

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
