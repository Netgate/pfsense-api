from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNClientConfig")


@_attrs_define
class OpenVPNClientConfig:
    """
    Attributes:
        vpnid (Union[Unset, str]): generated by system when create openvpn server
        disable (Union[Unset, bool]):
        dco (Union[Unset, bool]):
        protocol (Union[Unset, str]):
        dev_mode (Union[Unset, str]):
        interface (Union[Unset, str]):
        ipaddr (Union[Unset, str]):
        local_port (Union[Unset, int]):
        server_addr (Union[Unset, str]):
        server_port (Union[Unset, str]):
        proxy_addr (Union[Unset, str]):
        proxy_port (Union[Unset, str]):
        proxy_authtype (Union[Unset, str]):
        description (Union[Unset, str]):
        mode (Union[Unset, str]):
        topology (Union[Unset, str]):
        custom_options (Union[Unset, str]):
        caref (Union[Unset, str]):
        certref (Union[Unset, str]):
        crlref (Union[Unset, str]):
        tlsauth_enable (Union[Unset, bool]):
        autokey_enable (Union[Unset, bool]):
        autotls_enable (Union[Unset, bool]):
        tls (Union[Unset, str]):
        tls_type (Union[Unset, str]):
        tlsauth_keydir (Union[Unset, str]):
        remote_cert_tls (Union[Unset, bool]):
        shared_key (Union[Unset, str]):
        digest (Union[Unset, str]):
        tunnel_network (Union[Unset, str]):
        tunnel_networkv6 (Union[Unset, str]):
        remote_network (Union[Unset, str]):
        remote_networkv6 (Union[Unset, str]):
        use_shaper (Union[Unset, str]):
        allow_compression (Union[Unset, str]): "asym", "yes", "no"
        compression (Union[Unset, str]):
        auth_retry_none (Union[Unset, bool]):
        passtos (Union[Unset, bool]):
        udp_fast_io (Union[Unset, bool]):
        exit_notify (Union[Unset, str]):
        sndrcvbuf (Union[Unset, str]):
        route_no_pull (Union[Unset, bool]):
        route_no_exec (Union[Unset, bool]):
        dns_add (Union[Unset, bool]):
        verbosity_level (Union[Unset, str]):
        create_gw (Union[Unset, str]):
        dh_length (Union[Unset, str]):
        data_ciphers (Union[Unset, List[str]]):
        data_ciphers_fallback (Union[Unset, str]):
        ping_method (Union[Unset, str]):
        keepalive_interval (Union[Unset, str]):
        keepalive_timeout (Union[Unset, str]):
        ping_seconds (Union[Unset, str]):
        ping_action (Union[Unset, str]):
        ping_action_seconds (Union[Unset, str]):
        inactive_seconds (Union[Unset, str]):
    """

    vpnid: Union[Unset, str] = UNSET
    disable: Union[Unset, bool] = UNSET
    dco: Union[Unset, bool] = UNSET
    protocol: Union[Unset, str] = UNSET
    dev_mode: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    ipaddr: Union[Unset, str] = UNSET
    local_port: Union[Unset, int] = UNSET
    server_addr: Union[Unset, str] = UNSET
    server_port: Union[Unset, str] = UNSET
    proxy_addr: Union[Unset, str] = UNSET
    proxy_port: Union[Unset, str] = UNSET
    proxy_authtype: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    topology: Union[Unset, str] = UNSET
    custom_options: Union[Unset, str] = UNSET
    caref: Union[Unset, str] = UNSET
    certref: Union[Unset, str] = UNSET
    crlref: Union[Unset, str] = UNSET
    tlsauth_enable: Union[Unset, bool] = UNSET
    autokey_enable: Union[Unset, bool] = UNSET
    autotls_enable: Union[Unset, bool] = UNSET
    tls: Union[Unset, str] = UNSET
    tls_type: Union[Unset, str] = UNSET
    tlsauth_keydir: Union[Unset, str] = UNSET
    remote_cert_tls: Union[Unset, bool] = UNSET
    shared_key: Union[Unset, str] = UNSET
    digest: Union[Unset, str] = UNSET
    tunnel_network: Union[Unset, str] = UNSET
    tunnel_networkv6: Union[Unset, str] = UNSET
    remote_network: Union[Unset, str] = UNSET
    remote_networkv6: Union[Unset, str] = UNSET
    use_shaper: Union[Unset, str] = UNSET
    allow_compression: Union[Unset, str] = UNSET
    compression: Union[Unset, str] = UNSET
    auth_retry_none: Union[Unset, bool] = UNSET
    passtos: Union[Unset, bool] = UNSET
    udp_fast_io: Union[Unset, bool] = UNSET
    exit_notify: Union[Unset, str] = UNSET
    sndrcvbuf: Union[Unset, str] = UNSET
    route_no_pull: Union[Unset, bool] = UNSET
    route_no_exec: Union[Unset, bool] = UNSET
    dns_add: Union[Unset, bool] = UNSET
    verbosity_level: Union[Unset, str] = UNSET
    create_gw: Union[Unset, str] = UNSET
    dh_length: Union[Unset, str] = UNSET
    data_ciphers: Union[Unset, List[str]] = UNSET
    data_ciphers_fallback: Union[Unset, str] = UNSET
    ping_method: Union[Unset, str] = UNSET
    keepalive_interval: Union[Unset, str] = UNSET
    keepalive_timeout: Union[Unset, str] = UNSET
    ping_seconds: Union[Unset, str] = UNSET
    ping_action: Union[Unset, str] = UNSET
    ping_action_seconds: Union[Unset, str] = UNSET
    inactive_seconds: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vpnid = self.vpnid

        disable = self.disable

        dco = self.dco

        protocol = self.protocol

        dev_mode = self.dev_mode

        interface = self.interface

        ipaddr = self.ipaddr

        local_port = self.local_port

        server_addr = self.server_addr

        server_port = self.server_port

        proxy_addr = self.proxy_addr

        proxy_port = self.proxy_port

        proxy_authtype = self.proxy_authtype

        description = self.description

        mode = self.mode

        topology = self.topology

        custom_options = self.custom_options

        caref = self.caref

        certref = self.certref

        crlref = self.crlref

        tlsauth_enable = self.tlsauth_enable

        autokey_enable = self.autokey_enable

        autotls_enable = self.autotls_enable

        tls = self.tls

        tls_type = self.tls_type

        tlsauth_keydir = self.tlsauth_keydir

        remote_cert_tls = self.remote_cert_tls

        shared_key = self.shared_key

        digest = self.digest

        tunnel_network = self.tunnel_network

        tunnel_networkv6 = self.tunnel_networkv6

        remote_network = self.remote_network

        remote_networkv6 = self.remote_networkv6

        use_shaper = self.use_shaper

        allow_compression = self.allow_compression

        compression = self.compression

        auth_retry_none = self.auth_retry_none

        passtos = self.passtos

        udp_fast_io = self.udp_fast_io

        exit_notify = self.exit_notify

        sndrcvbuf = self.sndrcvbuf

        route_no_pull = self.route_no_pull

        route_no_exec = self.route_no_exec

        dns_add = self.dns_add

        verbosity_level = self.verbosity_level

        create_gw = self.create_gw

        dh_length = self.dh_length

        data_ciphers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_ciphers, Unset):
            data_ciphers = self.data_ciphers

        data_ciphers_fallback = self.data_ciphers_fallback

        ping_method = self.ping_method

        keepalive_interval = self.keepalive_interval

        keepalive_timeout = self.keepalive_timeout

        ping_seconds = self.ping_seconds

        ping_action = self.ping_action

        ping_action_seconds = self.ping_action_seconds

        inactive_seconds = self.inactive_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpnid is not UNSET:
            field_dict["vpnid"] = vpnid
        if disable is not UNSET:
            field_dict["disable"] = disable
        if dco is not UNSET:
            field_dict["dco"] = dco
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if dev_mode is not UNSET:
            field_dict["dev_mode"] = dev_mode
        if interface is not UNSET:
            field_dict["interface"] = interface
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
        if local_port is not UNSET:
            field_dict["local_port"] = local_port
        if server_addr is not UNSET:
            field_dict["server_addr"] = server_addr
        if server_port is not UNSET:
            field_dict["server_port"] = server_port
        if proxy_addr is not UNSET:
            field_dict["proxy_addr"] = proxy_addr
        if proxy_port is not UNSET:
            field_dict["proxy_port"] = proxy_port
        if proxy_authtype is not UNSET:
            field_dict["proxy_authtype"] = proxy_authtype
        if description is not UNSET:
            field_dict["description"] = description
        if mode is not UNSET:
            field_dict["mode"] = mode
        if topology is not UNSET:
            field_dict["topology"] = topology
        if custom_options is not UNSET:
            field_dict["custom_options"] = custom_options
        if caref is not UNSET:
            field_dict["caref"] = caref
        if certref is not UNSET:
            field_dict["certref"] = certref
        if crlref is not UNSET:
            field_dict["crlref"] = crlref
        if tlsauth_enable is not UNSET:
            field_dict["tlsauth_enable"] = tlsauth_enable
        if autokey_enable is not UNSET:
            field_dict["autokey_enable"] = autokey_enable
        if autotls_enable is not UNSET:
            field_dict["autotls_enable"] = autotls_enable
        if tls is not UNSET:
            field_dict["tls"] = tls
        if tls_type is not UNSET:
            field_dict["tls_type"] = tls_type
        if tlsauth_keydir is not UNSET:
            field_dict["tlsauth_keydir"] = tlsauth_keydir
        if remote_cert_tls is not UNSET:
            field_dict["remote_cert_tls"] = remote_cert_tls
        if shared_key is not UNSET:
            field_dict["shared_key"] = shared_key
        if digest is not UNSET:
            field_dict["digest"] = digest
        if tunnel_network is not UNSET:
            field_dict["tunnel_network"] = tunnel_network
        if tunnel_networkv6 is not UNSET:
            field_dict["tunnel_networkv6"] = tunnel_networkv6
        if remote_network is not UNSET:
            field_dict["remote_network"] = remote_network
        if remote_networkv6 is not UNSET:
            field_dict["remote_networkv6"] = remote_networkv6
        if use_shaper is not UNSET:
            field_dict["use_shaper"] = use_shaper
        if allow_compression is not UNSET:
            field_dict["allow_compression"] = allow_compression
        if compression is not UNSET:
            field_dict["compression"] = compression
        if auth_retry_none is not UNSET:
            field_dict["auth-retry-none"] = auth_retry_none
        if passtos is not UNSET:
            field_dict["passtos"] = passtos
        if udp_fast_io is not UNSET:
            field_dict["udp_fast_io"] = udp_fast_io
        if exit_notify is not UNSET:
            field_dict["exit_notify"] = exit_notify
        if sndrcvbuf is not UNSET:
            field_dict["sndrcvbuf"] = sndrcvbuf
        if route_no_pull is not UNSET:
            field_dict["route_no_pull"] = route_no_pull
        if route_no_exec is not UNSET:
            field_dict["route_no_exec"] = route_no_exec
        if dns_add is not UNSET:
            field_dict["dns_add"] = dns_add
        if verbosity_level is not UNSET:
            field_dict["verbosity_level"] = verbosity_level
        if create_gw is not UNSET:
            field_dict["create_gw"] = create_gw
        if dh_length is not UNSET:
            field_dict["dh_length"] = dh_length
        if data_ciphers is not UNSET:
            field_dict["data_ciphers"] = data_ciphers
        if data_ciphers_fallback is not UNSET:
            field_dict["data_ciphers_fallback"] = data_ciphers_fallback
        if ping_method is not UNSET:
            field_dict["ping_method"] = ping_method
        if keepalive_interval is not UNSET:
            field_dict["keepalive_interval"] = keepalive_interval
        if keepalive_timeout is not UNSET:
            field_dict["keepalive_timeout"] = keepalive_timeout
        if ping_seconds is not UNSET:
            field_dict["ping_seconds"] = ping_seconds
        if ping_action is not UNSET:
            field_dict["ping_action"] = ping_action
        if ping_action_seconds is not UNSET:
            field_dict["ping_action_seconds"] = ping_action_seconds
        if inactive_seconds is not UNSET:
            field_dict["inactive_seconds"] = inactive_seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vpnid = d.pop("vpnid", UNSET)

        disable = d.pop("disable", UNSET)

        dco = d.pop("dco", UNSET)

        protocol = d.pop("protocol", UNSET)

        dev_mode = d.pop("dev_mode", UNSET)

        interface = d.pop("interface", UNSET)

        ipaddr = d.pop("ipaddr", UNSET)

        local_port = d.pop("local_port", UNSET)

        server_addr = d.pop("server_addr", UNSET)

        server_port = d.pop("server_port", UNSET)

        proxy_addr = d.pop("proxy_addr", UNSET)

        proxy_port = d.pop("proxy_port", UNSET)

        proxy_authtype = d.pop("proxy_authtype", UNSET)

        description = d.pop("description", UNSET)

        mode = d.pop("mode", UNSET)

        topology = d.pop("topology", UNSET)

        custom_options = d.pop("custom_options", UNSET)

        caref = d.pop("caref", UNSET)

        certref = d.pop("certref", UNSET)

        crlref = d.pop("crlref", UNSET)

        tlsauth_enable = d.pop("tlsauth_enable", UNSET)

        autokey_enable = d.pop("autokey_enable", UNSET)

        autotls_enable = d.pop("autotls_enable", UNSET)

        tls = d.pop("tls", UNSET)

        tls_type = d.pop("tls_type", UNSET)

        tlsauth_keydir = d.pop("tlsauth_keydir", UNSET)

        remote_cert_tls = d.pop("remote_cert_tls", UNSET)

        shared_key = d.pop("shared_key", UNSET)

        digest = d.pop("digest", UNSET)

        tunnel_network = d.pop("tunnel_network", UNSET)

        tunnel_networkv6 = d.pop("tunnel_networkv6", UNSET)

        remote_network = d.pop("remote_network", UNSET)

        remote_networkv6 = d.pop("remote_networkv6", UNSET)

        use_shaper = d.pop("use_shaper", UNSET)

        allow_compression = d.pop("allow_compression", UNSET)

        compression = d.pop("compression", UNSET)

        auth_retry_none = d.pop("auth-retry-none", UNSET)

        passtos = d.pop("passtos", UNSET)

        udp_fast_io = d.pop("udp_fast_io", UNSET)

        exit_notify = d.pop("exit_notify", UNSET)

        sndrcvbuf = d.pop("sndrcvbuf", UNSET)

        route_no_pull = d.pop("route_no_pull", UNSET)

        route_no_exec = d.pop("route_no_exec", UNSET)

        dns_add = d.pop("dns_add", UNSET)

        verbosity_level = d.pop("verbosity_level", UNSET)

        create_gw = d.pop("create_gw", UNSET)

        dh_length = d.pop("dh_length", UNSET)

        data_ciphers = cast(List[str], d.pop("data_ciphers", UNSET))

        data_ciphers_fallback = d.pop("data_ciphers_fallback", UNSET)

        ping_method = d.pop("ping_method", UNSET)

        keepalive_interval = d.pop("keepalive_interval", UNSET)

        keepalive_timeout = d.pop("keepalive_timeout", UNSET)

        ping_seconds = d.pop("ping_seconds", UNSET)

        ping_action = d.pop("ping_action", UNSET)

        ping_action_seconds = d.pop("ping_action_seconds", UNSET)

        inactive_seconds = d.pop("inactive_seconds", UNSET)

        open_vpn_client_config = cls(
            vpnid=vpnid,
            disable=disable,
            dco=dco,
            protocol=protocol,
            dev_mode=dev_mode,
            interface=interface,
            ipaddr=ipaddr,
            local_port=local_port,
            server_addr=server_addr,
            server_port=server_port,
            proxy_addr=proxy_addr,
            proxy_port=proxy_port,
            proxy_authtype=proxy_authtype,
            description=description,
            mode=mode,
            topology=topology,
            custom_options=custom_options,
            caref=caref,
            certref=certref,
            crlref=crlref,
            tlsauth_enable=tlsauth_enable,
            autokey_enable=autokey_enable,
            autotls_enable=autotls_enable,
            tls=tls,
            tls_type=tls_type,
            tlsauth_keydir=tlsauth_keydir,
            remote_cert_tls=remote_cert_tls,
            shared_key=shared_key,
            digest=digest,
            tunnel_network=tunnel_network,
            tunnel_networkv6=tunnel_networkv6,
            remote_network=remote_network,
            remote_networkv6=remote_networkv6,
            use_shaper=use_shaper,
            allow_compression=allow_compression,
            compression=compression,
            auth_retry_none=auth_retry_none,
            passtos=passtos,
            udp_fast_io=udp_fast_io,
            exit_notify=exit_notify,
            sndrcvbuf=sndrcvbuf,
            route_no_pull=route_no_pull,
            route_no_exec=route_no_exec,
            dns_add=dns_add,
            verbosity_level=verbosity_level,
            create_gw=create_gw,
            dh_length=dh_length,
            data_ciphers=data_ciphers,
            data_ciphers_fallback=data_ciphers_fallback,
            ping_method=ping_method,
            keepalive_interval=keepalive_interval,
            keepalive_timeout=keepalive_timeout,
            ping_seconds=ping_seconds,
            ping_action=ping_action,
            ping_action_seconds=ping_action_seconds,
            inactive_seconds=inactive_seconds,
        )

        open_vpn_client_config.additional_properties = d
        return open_vpn_client_config

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
