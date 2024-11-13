from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DynDNSConfig")


@_attrs_define
class DynDNSConfig:
    """
    Attributes:
        type (Union[Unset, str]):
        username (Union[Unset, str]):
        password (Union[Unset, str]):
        host (Union[Unset, str]):
        domainname (Union[Unset, str]):
        mx (Union[Unset, int]):
        wildcard (Union[Unset, bool]):
        verboselog (Union[Unset, bool]):
        curl_ipresolve_v4 (Union[Unset, bool]):
        curl_ssl_verifypeer (Union[Unset, bool]):
        enable (Union[Unset, bool]):
        interface (Union[Unset, str]):
        zoneid (Union[Unset, str]):
        ttl (Union[Unset, str]):
        updateurl (Union[Unset, str]):
        resultmatch (Union[Unset, str]):
        requestif (Union[Unset, str]):
        proxied (Union[Unset, bool]):
        descr (Union[Unset, str]):
        id (Union[Unset, str]):
        ip (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    domainname: Union[Unset, str] = UNSET
    mx: Union[Unset, int] = UNSET
    wildcard: Union[Unset, bool] = UNSET
    verboselog: Union[Unset, bool] = UNSET
    curl_ipresolve_v4: Union[Unset, bool] = UNSET
    curl_ssl_verifypeer: Union[Unset, bool] = UNSET
    enable: Union[Unset, bool] = UNSET
    interface: Union[Unset, str] = UNSET
    zoneid: Union[Unset, str] = UNSET
    ttl: Union[Unset, str] = UNSET
    updateurl: Union[Unset, str] = UNSET
    resultmatch: Union[Unset, str] = UNSET
    requestif: Union[Unset, str] = UNSET
    proxied: Union[Unset, bool] = UNSET
    descr: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        enable = self.enable

        interface = self.interface

        zoneid = self.zoneid

        ttl = self.ttl

        updateurl = self.updateurl

        resultmatch = self.resultmatch

        requestif = self.requestif

        proxied = self.proxied

        descr = self.descr

        id = self.id

        ip = self.ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
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
        if enable is not UNSET:
            field_dict["enable"] = enable
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
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        host = d.pop("host", UNSET)

        domainname = d.pop("domainname", UNSET)

        mx = d.pop("mx", UNSET)

        wildcard = d.pop("wildcard", UNSET)

        verboselog = d.pop("verboselog", UNSET)

        curl_ipresolve_v4 = d.pop("curl_ipresolve_v4", UNSET)

        curl_ssl_verifypeer = d.pop("curl_ssl_verifypeer", UNSET)

        enable = d.pop("enable", UNSET)

        interface = d.pop("interface", UNSET)

        zoneid = d.pop("zoneid", UNSET)

        ttl = d.pop("ttl", UNSET)

        updateurl = d.pop("updateurl", UNSET)

        resultmatch = d.pop("resultmatch", UNSET)

        requestif = d.pop("requestif", UNSET)

        proxied = d.pop("proxied", UNSET)

        descr = d.pop("descr", UNSET)

        id = d.pop("id", UNSET)

        ip = d.pop("ip", UNSET)

        dyn_dns_config = cls(
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
            enable=enable,
            interface=interface,
            zoneid=zoneid,
            ttl=ttl,
            updateurl=updateurl,
            resultmatch=resultmatch,
            requestif=requestif,
            proxied=proxied,
            descr=descr,
            id=id,
            ip=ip,
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
