from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.haproxy_acl import HaproxyAcl
    from ..models.haproxy_action import HaproxyAction
    from ..models.haproxy_bind_address import HaproxyBindAddress
    from ..models.haproxy_certificate import HaproxyCertificate
    from ..models.haproxy_client_ca import HaproxyClientCa
    from ..models.haproxy_client_crl import HaproxyClientCrl
    from ..models.haproxy_error_file import HaproxyErrorFile


T = TypeVar("T", bound="HaproxyFrontend")


@_attrs_define
class HaproxyFrontend:
    """
    Attributes:
        name (str | Unset): Name

            Unique name for this frontend. Used as identifier in HAProxy configuration.
        descr (str | Unset): Description

            Optional description of this frontend's purpose.
        status (str | Unset): Status (active, disabled)

            Whether this frontend is active or disabled in the HAProxy configuration.
        type_ (str | Unset): Type (http, https, tcp)

            Protocol mode for this frontend.
            - http: Layer 7 HTTP processing
            - https: Layer 7 HTTP with SSL (offloading handled separately)
            - tcp: Layer 4 TCP passthrough
        secondary (bool | Unset): Secondary Frontend

            When true, this frontend is a secondary that shares settings with a primary frontend.
        primary_frontend (str | Unset): Primary Frontend

            Name of the primary frontend this secondary frontend shares settings with.
            Only applicable when secondary is true.
        backend_serverpool (str | Unset): Default Backend

            Name of the default backend pool to use when no ACL-based action matches.
        maxconn (str | Unset): Maximum Connections

            Maximum number of concurrent connections for this frontend.
        bind_addresses (list[HaproxyBindAddress] | Unset):
        forwardfor (bool | Unset): X-Forwarded-For

            Add X-Forwarded-For header containing the client's IP address.
        httpclose (str | Unset): Connection Mode (http-keep-alive, http-tunnel, httpclose, http-server-close,
            forceclose)

            HTTP connection handling mode.
            - http-keep-alive: Allow persistent connections (default for HTTP mode)
            - http-server-close: Close server-side connections after each response
            - httpclose: Close both sides after each transaction
            - forceclose: Aggressively close connections
        dontlognull (bool | Unset): Don't Log Null Connections

            Skip logging for connections that transfer no data (probes, health checks).
        dontlog_normal (bool | Unset): Don't Log Normal

            Skip logging for normal, successful connections. Only log errors.
        log_separate_errors (bool | Unset): Log Separate Errors

            Log connection errors and timeouts to a separate log facility.
        log_detailed (bool | Unset): Detailed Logging

            Enable verbose logging with additional connection and request details.
        socket_stats (bool | Unset): Socket Statistics

            Enable per-socket statistics for this frontend.
        client_timeout (str | Unset): Client Timeout

            Maximum time to wait for data from the client, in milliseconds.
        ssloffload (bool | Unset): SSL Offloading

            Enable SSL/TLS termination on this frontend.
        ssloffloadcert (str | Unset): SSL Certificate

            Reference ID of the primary SSL certificate for this frontend.
        sslsnifilter (str | Unset): SNI Filter

            Enable SNI-based certificate selection for this frontend.
        ssl_crtlist_advanced (str | Unset): Advanced Certificate List

            Raw crt-list directives for advanced certificate configuration.
        dcertadv (str | Unset): Default Certificate Advanced

            Advanced options appended to the default certificate's bind line.
        ssloffloadacl (bool | Unset): SSL ACL Name

            Add ACL for certificate CommonName. (host header matches the "CN" of the certificate.
        ssloffloadacl_an (bool | Unset): SSL ACL Additional Name

            Add ACL for certificate Subject Alternative Names.
        ssloffloadacladditional (bool | Unset): SSL ACL Additional CN

            Add ACL for certificate CommonName. (host header matches the "CN" of the certificate)
        ssloffloadacladditional_an (bool | Unset): SSL ACL Additional SAN

            Add ACL for certificate Subject Alternative Names.
        sslclientcert_none (bool | Unset): Without client cert

            Allows clients without a certificate to connect.
        sslclientcert_invalid (bool | Unset): Client Certificate Invalid Action

            Allows client with a invalid/expired/revoked or otherwise wrong certificate to connect.
        sslocsp (bool | Unset): OCSP Certificate

            Load certificate OCSP responses for easy certificate validation by the client.
        ha_certificates (list[HaproxyCertificate] | Unset):
        clientcert_ca (list[HaproxyClientCa] | Unset):
        clientcert_crl (list[HaproxyClientCrl] | Unset):
        ha_acls (list[HaproxyAcl] | Unset):
        a_actionitems (list[HaproxyAction] | Unset):
        a_errorfiles (list[HaproxyErrorFile] | Unset):
        advanced_bind (str | Unset): Bind Pass Thru

            Additional parameters appended to all bind lines in this frontend.
        advanced (str | Unset): Advanced Pass Thru

            Base64-encoded raw HAProxy configuration appended to this frontend section.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    status: str | Unset = UNSET
    type_: str | Unset = UNSET
    secondary: bool | Unset = UNSET
    primary_frontend: str | Unset = UNSET
    backend_serverpool: str | Unset = UNSET
    maxconn: str | Unset = UNSET
    bind_addresses: list[HaproxyBindAddress] | Unset = UNSET
    forwardfor: bool | Unset = UNSET
    httpclose: str | Unset = UNSET
    dontlognull: bool | Unset = UNSET
    dontlog_normal: bool | Unset = UNSET
    log_separate_errors: bool | Unset = UNSET
    log_detailed: bool | Unset = UNSET
    socket_stats: bool | Unset = UNSET
    client_timeout: str | Unset = UNSET
    ssloffload: bool | Unset = UNSET
    ssloffloadcert: str | Unset = UNSET
    sslsnifilter: str | Unset = UNSET
    ssl_crtlist_advanced: str | Unset = UNSET
    dcertadv: str | Unset = UNSET
    ssloffloadacl: bool | Unset = UNSET
    ssloffloadacl_an: bool | Unset = UNSET
    ssloffloadacladditional: bool | Unset = UNSET
    ssloffloadacladditional_an: bool | Unset = UNSET
    sslclientcert_none: bool | Unset = UNSET
    sslclientcert_invalid: bool | Unset = UNSET
    sslocsp: bool | Unset = UNSET
    ha_certificates: list[HaproxyCertificate] | Unset = UNSET
    clientcert_ca: list[HaproxyClientCa] | Unset = UNSET
    clientcert_crl: list[HaproxyClientCrl] | Unset = UNSET
    ha_acls: list[HaproxyAcl] | Unset = UNSET
    a_actionitems: list[HaproxyAction] | Unset = UNSET
    a_errorfiles: list[HaproxyErrorFile] | Unset = UNSET
    advanced_bind: str | Unset = UNSET
    advanced: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descr = self.descr

        status = self.status

        type_ = self.type_

        secondary = self.secondary

        primary_frontend = self.primary_frontend

        backend_serverpool = self.backend_serverpool

        maxconn = self.maxconn

        bind_addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bind_addresses, Unset):
            bind_addresses = []
            for bind_addresses_item_data in self.bind_addresses:
                bind_addresses_item = bind_addresses_item_data.to_dict()
                bind_addresses.append(bind_addresses_item)

        forwardfor = self.forwardfor

        httpclose = self.httpclose

        dontlognull = self.dontlognull

        dontlog_normal = self.dontlog_normal

        log_separate_errors = self.log_separate_errors

        log_detailed = self.log_detailed

        socket_stats = self.socket_stats

        client_timeout = self.client_timeout

        ssloffload = self.ssloffload

        ssloffloadcert = self.ssloffloadcert

        sslsnifilter = self.sslsnifilter

        ssl_crtlist_advanced = self.ssl_crtlist_advanced

        dcertadv = self.dcertadv

        ssloffloadacl = self.ssloffloadacl

        ssloffloadacl_an = self.ssloffloadacl_an

        ssloffloadacladditional = self.ssloffloadacladditional

        ssloffloadacladditional_an = self.ssloffloadacladditional_an

        sslclientcert_none = self.sslclientcert_none

        sslclientcert_invalid = self.sslclientcert_invalid

        sslocsp = self.sslocsp

        ha_certificates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ha_certificates, Unset):
            ha_certificates = []
            for ha_certificates_item_data in self.ha_certificates:
                ha_certificates_item = ha_certificates_item_data.to_dict()
                ha_certificates.append(ha_certificates_item)

        clientcert_ca: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clientcert_ca, Unset):
            clientcert_ca = []
            for clientcert_ca_item_data in self.clientcert_ca:
                clientcert_ca_item = clientcert_ca_item_data.to_dict()
                clientcert_ca.append(clientcert_ca_item)

        clientcert_crl: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clientcert_crl, Unset):
            clientcert_crl = []
            for clientcert_crl_item_data in self.clientcert_crl:
                clientcert_crl_item = clientcert_crl_item_data.to_dict()
                clientcert_crl.append(clientcert_crl_item)

        ha_acls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ha_acls, Unset):
            ha_acls = []
            for ha_acls_item_data in self.ha_acls:
                ha_acls_item = ha_acls_item_data.to_dict()
                ha_acls.append(ha_acls_item)

        a_actionitems: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.a_actionitems, Unset):
            a_actionitems = []
            for a_actionitems_item_data in self.a_actionitems:
                a_actionitems_item = a_actionitems_item_data.to_dict()
                a_actionitems.append(a_actionitems_item)

        a_errorfiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.a_errorfiles, Unset):
            a_errorfiles = []
            for a_errorfiles_item_data in self.a_errorfiles:
                a_errorfiles_item = a_errorfiles_item_data.to_dict()
                a_errorfiles.append(a_errorfiles_item)

        advanced_bind = self.advanced_bind

        advanced = self.advanced

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if secondary is not UNSET:
            field_dict["secondary"] = secondary
        if primary_frontend is not UNSET:
            field_dict["primary_frontend"] = primary_frontend
        if backend_serverpool is not UNSET:
            field_dict["backend_serverpool"] = backend_serverpool
        if maxconn is not UNSET:
            field_dict["maxconn"] = maxconn
        if bind_addresses is not UNSET:
            field_dict["bind_addresses"] = bind_addresses
        if forwardfor is not UNSET:
            field_dict["forwardfor"] = forwardfor
        if httpclose is not UNSET:
            field_dict["httpclose"] = httpclose
        if dontlognull is not UNSET:
            field_dict["dontlognull"] = dontlognull
        if dontlog_normal is not UNSET:
            field_dict["dontlog_normal"] = dontlog_normal
        if log_separate_errors is not UNSET:
            field_dict["log_separate_errors"] = log_separate_errors
        if log_detailed is not UNSET:
            field_dict["log_detailed"] = log_detailed
        if socket_stats is not UNSET:
            field_dict["socket_stats"] = socket_stats
        if client_timeout is not UNSET:
            field_dict["client_timeout"] = client_timeout
        if ssloffload is not UNSET:
            field_dict["ssloffload"] = ssloffload
        if ssloffloadcert is not UNSET:
            field_dict["ssloffloadcert"] = ssloffloadcert
        if sslsnifilter is not UNSET:
            field_dict["sslsnifilter"] = sslsnifilter
        if ssl_crtlist_advanced is not UNSET:
            field_dict["ssl_crtlist_advanced"] = ssl_crtlist_advanced
        if dcertadv is not UNSET:
            field_dict["dcertadv"] = dcertadv
        if ssloffloadacl is not UNSET:
            field_dict["ssloffloadacl"] = ssloffloadacl
        if ssloffloadacl_an is not UNSET:
            field_dict["ssloffloadacl_an"] = ssloffloadacl_an
        if ssloffloadacladditional is not UNSET:
            field_dict["ssloffloadacladditional"] = ssloffloadacladditional
        if ssloffloadacladditional_an is not UNSET:
            field_dict["ssloffloadacladditional_an"] = ssloffloadacladditional_an
        if sslclientcert_none is not UNSET:
            field_dict["sslclientcert_none"] = sslclientcert_none
        if sslclientcert_invalid is not UNSET:
            field_dict["sslclientcert_invalid"] = sslclientcert_invalid
        if sslocsp is not UNSET:
            field_dict["sslocsp"] = sslocsp
        if ha_certificates is not UNSET:
            field_dict["ha_certificates"] = ha_certificates
        if clientcert_ca is not UNSET:
            field_dict["clientcert_ca"] = clientcert_ca
        if clientcert_crl is not UNSET:
            field_dict["clientcert_crl"] = clientcert_crl
        if ha_acls is not UNSET:
            field_dict["ha_acls"] = ha_acls
        if a_actionitems is not UNSET:
            field_dict["a_actionitems"] = a_actionitems
        if a_errorfiles is not UNSET:
            field_dict["a_errorfiles"] = a_errorfiles
        if advanced_bind is not UNSET:
            field_dict["advanced_bind"] = advanced_bind
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.haproxy_acl import HaproxyAcl
        from ..models.haproxy_action import HaproxyAction
        from ..models.haproxy_bind_address import HaproxyBindAddress
        from ..models.haproxy_certificate import HaproxyCertificate
        from ..models.haproxy_client_ca import HaproxyClientCa
        from ..models.haproxy_client_crl import HaproxyClientCrl
        from ..models.haproxy_error_file import HaproxyErrorFile

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        status = d.pop("status", UNSET)

        type_ = d.pop("type", UNSET)

        secondary = d.pop("secondary", UNSET)

        primary_frontend = d.pop("primary_frontend", UNSET)

        backend_serverpool = d.pop("backend_serverpool", UNSET)

        maxconn = d.pop("maxconn", UNSET)

        _bind_addresses = d.pop("bind_addresses", UNSET)
        bind_addresses: list[HaproxyBindAddress] | Unset = UNSET
        if _bind_addresses is not UNSET:
            bind_addresses = []
            for bind_addresses_item_data in _bind_addresses:
                bind_addresses_item = HaproxyBindAddress.from_dict(bind_addresses_item_data)

                bind_addresses.append(bind_addresses_item)

        forwardfor = d.pop("forwardfor", UNSET)

        httpclose = d.pop("httpclose", UNSET)

        dontlognull = d.pop("dontlognull", UNSET)

        dontlog_normal = d.pop("dontlog_normal", UNSET)

        log_separate_errors = d.pop("log_separate_errors", UNSET)

        log_detailed = d.pop("log_detailed", UNSET)

        socket_stats = d.pop("socket_stats", UNSET)

        client_timeout = d.pop("client_timeout", UNSET)

        ssloffload = d.pop("ssloffload", UNSET)

        ssloffloadcert = d.pop("ssloffloadcert", UNSET)

        sslsnifilter = d.pop("sslsnifilter", UNSET)

        ssl_crtlist_advanced = d.pop("ssl_crtlist_advanced", UNSET)

        dcertadv = d.pop("dcertadv", UNSET)

        ssloffloadacl = d.pop("ssloffloadacl", UNSET)

        ssloffloadacl_an = d.pop("ssloffloadacl_an", UNSET)

        ssloffloadacladditional = d.pop("ssloffloadacladditional", UNSET)

        ssloffloadacladditional_an = d.pop("ssloffloadacladditional_an", UNSET)

        sslclientcert_none = d.pop("sslclientcert_none", UNSET)

        sslclientcert_invalid = d.pop("sslclientcert_invalid", UNSET)

        sslocsp = d.pop("sslocsp", UNSET)

        _ha_certificates = d.pop("ha_certificates", UNSET)
        ha_certificates: list[HaproxyCertificate] | Unset = UNSET
        if _ha_certificates is not UNSET:
            ha_certificates = []
            for ha_certificates_item_data in _ha_certificates:
                ha_certificates_item = HaproxyCertificate.from_dict(ha_certificates_item_data)

                ha_certificates.append(ha_certificates_item)

        _clientcert_ca = d.pop("clientcert_ca", UNSET)
        clientcert_ca: list[HaproxyClientCa] | Unset = UNSET
        if _clientcert_ca is not UNSET:
            clientcert_ca = []
            for clientcert_ca_item_data in _clientcert_ca:
                clientcert_ca_item = HaproxyClientCa.from_dict(clientcert_ca_item_data)

                clientcert_ca.append(clientcert_ca_item)

        _clientcert_crl = d.pop("clientcert_crl", UNSET)
        clientcert_crl: list[HaproxyClientCrl] | Unset = UNSET
        if _clientcert_crl is not UNSET:
            clientcert_crl = []
            for clientcert_crl_item_data in _clientcert_crl:
                clientcert_crl_item = HaproxyClientCrl.from_dict(clientcert_crl_item_data)

                clientcert_crl.append(clientcert_crl_item)

        _ha_acls = d.pop("ha_acls", UNSET)
        ha_acls: list[HaproxyAcl] | Unset = UNSET
        if _ha_acls is not UNSET:
            ha_acls = []
            for ha_acls_item_data in _ha_acls:
                ha_acls_item = HaproxyAcl.from_dict(ha_acls_item_data)

                ha_acls.append(ha_acls_item)

        _a_actionitems = d.pop("a_actionitems", UNSET)
        a_actionitems: list[HaproxyAction] | Unset = UNSET
        if _a_actionitems is not UNSET:
            a_actionitems = []
            for a_actionitems_item_data in _a_actionitems:
                a_actionitems_item = HaproxyAction.from_dict(a_actionitems_item_data)

                a_actionitems.append(a_actionitems_item)

        _a_errorfiles = d.pop("a_errorfiles", UNSET)
        a_errorfiles: list[HaproxyErrorFile] | Unset = UNSET
        if _a_errorfiles is not UNSET:
            a_errorfiles = []
            for a_errorfiles_item_data in _a_errorfiles:
                a_errorfiles_item = HaproxyErrorFile.from_dict(a_errorfiles_item_data)

                a_errorfiles.append(a_errorfiles_item)

        advanced_bind = d.pop("advanced_bind", UNSET)

        advanced = d.pop("advanced", UNSET)

        id = d.pop("id", UNSET)

        haproxy_frontend = cls(
            name=name,
            descr=descr,
            status=status,
            type_=type_,
            secondary=secondary,
            primary_frontend=primary_frontend,
            backend_serverpool=backend_serverpool,
            maxconn=maxconn,
            bind_addresses=bind_addresses,
            forwardfor=forwardfor,
            httpclose=httpclose,
            dontlognull=dontlognull,
            dontlog_normal=dontlog_normal,
            log_separate_errors=log_separate_errors,
            log_detailed=log_detailed,
            socket_stats=socket_stats,
            client_timeout=client_timeout,
            ssloffload=ssloffload,
            ssloffloadcert=ssloffloadcert,
            sslsnifilter=sslsnifilter,
            ssl_crtlist_advanced=ssl_crtlist_advanced,
            dcertadv=dcertadv,
            ssloffloadacl=ssloffloadacl,
            ssloffloadacl_an=ssloffloadacl_an,
            ssloffloadacladditional=ssloffloadacladditional,
            ssloffloadacladditional_an=ssloffloadacladditional_an,
            sslclientcert_none=sslclientcert_none,
            sslclientcert_invalid=sslclientcert_invalid,
            sslocsp=sslocsp,
            ha_certificates=ha_certificates,
            clientcert_ca=clientcert_ca,
            clientcert_crl=clientcert_crl,
            ha_acls=ha_acls,
            a_actionitems=a_actionitems,
            a_errorfiles=a_errorfiles,
            advanced_bind=advanced_bind,
            advanced=advanced,
            id=id,
        )

        haproxy_frontend.additional_properties = d
        return haproxy_frontend

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
