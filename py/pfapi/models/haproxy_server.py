from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyServer")


@_attrs_define
class HaproxyServer:
    """
    Attributes:
        name (str | Unset): Server Name

            Name for this backend server. Must be unique within the pool.
        status (str | Unset): Status (active, backup, disabled, inactive)

            Server status.
            - active: Normal active server
            - backup: Only used when all active servers are down
            - disabled: Server is configured but not used
            - inactive: Server is inactive
        address (str | Unset): Address

            IP address or hostname of the backend server.
        port (str | Unset): Port

            TCP port of the backend server. Defaults to the same port as the frontend.
        forwardto (str | Unset): Forward To

            Name of another frontend server to forward requests to instead of this server.
            Set to "" if using address and port.
        ssl (bool | Unset): Encrypt (SSL)

            Enable SSL/TLS when connecting to this backend server.
        checkssl (bool | Unset): SSL Health Check

            Use SSL/TLS for health check connections to this server.
        weight (str | Unset): Weight

            Load balancing weight for this server. Higher values receive more traffic.
            (Default: 1)
        cookie (str | Unset): Cookie Value

            Value to use for cookie-based persistence for this server.
        maxconn (str | Unset): Max Connections

            Maximum number of concurrent connections to this backend server.
        sslserververify (bool | Unset): SSL Verify

            Whether to verify the server's SSL certificate.
            - required: Verify against configured CA
            - none: Skip verification (not recommended)
        verifyhost (str | Unset): Verify Host

            Expected hostname in the server's SSL certificate for verification.
        ssl_server_ca (str | Unset): Server CA Certificate

            CA certificate reference for verifying the backend server's SSL certificate.
        ssl_server_crl (str | Unset): Server CRL

            CRL reference for checking backend server certificate revocation.
        ssl_server_clientcert (str | Unset): Client Certificate

            Client certificate reference to present when connecting to the backend server.
        istemplate (str | Unset): DNS SRV Template

            Number of server slots when using DNS SRV resolution. When set, the server
            acts as a template and HAProxy creates this many server slots dynamically.
        advanced (str | Unset): Advanced Server Options

            Additional raw options appended to this server line.
    """

    name: str | Unset = UNSET
    status: str | Unset = UNSET
    address: str | Unset = UNSET
    port: str | Unset = UNSET
    forwardto: str | Unset = UNSET
    ssl: bool | Unset = UNSET
    checkssl: bool | Unset = UNSET
    weight: str | Unset = UNSET
    cookie: str | Unset = UNSET
    maxconn: str | Unset = UNSET
    sslserververify: bool | Unset = UNSET
    verifyhost: str | Unset = UNSET
    ssl_server_ca: str | Unset = UNSET
    ssl_server_crl: str | Unset = UNSET
    ssl_server_clientcert: str | Unset = UNSET
    istemplate: str | Unset = UNSET
    advanced: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        address = self.address

        port = self.port

        forwardto = self.forwardto

        ssl = self.ssl

        checkssl = self.checkssl

        weight = self.weight

        cookie = self.cookie

        maxconn = self.maxconn

        sslserververify = self.sslserververify

        verifyhost = self.verifyhost

        ssl_server_ca = self.ssl_server_ca

        ssl_server_crl = self.ssl_server_crl

        ssl_server_clientcert = self.ssl_server_clientcert

        istemplate = self.istemplate

        advanced = self.advanced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if forwardto is not UNSET:
            field_dict["forwardto"] = forwardto
        if ssl is not UNSET:
            field_dict["ssl"] = ssl
        if checkssl is not UNSET:
            field_dict["checkssl"] = checkssl
        if weight is not UNSET:
            field_dict["weight"] = weight
        if cookie is not UNSET:
            field_dict["cookie"] = cookie
        if maxconn is not UNSET:
            field_dict["maxconn"] = maxconn
        if sslserververify is not UNSET:
            field_dict["sslserververify"] = sslserververify
        if verifyhost is not UNSET:
            field_dict["verifyhost"] = verifyhost
        if ssl_server_ca is not UNSET:
            field_dict["ssl_server_ca"] = ssl_server_ca
        if ssl_server_crl is not UNSET:
            field_dict["ssl_server_crl"] = ssl_server_crl
        if ssl_server_clientcert is not UNSET:
            field_dict["ssl_server_clientcert"] = ssl_server_clientcert
        if istemplate is not UNSET:
            field_dict["istemplate"] = istemplate
        if advanced is not UNSET:
            field_dict["advanced"] = advanced

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        forwardto = d.pop("forwardto", UNSET)

        ssl = d.pop("ssl", UNSET)

        checkssl = d.pop("checkssl", UNSET)

        weight = d.pop("weight", UNSET)

        cookie = d.pop("cookie", UNSET)

        maxconn = d.pop("maxconn", UNSET)

        sslserververify = d.pop("sslserververify", UNSET)

        verifyhost = d.pop("verifyhost", UNSET)

        ssl_server_ca = d.pop("ssl_server_ca", UNSET)

        ssl_server_crl = d.pop("ssl_server_crl", UNSET)

        ssl_server_clientcert = d.pop("ssl_server_clientcert", UNSET)

        istemplate = d.pop("istemplate", UNSET)

        advanced = d.pop("advanced", UNSET)

        haproxy_server = cls(
            name=name,
            status=status,
            address=address,
            port=port,
            forwardto=forwardto,
            ssl=ssl,
            checkssl=checkssl,
            weight=weight,
            cookie=cookie,
            maxconn=maxconn,
            sslserververify=sslserververify,
            verifyhost=verifyhost,
            ssl_server_ca=ssl_server_ca,
            ssl_server_crl=ssl_server_crl,
            ssl_server_clientcert=ssl_server_clientcert,
            istemplate=istemplate,
            advanced=advanced,
        )

        haproxy_server.additional_properties = d
        return haproxy_server

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
