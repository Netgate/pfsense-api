from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNServerConfig")


@_attrs_define
class OpenVPNServerConfig:
    """
    Attributes:
        vpnid (str):
        dco (bool):
        mode (str):
        protocol (str):
        dev_mode (str):
        interface (str):
        local_port (int):
        description (str):
        tls (str):
        tls_type (str):
        certref (str):
        caref (str):
        dh_length (str):
        data_ciphers_fallback (str):
        digest (str):
        engine (str):
        tunnel_network (str):
        local_network (str):
        maxclients (str):
        allow_compression (str):
        dynamic_ip (bool):
        topology (str):
        dns_domain (str):
        exit_notify (str):
        inactive_seconds (str):
        disable (bool):
        tlsauth_enable (bool):
        autotls_enable (bool):
        tlsauth_keydir (str):
        ocspcheck (bool):
        ocspurl (str):
        ecdh_curve (str):
        autokey_enable (bool):
        shared_key (str):
        cert_depth (str):
        remote_cert_tls (bool):
        tunnel_networkv6 (str):
        serverbridge_dhcp (str):
        serverbridge_interface (str):
        serverbridge_routegateway (str):
        serverbridge_dhcp_start (str):
        serverbridge_dhcp_end (str):
        gwredir (bool):
        gwredir6 (bool):
        local_networkv6 (str):
        remote_network (str):
        remote_networkv6 (str):
        compression (str):
        compression_push (bool):
        passtos (bool):
        client2client (bool):
        duplicate_cn (bool):
        ping_method (str):
        keepalive_interval (str):
        keepalive_timeout (str):
        ping_seconds (str):
        ping_push (bool):
        ping_action (str):
        ping_action_seconds (str):
        ping_action_push (bool):
        dns_domain_enable (bool):
        dns_server_enable (bool):
        dns_server1 (str):
        dns_server2 (str):
        dns_server3 (str):
        dns_server4 (str):
        push_blockoutsidedns (bool):
        push_register_dns (bool):
        ntp_server_enable (bool):
        ntp_server1 (str):
        ntp_server2 (str):
        netbios_enable (bool):
        netbios_ntype (str):
        netbios_scope (str):
        wins_server_enable (bool):
        wins_server1 (str):
        wins_server2 (str):
        custom_options (str):
        username_as_common_name (bool):
        udp_fast_io (bool):
        sndrcvbuf (str):
        create_gw (str):
        verbosity_level (str):
        strictusercn (bool):
        authmode (Union[Unset, List[str]]):
        data_ciphers (Union[Unset, List[str]]):
    """

    vpnid: str
    dco: bool
    mode: str
    protocol: str
    dev_mode: str
    interface: str
    local_port: int
    description: str
    tls: str
    tls_type: str
    certref: str
    caref: str
    dh_length: str
    data_ciphers_fallback: str
    digest: str
    engine: str
    tunnel_network: str
    local_network: str
    maxclients: str
    allow_compression: str
    dynamic_ip: bool
    topology: str
    dns_domain: str
    exit_notify: str
    inactive_seconds: str
    disable: bool
    tlsauth_enable: bool
    autotls_enable: bool
    tlsauth_keydir: str
    ocspcheck: bool
    ocspurl: str
    ecdh_curve: str
    autokey_enable: bool
    shared_key: str
    cert_depth: str
    remote_cert_tls: bool
    tunnel_networkv6: str
    serverbridge_dhcp: str
    serverbridge_interface: str
    serverbridge_routegateway: str
    serverbridge_dhcp_start: str
    serverbridge_dhcp_end: str
    gwredir: bool
    gwredir6: bool
    local_networkv6: str
    remote_network: str
    remote_networkv6: str
    compression: str
    compression_push: bool
    passtos: bool
    client2client: bool
    duplicate_cn: bool
    ping_method: str
    keepalive_interval: str
    keepalive_timeout: str
    ping_seconds: str
    ping_push: bool
    ping_action: str
    ping_action_seconds: str
    ping_action_push: bool
    dns_domain_enable: bool
    dns_server_enable: bool
    dns_server1: str
    dns_server2: str
    dns_server3: str
    dns_server4: str
    push_blockoutsidedns: bool
    push_register_dns: bool
    ntp_server_enable: bool
    ntp_server1: str
    ntp_server2: str
    netbios_enable: bool
    netbios_ntype: str
    netbios_scope: str
    wins_server_enable: bool
    wins_server1: str
    wins_server2: str
    custom_options: str
    username_as_common_name: bool
    udp_fast_io: bool
    sndrcvbuf: str
    create_gw: str
    verbosity_level: str
    strictusercn: bool
    authmode: Union[Unset, List[str]] = UNSET
    data_ciphers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vpnid = self.vpnid

        dco = self.dco

        mode = self.mode

        protocol = self.protocol

        dev_mode = self.dev_mode

        interface = self.interface

        local_port = self.local_port

        description = self.description

        tls = self.tls

        tls_type = self.tls_type

        certref = self.certref

        caref = self.caref

        dh_length = self.dh_length

        data_ciphers_fallback = self.data_ciphers_fallback

        digest = self.digest

        engine = self.engine

        tunnel_network = self.tunnel_network

        local_network = self.local_network

        maxclients = self.maxclients

        allow_compression = self.allow_compression

        dynamic_ip = self.dynamic_ip

        topology = self.topology

        dns_domain = self.dns_domain

        exit_notify = self.exit_notify

        inactive_seconds = self.inactive_seconds

        disable = self.disable

        tlsauth_enable = self.tlsauth_enable

        autotls_enable = self.autotls_enable

        tlsauth_keydir = self.tlsauth_keydir

        ocspcheck = self.ocspcheck

        ocspurl = self.ocspurl

        ecdh_curve = self.ecdh_curve

        autokey_enable = self.autokey_enable

        shared_key = self.shared_key

        cert_depth = self.cert_depth

        remote_cert_tls = self.remote_cert_tls

        tunnel_networkv6 = self.tunnel_networkv6

        serverbridge_dhcp = self.serverbridge_dhcp

        serverbridge_interface = self.serverbridge_interface

        serverbridge_routegateway = self.serverbridge_routegateway

        serverbridge_dhcp_start = self.serverbridge_dhcp_start

        serverbridge_dhcp_end = self.serverbridge_dhcp_end

        gwredir = self.gwredir

        gwredir6 = self.gwredir6

        local_networkv6 = self.local_networkv6

        remote_network = self.remote_network

        remote_networkv6 = self.remote_networkv6

        compression = self.compression

        compression_push = self.compression_push

        passtos = self.passtos

        client2client = self.client2client

        duplicate_cn = self.duplicate_cn

        ping_method = self.ping_method

        keepalive_interval = self.keepalive_interval

        keepalive_timeout = self.keepalive_timeout

        ping_seconds = self.ping_seconds

        ping_push = self.ping_push

        ping_action = self.ping_action

        ping_action_seconds = self.ping_action_seconds

        ping_action_push = self.ping_action_push

        dns_domain_enable = self.dns_domain_enable

        dns_server_enable = self.dns_server_enable

        dns_server1 = self.dns_server1

        dns_server2 = self.dns_server2

        dns_server3 = self.dns_server3

        dns_server4 = self.dns_server4

        push_blockoutsidedns = self.push_blockoutsidedns

        push_register_dns = self.push_register_dns

        ntp_server_enable = self.ntp_server_enable

        ntp_server1 = self.ntp_server1

        ntp_server2 = self.ntp_server2

        netbios_enable = self.netbios_enable

        netbios_ntype = self.netbios_ntype

        netbios_scope = self.netbios_scope

        wins_server_enable = self.wins_server_enable

        wins_server1 = self.wins_server1

        wins_server2 = self.wins_server2

        custom_options = self.custom_options

        username_as_common_name = self.username_as_common_name

        udp_fast_io = self.udp_fast_io

        sndrcvbuf = self.sndrcvbuf

        create_gw = self.create_gw

        verbosity_level = self.verbosity_level

        strictusercn = self.strictusercn

        authmode: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authmode, Unset):
            authmode = self.authmode

        data_ciphers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_ciphers, Unset):
            data_ciphers = self.data_ciphers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vpnid": vpnid,
                "dco": dco,
                "mode": mode,
                "protocol": protocol,
                "dev_mode": dev_mode,
                "interface": interface,
                "local_port": local_port,
                "description": description,
                "tls": tls,
                "tls_type": tls_type,
                "certref": certref,
                "caref": caref,
                "dh_length": dh_length,
                "data_ciphers_fallback": data_ciphers_fallback,
                "digest": digest,
                "engine": engine,
                "tunnel_network": tunnel_network,
                "local_network": local_network,
                "maxclients": maxclients,
                "allow_compression": allow_compression,
                "dynamic_ip": dynamic_ip,
                "topology": topology,
                "dns_domain": dns_domain,
                "exit_notify": exit_notify,
                "inactive_seconds": inactive_seconds,
                "disable": disable,
                "tlsauth_enable": tlsauth_enable,
                "autotls_enable": autotls_enable,
                "tlsauth_keydir": tlsauth_keydir,
                "ocspcheck": ocspcheck,
                "ocspurl": ocspurl,
                "ecdh_curve": ecdh_curve,
                "autokey_enable": autokey_enable,
                "shared_key": shared_key,
                "cert_depth": cert_depth,
                "remote_cert_tls": remote_cert_tls,
                "tunnel_networkv6": tunnel_networkv6,
                "serverbridge_dhcp": serverbridge_dhcp,
                "serverbridge_interface": serverbridge_interface,
                "serverbridge_routegateway": serverbridge_routegateway,
                "serverbridge_dhcp_start": serverbridge_dhcp_start,
                "serverbridge_dhcp_end": serverbridge_dhcp_end,
                "gwredir": gwredir,
                "gwredir6": gwredir6,
                "local_networkv6": local_networkv6,
                "remote_network": remote_network,
                "remote_networkv6": remote_networkv6,
                "compression": compression,
                "compression_push": compression_push,
                "passtos": passtos,
                "client2client": client2client,
                "duplicate_cn": duplicate_cn,
                "ping_method": ping_method,
                "keepalive_interval": keepalive_interval,
                "keepalive_timeout": keepalive_timeout,
                "ping_seconds": ping_seconds,
                "ping_push": ping_push,
                "ping_action": ping_action,
                "ping_action_seconds": ping_action_seconds,
                "ping_action_push": ping_action_push,
                "dns_domain_enable": dns_domain_enable,
                "dns_server_enable": dns_server_enable,
                "dns_server1": dns_server1,
                "dns_server2": dns_server2,
                "dns_server3": dns_server3,
                "dns_server4": dns_server4,
                "push_blockoutsidedns": push_blockoutsidedns,
                "push_register_dns": push_register_dns,
                "ntp_server_enable": ntp_server_enable,
                "ntp_server1": ntp_server1,
                "ntp_server2": ntp_server2,
                "netbios_enable": netbios_enable,
                "netbios_ntype": netbios_ntype,
                "netbios_scope": netbios_scope,
                "wins_server_enable": wins_server_enable,
                "wins_server1": wins_server1,
                "wins_server2": wins_server2,
                "custom_options": custom_options,
                "username_as_common_name": username_as_common_name,
                "udp_fast_io": udp_fast_io,
                "sndrcvbuf": sndrcvbuf,
                "create_gw": create_gw,
                "verbosity_level": verbosity_level,
                "strictusercn": strictusercn,
            }
        )
        if authmode is not UNSET:
            field_dict["authmode"] = authmode
        if data_ciphers is not UNSET:
            field_dict["data_ciphers"] = data_ciphers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vpnid = d.pop("vpnid")

        dco = d.pop("dco")

        mode = d.pop("mode")

        protocol = d.pop("protocol")

        dev_mode = d.pop("dev_mode")

        interface = d.pop("interface")

        local_port = d.pop("local_port")

        description = d.pop("description")

        tls = d.pop("tls")

        tls_type = d.pop("tls_type")

        certref = d.pop("certref")

        caref = d.pop("caref")

        dh_length = d.pop("dh_length")

        data_ciphers_fallback = d.pop("data_ciphers_fallback")

        digest = d.pop("digest")

        engine = d.pop("engine")

        tunnel_network = d.pop("tunnel_network")

        local_network = d.pop("local_network")

        maxclients = d.pop("maxclients")

        allow_compression = d.pop("allow_compression")

        dynamic_ip = d.pop("dynamic_ip")

        topology = d.pop("topology")

        dns_domain = d.pop("dns_domain")

        exit_notify = d.pop("exit_notify")

        inactive_seconds = d.pop("inactive_seconds")

        disable = d.pop("disable")

        tlsauth_enable = d.pop("tlsauth_enable")

        autotls_enable = d.pop("autotls_enable")

        tlsauth_keydir = d.pop("tlsauth_keydir")

        ocspcheck = d.pop("ocspcheck")

        ocspurl = d.pop("ocspurl")

        ecdh_curve = d.pop("ecdh_curve")

        autokey_enable = d.pop("autokey_enable")

        shared_key = d.pop("shared_key")

        cert_depth = d.pop("cert_depth")

        remote_cert_tls = d.pop("remote_cert_tls")

        tunnel_networkv6 = d.pop("tunnel_networkv6")

        serverbridge_dhcp = d.pop("serverbridge_dhcp")

        serverbridge_interface = d.pop("serverbridge_interface")

        serverbridge_routegateway = d.pop("serverbridge_routegateway")

        serverbridge_dhcp_start = d.pop("serverbridge_dhcp_start")

        serverbridge_dhcp_end = d.pop("serverbridge_dhcp_end")

        gwredir = d.pop("gwredir")

        gwredir6 = d.pop("gwredir6")

        local_networkv6 = d.pop("local_networkv6")

        remote_network = d.pop("remote_network")

        remote_networkv6 = d.pop("remote_networkv6")

        compression = d.pop("compression")

        compression_push = d.pop("compression_push")

        passtos = d.pop("passtos")

        client2client = d.pop("client2client")

        duplicate_cn = d.pop("duplicate_cn")

        ping_method = d.pop("ping_method")

        keepalive_interval = d.pop("keepalive_interval")

        keepalive_timeout = d.pop("keepalive_timeout")

        ping_seconds = d.pop("ping_seconds")

        ping_push = d.pop("ping_push")

        ping_action = d.pop("ping_action")

        ping_action_seconds = d.pop("ping_action_seconds")

        ping_action_push = d.pop("ping_action_push")

        dns_domain_enable = d.pop("dns_domain_enable")

        dns_server_enable = d.pop("dns_server_enable")

        dns_server1 = d.pop("dns_server1")

        dns_server2 = d.pop("dns_server2")

        dns_server3 = d.pop("dns_server3")

        dns_server4 = d.pop("dns_server4")

        push_blockoutsidedns = d.pop("push_blockoutsidedns")

        push_register_dns = d.pop("push_register_dns")

        ntp_server_enable = d.pop("ntp_server_enable")

        ntp_server1 = d.pop("ntp_server1")

        ntp_server2 = d.pop("ntp_server2")

        netbios_enable = d.pop("netbios_enable")

        netbios_ntype = d.pop("netbios_ntype")

        netbios_scope = d.pop("netbios_scope")

        wins_server_enable = d.pop("wins_server_enable")

        wins_server1 = d.pop("wins_server1")

        wins_server2 = d.pop("wins_server2")

        custom_options = d.pop("custom_options")

        username_as_common_name = d.pop("username_as_common_name")

        udp_fast_io = d.pop("udp_fast_io")

        sndrcvbuf = d.pop("sndrcvbuf")

        create_gw = d.pop("create_gw")

        verbosity_level = d.pop("verbosity_level")

        strictusercn = d.pop("strictusercn")

        authmode = cast(List[str], d.pop("authmode", UNSET))

        data_ciphers = cast(List[str], d.pop("data_ciphers", UNSET))

        open_vpn_server_config = cls(
            vpnid=vpnid,
            dco=dco,
            mode=mode,
            protocol=protocol,
            dev_mode=dev_mode,
            interface=interface,
            local_port=local_port,
            description=description,
            tls=tls,
            tls_type=tls_type,
            certref=certref,
            caref=caref,
            dh_length=dh_length,
            data_ciphers_fallback=data_ciphers_fallback,
            digest=digest,
            engine=engine,
            tunnel_network=tunnel_network,
            local_network=local_network,
            maxclients=maxclients,
            allow_compression=allow_compression,
            dynamic_ip=dynamic_ip,
            topology=topology,
            dns_domain=dns_domain,
            exit_notify=exit_notify,
            inactive_seconds=inactive_seconds,
            disable=disable,
            tlsauth_enable=tlsauth_enable,
            autotls_enable=autotls_enable,
            tlsauth_keydir=tlsauth_keydir,
            ocspcheck=ocspcheck,
            ocspurl=ocspurl,
            ecdh_curve=ecdh_curve,
            autokey_enable=autokey_enable,
            shared_key=shared_key,
            cert_depth=cert_depth,
            remote_cert_tls=remote_cert_tls,
            tunnel_networkv6=tunnel_networkv6,
            serverbridge_dhcp=serverbridge_dhcp,
            serverbridge_interface=serverbridge_interface,
            serverbridge_routegateway=serverbridge_routegateway,
            serverbridge_dhcp_start=serverbridge_dhcp_start,
            serverbridge_dhcp_end=serverbridge_dhcp_end,
            gwredir=gwredir,
            gwredir6=gwredir6,
            local_networkv6=local_networkv6,
            remote_network=remote_network,
            remote_networkv6=remote_networkv6,
            compression=compression,
            compression_push=compression_push,
            passtos=passtos,
            client2client=client2client,
            duplicate_cn=duplicate_cn,
            ping_method=ping_method,
            keepalive_interval=keepalive_interval,
            keepalive_timeout=keepalive_timeout,
            ping_seconds=ping_seconds,
            ping_push=ping_push,
            ping_action=ping_action,
            ping_action_seconds=ping_action_seconds,
            ping_action_push=ping_action_push,
            dns_domain_enable=dns_domain_enable,
            dns_server_enable=dns_server_enable,
            dns_server1=dns_server1,
            dns_server2=dns_server2,
            dns_server3=dns_server3,
            dns_server4=dns_server4,
            push_blockoutsidedns=push_blockoutsidedns,
            push_register_dns=push_register_dns,
            ntp_server_enable=ntp_server_enable,
            ntp_server1=ntp_server1,
            ntp_server2=ntp_server2,
            netbios_enable=netbios_enable,
            netbios_ntype=netbios_ntype,
            netbios_scope=netbios_scope,
            wins_server_enable=wins_server_enable,
            wins_server1=wins_server1,
            wins_server2=wins_server2,
            custom_options=custom_options,
            username_as_common_name=username_as_common_name,
            udp_fast_io=udp_fast_io,
            sndrcvbuf=sndrcvbuf,
            create_gw=create_gw,
            verbosity_level=verbosity_level,
            strictusercn=strictusercn,
            authmode=authmode,
            data_ciphers=data_ciphers,
        )

        open_vpn_server_config.additional_properties = d
        return open_vpn_server_config

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
