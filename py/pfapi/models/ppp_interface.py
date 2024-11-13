from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PPPInterface")


@_attrs_define
class PPPInterface:
    """
    Attributes:
        ptpid (Union[Unset, str]):
        type (Union[Unset, str]):
        if_ (Union[Unset, str]):
        ports (Union[Unset, str]):
        portslist (Union[Unset, List[str]]):
        phone (Union[Unset, str]):
        apn (Union[Unset, str]):
        apnum (Union[Unset, str]):
        simpin (Union[Unset, str]):
        country (Union[Unset, str]):
        provider (Union[Unset, str]):
        provider_list (Union[Unset, str]):
        providerplan (Union[Unset, str]):
        pin_wait (Union[Unset, str]):
        initstr (Union[Unset, str]):
        connect_timeout (Union[Unset, str]):
        uptime (Union[Unset, bool]):
        username (Union[Unset, str]):
        ppp_username (Union[Unset, str]):
        ppp_password (Union[Unset, str]):
        pppoe_password (Union[Unset, str]):
        pppoe_username (Union[Unset, str]):
        password (Union[Unset, str]):
        ondemand (Union[Unset, bool]):
        idletimeout (Union[Unset, str]):
        pppoe_idletimeout (Union[Unset, str]):
        descr (Union[Unset, str]):
        localip (Union[Unset, str]):
        gateway (Union[Unset, str]):
        pppoe_reset_type (Union[Unset, str]):
        pppoe_resethour (Union[Unset, str]):
        pppoe_resetminute (Union[Unset, str]):
        pppoe_resetdate (Union[Unset, str]):
        pppoe_pr_preset_val (Union[Unset, str]):
        pppoe_dialondemand (Union[Unset, bool]):
        hostuniq (Union[Unset, str]):
        pptp_dialondemand (Union[Unset, bool]):
        pptp_idletimeout (Union[Unset, str]):
        pptp_local0 (Union[Unset, str]):
        pptp_password (Union[Unset, str]):
        pptp_remote0 (Union[Unset, str]):
        pptp_username (Union[Unset, str]):
        l2tp_secret (Union[Unset, str]):
        shortseq (Union[Unset, bool]):
        acfcomp (Union[Unset, bool]):
        protocomp (Union[Unset, bool]):
        pppoe_multilink_over_singlelink (Union[Unset, bool]):
        mtu_override (Union[Unset, bool]):
        vjcomp (Union[Unset, bool]):
        tcpmssfix (Union[Unset, bool]):
        secret (Union[Unset, str]):
        bandwidth (Union[Unset, str]):
        mtu (Union[Unset, str]):
        mru (Union[Unset, str]):
        mrru (Union[Unset, str]):
        port (Union[Unset, str]):
    """

    ptpid: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    if_: Union[Unset, str] = UNSET
    ports: Union[Unset, str] = UNSET
    portslist: Union[Unset, List[str]] = UNSET
    phone: Union[Unset, str] = UNSET
    apn: Union[Unset, str] = UNSET
    apnum: Union[Unset, str] = UNSET
    simpin: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    provider_list: Union[Unset, str] = UNSET
    providerplan: Union[Unset, str] = UNSET
    pin_wait: Union[Unset, str] = UNSET
    initstr: Union[Unset, str] = UNSET
    connect_timeout: Union[Unset, str] = UNSET
    uptime: Union[Unset, bool] = UNSET
    username: Union[Unset, str] = UNSET
    ppp_username: Union[Unset, str] = UNSET
    ppp_password: Union[Unset, str] = UNSET
    pppoe_password: Union[Unset, str] = UNSET
    pppoe_username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    ondemand: Union[Unset, bool] = UNSET
    idletimeout: Union[Unset, str] = UNSET
    pppoe_idletimeout: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    localip: Union[Unset, str] = UNSET
    gateway: Union[Unset, str] = UNSET
    pppoe_reset_type: Union[Unset, str] = UNSET
    pppoe_resethour: Union[Unset, str] = UNSET
    pppoe_resetminute: Union[Unset, str] = UNSET
    pppoe_resetdate: Union[Unset, str] = UNSET
    pppoe_pr_preset_val: Union[Unset, str] = UNSET
    pppoe_dialondemand: Union[Unset, bool] = UNSET
    hostuniq: Union[Unset, str] = UNSET
    pptp_dialondemand: Union[Unset, bool] = UNSET
    pptp_idletimeout: Union[Unset, str] = UNSET
    pptp_local0: Union[Unset, str] = UNSET
    pptp_password: Union[Unset, str] = UNSET
    pptp_remote0: Union[Unset, str] = UNSET
    pptp_username: Union[Unset, str] = UNSET
    l2tp_secret: Union[Unset, str] = UNSET
    shortseq: Union[Unset, bool] = UNSET
    acfcomp: Union[Unset, bool] = UNSET
    protocomp: Union[Unset, bool] = UNSET
    pppoe_multilink_over_singlelink: Union[Unset, bool] = UNSET
    mtu_override: Union[Unset, bool] = UNSET
    vjcomp: Union[Unset, bool] = UNSET
    tcpmssfix: Union[Unset, bool] = UNSET
    secret: Union[Unset, str] = UNSET
    bandwidth: Union[Unset, str] = UNSET
    mtu: Union[Unset, str] = UNSET
    mru: Union[Unset, str] = UNSET
    mrru: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ptpid = self.ptpid

        type = self.type

        if_ = self.if_

        ports = self.ports

        portslist: Union[Unset, List[str]] = UNSET
        if not isinstance(self.portslist, Unset):
            portslist = self.portslist

        phone = self.phone

        apn = self.apn

        apnum = self.apnum

        simpin = self.simpin

        country = self.country

        provider = self.provider

        provider_list = self.provider_list

        providerplan = self.providerplan

        pin_wait = self.pin_wait

        initstr = self.initstr

        connect_timeout = self.connect_timeout

        uptime = self.uptime

        username = self.username

        ppp_username = self.ppp_username

        ppp_password = self.ppp_password

        pppoe_password = self.pppoe_password

        pppoe_username = self.pppoe_username

        password = self.password

        ondemand = self.ondemand

        idletimeout = self.idletimeout

        pppoe_idletimeout = self.pppoe_idletimeout

        descr = self.descr

        localip = self.localip

        gateway = self.gateway

        pppoe_reset_type = self.pppoe_reset_type

        pppoe_resethour = self.pppoe_resethour

        pppoe_resetminute = self.pppoe_resetminute

        pppoe_resetdate = self.pppoe_resetdate

        pppoe_pr_preset_val = self.pppoe_pr_preset_val

        pppoe_dialondemand = self.pppoe_dialondemand

        hostuniq = self.hostuniq

        pptp_dialondemand = self.pptp_dialondemand

        pptp_idletimeout = self.pptp_idletimeout

        pptp_local0 = self.pptp_local0

        pptp_password = self.pptp_password

        pptp_remote0 = self.pptp_remote0

        pptp_username = self.pptp_username

        l2tp_secret = self.l2tp_secret

        shortseq = self.shortseq

        acfcomp = self.acfcomp

        protocomp = self.protocomp

        pppoe_multilink_over_singlelink = self.pppoe_multilink_over_singlelink

        mtu_override = self.mtu_override

        vjcomp = self.vjcomp

        tcpmssfix = self.tcpmssfix

        secret = self.secret

        bandwidth = self.bandwidth

        mtu = self.mtu

        mru = self.mru

        mrru = self.mrru

        port = self.port

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ptpid is not UNSET:
            field_dict["ptpid"] = ptpid
        if type is not UNSET:
            field_dict["type"] = type
        if if_ is not UNSET:
            field_dict["if"] = if_
        if ports is not UNSET:
            field_dict["ports"] = ports
        if portslist is not UNSET:
            field_dict["portslist"] = portslist
        if phone is not UNSET:
            field_dict["phone"] = phone
        if apn is not UNSET:
            field_dict["apn"] = apn
        if apnum is not UNSET:
            field_dict["apnum"] = apnum
        if simpin is not UNSET:
            field_dict["simpin"] = simpin
        if country is not UNSET:
            field_dict["country"] = country
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_list is not UNSET:
            field_dict["provider_list"] = provider_list
        if providerplan is not UNSET:
            field_dict["providerplan"] = providerplan
        if pin_wait is not UNSET:
            field_dict["pin_wait"] = pin_wait
        if initstr is not UNSET:
            field_dict["initstr"] = initstr
        if connect_timeout is not UNSET:
            field_dict["connect_timeout"] = connect_timeout
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if username is not UNSET:
            field_dict["username"] = username
        if ppp_username is not UNSET:
            field_dict["ppp_username"] = ppp_username
        if ppp_password is not UNSET:
            field_dict["ppp_password"] = ppp_password
        if pppoe_password is not UNSET:
            field_dict["pppoe_password"] = pppoe_password
        if pppoe_username is not UNSET:
            field_dict["pppoe_username"] = pppoe_username
        if password is not UNSET:
            field_dict["password"] = password
        if ondemand is not UNSET:
            field_dict["ondemand"] = ondemand
        if idletimeout is not UNSET:
            field_dict["idletimeout"] = idletimeout
        if pppoe_idletimeout is not UNSET:
            field_dict["pppoe_idletimeout"] = pppoe_idletimeout
        if descr is not UNSET:
            field_dict["descr"] = descr
        if localip is not UNSET:
            field_dict["localip"] = localip
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if pppoe_reset_type is not UNSET:
            field_dict["pppoe_reset_type"] = pppoe_reset_type
        if pppoe_resethour is not UNSET:
            field_dict["pppoe_resethour"] = pppoe_resethour
        if pppoe_resetminute is not UNSET:
            field_dict["pppoe_resetminute"] = pppoe_resetminute
        if pppoe_resetdate is not UNSET:
            field_dict["pppoe_resetdate"] = pppoe_resetdate
        if pppoe_pr_preset_val is not UNSET:
            field_dict["pppoe_pr_preset_val"] = pppoe_pr_preset_val
        if pppoe_dialondemand is not UNSET:
            field_dict["pppoe_dialondemand"] = pppoe_dialondemand
        if hostuniq is not UNSET:
            field_dict["hostuniq"] = hostuniq
        if pptp_dialondemand is not UNSET:
            field_dict["pptp_dialondemand"] = pptp_dialondemand
        if pptp_idletimeout is not UNSET:
            field_dict["pptp_idletimeout"] = pptp_idletimeout
        if pptp_local0 is not UNSET:
            field_dict["pptp_local0"] = pptp_local0
        if pptp_password is not UNSET:
            field_dict["pptp_password"] = pptp_password
        if pptp_remote0 is not UNSET:
            field_dict["pptp_remote0"] = pptp_remote0
        if pptp_username is not UNSET:
            field_dict["pptp_username"] = pptp_username
        if l2tp_secret is not UNSET:
            field_dict["l2tp_secret"] = l2tp_secret
        if shortseq is not UNSET:
            field_dict["shortseq"] = shortseq
        if acfcomp is not UNSET:
            field_dict["acfcomp"] = acfcomp
        if protocomp is not UNSET:
            field_dict["protocomp"] = protocomp
        if pppoe_multilink_over_singlelink is not UNSET:
            field_dict["pppoe_multilink_over_singlelink"] = pppoe_multilink_over_singlelink
        if mtu_override is not UNSET:
            field_dict["mtu_override"] = mtu_override
        if vjcomp is not UNSET:
            field_dict["vjcomp"] = vjcomp
        if tcpmssfix is not UNSET:
            field_dict["tcpmssfix"] = tcpmssfix
        if secret is not UNSET:
            field_dict["secret"] = secret
        if bandwidth is not UNSET:
            field_dict["bandwidth"] = bandwidth
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if mru is not UNSET:
            field_dict["mru"] = mru
        if mrru is not UNSET:
            field_dict["mrru"] = mrru
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ptpid = d.pop("ptpid", UNSET)

        type = d.pop("type", UNSET)

        if_ = d.pop("if", UNSET)

        ports = d.pop("ports", UNSET)

        portslist = cast(List[str], d.pop("portslist", UNSET))

        phone = d.pop("phone", UNSET)

        apn = d.pop("apn", UNSET)

        apnum = d.pop("apnum", UNSET)

        simpin = d.pop("simpin", UNSET)

        country = d.pop("country", UNSET)

        provider = d.pop("provider", UNSET)

        provider_list = d.pop("provider_list", UNSET)

        providerplan = d.pop("providerplan", UNSET)

        pin_wait = d.pop("pin_wait", UNSET)

        initstr = d.pop("initstr", UNSET)

        connect_timeout = d.pop("connect_timeout", UNSET)

        uptime = d.pop("uptime", UNSET)

        username = d.pop("username", UNSET)

        ppp_username = d.pop("ppp_username", UNSET)

        ppp_password = d.pop("ppp_password", UNSET)

        pppoe_password = d.pop("pppoe_password", UNSET)

        pppoe_username = d.pop("pppoe_username", UNSET)

        password = d.pop("password", UNSET)

        ondemand = d.pop("ondemand", UNSET)

        idletimeout = d.pop("idletimeout", UNSET)

        pppoe_idletimeout = d.pop("pppoe_idletimeout", UNSET)

        descr = d.pop("descr", UNSET)

        localip = d.pop("localip", UNSET)

        gateway = d.pop("gateway", UNSET)

        pppoe_reset_type = d.pop("pppoe_reset_type", UNSET)

        pppoe_resethour = d.pop("pppoe_resethour", UNSET)

        pppoe_resetminute = d.pop("pppoe_resetminute", UNSET)

        pppoe_resetdate = d.pop("pppoe_resetdate", UNSET)

        pppoe_pr_preset_val = d.pop("pppoe_pr_preset_val", UNSET)

        pppoe_dialondemand = d.pop("pppoe_dialondemand", UNSET)

        hostuniq = d.pop("hostuniq", UNSET)

        pptp_dialondemand = d.pop("pptp_dialondemand", UNSET)

        pptp_idletimeout = d.pop("pptp_idletimeout", UNSET)

        pptp_local0 = d.pop("pptp_local0", UNSET)

        pptp_password = d.pop("pptp_password", UNSET)

        pptp_remote0 = d.pop("pptp_remote0", UNSET)

        pptp_username = d.pop("pptp_username", UNSET)

        l2tp_secret = d.pop("l2tp_secret", UNSET)

        shortseq = d.pop("shortseq", UNSET)

        acfcomp = d.pop("acfcomp", UNSET)

        protocomp = d.pop("protocomp", UNSET)

        pppoe_multilink_over_singlelink = d.pop("pppoe_multilink_over_singlelink", UNSET)

        mtu_override = d.pop("mtu_override", UNSET)

        vjcomp = d.pop("vjcomp", UNSET)

        tcpmssfix = d.pop("tcpmssfix", UNSET)

        secret = d.pop("secret", UNSET)

        bandwidth = d.pop("bandwidth", UNSET)

        mtu = d.pop("mtu", UNSET)

        mru = d.pop("mru", UNSET)

        mrru = d.pop("mrru", UNSET)

        port = d.pop("port", UNSET)

        ppp_interface = cls(
            ptpid=ptpid,
            type=type,
            if_=if_,
            ports=ports,
            portslist=portslist,
            phone=phone,
            apn=apn,
            apnum=apnum,
            simpin=simpin,
            country=country,
            provider=provider,
            provider_list=provider_list,
            providerplan=providerplan,
            pin_wait=pin_wait,
            initstr=initstr,
            connect_timeout=connect_timeout,
            uptime=uptime,
            username=username,
            ppp_username=ppp_username,
            ppp_password=ppp_password,
            pppoe_password=pppoe_password,
            pppoe_username=pppoe_username,
            password=password,
            ondemand=ondemand,
            idletimeout=idletimeout,
            pppoe_idletimeout=pppoe_idletimeout,
            descr=descr,
            localip=localip,
            gateway=gateway,
            pppoe_reset_type=pppoe_reset_type,
            pppoe_resethour=pppoe_resethour,
            pppoe_resetminute=pppoe_resetminute,
            pppoe_resetdate=pppoe_resetdate,
            pppoe_pr_preset_val=pppoe_pr_preset_val,
            pppoe_dialondemand=pppoe_dialondemand,
            hostuniq=hostuniq,
            pptp_dialondemand=pptp_dialondemand,
            pptp_idletimeout=pptp_idletimeout,
            pptp_local0=pptp_local0,
            pptp_password=pptp_password,
            pptp_remote0=pptp_remote0,
            pptp_username=pptp_username,
            l2tp_secret=l2tp_secret,
            shortseq=shortseq,
            acfcomp=acfcomp,
            protocomp=protocomp,
            pppoe_multilink_over_singlelink=pppoe_multilink_over_singlelink,
            mtu_override=mtu_override,
            vjcomp=vjcomp,
            tcpmssfix=tcpmssfix,
            secret=secret,
            bandwidth=bandwidth,
            mtu=mtu,
            mru=mru,
            mrru=mrru,
            port=port,
        )

        ppp_interface.additional_properties = d
        return ppp_interface

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
