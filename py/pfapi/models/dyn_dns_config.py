from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DynDNSConfig")


@_attrs_define
class DynDNSConfig:
    """
    Attributes:
        enable (bool):
        type (str):
        username (str):
        password (str):
        host (str):
        domainname (str):
        mx (str):
        wildcard (bool):
        verboselog (bool):
        curl_ipresolve_v4 (bool):
        curl_ssl_verifypeer (bool):
        curl_proxy (bool):
        maxcacheage (str):
        interface (str):
        zoneid (str):
        ttl (str):
        updateurl (str):
        resultmatch (str):
        requestif (str):
        proxied (bool):
        descr (str):
        id (str):
        status (str):
        ipv4 (str):
        ipv6 (str):
    """

    enable: bool
    type: str
    username: str
    password: str
    host: str
    domainname: str
    mx: str
    wildcard: bool
    verboselog: bool
    curl_ipresolve_v4: bool
    curl_ssl_verifypeer: bool
    curl_proxy: bool
    maxcacheage: str
    interface: str
    zoneid: str
    ttl: str
    updateurl: str
    resultmatch: str
    requestif: str
    proxied: bool
    descr: str
    id: str
    status: str
    ipv4: str
    ipv6: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        type = self.type

        username = self.username

        password = self.password

        host = self.host

        domainname = self.domainname

        mx = self.mx

        wildcard = self.wildcard

        verboselog = self.verboselog

        curl_ipresolve_v4 = self.curl_ipresolve_v4

        curl_ssl_verifypeer = self.curl_ssl_verifypeer

        curl_proxy = self.curl_proxy

        maxcacheage = self.maxcacheage

        interface = self.interface

        zoneid = self.zoneid

        ttl = self.ttl

        updateurl = self.updateurl

        resultmatch = self.resultmatch

        requestif = self.requestif

        proxied = self.proxied

        descr = self.descr

        id = self.id

        status = self.status

        ipv4 = self.ipv4

        ipv6 = self.ipv6

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "type": type,
                "username": username,
                "password": password,
                "host": host,
                "domainname": domainname,
                "mx": mx,
                "wildcard": wildcard,
                "verboselog": verboselog,
                "curl_ipresolve_v4": curl_ipresolve_v4,
                "curl_ssl_verifypeer": curl_ssl_verifypeer,
                "curl_proxy": curl_proxy,
                "maxcacheage": maxcacheage,
                "interface": interface,
                "zoneid": zoneid,
                "ttl": ttl,
                "updateurl": updateurl,
                "resultmatch": resultmatch,
                "requestif": requestif,
                "proxied": proxied,
                "descr": descr,
                "id": id,
                "status": status,
                "ipv4": ipv4,
                "ipv6": ipv6,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable")

        type = d.pop("type")

        username = d.pop("username")

        password = d.pop("password")

        host = d.pop("host")

        domainname = d.pop("domainname")

        mx = d.pop("mx")

        wildcard = d.pop("wildcard")

        verboselog = d.pop("verboselog")

        curl_ipresolve_v4 = d.pop("curl_ipresolve_v4")

        curl_ssl_verifypeer = d.pop("curl_ssl_verifypeer")

        curl_proxy = d.pop("curl_proxy")

        maxcacheage = d.pop("maxcacheage")

        interface = d.pop("interface")

        zoneid = d.pop("zoneid")

        ttl = d.pop("ttl")

        updateurl = d.pop("updateurl")

        resultmatch = d.pop("resultmatch")

        requestif = d.pop("requestif")

        proxied = d.pop("proxied")

        descr = d.pop("descr")

        id = d.pop("id")

        status = d.pop("status")

        ipv4 = d.pop("ipv4")

        ipv6 = d.pop("ipv6")

        dyn_dns_config = cls(
            enable=enable,
            type=type,
            username=username,
            password=password,
            host=host,
            domainname=domainname,
            mx=mx,
            wildcard=wildcard,
            verboselog=verboselog,
            curl_ipresolve_v4=curl_ipresolve_v4,
            curl_ssl_verifypeer=curl_ssl_verifypeer,
            curl_proxy=curl_proxy,
            maxcacheage=maxcacheage,
            interface=interface,
            zoneid=zoneid,
            ttl=ttl,
            updateurl=updateurl,
            resultmatch=resultmatch,
            requestif=requestif,
            proxied=proxied,
            descr=descr,
            id=id,
            status=status,
            ipv4=ipv4,
            ipv6=ipv6,
        )

        dyn_dns_config.additional_properties = d
        return dyn_dns_config

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
