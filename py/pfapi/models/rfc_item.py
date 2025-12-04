from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RFCItem")


@_attrs_define
class RFCItem:
    """
    Attributes:
        enable (bool):
        host (str | Unset):
        zone (str | Unset):
        ttl (str | Unset):
        keyname (str | Unset):
        keyalgorithm (str | Unset):
        keydata (str | Unset):
        server (str | Unset):
        usetcp (bool | Unset):
        usepublicip (bool | Unset):
        recordtype (str | Unset):
        interface (str | Unset):
        updatesource (str | Unset):
        updatesourcefamily (str | Unset):
        descr (str | Unset):
        status (str | Unset): failed or updated
        ip (str | Unset): cached IP/IPv6
    """

    enable: bool
    host: str | Unset = UNSET
    zone: str | Unset = UNSET
    ttl: str | Unset = UNSET
    keyname: str | Unset = UNSET
    keyalgorithm: str | Unset = UNSET
    keydata: str | Unset = UNSET
    server: str | Unset = UNSET
    usetcp: bool | Unset = UNSET
    usepublicip: bool | Unset = UNSET
    recordtype: str | Unset = UNSET
    interface: str | Unset = UNSET
    updatesource: str | Unset = UNSET
    updatesourcefamily: str | Unset = UNSET
    descr: str | Unset = UNSET
    status: str | Unset = UNSET
    ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        status = self.status

        ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if host is not UNSET:
            field_dict["host"] = host
        if zone is not UNSET:
            field_dict["zone"] = zone
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if keyname is not UNSET:
            field_dict["keyname"] = keyname
        if keyalgorithm is not UNSET:
            field_dict["keyalgorithm"] = keyalgorithm
        if keydata is not UNSET:
            field_dict["keydata"] = keydata
        if server is not UNSET:
            field_dict["server"] = server
        if usetcp is not UNSET:
            field_dict["usetcp"] = usetcp
        if usepublicip is not UNSET:
            field_dict["usepublicip"] = usepublicip
        if recordtype is not UNSET:
            field_dict["recordtype"] = recordtype
        if interface is not UNSET:
            field_dict["interface"] = interface
        if updatesource is not UNSET:
            field_dict["updatesource"] = updatesource
        if updatesourcefamily is not UNSET:
            field_dict["updatesourcefamily"] = updatesourcefamily
        if descr is not UNSET:
            field_dict["descr"] = descr
        if status is not UNSET:
            field_dict["status"] = status
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable")

        host = d.pop("host", UNSET)

        zone = d.pop("zone", UNSET)

        ttl = d.pop("ttl", UNSET)

        keyname = d.pop("keyname", UNSET)

        keyalgorithm = d.pop("keyalgorithm", UNSET)

        keydata = d.pop("keydata", UNSET)

        server = d.pop("server", UNSET)

        usetcp = d.pop("usetcp", UNSET)

        usepublicip = d.pop("usepublicip", UNSET)

        recordtype = d.pop("recordtype", UNSET)

        interface = d.pop("interface", UNSET)

        updatesource = d.pop("updatesource", UNSET)

        updatesourcefamily = d.pop("updatesourcefamily", UNSET)

        descr = d.pop("descr", UNSET)

        status = d.pop("status", UNSET)

        ip = d.pop("ip", UNSET)

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
            status=status,
            ip=ip,
        )

        rfc_item.additional_properties = d
        return rfc_item

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
