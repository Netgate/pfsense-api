from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNClientConfig")


@_attrs_define
class OpenVPNClientConfig:
    """
    Attributes:
        vpnid (str):
        disable (bool):
        dco (bool):
        protocol (str):
        dev_mode (str):
        interface (str):
        ipaddr (str):
        local_port (int):
        server_addr (str):
        server_port (str):
        proxy_addr (str):
        proxy_port (str):
        proxy_authtype (str):
        description (str):
        mode (str):
        topology (str):
        custom_options (str):
        caref (str):
        certref (str):
        crlref (str):
        tlsauth_enable (bool):
        autokey_enable (bool):
        autotls_enable (bool):
        tls (str):
        tls_type (str):
        tlsauth_keydir (str):
        remote_cert_tls (bool):
        shared_key (str):
        digest (str):
        tunnel_network (str):
        tunnel_networkv6 (str):
        remote_network (str):
        remote_networkv6 (str):
        use_shaper (str):
        allow_compression (str):
        compression (str):
        auth_retry_none (bool):
        passtos (bool):
        udp_fast_io (bool):
        exit_notify (str):
        sndrcvbuf (str):
        route_no_pull (bool):
        route_no_exec (bool):
        dns_add (bool):
        verbosity_level (str):
        create_gw (str):
        dh_length (str):
        data_ciphers_fallback (str):
        ping_method (str):
        keepalive_interval (str):
        keepalive_timeout (str):
        ping_seconds (str):
        ping_action (str):
        ping_action_seconds (str):
        inactive_seconds (str):
        data_ciphers (Union[Unset, List[str]]):
    """

    vpnid: str
    disable: bool
    dco: bool
    protocol: str
    dev_mode: str
    interface: str
    ipaddr: str
    local_port: int
    server_addr: str
    server_port: str
    proxy_addr: str
    proxy_port: str
    proxy_authtype: str
    description: str
    mode: str
    topology: str
    custom_options: str
    caref: str
    certref: str
    crlref: str
    tlsauth_enable: bool
    autokey_enable: bool
    autotls_enable: bool
    tls: str
    tls_type: str
    tlsauth_keydir: str
    remote_cert_tls: bool
    shared_key: str
    digest: str
    tunnel_network: str
    tunnel_networkv6: str
    remote_network: str
    remote_networkv6: str
    use_shaper: str
    allow_compression: str
    compression: str
    auth_retry_none: bool
    passtos: bool
    udp_fast_io: bool
    exit_notify: str
    sndrcvbuf: str
    route_no_pull: bool
    route_no_exec: bool
    dns_add: bool
    verbosity_level: str
    create_gw: str
    dh_length: str
    data_ciphers_fallback: str
    ping_method: str
    keepalive_interval: str
    keepalive_timeout: str
    ping_seconds: str
    ping_action: str
    ping_action_seconds: str
    inactive_seconds: str
    data_ciphers: Union[Unset, List[str]] = UNSET
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

        data_ciphers_fallback = self.data_ciphers_fallback

        ping_method = self.ping_method

        keepalive_interval = self.keepalive_interval

        keepalive_timeout = self.keepalive_timeout

        ping_seconds = self.ping_seconds

        ping_action = self.ping_action

        ping_action_seconds = self.ping_action_seconds

        inactive_seconds = self.inactive_seconds

        data_ciphers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_ciphers, Unset):
            data_ciphers = self.data_ciphers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vpnid": vpnid,
                "disable": disable,
                "dco": dco,
                "protocol": protocol,
                "dev_mode": dev_mode,
                "interface": interface,
                "ipaddr": ipaddr,
                "local_port": local_port,
                "server_addr": server_addr,
                "server_port": server_port,
                "proxy_addr": proxy_addr,
                "proxy_port": proxy_port,
                "proxy_authtype": proxy_authtype,
                "description": description,
                "mode": mode,
                "topology": topology,
                "custom_options": custom_options,
                "caref": caref,
                "certref": certref,
                "crlref": crlref,
                "tlsauth_enable": tlsauth_enable,
                "autokey_enable": autokey_enable,
                "autotls_enable": autotls_enable,
                "tls": tls,
                "tls_type": tls_type,
                "tlsauth_keydir": tlsauth_keydir,
                "remote_cert_tls": remote_cert_tls,
                "shared_key": shared_key,
                "digest": digest,
                "tunnel_network": tunnel_network,
                "tunnel_networkv6": tunnel_networkv6,
                "remote_network": remote_network,
                "remote_networkv6": remote_networkv6,
                "use_shaper": use_shaper,
                "allow_compression": allow_compression,
                "compression": compression,
                "auth-retry-none": auth_retry_none,
                "passtos": passtos,
                "udp_fast_io": udp_fast_io,
                "exit_notify": exit_notify,
                "sndrcvbuf": sndrcvbuf,
                "route_no_pull": route_no_pull,
                "route_no_exec": route_no_exec,
                "dns_add": dns_add,
                "verbosity_level": verbosity_level,
                "create_gw": create_gw,
                "dh_length": dh_length,
                "data_ciphers_fallback": data_ciphers_fallback,
                "ping_method": ping_method,
                "keepalive_interval": keepalive_interval,
                "keepalive_timeout": keepalive_timeout,
                "ping_seconds": ping_seconds,
                "ping_action": ping_action,
                "ping_action_seconds": ping_action_seconds,
                "inactive_seconds": inactive_seconds,
            }
        )
        if data_ciphers is not UNSET:
            field_dict["data_ciphers"] = data_ciphers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vpnid = d.pop("vpnid")

        disable = d.pop("disable")

        dco = d.pop("dco")

        protocol = d.pop("protocol")

        dev_mode = d.pop("dev_mode")

        interface = d.pop("interface")

        ipaddr = d.pop("ipaddr")

        local_port = d.pop("local_port")

        server_addr = d.pop("server_addr")

        server_port = d.pop("server_port")

        proxy_addr = d.pop("proxy_addr")

        proxy_port = d.pop("proxy_port")

        proxy_authtype = d.pop("proxy_authtype")

        description = d.pop("description")

        mode = d.pop("mode")

        topology = d.pop("topology")

        custom_options = d.pop("custom_options")

        caref = d.pop("caref")

        certref = d.pop("certref")

        crlref = d.pop("crlref")

        tlsauth_enable = d.pop("tlsauth_enable")

        autokey_enable = d.pop("autokey_enable")

        autotls_enable = d.pop("autotls_enable")

        tls = d.pop("tls")

        tls_type = d.pop("tls_type")

        tlsauth_keydir = d.pop("tlsauth_keydir")

        remote_cert_tls = d.pop("remote_cert_tls")

        shared_key = d.pop("shared_key")

        digest = d.pop("digest")

        tunnel_network = d.pop("tunnel_network")

        tunnel_networkv6 = d.pop("tunnel_networkv6")

        remote_network = d.pop("remote_network")

        remote_networkv6 = d.pop("remote_networkv6")

        use_shaper = d.pop("use_shaper")

        allow_compression = d.pop("allow_compression")

        compression = d.pop("compression")

        auth_retry_none = d.pop("auth-retry-none")

        passtos = d.pop("passtos")

        udp_fast_io = d.pop("udp_fast_io")

        exit_notify = d.pop("exit_notify")

        sndrcvbuf = d.pop("sndrcvbuf")

        route_no_pull = d.pop("route_no_pull")

        route_no_exec = d.pop("route_no_exec")

        dns_add = d.pop("dns_add")

        verbosity_level = d.pop("verbosity_level")

        create_gw = d.pop("create_gw")

        dh_length = d.pop("dh_length")

        data_ciphers_fallback = d.pop("data_ciphers_fallback")

        ping_method = d.pop("ping_method")

        keepalive_interval = d.pop("keepalive_interval")

        keepalive_timeout = d.pop("keepalive_timeout")

        ping_seconds = d.pop("ping_seconds")

        ping_action = d.pop("ping_action")

        ping_action_seconds = d.pop("ping_action_seconds")

        inactive_seconds = d.pop("inactive_seconds")

        data_ciphers = cast(List[str], d.pop("data_ciphers", UNSET))

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
            data_ciphers_fallback=data_ciphers_fallback,
            ping_method=ping_method,
            keepalive_interval=keepalive_interval,
            keepalive_timeout=keepalive_timeout,
            ping_seconds=ping_seconds,
            ping_action=ping_action,
            ping_action_seconds=ping_action_seconds,
            inactive_seconds=inactive_seconds,
            data_ciphers=data_ciphers,
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
