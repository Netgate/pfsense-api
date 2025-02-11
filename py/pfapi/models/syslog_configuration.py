from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SyslogConfiguration")


@_attrs_define
class SyslogConfiguration:
    """
    Attributes:
        reverse (bool):
        nentries (int):
        logfilesize (int):
        logcompressiontype (str):
        format_ (str):
        rotatecount (int):
        remoteserver (str):
        remoteserver2 (str):
        remoteserver3 (str):
        sourceip (str):
        ipproto (str):
        filter_ (bool):
        dhcp (bool):
        auth (bool):
        portalauth (bool):
        vpn (bool):
        dpinger (bool):
        hostapd (bool):
        logall (bool):
        system (bool):
        pfnet_controller (bool):
        resolver (bool):
        ppp (bool):
        routing (bool):
        ntpd (bool):
        disablelocallogging (bool):
        logconfigchanges (bool):
        enable (bool):
        logdefaultblock (bool):
        logdefaultpass (bool):
        logbogons (bool):
        logprivatenets (bool):
        lognginx (bool):
        rawfilter (bool):
        filterdescriptions (int):
    """

    reverse: bool
    nentries: int
    logfilesize: int
    logcompressiontype: str
    format_: str
    rotatecount: int
    remoteserver: str
    remoteserver2: str
    remoteserver3: str
    sourceip: str
    ipproto: str
    filter_: bool
    dhcp: bool
    auth: bool
    portalauth: bool
    vpn: bool
    dpinger: bool
    hostapd: bool
    logall: bool
    system: bool
    pfnet_controller: bool
    resolver: bool
    ppp: bool
    routing: bool
    ntpd: bool
    disablelocallogging: bool
    logconfigchanges: bool
    enable: bool
    logdefaultblock: bool
    logdefaultpass: bool
    logbogons: bool
    logprivatenets: bool
    lognginx: bool
    rawfilter: bool
    filterdescriptions: int
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
        field_dict.update(
            {
                "reverse": reverse,
                "nentries": nentries,
                "logfilesize": logfilesize,
                "logcompressiontype": logcompressiontype,
                "format": format_,
                "rotatecount": rotatecount,
                "remoteserver": remoteserver,
                "remoteserver2": remoteserver2,
                "remoteserver3": remoteserver3,
                "sourceip": sourceip,
                "ipproto": ipproto,
                "filter": filter_,
                "dhcp": dhcp,
                "auth": auth,
                "portalauth": portalauth,
                "vpn": vpn,
                "dpinger": dpinger,
                "hostapd": hostapd,
                "logall": logall,
                "system": system,
                "pfnet_controller": pfnet_controller,
                "resolver": resolver,
                "ppp": ppp,
                "routing": routing,
                "ntpd": ntpd,
                "disablelocallogging": disablelocallogging,
                "logconfigchanges": logconfigchanges,
                "enable": enable,
                "logdefaultblock": logdefaultblock,
                "logdefaultpass": logdefaultpass,
                "logbogons": logbogons,
                "logprivatenets": logprivatenets,
                "lognginx": lognginx,
                "rawfilter": rawfilter,
                "filterdescriptions": filterdescriptions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reverse = d.pop("reverse")

        nentries = d.pop("nentries")

        logfilesize = d.pop("logfilesize")

        logcompressiontype = d.pop("logcompressiontype")

        format_ = d.pop("format")

        rotatecount = d.pop("rotatecount")

        remoteserver = d.pop("remoteserver")

        remoteserver2 = d.pop("remoteserver2")

        remoteserver3 = d.pop("remoteserver3")

        sourceip = d.pop("sourceip")

        ipproto = d.pop("ipproto")

        filter_ = d.pop("filter")

        dhcp = d.pop("dhcp")

        auth = d.pop("auth")

        portalauth = d.pop("portalauth")

        vpn = d.pop("vpn")

        dpinger = d.pop("dpinger")

        hostapd = d.pop("hostapd")

        logall = d.pop("logall")

        system = d.pop("system")

        pfnet_controller = d.pop("pfnet_controller")

        resolver = d.pop("resolver")

        ppp = d.pop("ppp")

        routing = d.pop("routing")

        ntpd = d.pop("ntpd")

        disablelocallogging = d.pop("disablelocallogging")

        logconfigchanges = d.pop("logconfigchanges")

        enable = d.pop("enable")

        logdefaultblock = d.pop("logdefaultblock")

        logdefaultpass = d.pop("logdefaultpass")

        logbogons = d.pop("logbogons")

        logprivatenets = d.pop("logprivatenets")

        lognginx = d.pop("lognginx")

        rawfilter = d.pop("rawfilter")

        filterdescriptions = d.pop("filterdescriptions")

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
