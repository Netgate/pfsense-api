from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNServerConfig")


@_attrs_define
class OpenVPNServerConfig:
    """
    Attributes:
        vpnid (Union[Unset, str]):
        dco (Union[Unset, bool]):
        mode (Union[Unset, str]):
        authmode (Union[Unset, List[str]]):
        protocol (Union[Unset, str]):
        dev_mode (Union[Unset, str]):
        interface (Union[Unset, str]):
        local_port (Union[Unset, int]):
        description (Union[Unset, str]):
        tls (Union[Unset, str]):
        tls_type (Union[Unset, str]):
        certref (Union[Unset, str]):
        caref (Union[Unset, str]):
        dh_length (Union[Unset, str]):
        data_ciphers (Union[Unset, List[str]]):
        data_ciphers_fallback (Union[Unset, str]):
        digest (Union[Unset, str]):
        engine (Union[Unset, str]):
        tunnel_network (Union[Unset, str]):
        local_network (Union[Unset, str]):
        maxclients (Union[Unset, str]):
        allow_compression (Union[Unset, str]):
        dynamic_ip (Union[Unset, bool]):
        topology (Union[Unset, str]):
        dns_domain (Union[Unset, str]):
        exit_notify (Union[Unset, str]):
        inactive_seconds (Union[Unset, str]):
        disable (Union[Unset, bool]):
        tlsauth_enable (Union[Unset, bool]):
        autotls_enable (Union[Unset, bool]):
        tlsauth_keydir (Union[Unset, str]):
        ocspcheck (Union[Unset, bool]):
        ocspurl (Union[Unset, str]):
        ecdh_curve (Union[Unset, str]):
        autokey_enable (Union[Unset, bool]):
        shared_key (Union[Unset, str]):
        cert_depth (Union[Unset, str]):
        remote_cert_tls (Union[Unset, bool]):
        tunnel_networkv6 (Union[Unset, str]):
        serverbridge_dhcp (Union[Unset, str]):
        serverbridge_interface (Union[Unset, str]):
        serverbridge_routegateway (Union[Unset, str]):
        serverbridge_dhcp_start (Union[Unset, str]):
        serverbridge_dhcp_end (Union[Unset, str]):
        gwredir (Union[Unset, bool]):
        gwredir6 (Union[Unset, bool]):
        local_networkv6 (Union[Unset, str]):
        remote_network (Union[Unset, str]):
        remote_networkv6 (Union[Unset, str]):
        compression (Union[Unset, str]):
        compression_push (Union[Unset, bool]):
        passtos (Union[Unset, bool]):
        client2client (Union[Unset, bool]):
        duplicate_cn (Union[Unset, bool]):
        ping_method (Union[Unset, str]):
        keepalive_interval (Union[Unset, str]):
        keepalive_timeout (Union[Unset, str]):
        ping_seconds (Union[Unset, str]):
        ping_push (Union[Unset, bool]):
        ping_action (Union[Unset, str]):
        ping_action_seconds (Union[Unset, str]):
        ping_action_push (Union[Unset, bool]):
        dns_domain_enable (Union[Unset, bool]):
        dns_server_enable (Union[Unset, bool]):
        dns_server1 (Union[Unset, str]):
        dns_server2 (Union[Unset, str]):
        dns_server3 (Union[Unset, str]):
        dns_server4 (Union[Unset, str]):
        push_blockoutsidedns (Union[Unset, bool]):
        push_register_dns (Union[Unset, bool]):
        ntp_server_enable (Union[Unset, bool]):
        ntp_server1 (Union[Unset, str]):
        ntp_server2 (Union[Unset, str]):
        netbios_enable (Union[Unset, bool]):
        netbios_ntype (Union[Unset, str]):
        netbios_scope (Union[Unset, str]):
        wins_server_enable (Union[Unset, bool]):
        wins_server1 (Union[Unset, str]):
        wins_server2 (Union[Unset, str]):
        custom_options (Union[Unset, str]):
        username_as_common_name (Union[Unset, bool]):
        udp_fast_io (Union[Unset, bool]):
        sndrcvbuf (Union[Unset, str]):
        create_gw (Union[Unset, str]):
        verbosity_level (Union[Unset, str]):
        strictusercn (Union[Unset, bool]):
    """

    vpnid: Union[Unset, str] = UNSET
    dco: Union[Unset, bool] = UNSET
    mode: Union[Unset, str] = UNSET
    authmode: Union[Unset, List[str]] = UNSET
    protocol: Union[Unset, str] = UNSET
    dev_mode: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    local_port: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    tls: Union[Unset, str] = UNSET
    tls_type: Union[Unset, str] = UNSET
    certref: Union[Unset, str] = UNSET
    caref: Union[Unset, str] = UNSET
    dh_length: Union[Unset, str] = UNSET
    data_ciphers: Union[Unset, List[str]] = UNSET
    data_ciphers_fallback: Union[Unset, str] = UNSET
    digest: Union[Unset, str] = UNSET
    engine: Union[Unset, str] = UNSET
    tunnel_network: Union[Unset, str] = UNSET
    local_network: Union[Unset, str] = UNSET
    maxclients: Union[Unset, str] = UNSET
    allow_compression: Union[Unset, str] = UNSET
    dynamic_ip: Union[Unset, bool] = UNSET
    topology: Union[Unset, str] = UNSET
    dns_domain: Union[Unset, str] = UNSET
    exit_notify: Union[Unset, str] = UNSET
    inactive_seconds: Union[Unset, str] = UNSET
    disable: Union[Unset, bool] = UNSET
    tlsauth_enable: Union[Unset, bool] = UNSET
    autotls_enable: Union[Unset, bool] = UNSET
    tlsauth_keydir: Union[Unset, str] = UNSET
    ocspcheck: Union[Unset, bool] = UNSET
    ocspurl: Union[Unset, str] = UNSET
    ecdh_curve: Union[Unset, str] = UNSET
    autokey_enable: Union[Unset, bool] = UNSET
    shared_key: Union[Unset, str] = UNSET
    cert_depth: Union[Unset, str] = UNSET
    remote_cert_tls: Union[Unset, bool] = UNSET
    tunnel_networkv6: Union[Unset, str] = UNSET
    serverbridge_dhcp: Union[Unset, str] = UNSET
    serverbridge_interface: Union[Unset, str] = UNSET
    serverbridge_routegateway: Union[Unset, str] = UNSET
    serverbridge_dhcp_start: Union[Unset, str] = UNSET
    serverbridge_dhcp_end: Union[Unset, str] = UNSET
    gwredir: Union[Unset, bool] = UNSET
    gwredir6: Union[Unset, bool] = UNSET
    local_networkv6: Union[Unset, str] = UNSET
    remote_network: Union[Unset, str] = UNSET
    remote_networkv6: Union[Unset, str] = UNSET
    compression: Union[Unset, str] = UNSET
    compression_push: Union[Unset, bool] = UNSET
    passtos: Union[Unset, bool] = UNSET
    client2client: Union[Unset, bool] = UNSET
    duplicate_cn: Union[Unset, bool] = UNSET
    ping_method: Union[Unset, str] = UNSET
    keepalive_interval: Union[Unset, str] = UNSET
    keepalive_timeout: Union[Unset, str] = UNSET
    ping_seconds: Union[Unset, str] = UNSET
    ping_push: Union[Unset, bool] = UNSET
    ping_action: Union[Unset, str] = UNSET
    ping_action_seconds: Union[Unset, str] = UNSET
    ping_action_push: Union[Unset, bool] = UNSET
    dns_domain_enable: Union[Unset, bool] = UNSET
    dns_server_enable: Union[Unset, bool] = UNSET
    dns_server1: Union[Unset, str] = UNSET
    dns_server2: Union[Unset, str] = UNSET
    dns_server3: Union[Unset, str] = UNSET
    dns_server4: Union[Unset, str] = UNSET
    push_blockoutsidedns: Union[Unset, bool] = UNSET
    push_register_dns: Union[Unset, bool] = UNSET
    ntp_server_enable: Union[Unset, bool] = UNSET
    ntp_server1: Union[Unset, str] = UNSET
    ntp_server2: Union[Unset, str] = UNSET
    netbios_enable: Union[Unset, bool] = UNSET
    netbios_ntype: Union[Unset, str] = UNSET
    netbios_scope: Union[Unset, str] = UNSET
    wins_server_enable: Union[Unset, bool] = UNSET
    wins_server1: Union[Unset, str] = UNSET
    wins_server2: Union[Unset, str] = UNSET
    custom_options: Union[Unset, str] = UNSET
    username_as_common_name: Union[Unset, bool] = UNSET
    udp_fast_io: Union[Unset, bool] = UNSET
    sndrcvbuf: Union[Unset, str] = UNSET
    create_gw: Union[Unset, str] = UNSET
    verbosity_level: Union[Unset, str] = UNSET
    strictusercn: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vpnid = self.vpnid

        dco = self.dco

        mode = self.mode

        authmode: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authmode, Unset):
            authmode = self.authmode

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

        data_ciphers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_ciphers, Unset):
            data_ciphers = self.data_ciphers

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpnid is not UNSET:
            field_dict["vpnid"] = vpnid
        if dco is not UNSET:
            field_dict["dco"] = dco
        if mode is not UNSET:
            field_dict["mode"] = mode
        if authmode is not UNSET:
            field_dict["authmode"] = authmode
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if dev_mode is not UNSET:
            field_dict["dev_mode"] = dev_mode
        if interface is not UNSET:
            field_dict["interface"] = interface
        if local_port is not UNSET:
            field_dict["local_port"] = local_port
        if description is not UNSET:
            field_dict["description"] = description
        if tls is not UNSET:
            field_dict["tls"] = tls
        if tls_type is not UNSET:
            field_dict["tls_type"] = tls_type
        if certref is not UNSET:
            field_dict["certref"] = certref
        if caref is not UNSET:
            field_dict["caref"] = caref
        if dh_length is not UNSET:
            field_dict["dh_length"] = dh_length
        if data_ciphers is not UNSET:
            field_dict["data_ciphers"] = data_ciphers
        if data_ciphers_fallback is not UNSET:
            field_dict["data_ciphers_fallback"] = data_ciphers_fallback
        if digest is not UNSET:
            field_dict["digest"] = digest
        if engine is not UNSET:
            field_dict["engine"] = engine
        if tunnel_network is not UNSET:
            field_dict["tunnel_network"] = tunnel_network
        if local_network is not UNSET:
            field_dict["local_network"] = local_network
        if maxclients is not UNSET:
            field_dict["maxclients"] = maxclients
        if allow_compression is not UNSET:
            field_dict["allow_compression"] = allow_compression
        if dynamic_ip is not UNSET:
            field_dict["dynamic_ip"] = dynamic_ip
        if topology is not UNSET:
            field_dict["topology"] = topology
        if dns_domain is not UNSET:
            field_dict["dns_domain"] = dns_domain
        if exit_notify is not UNSET:
            field_dict["exit_notify"] = exit_notify
        if inactive_seconds is not UNSET:
            field_dict["inactive_seconds"] = inactive_seconds
        if disable is not UNSET:
            field_dict["disable"] = disable
        if tlsauth_enable is not UNSET:
            field_dict["tlsauth_enable"] = tlsauth_enable
        if autotls_enable is not UNSET:
            field_dict["autotls_enable"] = autotls_enable
        if tlsauth_keydir is not UNSET:
            field_dict["tlsauth_keydir"] = tlsauth_keydir
        if ocspcheck is not UNSET:
            field_dict["ocspcheck"] = ocspcheck
        if ocspurl is not UNSET:
            field_dict["ocspurl"] = ocspurl
        if ecdh_curve is not UNSET:
            field_dict["ecdh_curve"] = ecdh_curve
        if autokey_enable is not UNSET:
            field_dict["autokey_enable"] = autokey_enable
        if shared_key is not UNSET:
            field_dict["shared_key"] = shared_key
        if cert_depth is not UNSET:
            field_dict["cert_depth"] = cert_depth
        if remote_cert_tls is not UNSET:
            field_dict["remote_cert_tls"] = remote_cert_tls
        if tunnel_networkv6 is not UNSET:
            field_dict["tunnel_networkv6"] = tunnel_networkv6
        if serverbridge_dhcp is not UNSET:
            field_dict["serverbridge_dhcp"] = serverbridge_dhcp
        if serverbridge_interface is not UNSET:
            field_dict["serverbridge_interface"] = serverbridge_interface
        if serverbridge_routegateway is not UNSET:
            field_dict["serverbridge_routegateway"] = serverbridge_routegateway
        if serverbridge_dhcp_start is not UNSET:
            field_dict["serverbridge_dhcp_start"] = serverbridge_dhcp_start
        if serverbridge_dhcp_end is not UNSET:
            field_dict["serverbridge_dhcp_end"] = serverbridge_dhcp_end
        if gwredir is not UNSET:
            field_dict["gwredir"] = gwredir
        if gwredir6 is not UNSET:
            field_dict["gwredir6"] = gwredir6
        if local_networkv6 is not UNSET:
            field_dict["local_networkv6"] = local_networkv6
        if remote_network is not UNSET:
            field_dict["remote_network"] = remote_network
        if remote_networkv6 is not UNSET:
            field_dict["remote_networkv6"] = remote_networkv6
        if compression is not UNSET:
            field_dict["compression"] = compression
        if compression_push is not UNSET:
            field_dict["compression_push"] = compression_push
        if passtos is not UNSET:
            field_dict["passtos"] = passtos
        if client2client is not UNSET:
            field_dict["client2client"] = client2client
        if duplicate_cn is not UNSET:
            field_dict["duplicate_cn"] = duplicate_cn
        if ping_method is not UNSET:
            field_dict["ping_method"] = ping_method
        if keepalive_interval is not UNSET:
            field_dict["keepalive_interval"] = keepalive_interval
        if keepalive_timeout is not UNSET:
            field_dict["keepalive_timeout"] = keepalive_timeout
        if ping_seconds is not UNSET:
            field_dict["ping_seconds"] = ping_seconds
        if ping_push is not UNSET:
            field_dict["ping_push"] = ping_push
        if ping_action is not UNSET:
            field_dict["ping_action"] = ping_action
        if ping_action_seconds is not UNSET:
            field_dict["ping_action_seconds"] = ping_action_seconds
        if ping_action_push is not UNSET:
            field_dict["ping_action_push"] = ping_action_push
        if dns_domain_enable is not UNSET:
            field_dict["dns_domain_enable"] = dns_domain_enable
        if dns_server_enable is not UNSET:
            field_dict["dns_server_enable"] = dns_server_enable
        if dns_server1 is not UNSET:
            field_dict["dns_server1"] = dns_server1
        if dns_server2 is not UNSET:
            field_dict["dns_server2"] = dns_server2
        if dns_server3 is not UNSET:
            field_dict["dns_server3"] = dns_server3
        if dns_server4 is not UNSET:
            field_dict["dns_server4"] = dns_server4
        if push_blockoutsidedns is not UNSET:
            field_dict["push_blockoutsidedns"] = push_blockoutsidedns
        if push_register_dns is not UNSET:
            field_dict["push_register_dns"] = push_register_dns
        if ntp_server_enable is not UNSET:
            field_dict["ntp_server_enable"] = ntp_server_enable
        if ntp_server1 is not UNSET:
            field_dict["ntp_server1"] = ntp_server1
        if ntp_server2 is not UNSET:
            field_dict["ntp_server2"] = ntp_server2
        if netbios_enable is not UNSET:
            field_dict["netbios_enable"] = netbios_enable
        if netbios_ntype is not UNSET:
            field_dict["netbios_ntype"] = netbios_ntype
        if netbios_scope is not UNSET:
            field_dict["netbios_scope"] = netbios_scope
        if wins_server_enable is not UNSET:
            field_dict["wins_server_enable"] = wins_server_enable
        if wins_server1 is not UNSET:
            field_dict["wins_server1"] = wins_server1
        if wins_server2 is not UNSET:
            field_dict["wins_server2"] = wins_server2
        if custom_options is not UNSET:
            field_dict["custom_options"] = custom_options
        if username_as_common_name is not UNSET:
            field_dict["username_as_common_name"] = username_as_common_name
        if udp_fast_io is not UNSET:
            field_dict["udp_fast_io"] = udp_fast_io
        if sndrcvbuf is not UNSET:
            field_dict["sndrcvbuf"] = sndrcvbuf
        if create_gw is not UNSET:
            field_dict["create_gw"] = create_gw
        if verbosity_level is not UNSET:
            field_dict["verbosity_level"] = verbosity_level
        if strictusercn is not UNSET:
            field_dict["strictusercn"] = strictusercn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vpnid = d.pop("vpnid", UNSET)

        dco = d.pop("dco", UNSET)

        mode = d.pop("mode", UNSET)

        authmode = cast(List[str], d.pop("authmode", UNSET))

        protocol = d.pop("protocol", UNSET)

        dev_mode = d.pop("dev_mode", UNSET)

        interface = d.pop("interface", UNSET)

        local_port = d.pop("local_port", UNSET)

        description = d.pop("description", UNSET)

        tls = d.pop("tls", UNSET)

        tls_type = d.pop("tls_type", UNSET)

        certref = d.pop("certref", UNSET)

        caref = d.pop("caref", UNSET)

        dh_length = d.pop("dh_length", UNSET)

        data_ciphers = cast(List[str], d.pop("data_ciphers", UNSET))

        data_ciphers_fallback = d.pop("data_ciphers_fallback", UNSET)

        digest = d.pop("digest", UNSET)

        engine = d.pop("engine", UNSET)

        tunnel_network = d.pop("tunnel_network", UNSET)

        local_network = d.pop("local_network", UNSET)

        maxclients = d.pop("maxclients", UNSET)

        allow_compression = d.pop("allow_compression", UNSET)

        dynamic_ip = d.pop("dynamic_ip", UNSET)

        topology = d.pop("topology", UNSET)

        dns_domain = d.pop("dns_domain", UNSET)

        exit_notify = d.pop("exit_notify", UNSET)

        inactive_seconds = d.pop("inactive_seconds", UNSET)

        disable = d.pop("disable", UNSET)

        tlsauth_enable = d.pop("tlsauth_enable", UNSET)

        autotls_enable = d.pop("autotls_enable", UNSET)

        tlsauth_keydir = d.pop("tlsauth_keydir", UNSET)

        ocspcheck = d.pop("ocspcheck", UNSET)

        ocspurl = d.pop("ocspurl", UNSET)

        ecdh_curve = d.pop("ecdh_curve", UNSET)

        autokey_enable = d.pop("autokey_enable", UNSET)

        shared_key = d.pop("shared_key", UNSET)

        cert_depth = d.pop("cert_depth", UNSET)

        remote_cert_tls = d.pop("remote_cert_tls", UNSET)

        tunnel_networkv6 = d.pop("tunnel_networkv6", UNSET)

        serverbridge_dhcp = d.pop("serverbridge_dhcp", UNSET)

        serverbridge_interface = d.pop("serverbridge_interface", UNSET)

        serverbridge_routegateway = d.pop("serverbridge_routegateway", UNSET)

        serverbridge_dhcp_start = d.pop("serverbridge_dhcp_start", UNSET)

        serverbridge_dhcp_end = d.pop("serverbridge_dhcp_end", UNSET)

        gwredir = d.pop("gwredir", UNSET)

        gwredir6 = d.pop("gwredir6", UNSET)

        local_networkv6 = d.pop("local_networkv6", UNSET)

        remote_network = d.pop("remote_network", UNSET)

        remote_networkv6 = d.pop("remote_networkv6", UNSET)

        compression = d.pop("compression", UNSET)

        compression_push = d.pop("compression_push", UNSET)

        passtos = d.pop("passtos", UNSET)

        client2client = d.pop("client2client", UNSET)

        duplicate_cn = d.pop("duplicate_cn", UNSET)

        ping_method = d.pop("ping_method", UNSET)

        keepalive_interval = d.pop("keepalive_interval", UNSET)

        keepalive_timeout = d.pop("keepalive_timeout", UNSET)

        ping_seconds = d.pop("ping_seconds", UNSET)

        ping_push = d.pop("ping_push", UNSET)

        ping_action = d.pop("ping_action", UNSET)

        ping_action_seconds = d.pop("ping_action_seconds", UNSET)

        ping_action_push = d.pop("ping_action_push", UNSET)

        dns_domain_enable = d.pop("dns_domain_enable", UNSET)

        dns_server_enable = d.pop("dns_server_enable", UNSET)

        dns_server1 = d.pop("dns_server1", UNSET)

        dns_server2 = d.pop("dns_server2", UNSET)

        dns_server3 = d.pop("dns_server3", UNSET)

        dns_server4 = d.pop("dns_server4", UNSET)

        push_blockoutsidedns = d.pop("push_blockoutsidedns", UNSET)

        push_register_dns = d.pop("push_register_dns", UNSET)

        ntp_server_enable = d.pop("ntp_server_enable", UNSET)

        ntp_server1 = d.pop("ntp_server1", UNSET)

        ntp_server2 = d.pop("ntp_server2", UNSET)

        netbios_enable = d.pop("netbios_enable", UNSET)

        netbios_ntype = d.pop("netbios_ntype", UNSET)

        netbios_scope = d.pop("netbios_scope", UNSET)

        wins_server_enable = d.pop("wins_server_enable", UNSET)

        wins_server1 = d.pop("wins_server1", UNSET)

        wins_server2 = d.pop("wins_server2", UNSET)

        custom_options = d.pop("custom_options", UNSET)

        username_as_common_name = d.pop("username_as_common_name", UNSET)

        udp_fast_io = d.pop("udp_fast_io", UNSET)

        sndrcvbuf = d.pop("sndrcvbuf", UNSET)

        create_gw = d.pop("create_gw", UNSET)

        verbosity_level = d.pop("verbosity_level", UNSET)

        strictusercn = d.pop("strictusercn", UNSET)

        open_vpn_server_config = cls(
            vpnid=vpnid,
            dco=dco,
            mode=mode,
            authmode=authmode,
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
            data_ciphers=data_ciphers,
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