from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvFirewall")


@_attrs_define
class AdvFirewall:
    """
    Attributes:
        adaptiveend (str | Unset):
        adaptivestart (str | Unset):
        aliasesresolveinterval (str | Unset):
        bogonsinterval (str | Unset):
        bypassstaticroutes (bool | Unset):
        checkaliasesurlcert (bool | Unset):
        disablefilter (bool | Unset):
        disablenegate (bool | Unset):
        disablereplyto (bool | Unset):
        disablescrub (bool | Unset):
        disablevpnrules (bool | Unset):
        enablebinatreflection (bool | Unset):
        enablenatreflectionhelper (bool | Unset):
        enableethfilter (bool | Unset):
        icmperrortimeout (str | Unset):
        icmpfirsttimeout (str | Unset):
        maximumfrags (str | Unset):
        maximumstates (str | Unset):
        maximumtableentries (str | Unset):
        maxmss (str | Unset):
        maxmss_enable (bool | Unset):
        vpn_fragment_reassemble (bool | Unset):
        natreflection (str | Unset):
        no_apipa_block (bool | Unset):
        optimization (str | Unset):
        otherfirsttimeout (str | Unset):
        othermultipletimeout (str | Unset):
        othersingletimeout (str | Unset):
        reflectiontimeout (str | Unset):
        scrubnodf (bool | Unset):
        scrubrnid (bool | Unset):
        sctpfirsttimeout (str | Unset):
        sctpopeningtimeout (str | Unset):
        sctpestablishedtimeout (str | Unset):
        sctpclosingtimeout (str | Unset):
        sctpclosedtimeout (str | Unset):
        statepolicy (str | Unset):
        tcpclosedtimeout (str | Unset):
        tcpclosingtimeout (str | Unset):
        tcpestablishedtimeout (str | Unset):
        tcpfinwaittimeout (str | Unset):
        tcpfirsttimeout (str | Unset):
        tcpopeningtimeout (str | Unset):
        tcptsdifftimeout (str | Unset):
        tftpinterface (list[str] | Unset):
        udpfirsttimeout (str | Unset):
        udpmultipletimeout (str | Unset):
        udpsingletimeout (str | Unset):
        allow_nat64_prefix_override (bool | Unset): Allow overriding the NAT64 prefix used in rules and services
    """

    adaptiveend: str | Unset = UNSET
    adaptivestart: str | Unset = UNSET
    aliasesresolveinterval: str | Unset = UNSET
    bogonsinterval: str | Unset = UNSET
    bypassstaticroutes: bool | Unset = UNSET
    checkaliasesurlcert: bool | Unset = UNSET
    disablefilter: bool | Unset = UNSET
    disablenegate: bool | Unset = UNSET
    disablereplyto: bool | Unset = UNSET
    disablescrub: bool | Unset = UNSET
    disablevpnrules: bool | Unset = UNSET
    enablebinatreflection: bool | Unset = UNSET
    enablenatreflectionhelper: bool | Unset = UNSET
    enableethfilter: bool | Unset = UNSET
    icmperrortimeout: str | Unset = UNSET
    icmpfirsttimeout: str | Unset = UNSET
    maximumfrags: str | Unset = UNSET
    maximumstates: str | Unset = UNSET
    maximumtableentries: str | Unset = UNSET
    maxmss: str | Unset = UNSET
    maxmss_enable: bool | Unset = UNSET
    vpn_fragment_reassemble: bool | Unset = UNSET
    natreflection: str | Unset = UNSET
    no_apipa_block: bool | Unset = UNSET
    optimization: str | Unset = UNSET
    otherfirsttimeout: str | Unset = UNSET
    othermultipletimeout: str | Unset = UNSET
    othersingletimeout: str | Unset = UNSET
    reflectiontimeout: str | Unset = UNSET
    scrubnodf: bool | Unset = UNSET
    scrubrnid: bool | Unset = UNSET
    sctpfirsttimeout: str | Unset = UNSET
    sctpopeningtimeout: str | Unset = UNSET
    sctpestablishedtimeout: str | Unset = UNSET
    sctpclosingtimeout: str | Unset = UNSET
    sctpclosedtimeout: str | Unset = UNSET
    statepolicy: str | Unset = UNSET
    tcpclosedtimeout: str | Unset = UNSET
    tcpclosingtimeout: str | Unset = UNSET
    tcpestablishedtimeout: str | Unset = UNSET
    tcpfinwaittimeout: str | Unset = UNSET
    tcpfirsttimeout: str | Unset = UNSET
    tcpopeningtimeout: str | Unset = UNSET
    tcptsdifftimeout: str | Unset = UNSET
    tftpinterface: list[str] | Unset = UNSET
    udpfirsttimeout: str | Unset = UNSET
    udpmultipletimeout: str | Unset = UNSET
    udpsingletimeout: str | Unset = UNSET
    allow_nat64_prefix_override: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adaptiveend = self.adaptiveend

        adaptivestart = self.adaptivestart

        aliasesresolveinterval = self.aliasesresolveinterval

        bogonsinterval = self.bogonsinterval

        bypassstaticroutes = self.bypassstaticroutes

        checkaliasesurlcert = self.checkaliasesurlcert

        disablefilter = self.disablefilter

        disablenegate = self.disablenegate

        disablereplyto = self.disablereplyto

        disablescrub = self.disablescrub

        disablevpnrules = self.disablevpnrules

        enablebinatreflection = self.enablebinatreflection

        enablenatreflectionhelper = self.enablenatreflectionhelper

        enableethfilter = self.enableethfilter

        icmperrortimeout = self.icmperrortimeout

        icmpfirsttimeout = self.icmpfirsttimeout

        maximumfrags = self.maximumfrags

        maximumstates = self.maximumstates

        maximumtableentries = self.maximumtableentries

        maxmss = self.maxmss

        maxmss_enable = self.maxmss_enable

        vpn_fragment_reassemble = self.vpn_fragment_reassemble

        natreflection = self.natreflection

        no_apipa_block = self.no_apipa_block

        optimization = self.optimization

        otherfirsttimeout = self.otherfirsttimeout

        othermultipletimeout = self.othermultipletimeout

        othersingletimeout = self.othersingletimeout

        reflectiontimeout = self.reflectiontimeout

        scrubnodf = self.scrubnodf

        scrubrnid = self.scrubrnid

        sctpfirsttimeout = self.sctpfirsttimeout

        sctpopeningtimeout = self.sctpopeningtimeout

        sctpestablishedtimeout = self.sctpestablishedtimeout

        sctpclosingtimeout = self.sctpclosingtimeout

        sctpclosedtimeout = self.sctpclosedtimeout

        statepolicy = self.statepolicy

        tcpclosedtimeout = self.tcpclosedtimeout

        tcpclosingtimeout = self.tcpclosingtimeout

        tcpestablishedtimeout = self.tcpestablishedtimeout

        tcpfinwaittimeout = self.tcpfinwaittimeout

        tcpfirsttimeout = self.tcpfirsttimeout

        tcpopeningtimeout = self.tcpopeningtimeout

        tcptsdifftimeout = self.tcptsdifftimeout

        tftpinterface: list[str] | Unset = UNSET
        if not isinstance(self.tftpinterface, Unset):
            tftpinterface = self.tftpinterface

        udpfirsttimeout = self.udpfirsttimeout

        udpmultipletimeout = self.udpmultipletimeout

        udpsingletimeout = self.udpsingletimeout

        allow_nat64_prefix_override = self.allow_nat64_prefix_override

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adaptiveend is not UNSET:
            field_dict["adaptiveend"] = adaptiveend
        if adaptivestart is not UNSET:
            field_dict["adaptivestart"] = adaptivestart
        if aliasesresolveinterval is not UNSET:
            field_dict["aliasesresolveinterval"] = aliasesresolveinterval
        if bogonsinterval is not UNSET:
            field_dict["bogonsinterval"] = bogonsinterval
        if bypassstaticroutes is not UNSET:
            field_dict["bypassstaticroutes"] = bypassstaticroutes
        if checkaliasesurlcert is not UNSET:
            field_dict["checkaliasesurlcert"] = checkaliasesurlcert
        if disablefilter is not UNSET:
            field_dict["disablefilter"] = disablefilter
        if disablenegate is not UNSET:
            field_dict["disablenegate"] = disablenegate
        if disablereplyto is not UNSET:
            field_dict["disablereplyto"] = disablereplyto
        if disablescrub is not UNSET:
            field_dict["disablescrub"] = disablescrub
        if disablevpnrules is not UNSET:
            field_dict["disablevpnrules"] = disablevpnrules
        if enablebinatreflection is not UNSET:
            field_dict["enablebinatreflection"] = enablebinatreflection
        if enablenatreflectionhelper is not UNSET:
            field_dict["enablenatreflectionhelper"] = enablenatreflectionhelper
        if enableethfilter is not UNSET:
            field_dict["enableethfilter"] = enableethfilter
        if icmperrortimeout is not UNSET:
            field_dict["icmperrortimeout"] = icmperrortimeout
        if icmpfirsttimeout is not UNSET:
            field_dict["icmpfirsttimeout"] = icmpfirsttimeout
        if maximumfrags is not UNSET:
            field_dict["maximumfrags"] = maximumfrags
        if maximumstates is not UNSET:
            field_dict["maximumstates"] = maximumstates
        if maximumtableentries is not UNSET:
            field_dict["maximumtableentries"] = maximumtableentries
        if maxmss is not UNSET:
            field_dict["maxmss"] = maxmss
        if maxmss_enable is not UNSET:
            field_dict["maxmss_enable"] = maxmss_enable
        if vpn_fragment_reassemble is not UNSET:
            field_dict["vpn_fragment_reassemble"] = vpn_fragment_reassemble
        if natreflection is not UNSET:
            field_dict["natreflection"] = natreflection
        if no_apipa_block is not UNSET:
            field_dict["no_apipa_block"] = no_apipa_block
        if optimization is not UNSET:
            field_dict["optimization"] = optimization
        if otherfirsttimeout is not UNSET:
            field_dict["otherfirsttimeout"] = otherfirsttimeout
        if othermultipletimeout is not UNSET:
            field_dict["othermultipletimeout"] = othermultipletimeout
        if othersingletimeout is not UNSET:
            field_dict["othersingletimeout"] = othersingletimeout
        if reflectiontimeout is not UNSET:
            field_dict["reflectiontimeout"] = reflectiontimeout
        if scrubnodf is not UNSET:
            field_dict["scrubnodf"] = scrubnodf
        if scrubrnid is not UNSET:
            field_dict["scrubrnid"] = scrubrnid
        if sctpfirsttimeout is not UNSET:
            field_dict["sctpfirsttimeout"] = sctpfirsttimeout
        if sctpopeningtimeout is not UNSET:
            field_dict["sctpopeningtimeout"] = sctpopeningtimeout
        if sctpestablishedtimeout is not UNSET:
            field_dict["sctpestablishedtimeout"] = sctpestablishedtimeout
        if sctpclosingtimeout is not UNSET:
            field_dict["sctpclosingtimeout"] = sctpclosingtimeout
        if sctpclosedtimeout is not UNSET:
            field_dict["sctpclosedtimeout"] = sctpclosedtimeout
        if statepolicy is not UNSET:
            field_dict["statepolicy"] = statepolicy
        if tcpclosedtimeout is not UNSET:
            field_dict["tcpclosedtimeout"] = tcpclosedtimeout
        if tcpclosingtimeout is not UNSET:
            field_dict["tcpclosingtimeout"] = tcpclosingtimeout
        if tcpestablishedtimeout is not UNSET:
            field_dict["tcpestablishedtimeout"] = tcpestablishedtimeout
        if tcpfinwaittimeout is not UNSET:
            field_dict["tcpfinwaittimeout"] = tcpfinwaittimeout
        if tcpfirsttimeout is not UNSET:
            field_dict["tcpfirsttimeout"] = tcpfirsttimeout
        if tcpopeningtimeout is not UNSET:
            field_dict["tcpopeningtimeout"] = tcpopeningtimeout
        if tcptsdifftimeout is not UNSET:
            field_dict["tcptsdifftimeout"] = tcptsdifftimeout
        if tftpinterface is not UNSET:
            field_dict["tftpinterface"] = tftpinterface
        if udpfirsttimeout is not UNSET:
            field_dict["udpfirsttimeout"] = udpfirsttimeout
        if udpmultipletimeout is not UNSET:
            field_dict["udpmultipletimeout"] = udpmultipletimeout
        if udpsingletimeout is not UNSET:
            field_dict["udpsingletimeout"] = udpsingletimeout
        if allow_nat64_prefix_override is not UNSET:
            field_dict["allow_nat64_prefix_override"] = allow_nat64_prefix_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        adaptiveend = d.pop("adaptiveend", UNSET)

        adaptivestart = d.pop("adaptivestart", UNSET)

        aliasesresolveinterval = d.pop("aliasesresolveinterval", UNSET)

        bogonsinterval = d.pop("bogonsinterval", UNSET)

        bypassstaticroutes = d.pop("bypassstaticroutes", UNSET)

        checkaliasesurlcert = d.pop("checkaliasesurlcert", UNSET)

        disablefilter = d.pop("disablefilter", UNSET)

        disablenegate = d.pop("disablenegate", UNSET)

        disablereplyto = d.pop("disablereplyto", UNSET)

        disablescrub = d.pop("disablescrub", UNSET)

        disablevpnrules = d.pop("disablevpnrules", UNSET)

        enablebinatreflection = d.pop("enablebinatreflection", UNSET)

        enablenatreflectionhelper = d.pop("enablenatreflectionhelper", UNSET)

        enableethfilter = d.pop("enableethfilter", UNSET)

        icmperrortimeout = d.pop("icmperrortimeout", UNSET)

        icmpfirsttimeout = d.pop("icmpfirsttimeout", UNSET)

        maximumfrags = d.pop("maximumfrags", UNSET)

        maximumstates = d.pop("maximumstates", UNSET)

        maximumtableentries = d.pop("maximumtableentries", UNSET)

        maxmss = d.pop("maxmss", UNSET)

        maxmss_enable = d.pop("maxmss_enable", UNSET)

        vpn_fragment_reassemble = d.pop("vpn_fragment_reassemble", UNSET)

        natreflection = d.pop("natreflection", UNSET)

        no_apipa_block = d.pop("no_apipa_block", UNSET)

        optimization = d.pop("optimization", UNSET)

        otherfirsttimeout = d.pop("otherfirsttimeout", UNSET)

        othermultipletimeout = d.pop("othermultipletimeout", UNSET)

        othersingletimeout = d.pop("othersingletimeout", UNSET)

        reflectiontimeout = d.pop("reflectiontimeout", UNSET)

        scrubnodf = d.pop("scrubnodf", UNSET)

        scrubrnid = d.pop("scrubrnid", UNSET)

        sctpfirsttimeout = d.pop("sctpfirsttimeout", UNSET)

        sctpopeningtimeout = d.pop("sctpopeningtimeout", UNSET)

        sctpestablishedtimeout = d.pop("sctpestablishedtimeout", UNSET)

        sctpclosingtimeout = d.pop("sctpclosingtimeout", UNSET)

        sctpclosedtimeout = d.pop("sctpclosedtimeout", UNSET)

        statepolicy = d.pop("statepolicy", UNSET)

        tcpclosedtimeout = d.pop("tcpclosedtimeout", UNSET)

        tcpclosingtimeout = d.pop("tcpclosingtimeout", UNSET)

        tcpestablishedtimeout = d.pop("tcpestablishedtimeout", UNSET)

        tcpfinwaittimeout = d.pop("tcpfinwaittimeout", UNSET)

        tcpfirsttimeout = d.pop("tcpfirsttimeout", UNSET)

        tcpopeningtimeout = d.pop("tcpopeningtimeout", UNSET)

        tcptsdifftimeout = d.pop("tcptsdifftimeout", UNSET)

        tftpinterface = cast(list[str], d.pop("tftpinterface", UNSET))

        udpfirsttimeout = d.pop("udpfirsttimeout", UNSET)

        udpmultipletimeout = d.pop("udpmultipletimeout", UNSET)

        udpsingletimeout = d.pop("udpsingletimeout", UNSET)

        allow_nat64_prefix_override = d.pop("allow_nat64_prefix_override", UNSET)

        adv_firewall = cls(
            adaptiveend=adaptiveend,
            adaptivestart=adaptivestart,
            aliasesresolveinterval=aliasesresolveinterval,
            bogonsinterval=bogonsinterval,
            bypassstaticroutes=bypassstaticroutes,
            checkaliasesurlcert=checkaliasesurlcert,
            disablefilter=disablefilter,
            disablenegate=disablenegate,
            disablereplyto=disablereplyto,
            disablescrub=disablescrub,
            disablevpnrules=disablevpnrules,
            enablebinatreflection=enablebinatreflection,
            enablenatreflectionhelper=enablenatreflectionhelper,
            enableethfilter=enableethfilter,
            icmperrortimeout=icmperrortimeout,
            icmpfirsttimeout=icmpfirsttimeout,
            maximumfrags=maximumfrags,
            maximumstates=maximumstates,
            maximumtableentries=maximumtableentries,
            maxmss=maxmss,
            maxmss_enable=maxmss_enable,
            vpn_fragment_reassemble=vpn_fragment_reassemble,
            natreflection=natreflection,
            no_apipa_block=no_apipa_block,
            optimization=optimization,
            otherfirsttimeout=otherfirsttimeout,
            othermultipletimeout=othermultipletimeout,
            othersingletimeout=othersingletimeout,
            reflectiontimeout=reflectiontimeout,
            scrubnodf=scrubnodf,
            scrubrnid=scrubrnid,
            sctpfirsttimeout=sctpfirsttimeout,
            sctpopeningtimeout=sctpopeningtimeout,
            sctpestablishedtimeout=sctpestablishedtimeout,
            sctpclosingtimeout=sctpclosingtimeout,
            sctpclosedtimeout=sctpclosedtimeout,
            statepolicy=statepolicy,
            tcpclosedtimeout=tcpclosedtimeout,
            tcpclosingtimeout=tcpclosingtimeout,
            tcpestablishedtimeout=tcpestablishedtimeout,
            tcpfinwaittimeout=tcpfinwaittimeout,
            tcpfirsttimeout=tcpfirsttimeout,
            tcpopeningtimeout=tcpopeningtimeout,
            tcptsdifftimeout=tcptsdifftimeout,
            tftpinterface=tftpinterface,
            udpfirsttimeout=udpfirsttimeout,
            udpmultipletimeout=udpmultipletimeout,
            udpsingletimeout=udpsingletimeout,
            allow_nat64_prefix_override=allow_nat64_prefix_override,
        )

        adv_firewall.additional_properties = d
        return adv_firewall

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
