from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DynDNSConfig")


@_attrs_define
class DynDNSConfig:
    """
    Attributes:
        enable (bool):
        type_ (str):
        username (str | Unset):
        password (str | Unset): base64 encoded
        host (str | Unset):
        domainname (str | Unset):
        mx (str | Unset):
        wildcard (bool | Unset):
        verboselog (bool | Unset):
        curl_ipresolve_v4 (bool | Unset):
        curl_ssl_verifypeer (bool | Unset):
        curl_proxy (bool | Unset):
        maxcacheage (str | Unset):
        interface (str | Unset):
        zoneid (str | Unset):
        ttl (str | Unset):
        updateurl (str | Unset):
        resultmatch (str | Unset):
        requestif (str | Unset):
        proxied (bool | Unset):
        descr (str | Unset):
        id (str | Unset):
        check_ip_mode (str | Unset): auto (default), always, never
        status (str | Unset): failed or updated
        ip (str | Unset): cached IP/IPv6
    """

    enable: bool
    type_: str
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    host: str | Unset = UNSET
    domainname: str | Unset = UNSET
    mx: str | Unset = UNSET
    wildcard: bool | Unset = UNSET
    verboselog: bool | Unset = UNSET
    curl_ipresolve_v4: bool | Unset = UNSET
    curl_ssl_verifypeer: bool | Unset = UNSET
    curl_proxy: bool | Unset = UNSET
    maxcacheage: str | Unset = UNSET
    interface: str | Unset = UNSET
    zoneid: str | Unset = UNSET
    ttl: str | Unset = UNSET
    updateurl: str | Unset = UNSET
    resultmatch: str | Unset = UNSET
    requestif: str | Unset = UNSET
    proxied: bool | Unset = UNSET
    descr: str | Unset = UNSET
    id: str | Unset = UNSET
    check_ip_mode: str | Unset = UNSET
    status: str | Unset = UNSET
    ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        type_ = self.type_

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

        check_ip_mode = self.check_ip_mode

        status = self.status

        ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "type": type_,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if host is not UNSET:
            field_dict["host"] = host
        if domainname is not UNSET:
            field_dict["domainname"] = domainname
        if mx is not UNSET:
            field_dict["mx"] = mx
        if wildcard is not UNSET:
            field_dict["wildcard"] = wildcard
        if verboselog is not UNSET:
            field_dict["verboselog"] = verboselog
        if curl_ipresolve_v4 is not UNSET:
            field_dict["curl_ipresolve_v4"] = curl_ipresolve_v4
        if curl_ssl_verifypeer is not UNSET:
            field_dict["curl_ssl_verifypeer"] = curl_ssl_verifypeer
        if curl_proxy is not UNSET:
            field_dict["curl_proxy"] = curl_proxy
        if maxcacheage is not UNSET:
            field_dict["maxcacheage"] = maxcacheage
        if interface is not UNSET:
            field_dict["interface"] = interface
        if zoneid is not UNSET:
            field_dict["zoneid"] = zoneid
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if updateurl is not UNSET:
            field_dict["updateurl"] = updateurl
        if resultmatch is not UNSET:
            field_dict["resultmatch"] = resultmatch
        if requestif is not UNSET:
            field_dict["requestif"] = requestif
        if proxied is not UNSET:
            field_dict["proxied"] = proxied
        if descr is not UNSET:
            field_dict["descr"] = descr
        if id is not UNSET:
            field_dict["id"] = id
        if check_ip_mode is not UNSET:
            field_dict["check_ip_mode"] = check_ip_mode
        if status is not UNSET:
            field_dict["status"] = status
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable")

        type_ = d.pop("type")

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        host = d.pop("host", UNSET)

        domainname = d.pop("domainname", UNSET)

        mx = d.pop("mx", UNSET)

        wildcard = d.pop("wildcard", UNSET)

        verboselog = d.pop("verboselog", UNSET)

        curl_ipresolve_v4 = d.pop("curl_ipresolve_v4", UNSET)

        curl_ssl_verifypeer = d.pop("curl_ssl_verifypeer", UNSET)

        curl_proxy = d.pop("curl_proxy", UNSET)

        maxcacheage = d.pop("maxcacheage", UNSET)

        interface = d.pop("interface", UNSET)

        zoneid = d.pop("zoneid", UNSET)

        ttl = d.pop("ttl", UNSET)

        updateurl = d.pop("updateurl", UNSET)

        resultmatch = d.pop("resultmatch", UNSET)

        requestif = d.pop("requestif", UNSET)

        proxied = d.pop("proxied", UNSET)

        descr = d.pop("descr", UNSET)

        id = d.pop("id", UNSET)

        check_ip_mode = d.pop("check_ip_mode", UNSET)

        status = d.pop("status", UNSET)

        ip = d.pop("ip", UNSET)

        dyn_dns_config = cls(
            enable=enable,
            type_=type_,
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
            check_ip_mode=check_ip_mode,
            status=status,
            ip=ip,
        )

        dyn_dns_config.additional_properties = d
        return dyn_dns_config

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
