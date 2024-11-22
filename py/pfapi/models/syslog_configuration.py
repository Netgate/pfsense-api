from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyslogConfiguration")


@_attrs_define
class SyslogConfiguration:
    """
    Attributes:
        reverse (Union[Unset, bool]):
        nentries (Union[Unset, int]):
        logfilesize (Union[Unset, int]):
        logcompressiontype (Union[Unset, str]):
        format_ (Union[Unset, str]):
        rotatecount (Union[Unset, int]):
        remoteserver (Union[Unset, str]):
        remoteserver2 (Union[Unset, str]):
        remoteserver3 (Union[Unset, str]):
        sourceip (Union[Unset, str]):
        ipproto (Union[Unset, str]):
        filter_ (Union[Unset, bool]):
        dhcp (Union[Unset, bool]):
        auth (Union[Unset, bool]):
        portalauth (Union[Unset, bool]):
        vpn (Union[Unset, bool]):
        dpinger (Union[Unset, bool]):
        hostapd (Union[Unset, bool]):
        logall (Union[Unset, bool]):
        system (Union[Unset, bool]):
        pfnet_controller (Union[Unset, bool]):
        resolver (Union[Unset, bool]):
        ppp (Union[Unset, bool]):
        routing (Union[Unset, bool]):
        ntpd (Union[Unset, bool]):
        disablelocallogging (Union[Unset, bool]):
        logconfigchanges (Union[Unset, bool]):
        enable (Union[Unset, bool]):
        logdefaultblock (Union[Unset, bool]):
        logdefaultpass (Union[Unset, bool]):
        logbogons (Union[Unset, bool]):
        logprivatenets (Union[Unset, bool]):
        lognginx (Union[Unset, bool]):
        rawfilter (Union[Unset, bool]):
        filterdescriptions (Union[Unset, int]):
    """

    reverse: Union[Unset, bool] = UNSET
    nentries: Union[Unset, int] = UNSET
    logfilesize: Union[Unset, int] = UNSET
    logcompressiontype: Union[Unset, str] = UNSET
    format_: Union[Unset, str] = UNSET
    rotatecount: Union[Unset, int] = UNSET
    remoteserver: Union[Unset, str] = UNSET
    remoteserver2: Union[Unset, str] = UNSET
    remoteserver3: Union[Unset, str] = UNSET
    sourceip: Union[Unset, str] = UNSET
    ipproto: Union[Unset, str] = UNSET
    filter_: Union[Unset, bool] = UNSET
    dhcp: Union[Unset, bool] = UNSET
    auth: Union[Unset, bool] = UNSET
    portalauth: Union[Unset, bool] = UNSET
    vpn: Union[Unset, bool] = UNSET
    dpinger: Union[Unset, bool] = UNSET
    hostapd: Union[Unset, bool] = UNSET
    logall: Union[Unset, bool] = UNSET
    system: Union[Unset, bool] = UNSET
    pfnet_controller: Union[Unset, bool] = UNSET
    resolver: Union[Unset, bool] = UNSET
    ppp: Union[Unset, bool] = UNSET
    routing: Union[Unset, bool] = UNSET
    ntpd: Union[Unset, bool] = UNSET
    disablelocallogging: Union[Unset, bool] = UNSET
    logconfigchanges: Union[Unset, bool] = UNSET
    enable: Union[Unset, bool] = UNSET
    logdefaultblock: Union[Unset, bool] = UNSET
    logdefaultpass: Union[Unset, bool] = UNSET
    logbogons: Union[Unset, bool] = UNSET
    logprivatenets: Union[Unset, bool] = UNSET
    lognginx: Union[Unset, bool] = UNSET
    rawfilter: Union[Unset, bool] = UNSET
    filterdescriptions: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reverse = self.reverse

        nentries = self.nentries

        logfilesize = self.logfilesize

        logcompressiontype = self.logcompressiontype

        format_ = self.format_

        rotatecount = self.rotatecount

        remoteserver = self.remoteserver

        remoteserver2 = self.remoteserver2

        remoteserver3 = self.remoteserver3

        sourceip = self.sourceip

        ipproto = self.ipproto

        filter_ = self.filter_

        dhcp = self.dhcp

        auth = self.auth

        portalauth = self.portalauth

        vpn = self.vpn

        dpinger = self.dpinger

        hostapd = self.hostapd

        logall = self.logall

        system = self.system

        pfnet_controller = self.pfnet_controller

        resolver = self.resolver

        ppp = self.ppp

        routing = self.routing

        ntpd = self.ntpd

        disablelocallogging = self.disablelocallogging

        logconfigchanges = self.logconfigchanges

        enable = self.enable

        logdefaultblock = self.logdefaultblock

        logdefaultpass = self.logdefaultpass

        logbogons = self.logbogons

        logprivatenets = self.logprivatenets

        lognginx = self.lognginx

        rawfilter = self.rawfilter

        filterdescriptions = self.filterdescriptions

        field_dict: Dict[str, Any] = {}
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
        if rotatecount is not UNSET:
            field_dict["rotatecount"] = rotatecount
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
        if logall is not UNSET:
            field_dict["logall"] = logall
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
        if logconfigchanges is not UNSET:
            field_dict["logconfigchanges"] = logconfigchanges
        if enable is not UNSET:
            field_dict["enable"] = enable
        if logdefaultblock is not UNSET:
            field_dict["logdefaultblock"] = logdefaultblock
        if logdefaultpass is not UNSET:
            field_dict["logdefaultpass"] = logdefaultpass
        if logbogons is not UNSET:
            field_dict["logbogons"] = logbogons
        if logprivatenets is not UNSET:
            field_dict["logprivatenets"] = logprivatenets
        if lognginx is not UNSET:
            field_dict["lognginx"] = lognginx
        if rawfilter is not UNSET:
            field_dict["rawfilter"] = rawfilter
        if filterdescriptions is not UNSET:
            field_dict["filterdescriptions"] = filterdescriptions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reverse = d.pop("reverse", UNSET)

        nentries = d.pop("nentries", UNSET)

        logfilesize = d.pop("logfilesize", UNSET)

        logcompressiontype = d.pop("logcompressiontype", UNSET)

        format_ = d.pop("format", UNSET)

        rotatecount = d.pop("rotatecount", UNSET)

        remoteserver = d.pop("remoteserver", UNSET)

        remoteserver2 = d.pop("remoteserver2", UNSET)

        remoteserver3 = d.pop("remoteserver3", UNSET)

        sourceip = d.pop("sourceip", UNSET)

        ipproto = d.pop("ipproto", UNSET)

        filter_ = d.pop("filter", UNSET)

        dhcp = d.pop("dhcp", UNSET)

        auth = d.pop("auth", UNSET)

        portalauth = d.pop("portalauth", UNSET)

        vpn = d.pop("vpn", UNSET)

        dpinger = d.pop("dpinger", UNSET)

        hostapd = d.pop("hostapd", UNSET)

        logall = d.pop("logall", UNSET)

        system = d.pop("system", UNSET)

        pfnet_controller = d.pop("pfnet_controller", UNSET)

        resolver = d.pop("resolver", UNSET)

        ppp = d.pop("ppp", UNSET)

        routing = d.pop("routing", UNSET)

        ntpd = d.pop("ntpd", UNSET)

        disablelocallogging = d.pop("disablelocallogging", UNSET)

        logconfigchanges = d.pop("logconfigchanges", UNSET)

        enable = d.pop("enable", UNSET)

        logdefaultblock = d.pop("logdefaultblock", UNSET)

        logdefaultpass = d.pop("logdefaultpass", UNSET)

        logbogons = d.pop("logbogons", UNSET)

        logprivatenets = d.pop("logprivatenets", UNSET)

        lognginx = d.pop("lognginx", UNSET)

        rawfilter = d.pop("rawfilter", UNSET)

        filterdescriptions = d.pop("filterdescriptions", UNSET)

        syslog_configuration = cls(
            reverse=reverse,
            nentries=nentries,
            logfilesize=logfilesize,
            logcompressiontype=logcompressiontype,
            format_=format_,
            rotatecount=rotatecount,
            remoteserver=remoteserver,
            remoteserver2=remoteserver2,
            remoteserver3=remoteserver3,
            sourceip=sourceip,
            ipproto=ipproto,
            filter_=filter_,
            dhcp=dhcp,
            auth=auth,
            portalauth=portalauth,
            vpn=vpn,
            dpinger=dpinger,
            hostapd=hostapd,
            logall=logall,
            system=system,
            pfnet_controller=pfnet_controller,
            resolver=resolver,
            ppp=ppp,
            routing=routing,
            ntpd=ntpd,
            disablelocallogging=disablelocallogging,
            logconfigchanges=logconfigchanges,
            enable=enable,
            logdefaultblock=logdefaultblock,
            logdefaultpass=logdefaultpass,
            logbogons=logbogons,
            logprivatenets=logprivatenets,
            lognginx=lognginx,
            rawfilter=rawfilter,
            filterdescriptions=filterdescriptions,
        )

        syslog_configuration.additional_properties = d
        return syslog_configuration

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
