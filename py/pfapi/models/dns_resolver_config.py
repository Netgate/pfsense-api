from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_forwarder_host import DNSForwarderHost
    from ..models.dns_resolver_domain import DNSResolverDomain
    from ..models.dnsacl import DNSACL


T = TypeVar("T", bound="DNSResolverConfig")


@_attrs_define
class DNSResolverConfig:
    """
    Attributes:
        enable (Union[Unset, bool]):
        dnssec (Union[Unset, bool]):
        active_interface (Union[Unset, List[str]]):
        outgoing_interface (Union[Unset, List[str]]):
        custom_options (Union[Unset, str]):
        hideidentity (Union[Unset, bool]):
        hideversion (Union[Unset, bool]):
        dnssecstripped (Union[Unset, bool]):
        drop_old_udp_pkts (Union[Unset, int]):
        keep_probing (Union[Unset, bool]):
        qname_minimisation (Union[Unset, bool]):
        qname_minimisation_strict (Union[Unset, bool]):
        prefetch (Union[Unset, bool]):
        prefetchkey (Union[Unset, bool]):
        dnsrecordcache (Union[Unset, bool]):
        aggressivensec (Union[Unset, bool]):
        msgcachesize (Union[Unset, str]):
        outgoing_num_tcp (Union[Unset, str]):
        incoming_num_tcp (Union[Unset, str]):
        edns_buffer_size (Union[Unset, str]):
        num_queries_per_thread (Union[Unset, str]):
        jostle_timeout (Union[Unset, str]):
        cache_max_ttl (Union[Unset, str]):
        cache_min_ttl (Union[Unset, str]):
        infra_host_ttl (Union[Unset, str]):
        infra_cache_numhosts (Union[Unset, str]):
        unwanted_reply_threshold (Union[Unset, str]):
        log_verbosity (Union[Unset, str]):
        disable_auto_added_access_control (Union[Unset, bool]):
        disable_auto_added_host_entries (Union[Unset, bool]):
        use_caps (Union[Unset, bool]):
        dns64 (Union[Unset, bool]):
        dns64prefix (Union[Unset, str]):
        dns64netbits (Union[Unset, str]):
        port (Union[Unset, int]):
        sslport (Union[Unset, int]):
        sslcertref (Union[Unset, str]):
        system_domain_local_zone_type (Union[Unset, str]):
        regdhcp (Union[Unset, bool]):
        enablessl (Union[Unset, bool]):
        python (Union[Unset, bool]):
        python_order (Union[Unset, str]):
        python_script (Union[Unset, str]):
        forwarding (Union[Unset, bool]):
        forward_tls_upstream (Union[Unset, bool]):
        regdhcpstatic (Union[Unset, bool]):
        regovpnclients (Union[Unset, bool]):
        hosts (Union[Unset, List['DNSForwarderHost']]):
        domainoverrides (Union[Unset, List['DNSResolverDomain']]):
        acls (Union[Unset, List['DNSACL']]):
    """

    enable: Union[Unset, bool] = UNSET
    dnssec: Union[Unset, bool] = UNSET
    active_interface: Union[Unset, List[str]] = UNSET
    outgoing_interface: Union[Unset, List[str]] = UNSET
    custom_options: Union[Unset, str] = UNSET
    hideidentity: Union[Unset, bool] = UNSET
    hideversion: Union[Unset, bool] = UNSET
    dnssecstripped: Union[Unset, bool] = UNSET
    drop_old_udp_pkts: Union[Unset, int] = UNSET
    keep_probing: Union[Unset, bool] = UNSET
    qname_minimisation: Union[Unset, bool] = UNSET
    qname_minimisation_strict: Union[Unset, bool] = UNSET
    prefetch: Union[Unset, bool] = UNSET
    prefetchkey: Union[Unset, bool] = UNSET
    dnsrecordcache: Union[Unset, bool] = UNSET
    aggressivensec: Union[Unset, bool] = UNSET
    msgcachesize: Union[Unset, str] = UNSET
    outgoing_num_tcp: Union[Unset, str] = UNSET
    incoming_num_tcp: Union[Unset, str] = UNSET
    edns_buffer_size: Union[Unset, str] = UNSET
    num_queries_per_thread: Union[Unset, str] = UNSET
    jostle_timeout: Union[Unset, str] = UNSET
    cache_max_ttl: Union[Unset, str] = UNSET
    cache_min_ttl: Union[Unset, str] = UNSET
    infra_host_ttl: Union[Unset, str] = UNSET
    infra_cache_numhosts: Union[Unset, str] = UNSET
    unwanted_reply_threshold: Union[Unset, str] = UNSET
    log_verbosity: Union[Unset, str] = UNSET
    disable_auto_added_access_control: Union[Unset, bool] = UNSET
    disable_auto_added_host_entries: Union[Unset, bool] = UNSET
    use_caps: Union[Unset, bool] = UNSET
    dns64: Union[Unset, bool] = UNSET
    dns64prefix: Union[Unset, str] = UNSET
    dns64netbits: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    sslport: Union[Unset, int] = UNSET
    sslcertref: Union[Unset, str] = UNSET
    system_domain_local_zone_type: Union[Unset, str] = UNSET
    regdhcp: Union[Unset, bool] = UNSET
    enablessl: Union[Unset, bool] = UNSET
    python: Union[Unset, bool] = UNSET
    python_order: Union[Unset, str] = UNSET
    python_script: Union[Unset, str] = UNSET
    forwarding: Union[Unset, bool] = UNSET
    forward_tls_upstream: Union[Unset, bool] = UNSET
    regdhcpstatic: Union[Unset, bool] = UNSET
    regovpnclients: Union[Unset, bool] = UNSET
    hosts: Union[Unset, List["DNSForwarderHost"]] = UNSET
    domainoverrides: Union[Unset, List["DNSResolverDomain"]] = UNSET
    acls: Union[Unset, List["DNSACL"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        dnssec = self.dnssec

        active_interface: Union[Unset, List[str]] = UNSET
        if not isinstance(self.active_interface, Unset):
            active_interface = self.active_interface

        outgoing_interface: Union[Unset, List[str]] = UNSET
        if not isinstance(self.outgoing_interface, Unset):
            outgoing_interface = self.outgoing_interface

        custom_options = self.custom_options

        hideidentity = self.hideidentity

        hideversion = self.hideversion

        dnssecstripped = self.dnssecstripped

        drop_old_udp_pkts = self.drop_old_udp_pkts

        keep_probing = self.keep_probing

        qname_minimisation = self.qname_minimisation

        qname_minimisation_strict = self.qname_minimisation_strict

        prefetch = self.prefetch

        prefetchkey = self.prefetchkey

        dnsrecordcache = self.dnsrecordcache

        aggressivensec = self.aggressivensec

        msgcachesize = self.msgcachesize

        outgoing_num_tcp = self.outgoing_num_tcp

        incoming_num_tcp = self.incoming_num_tcp

        edns_buffer_size = self.edns_buffer_size

        num_queries_per_thread = self.num_queries_per_thread

        jostle_timeout = self.jostle_timeout

        cache_max_ttl = self.cache_max_ttl

        cache_min_ttl = self.cache_min_ttl

        infra_host_ttl = self.infra_host_ttl

        infra_cache_numhosts = self.infra_cache_numhosts

        unwanted_reply_threshold = self.unwanted_reply_threshold

        log_verbosity = self.log_verbosity

        disable_auto_added_access_control = self.disable_auto_added_access_control

        disable_auto_added_host_entries = self.disable_auto_added_host_entries

        use_caps = self.use_caps

        dns64 = self.dns64

        dns64prefix = self.dns64prefix

        dns64netbits = self.dns64netbits

        port = self.port

        sslport = self.sslport

        sslcertref = self.sslcertref

        system_domain_local_zone_type = self.system_domain_local_zone_type

        regdhcp = self.regdhcp

        enablessl = self.enablessl

        python = self.python

        python_order = self.python_order

        python_script = self.python_script

        forwarding = self.forwarding

        forward_tls_upstream = self.forward_tls_upstream

        regdhcpstatic = self.regdhcpstatic

        regovpnclients = self.regovpnclients

        hosts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = []
            for hosts_item_data in self.hosts:
                hosts_item = hosts_item_data.to_dict()
                hosts.append(hosts_item)

        domainoverrides: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.domainoverrides, Unset):
            domainoverrides = []
            for domainoverrides_item_data in self.domainoverrides:
                domainoverrides_item = domainoverrides_item_data.to_dict()
                domainoverrides.append(domainoverrides_item)

        acls: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acls, Unset):
            acls = []
            for acls_item_data in self.acls:
                acls_item = acls_item_data.to_dict()
                acls.append(acls_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if dnssec is not UNSET:
            field_dict["dnssec"] = dnssec
        if active_interface is not UNSET:
            field_dict["active_interface"] = active_interface
        if outgoing_interface is not UNSET:
            field_dict["outgoing_interface"] = outgoing_interface
        if custom_options is not UNSET:
            field_dict["custom_options"] = custom_options
        if hideidentity is not UNSET:
            field_dict["hideidentity"] = hideidentity
        if hideversion is not UNSET:
            field_dict["hideversion"] = hideversion
        if dnssecstripped is not UNSET:
            field_dict["dnssecstripped"] = dnssecstripped
        if drop_old_udp_pkts is not UNSET:
            field_dict["drop_old_udp_pkts"] = drop_old_udp_pkts
        if keep_probing is not UNSET:
            field_dict["keep_probing"] = keep_probing
        if qname_minimisation is not UNSET:
            field_dict["qname_minimisation"] = qname_minimisation
        if qname_minimisation_strict is not UNSET:
            field_dict["qname_minimisation_strict"] = qname_minimisation_strict
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch
        if prefetchkey is not UNSET:
            field_dict["prefetchkey"] = prefetchkey
        if dnsrecordcache is not UNSET:
            field_dict["dnsrecordcache"] = dnsrecordcache
        if aggressivensec is not UNSET:
            field_dict["aggressivensec"] = aggressivensec
        if msgcachesize is not UNSET:
            field_dict["msgcachesize"] = msgcachesize
        if outgoing_num_tcp is not UNSET:
            field_dict["outgoing_num_tcp"] = outgoing_num_tcp
        if incoming_num_tcp is not UNSET:
            field_dict["incoming_num_tcp"] = incoming_num_tcp
        if edns_buffer_size is not UNSET:
            field_dict["edns_buffer_size"] = edns_buffer_size
        if num_queries_per_thread is not UNSET:
            field_dict["num_queries_per_thread"] = num_queries_per_thread
        if jostle_timeout is not UNSET:
            field_dict["jostle_timeout"] = jostle_timeout
        if cache_max_ttl is not UNSET:
            field_dict["cache_max_ttl"] = cache_max_ttl
        if cache_min_ttl is not UNSET:
            field_dict["cache_min_ttl"] = cache_min_ttl
        if infra_host_ttl is not UNSET:
            field_dict["infra_host_ttl"] = infra_host_ttl
        if infra_cache_numhosts is not UNSET:
            field_dict["infra_cache_numhosts"] = infra_cache_numhosts
        if unwanted_reply_threshold is not UNSET:
            field_dict["unwanted_reply_threshold"] = unwanted_reply_threshold
        if log_verbosity is not UNSET:
            field_dict["log_verbosity"] = log_verbosity
        if disable_auto_added_access_control is not UNSET:
            field_dict["disable_auto_added_access_control"] = disable_auto_added_access_control
        if disable_auto_added_host_entries is not UNSET:
            field_dict["disable_auto_added_host_entries"] = disable_auto_added_host_entries
        if use_caps is not UNSET:
            field_dict["use_caps"] = use_caps
        if dns64 is not UNSET:
            field_dict["dns64"] = dns64
        if dns64prefix is not UNSET:
            field_dict["dns64prefix"] = dns64prefix
        if dns64netbits is not UNSET:
            field_dict["dns64netbits"] = dns64netbits
        if port is not UNSET:
            field_dict["port"] = port
        if sslport is not UNSET:
            field_dict["sslport"] = sslport
        if sslcertref is not UNSET:
            field_dict["sslcertref"] = sslcertref
        if system_domain_local_zone_type is not UNSET:
            field_dict["system_domain_local_zone_type"] = system_domain_local_zone_type
        if regdhcp is not UNSET:
            field_dict["regdhcp"] = regdhcp
        if enablessl is not UNSET:
            field_dict["enablessl"] = enablessl
        if python is not UNSET:
            field_dict["python"] = python
        if python_order is not UNSET:
            field_dict["python_order"] = python_order
        if python_script is not UNSET:
            field_dict["python_script"] = python_script
        if forwarding is not UNSET:
            field_dict["forwarding"] = forwarding
        if forward_tls_upstream is not UNSET:
            field_dict["forward_tls_upstream"] = forward_tls_upstream
        if regdhcpstatic is not UNSET:
            field_dict["regdhcpstatic"] = regdhcpstatic
        if regovpnclients is not UNSET:
            field_dict["regovpnclients"] = regovpnclients
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if domainoverrides is not UNSET:
            field_dict["domainoverrides"] = domainoverrides
        if acls is not UNSET:
            field_dict["acls"] = acls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dns_forwarder_host import DNSForwarderHost
        from ..models.dns_resolver_domain import DNSResolverDomain
        from ..models.dnsacl import DNSACL

        d = src_dict.copy()
        enable = d.pop("enable", UNSET)

        dnssec = d.pop("dnssec", UNSET)

        active_interface = cast(List[str], d.pop("active_interface", UNSET))

        outgoing_interface = cast(List[str], d.pop("outgoing_interface", UNSET))

        custom_options = d.pop("custom_options", UNSET)

        hideidentity = d.pop("hideidentity", UNSET)

        hideversion = d.pop("hideversion", UNSET)

        dnssecstripped = d.pop("dnssecstripped", UNSET)

        drop_old_udp_pkts = d.pop("drop_old_udp_pkts", UNSET)

        keep_probing = d.pop("keep_probing", UNSET)

        qname_minimisation = d.pop("qname_minimisation", UNSET)

        qname_minimisation_strict = d.pop("qname_minimisation_strict", UNSET)

        prefetch = d.pop("prefetch", UNSET)

        prefetchkey = d.pop("prefetchkey", UNSET)

        dnsrecordcache = d.pop("dnsrecordcache", UNSET)

        aggressivensec = d.pop("aggressivensec", UNSET)

        msgcachesize = d.pop("msgcachesize", UNSET)

        outgoing_num_tcp = d.pop("outgoing_num_tcp", UNSET)

        incoming_num_tcp = d.pop("incoming_num_tcp", UNSET)

        edns_buffer_size = d.pop("edns_buffer_size", UNSET)

        num_queries_per_thread = d.pop("num_queries_per_thread", UNSET)

        jostle_timeout = d.pop("jostle_timeout", UNSET)

        cache_max_ttl = d.pop("cache_max_ttl", UNSET)

        cache_min_ttl = d.pop("cache_min_ttl", UNSET)

        infra_host_ttl = d.pop("infra_host_ttl", UNSET)

        infra_cache_numhosts = d.pop("infra_cache_numhosts", UNSET)

        unwanted_reply_threshold = d.pop("unwanted_reply_threshold", UNSET)

        log_verbosity = d.pop("log_verbosity", UNSET)

        disable_auto_added_access_control = d.pop("disable_auto_added_access_control", UNSET)

        disable_auto_added_host_entries = d.pop("disable_auto_added_host_entries", UNSET)

        use_caps = d.pop("use_caps", UNSET)

        dns64 = d.pop("dns64", UNSET)

        dns64prefix = d.pop("dns64prefix", UNSET)

        dns64netbits = d.pop("dns64netbits", UNSET)

        port = d.pop("port", UNSET)

        sslport = d.pop("sslport", UNSET)

        sslcertref = d.pop("sslcertref", UNSET)

        system_domain_local_zone_type = d.pop("system_domain_local_zone_type", UNSET)

        regdhcp = d.pop("regdhcp", UNSET)

        enablessl = d.pop("enablessl", UNSET)

        python = d.pop("python", UNSET)

        python_order = d.pop("python_order", UNSET)

        python_script = d.pop("python_script", UNSET)

        forwarding = d.pop("forwarding", UNSET)

        forward_tls_upstream = d.pop("forward_tls_upstream", UNSET)

        regdhcpstatic = d.pop("regdhcpstatic", UNSET)

        regovpnclients = d.pop("regovpnclients", UNSET)

        hosts = []
        _hosts = d.pop("hosts", UNSET)
        for hosts_item_data in _hosts or []:
            hosts_item = DNSForwarderHost.from_dict(hosts_item_data)

            hosts.append(hosts_item)

        domainoverrides = []
        _domainoverrides = d.pop("domainoverrides", UNSET)
        for domainoverrides_item_data in _domainoverrides or []:
            domainoverrides_item = DNSResolverDomain.from_dict(domainoverrides_item_data)

            domainoverrides.append(domainoverrides_item)

        acls = []
        _acls = d.pop("acls", UNSET)
        for acls_item_data in _acls or []:
            acls_item = DNSACL.from_dict(acls_item_data)

            acls.append(acls_item)

        dns_resolver_config = cls(
            enable=enable,
            dnssec=dnssec,
            active_interface=active_interface,
            outgoing_interface=outgoing_interface,
            custom_options=custom_options,
            hideidentity=hideidentity,
            hideversion=hideversion,
            dnssecstripped=dnssecstripped,
            drop_old_udp_pkts=drop_old_udp_pkts,
            keep_probing=keep_probing,
            qname_minimisation=qname_minimisation,
            qname_minimisation_strict=qname_minimisation_strict,
            prefetch=prefetch,
            prefetchkey=prefetchkey,
            dnsrecordcache=dnsrecordcache,
            aggressivensec=aggressivensec,
            msgcachesize=msgcachesize,
            outgoing_num_tcp=outgoing_num_tcp,
            incoming_num_tcp=incoming_num_tcp,
            edns_buffer_size=edns_buffer_size,
            num_queries_per_thread=num_queries_per_thread,
            jostle_timeout=jostle_timeout,
            cache_max_ttl=cache_max_ttl,
            cache_min_ttl=cache_min_ttl,
            infra_host_ttl=infra_host_ttl,
            infra_cache_numhosts=infra_cache_numhosts,
            unwanted_reply_threshold=unwanted_reply_threshold,
            log_verbosity=log_verbosity,
            disable_auto_added_access_control=disable_auto_added_access_control,
            disable_auto_added_host_entries=disable_auto_added_host_entries,
            use_caps=use_caps,
            dns64=dns64,
            dns64prefix=dns64prefix,
            dns64netbits=dns64netbits,
            port=port,
            sslport=sslport,
            sslcertref=sslcertref,
            system_domain_local_zone_type=system_domain_local_zone_type,
            regdhcp=regdhcp,
            enablessl=enablessl,
            python=python,
            python_order=python_order,
            python_script=python_script,
            forwarding=forwarding,
            forward_tls_upstream=forward_tls_upstream,
            regdhcpstatic=regdhcpstatic,
            regovpnclients=regovpnclients,
            hosts=hosts,
            domainoverrides=domainoverrides,
            acls=acls,
        )

        dns_resolver_config.additional_properties = d
        return dns_resolver_config

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
