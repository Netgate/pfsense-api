from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RFCItem")


@_attrs_define
class RFCItem:
    """
    Attributes:
        enable (bool):
        host (str):
        zone (str):
        ttl (str):
        keyname (str):
        keyalgorithm (str):
        keydata (str):
        server (str):
        usetcp (bool):
        usepublicip (bool):
        recordtype (str):
        interface (str):
        updatesource (str):
        updatesourcefamily (str):
        descr (str):
        ipv4 (str):
        ipv6 (str):
    """

    enable: bool
    host: str
    zone: str
    ttl: str
    keyname: str
    keyalgorithm: str
    keydata: str
    server: str
    usetcp: bool
    usepublicip: bool
    recordtype: str
    interface: str
    updatesource: str
    updatesourcefamily: str
    descr: str
    ipv4: str
    ipv6: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        host = self.host

        zone = self.zone

        ttl = self.ttl

        keyname = self.keyname

        keyalgorithm = self.keyalgorithm

        keydata = self.keydata

        server = self.server

        usetcp = self.usetcp

        usepublicip = self.usepublicip

        recordtype = self.recordtype

        interface = self.interface

        updatesource = self.updatesource

        updatesourcefamily = self.updatesourcefamily

        descr = self.descr

        ipv4 = self.ipv4

        ipv6 = self.ipv6

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "host": host,
                "zone": zone,
                "ttl": ttl,
                "keyname": keyname,
                "keyalgorithm": keyalgorithm,
                "keydata": keydata,
                "server": server,
                "usetcp": usetcp,
                "usepublicip": usepublicip,
                "recordtype": recordtype,
                "interface": interface,
                "updatesource": updatesource,
                "updatesourcefamily": updatesourcefamily,
                "descr": descr,
                "ipv4": ipv4,
                "ipv6": ipv6,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable")

        host = d.pop("host")

        zone = d.pop("zone")

        ttl = d.pop("ttl")

        keyname = d.pop("keyname")

        keyalgorithm = d.pop("keyalgorithm")

        keydata = d.pop("keydata")

        server = d.pop("server")

        usetcp = d.pop("usetcp")

        usepublicip = d.pop("usepublicip")

        recordtype = d.pop("recordtype")

        interface = d.pop("interface")

        updatesource = d.pop("updatesource")

        updatesourcefamily = d.pop("updatesourcefamily")

        descr = d.pop("descr")

        ipv4 = d.pop("ipv4")

        ipv6 = d.pop("ipv6")

        rfc_item = cls(
            enable=enable,
            host=host,
            zone=zone,
            ttl=ttl,
            keyname=keyname,
            keyalgorithm=keyalgorithm,
            keydata=keydata,
            server=server,
            usetcp=usetcp,
            usepublicip=usepublicip,
            recordtype=recordtype,
            interface=interface,
            updatesource=updatesource,
            updatesourcefamily=updatesourcefamily,
            descr=descr,
            ipv4=ipv4,
            ipv6=ipv6,
        )

        rfc_item.additional_properties = d
        return rfc_item

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
