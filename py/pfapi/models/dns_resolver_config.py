from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_forwarder_domain import DNSForwarderDomain
    from ..models.dns_forwarder_host import DNSForwarderHost
    from ..models.dnsacl import DNSACL


T = TypeVar("T", bound="DNSResolverConfig")


@_attrs_define
class DNSResolverConfig:
    """
    Attributes:
        enable (bool):
        dnssec (bool):
        custom_options (str):
        hideidentity (bool):
        hideversion (bool):
        dnssecstripped (bool):
        qname_minimisation (bool):
        qname_minimisation_strict (bool):
        prefetch (bool):
        prefetchkey (bool):
        dnsrecordcache (bool):
        aggressivensec (bool):
        msgcachesize (str):
        outgoing_num_tcp (str):
        incoming_num_tcp (str):
        edns_buffer_size (str):
        num_queries_per_thread (str):
        jostle_timeout (str):
        cache_max_ttl (str):
        cache_min_ttl (str):
        infra_host_ttl (str):
        infra_cache_numhosts (str):
        unwanted_reply_threshold (str):
        log_verbosity (str):
        disable_auto_added_access_control (bool):
        disable_auto_added_host_entries (bool):
        use_caps (bool):
        dns64 (bool):
        dns64prefix (str):
        dns64netbits (str):
        port (int):
        sslport (int):
        sslcertref (str):
        system_domain_local_zone_type (str):
        regdhcp (bool):
        enablessl (bool):
        python (bool):
        python_order (str):
        python_script (str):
        forwarding (bool):
        forward_tls_upstream (bool):
        regdhcpstatic (bool):
        regovpnclients (bool):
        active_interface (Union[Unset, List[str]]):
        outgoing_interface (Union[Unset, List[str]]):
        hosts (Union[Unset, List['DNSForwarderHost']]):
        domainoverrides (Union[Unset, List['DNSForwarderDomain']]):
        acls (Union[Unset, List['DNSACL']]):
    """

    enable: bool
    dnssec: bool
    custom_options: str
    hideidentity: bool
    hideversion: bool
    dnssecstripped: bool
    qname_minimisation: bool
    qname_minimisation_strict: bool
    prefetch: bool
    prefetchkey: bool
    dnsrecordcache: bool
    aggressivensec: bool
    msgcachesize: str
    outgoing_num_tcp: str
    incoming_num_tcp: str
    edns_buffer_size: str
    num_queries_per_thread: str
    jostle_timeout: str
    cache_max_ttl: str
    cache_min_ttl: str
    infra_host_ttl: str
    infra_cache_numhosts: str
    unwanted_reply_threshold: str
    log_verbosity: str
    disable_auto_added_access_control: bool
    disable_auto_added_host_entries: bool
    use_caps: bool
    dns64: bool
    dns64prefix: str
    dns64netbits: str
    port: int
    sslport: int
    sslcertref: str
    system_domain_local_zone_type: str
    regdhcp: bool
    enablessl: bool
    python: bool
    python_order: str
    python_script: str
    forwarding: bool
    forward_tls_upstream: bool
    regdhcpstatic: bool
    regovpnclients: bool
    active_interface: Union[Unset, List[str]] = UNSET
    outgoing_interface: Union[Unset, List[str]] = UNSET
    hosts: Union[Unset, List["DNSForwarderHost"]] = UNSET
    domainoverrides: Union[Unset, List["DNSForwarderDomain"]] = UNSET
    acls: Union[Unset, List["DNSACL"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        dnssec = self.dnssec

        custom_options = self.custom_options

        hideidentity = self.hideidentity

        hideversion = self.hideversion

        dnssecstripped = self.dnssecstripped

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

        active_interface: Union[Unset, List[str]] = UNSET
        if not isinstance(self.active_interface, Unset):
            active_interface = self.active_interface

        outgoing_interface: Union[Unset, List[str]] = UNSET
        if not isinstance(self.outgoing_interface, Unset):
            outgoing_interface = self.outgoing_interface

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
        field_dict.update(
            {
                "enable": enable,
                "dnssec": dnssec,
                "custom_options": custom_options,
                "hideidentity": hideidentity,
                "hideversion": hideversion,
                "dnssecstripped": dnssecstripped,
                "qname_minimisation": qname_minimisation,
                "qname_minimisation_strict": qname_minimisation_strict,
                "prefetch": prefetch,
                "prefetchkey": prefetchkey,
                "dnsrecordcache": dnsrecordcache,
                "aggressivensec": aggressivensec,
                "msgcachesize": msgcachesize,
                "outgoing_num_tcp": outgoing_num_tcp,
                "incoming_num_tcp": incoming_num_tcp,
                "edns_buffer_size": edns_buffer_size,
                "num_queries_per_thread": num_queries_per_thread,
                "jostle_timeout": jostle_timeout,
                "cache_max_ttl": cache_max_ttl,
                "cache_min_ttl": cache_min_ttl,
                "infra_host_ttl": infra_host_ttl,
                "infra_cache_numhosts": infra_cache_numhosts,
                "unwanted_reply_threshold": unwanted_reply_threshold,
                "log_verbosity": log_verbosity,
                "disable_auto_added_access_control": disable_auto_added_access_control,
                "disable_auto_added_host_entries": disable_auto_added_host_entries,
                "use_caps": use_caps,
                "dns64": dns64,
                "dns64prefix": dns64prefix,
                "dns64netbits": dns64netbits,
                "port": port,
                "sslport": sslport,
                "sslcertref": sslcertref,
                "system_domain_local_zone_type": system_domain_local_zone_type,
                "regdhcp": regdhcp,
                "enablessl": enablessl,
                "python": python,
                "python_order": python_order,
                "python_script": python_script,
                "forwarding": forwarding,
                "forward_tls_upstream": forward_tls_upstream,
                "regdhcpstatic": regdhcpstatic,
                "regovpnclients": regovpnclients,
            }
        )
        if active_interface is not UNSET:
            field_dict["active_interface"] = active_interface
        if outgoing_interface is not UNSET:
            field_dict["outgoing_interface"] = outgoing_interface
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if domainoverrides is not UNSET:
            field_dict["domainoverrides"] = domainoverrides
        if acls is not UNSET:
            field_dict["acls"] = acls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dns_forwarder_domain import DNSForwarderDomain
        from ..models.dns_forwarder_host import DNSForwarderHost
        from ..models.dnsacl import DNSACL

        d = src_dict.copy()
        enable = d.pop("enable")

        dnssec = d.pop("dnssec")

        custom_options = d.pop("custom_options")

        hideidentity = d.pop("hideidentity")

        hideversion = d.pop("hideversion")

        dnssecstripped = d.pop("dnssecstripped")

        qname_minimisation = d.pop("qname_minimisation")

        qname_minimisation_strict = d.pop("qname_minimisation_strict")

        prefetch = d.pop("prefetch")

        prefetchkey = d.pop("prefetchkey")

        dnsrecordcache = d.pop("dnsrecordcache")

        aggressivensec = d.pop("aggressivensec")

        msgcachesize = d.pop("msgcachesize")

        outgoing_num_tcp = d.pop("outgoing_num_tcp")

        incoming_num_tcp = d.pop("incoming_num_tcp")

        edns_buffer_size = d.pop("edns_buffer_size")

        num_queries_per_thread = d.pop("num_queries_per_thread")

        jostle_timeout = d.pop("jostle_timeout")

        cache_max_ttl = d.pop("cache_max_ttl")

        cache_min_ttl = d.pop("cache_min_ttl")

        infra_host_ttl = d.pop("infra_host_ttl")

        infra_cache_numhosts = d.pop("infra_cache_numhosts")

        unwanted_reply_threshold = d.pop("unwanted_reply_threshold")

        log_verbosity = d.pop("log_verbosity")

        disable_auto_added_access_control = d.pop("disable_auto_added_access_control")

        disable_auto_added_host_entries = d.pop("disable_auto_added_host_entries")

        use_caps = d.pop("use_caps")

        dns64 = d.pop("dns64")

        dns64prefix = d.pop("dns64prefix")

        dns64netbits = d.pop("dns64netbits")

        port = d.pop("port")

        sslport = d.pop("sslport")

        sslcertref = d.pop("sslcertref")

        system_domain_local_zone_type = d.pop("system_domain_local_zone_type")

        regdhcp = d.pop("regdhcp")

        enablessl = d.pop("enablessl")

        python = d.pop("python")

        python_order = d.pop("python_order")

        python_script = d.pop("python_script")

        forwarding = d.pop("forwarding")

        forward_tls_upstream = d.pop("forward_tls_upstream")

        regdhcpstatic = d.pop("regdhcpstatic")

        regovpnclients = d.pop("regovpnclients")

        active_interface = cast(List[str], d.pop("active_interface", UNSET))

        outgoing_interface = cast(List[str], d.pop("outgoing_interface", UNSET))

        hosts = []
        _hosts = d.pop("hosts", UNSET)
        for hosts_item_data in _hosts or []:
            hosts_item = DNSForwarderHost.from_dict(hosts_item_data)

            hosts.append(hosts_item)

        domainoverrides = []
        _domainoverrides = d.pop("domainoverrides", UNSET)
        for domainoverrides_item_data in _domainoverrides or []:
            domainoverrides_item = DNSForwarderDomain.from_dict(domainoverrides_item_data)

            domainoverrides.append(domainoverrides_item)

        acls = []
        _acls = d.pop("acls", UNSET)
        for acls_item_data in _acls or []:
            acls_item = DNSACL.from_dict(acls_item_data)

            acls.append(acls_item)

        dns_resolver_config = cls(
            enable=enable,
            dnssec=dnssec,
            custom_options=custom_options,
            hideidentity=hideidentity,
            hideversion=hideversion,
            dnssecstripped=dnssecstripped,
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
            active_interface=active_interface,
            outgoing_interface=outgoing_interface,
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
