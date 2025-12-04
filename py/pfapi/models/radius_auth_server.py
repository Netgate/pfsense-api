from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RadiusAuthServer")


@_attrs_define
class RadiusAuthServer:
    """
    Attributes:
        name (str):
        host (str):
        protocol (str): pap, chap_md5, mschapv1, mschapv2
        type_ (str | Unset):
        nasip_attribute (str | Unset):
        secret (str | Unset):
        timeout (int | Unset):
        auth_port (int | Unset):
        acct_port (int | Unset):
        refid (str | Unset):
    """

    name: str
    host: str
    protocol: str
    type_: str | Unset = UNSET
    nasip_attribute: str | Unset = UNSET
    secret: str | Unset = UNSET
    timeout: int | Unset = UNSET
    auth_port: int | Unset = UNSET
    acct_port: int | Unset = UNSET
    refid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        host = self.host

        protocol = self.protocol

        type_ = self.type_

        nasip_attribute = self.nasip_attribute

        secret = self.secret

        timeout = self.timeout

        auth_port = self.auth_port

        acct_port = self.acct_port

        refid = self.refid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "host": host,
                "protocol": protocol,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if nasip_attribute is not UNSET:
            field_dict["nasip_attribute"] = nasip_attribute
        if secret is not UNSET:
            field_dict["secret"] = secret
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if auth_port is not UNSET:
            field_dict["auth_port"] = auth_port
        if acct_port is not UNSET:
            field_dict["acct_port"] = acct_port
        if refid is not UNSET:
            field_dict["refid"] = refid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        host = d.pop("host")

        protocol = d.pop("protocol")

        type_ = d.pop("type", UNSET)

        nasip_attribute = d.pop("nasip_attribute", UNSET)

        secret = d.pop("secret", UNSET)

        timeout = d.pop("timeout", UNSET)

        auth_port = d.pop("auth_port", UNSET)

        acct_port = d.pop("acct_port", UNSET)

        refid = d.pop("refid", UNSET)

        radius_auth_server = cls(
            name=name,
            host=host,
            protocol=protocol,
            type_=type_,
            nasip_attribute=nasip_attribute,
            secret=secret,
            timeout=timeout,
            auth_port=auth_port,
            acct_port=acct_port,
            refid=refid,
        )

        radius_auth_server.additional_properties = d
        return radius_auth_server

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
