from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_value import TextValue


T = TypeVar("T", bound="SyslogConfiguration")


@_attrs_define
class SyslogConfiguration:
    """
    Attributes:
        reverse (bool | Unset):
        nentries (int | Unset):
        logfilesize (int | Unset):
        logcompressiontype (str | Unset): none, bzip2, gzip, xz, zstd
        format_ (str | Unset): rfc3164, rfc5424
        default_log_level (str | Unset): refer to options in syslog_levels
        rotatecount (int | Unset):
        enable_remote (bool | Unset):
        remoteserver (str | Unset): ip:port of remote server
        remoteserver2 (str | Unset): ip:port of second remote server
        remoteserver3 (str | Unset): ip:port of third remote server
        sourceip (str | Unset): source network interface for binding to
        ipproto (str | Unset): ipv4, ipv6
        logall (bool | Unset): remote log everything
        filter_ (bool | Unset): remote log firewall events
        dhcp (bool | Unset): remote log DHCP events
        auth (bool | Unset): remote log authentication events
        portalauth (bool | Unset): remtoe log captive portal events
        vpn (bool | Unset): remote log vpn events
        dpinger (bool | Unset): remote log gateway monitor events
        hostapd (bool | Unset): remote log wireless events
        system (bool | Unset): remote log system events
        pfnet_controller (bool | Unset): remote log Nexus events
        resolver (bool | Unset): remote log DNS events
        ppp (bool | Unset): remote log PPP events
        routing (bool | Unset): remote log routing daemon events
        ntpd (bool | Unset): remote log NTP events
        disablelocallogging (bool | Unset): disable local logging
        rawfilter (bool | Unset): show raw filter logs
        showfilterdescrips (str | Unset): where to show firewall rule descriptions:
            * "disable" - don't show,
            * "column"  - as column,
            * "row"     - as second row
        logipoptions (bool | Unset): log blocked packets due to IP options
        logdefaultblock (bool | Unset): log default "block" rules
        logdefaultpass (bool | Unset): log default "pass" rules
        logbogons (bool | Unset): log Bogon Networks block rules
        logprivatenets (bool | Unset): log Private Networks block rules
        loglinklocal4 (bool | Unset): log IPv4 link-local block rules
        logids (bool | Unset): log hosts blocked by IDS
        lognginx (bool | Unset): log web server
        logconfigchanges (bool | Unset): log configuration changes
        source_addresses (list[TextValue] | Unset):
        syslog_levels (list[TextValue] | Unset):
    """

    reverse: bool | Unset = UNSET
    nentries: int | Unset = UNSET
    logfilesize: int | Unset = UNSET
    logcompressiontype: str | Unset = UNSET
    format_: str | Unset = UNSET
    default_log_level: str | Unset = UNSET
    rotatecount: int | Unset = UNSET
    enable_remote: bool | Unset = UNSET
    remoteserver: str | Unset = UNSET
    remoteserver2: str | Unset = UNSET
    remoteserver3: str | Unset = UNSET
    sourceip: str | Unset = UNSET
    ipproto: str | Unset = UNSET
    logall: bool | Unset = UNSET
    filter_: bool | Unset = UNSET
    dhcp: bool | Unset = UNSET
    auth: bool | Unset = UNSET
    portalauth: bool | Unset = UNSET
    vpn: bool | Unset = UNSET
    dpinger: bool | Unset = UNSET
    hostapd: bool | Unset = UNSET
    system: bool | Unset = UNSET
    pfnet_controller: bool | Unset = UNSET
    resolver: bool | Unset = UNSET
    ppp: bool | Unset = UNSET
    routing: bool | Unset = UNSET
    ntpd: bool | Unset = UNSET
    disablelocallogging: bool | Unset = UNSET
    rawfilter: bool | Unset = UNSET
    showfilterdescrips: str | Unset = UNSET
    logipoptions: bool | Unset = UNSET
    logdefaultblock: bool | Unset = UNSET
    logdefaultpass: bool | Unset = UNSET
    logbogons: bool | Unset = UNSET
    logprivatenets: bool | Unset = UNSET
    loglinklocal4: bool | Unset = UNSET
    logids: bool | Unset = UNSET
    lognginx: bool | Unset = UNSET
    logconfigchanges: bool | Unset = UNSET
    source_addresses: list[TextValue] | Unset = UNSET
    syslog_levels: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reverse = self.reverse

        nentries = self.nentries

        logfilesize = self.logfilesize

        logcompressiontype = self.logcompressiontype

        format_ = self.format_

        default_log_level = self.default_log_level

        rotatecount = self.rotatecount

        enable_remote = self.enable_remote

        remoteserver = self.remoteserver

        remoteserver2 = self.remoteserver2

        remoteserver3 = self.remoteserver3

        sourceip = self.sourceip

        ipproto = self.ipproto

        logall = self.logall

        filter_ = self.filter_

        dhcp = self.dhcp

        auth = self.auth

        portalauth = self.portalauth

        vpn = self.vpn

        dpinger = self.dpinger

        hostapd = self.hostapd

        system = self.system

        pfnet_controller = self.pfnet_controller

        resolver = self.resolver

        ppp = self.ppp

        routing = self.routing

        ntpd = self.ntpd

        disablelocallogging = self.disablelocallogging

        rawfilter = self.rawfilter

        showfilterdescrips = self.showfilterdescrips

        logipoptions = self.logipoptions

        logdefaultblock = self.logdefaultblock

        logdefaultpass = self.logdefaultpass

        logbogons = self.logbogons

        logprivatenets = self.logprivatenets

        loglinklocal4 = self.loglinklocal4

        logids = self.logids

        lognginx = self.lognginx

        logconfigchanges = self.logconfigchanges

        source_addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.source_addresses, Unset):
            source_addresses = []
            for source_addresses_item_data in self.source_addresses:
                source_addresses_item = source_addresses_item_data.to_dict()
                source_addresses.append(source_addresses_item)

        syslog_levels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.syslog_levels, Unset):
            syslog_levels = []
            for syslog_levels_item_data in self.syslog_levels:
                syslog_levels_item = syslog_levels_item_data.to_dict()
                syslog_levels.append(syslog_levels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reverse is not UNSET:
            field_dict["reverse"] = reverse
        if nentries is not UNSET:
            field_dict["nentries"] = nentries
        if logfilesize is not UNSET:
            field_dict["logfilesize"] = logfilesize
        if logcompressiontype is not UNSET:
            field_dict["logcompressiontype"] = logcompressiontype
        if format_ is not UNSET:
            field_dict["format"] = format_
        if default_log_level is not UNSET:
            field_dict["default_log_level"] = default_log_level
        if rotatecount is not UNSET:
            field_dict["rotatecount"] = rotatecount
        if enable_remote is not UNSET:
            field_dict["enable_remote"] = enable_remote
        if remoteserver is not UNSET:
            field_dict["remoteserver"] = remoteserver
        if remoteserver2 is not UNSET:
            field_dict["remoteserver2"] = remoteserver2
        if remoteserver3 is not UNSET:
            field_dict["remoteserver3"] = remoteserver3
        if sourceip is not UNSET:
            field_dict["sourceip"] = sourceip
        if ipproto is not UNSET:
            field_dict["ipproto"] = ipproto
        if logall is not UNSET:
            field_dict["logall"] = logall
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if dhcp is not UNSET:
            field_dict["dhcp"] = dhcp
        if auth is not UNSET:
            field_dict["auth"] = auth
        if portalauth is not UNSET:
            field_dict["portalauth"] = portalauth
        if vpn is not UNSET:
            field_dict["vpn"] = vpn
        if dpinger is not UNSET:
            field_dict["dpinger"] = dpinger
        if hostapd is not UNSET:
            field_dict["hostapd"] = hostapd
        if system is not UNSET:
            field_dict["system"] = system
        if pfnet_controller is not UNSET:
            field_dict["pfnet_controller"] = pfnet_controller
        if resolver is not UNSET:
            field_dict["resolver"] = resolver
        if ppp is not UNSET:
            field_dict["ppp"] = ppp
        if routing is not UNSET:
            field_dict["routing"] = routing
        if ntpd is not UNSET:
            field_dict["ntpd"] = ntpd
        if disablelocallogging is not UNSET:
            field_dict["disablelocallogging"] = disablelocallogging
        if rawfilter is not UNSET:
            field_dict["rawfilter"] = rawfilter
        if showfilterdescrips is not UNSET:
            field_dict["showfilterdescrips"] = showfilterdescrips
        if logipoptions is not UNSET:
            field_dict["logipoptions"] = logipoptions
        if logdefaultblock is not UNSET:
            field_dict["logdefaultblock"] = logdefaultblock
        if logdefaultpass is not UNSET:
            field_dict["logdefaultpass"] = logdefaultpass
        if logbogons is not UNSET:
            field_dict["logbogons"] = logbogons
        if logprivatenets is not UNSET:
            field_dict["logprivatenets"] = logprivatenets
        if loglinklocal4 is not UNSET:
            field_dict["loglinklocal4"] = loglinklocal4
        if logids is not UNSET:
            field_dict["logids"] = logids
        if lognginx is not UNSET:
            field_dict["lognginx"] = lognginx
        if logconfigchanges is not UNSET:
            field_dict["logconfigchanges"] = logconfigchanges
        if source_addresses is not UNSET:
            field_dict["source_addresses"] = source_addresses
        if syslog_levels is not UNSET:
            field_dict["syslog_levels"] = syslog_levels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_value import TextValue

        d = dict(src_dict)
        reverse = d.pop("reverse", UNSET)

        nentries = d.pop("nentries", UNSET)

        logfilesize = d.pop("logfilesize", UNSET)

        logcompressiontype = d.pop("logcompressiontype", UNSET)

        format_ = d.pop("format", UNSET)

        default_log_level = d.pop("default_log_level", UNSET)

        rotatecount = d.pop("rotatecount", UNSET)

        enable_remote = d.pop("enable_remote", UNSET)

        remoteserver = d.pop("remoteserver", UNSET)

        remoteserver2 = d.pop("remoteserver2", UNSET)

        remoteserver3 = d.pop("remoteserver3", UNSET)

        sourceip = d.pop("sourceip", UNSET)

        ipproto = d.pop("ipproto", UNSET)

        logall = d.pop("logall", UNSET)

        filter_ = d.pop("filter", UNSET)

        dhcp = d.pop("dhcp", UNSET)

        auth = d.pop("auth", UNSET)

        portalauth = d.pop("portalauth", UNSET)

        vpn = d.pop("vpn", UNSET)

        dpinger = d.pop("dpinger", UNSET)

        hostapd = d.pop("hostapd", UNSET)

        system = d.pop("system", UNSET)

        pfnet_controller = d.pop("pfnet_controller", UNSET)

        resolver = d.pop("resolver", UNSET)

        ppp = d.pop("ppp", UNSET)

        routing = d.pop("routing", UNSET)

        ntpd = d.pop("ntpd", UNSET)

        disablelocallogging = d.pop("disablelocallogging", UNSET)

        rawfilter = d.pop("rawfilter", UNSET)

        showfilterdescrips = d.pop("showfilterdescrips", UNSET)

        logipoptions = d.pop("logipoptions", UNSET)

        logdefaultblock = d.pop("logdefaultblock", UNSET)

        logdefaultpass = d.pop("logdefaultpass", UNSET)

        logbogons = d.pop("logbogons", UNSET)

        logprivatenets = d.pop("logprivatenets", UNSET)

        loglinklocal4 = d.pop("loglinklocal4", UNSET)

        logids = d.pop("logids", UNSET)

        lognginx = d.pop("lognginx", UNSET)

        logconfigchanges = d.pop("logconfigchanges", UNSET)

        _source_addresses = d.pop("source_addresses", UNSET)
        source_addresses: list[TextValue] | Unset = UNSET
        if _source_addresses is not UNSET:
            source_addresses = []
            for source_addresses_item_data in _source_addresses:
                source_addresses_item = TextValue.from_dict(source_addresses_item_data)

                source_addresses.append(source_addresses_item)

        _syslog_levels = d.pop("syslog_levels", UNSET)
        syslog_levels: list[TextValue] | Unset = UNSET
        if _syslog_levels is not UNSET:
            syslog_levels = []
            for syslog_levels_item_data in _syslog_levels:
                syslog_levels_item = TextValue.from_dict(syslog_levels_item_data)

                syslog_levels.append(syslog_levels_item)

        syslog_configuration = cls(
            reverse=reverse,
            nentries=nentries,
            logfilesize=logfilesize,
            logcompressiontype=logcompressiontype,
            format_=format_,
            default_log_level=default_log_level,
            rotatecount=rotatecount,
            enable_remote=enable_remote,
            remoteserver=remoteserver,
            remoteserver2=remoteserver2,
            remoteserver3=remoteserver3,
            sourceip=sourceip,
            ipproto=ipproto,
            logall=logall,
            filter_=filter_,
            dhcp=dhcp,
            auth=auth,
            portalauth=portalauth,
            vpn=vpn,
            dpinger=dpinger,
            hostapd=hostapd,
            system=system,
            pfnet_controller=pfnet_controller,
            resolver=resolver,
            ppp=ppp,
            routing=routing,
            ntpd=ntpd,
            disablelocallogging=disablelocallogging,
            rawfilter=rawfilter,
            showfilterdescrips=showfilterdescrips,
            logipoptions=logipoptions,
            logdefaultblock=logdefaultblock,
            logdefaultpass=logdefaultpass,
            logbogons=logbogons,
            logprivatenets=logprivatenets,
            loglinklocal4=loglinklocal4,
            logids=logids,
            lognginx=lognginx,
            logconfigchanges=logconfigchanges,
            source_addresses=source_addresses,
            syslog_levels=syslog_levels,
        )

        syslog_configuration.additional_properties = d
        return syslog_configuration

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
