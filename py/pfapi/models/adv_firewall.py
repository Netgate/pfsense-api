from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvFirewall")


@_attrs_define
class AdvFirewall:
    """
    Attributes:
        adaptiveend (Union[Unset, str]):
        adaptivestart (Union[Unset, str]):
        aliasesresolveinterval (Union[Unset, str]):
        bogonsinterval (Union[Unset, str]):
        bypassstaticroutes (Union[Unset, bool]):
        checkaliasesurlcert (Union[Unset, bool]):
        disablefilter (Union[Unset, bool]):
        disablenatreflection (Union[Unset, bool]):
        disablenegate (Union[Unset, bool]):
        disablereplyto (Union[Unset, bool]):
        disablescrub (Union[Unset, bool]):
        disablevpnrules (Union[Unset, bool]):
        enablebinatreflection (Union[Unset, bool]):
        enablenatreflectionhelper (Union[Unset, bool]):
        enablenatreflectionpurenat (Union[Unset, bool]):
        icmperrortimeout (Union[Unset, str]):
        icmpfirsttimeout (Union[Unset, str]):
        maximumfrags (Union[Unset, str]):
        maximumstates (Union[Unset, str]):
        maximumtableentries (Union[Unset, str]):
        maxmss (Union[Unset, str]):
        maxmss_enable (Union[Unset, bool]):
        vpn_scrubenodf (Union[Unset, bool]):
        vpn_fragment_reassemble (Union[Unset, bool]):
        natreflection (Union[Unset, str]):
        no_apipa_block (Union[Unset, bool]):
        optimization (Union[Unset, str]):
        otherfirsttimeout (Union[Unset, str]):
        othermultipletimeout (Union[Unset, str]):
        othersingletimeout (Union[Unset, str]):
        reflectiontimeout (Union[Unset, str]):
        scrubnodf (Union[Unset, bool]):
        scrubrnid (Union[Unset, bool]):
        sctpfirsttimeout (Union[Unset, str]):
        sctpopeningtimeout (Union[Unset, str]):
        sctpestablishedtimeout (Union[Unset, str]):
        sctpclosingtimeout (Union[Unset, str]):
        sctpclosedtimeout (Union[Unset, str]):
        tcpclosedtimeout (Union[Unset, str]):
        tcpclosingtimeout (Union[Unset, str]):
        tcpestablishedtimeout (Union[Unset, str]):
        tcpfinwaittimeout (Union[Unset, str]):
        tcpfirsttimeout (Union[Unset, str]):
        tcpopeningtimeout (Union[Unset, str]):
        tcptsdifftimeout (Union[Unset, str]):
        tftpinterface (Union[Unset, List[str]]):
        udpfirsttimeout (Union[Unset, str]):
        udpmultipletimeout (Union[Unset, str]):
        udpsingletimeout (Union[Unset, str]):
    """

    adaptiveend: Union[Unset, str] = UNSET
    adaptivestart: Union[Unset, str] = UNSET
    aliasesresolveinterval: Union[Unset, str] = UNSET
    bogonsinterval: Union[Unset, str] = UNSET
    bypassstaticroutes: Union[Unset, bool] = UNSET
    checkaliasesurlcert: Union[Unset, bool] = UNSET
    disablefilter: Union[Unset, bool] = UNSET
    disablenatreflection: Union[Unset, bool] = UNSET
    disablenegate: Union[Unset, bool] = UNSET
    disablereplyto: Union[Unset, bool] = UNSET
    disablescrub: Union[Unset, bool] = UNSET
    disablevpnrules: Union[Unset, bool] = UNSET
    enablebinatreflection: Union[Unset, bool] = UNSET
    enablenatreflectionhelper: Union[Unset, bool] = UNSET
    enablenatreflectionpurenat: Union[Unset, bool] = UNSET
    icmperrortimeout: Union[Unset, str] = UNSET
    icmpfirsttimeout: Union[Unset, str] = UNSET
    maximumfrags: Union[Unset, str] = UNSET
    maximumstates: Union[Unset, str] = UNSET
    maximumtableentries: Union[Unset, str] = UNSET
    maxmss: Union[Unset, str] = UNSET
    maxmss_enable: Union[Unset, bool] = UNSET
    vpn_scrubenodf: Union[Unset, bool] = UNSET
    vpn_fragment_reassemble: Union[Unset, bool] = UNSET
    natreflection: Union[Unset, str] = UNSET
    no_apipa_block: Union[Unset, bool] = UNSET
    optimization: Union[Unset, str] = UNSET
    otherfirsttimeout: Union[Unset, str] = UNSET
    othermultipletimeout: Union[Unset, str] = UNSET
    othersingletimeout: Union[Unset, str] = UNSET
    reflectiontimeout: Union[Unset, str] = UNSET
    scrubnodf: Union[Unset, bool] = UNSET
    scrubrnid: Union[Unset, bool] = UNSET
    sctpfirsttimeout: Union[Unset, str] = UNSET
    sctpopeningtimeout: Union[Unset, str] = UNSET
    sctpestablishedtimeout: Union[Unset, str] = UNSET
    sctpclosingtimeout: Union[Unset, str] = UNSET
    sctpclosedtimeout: Union[Unset, str] = UNSET
    tcpclosedtimeout: Union[Unset, str] = UNSET
    tcpclosingtimeout: Union[Unset, str] = UNSET
    tcpestablishedtimeout: Union[Unset, str] = UNSET
    tcpfinwaittimeout: Union[Unset, str] = UNSET
    tcpfirsttimeout: Union[Unset, str] = UNSET
    tcpopeningtimeout: Union[Unset, str] = UNSET
    tcptsdifftimeout: Union[Unset, str] = UNSET
    tftpinterface: Union[Unset, List[str]] = UNSET
    udpfirsttimeout: Union[Unset, str] = UNSET
    udpmultipletimeout: Union[Unset, str] = UNSET
    udpsingletimeout: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        adaptiveend = self.adaptiveend

        adaptivestart = self.adaptivestart

        aliasesresolveinterval = self.aliasesresolveinterval

        bogonsinterval = self.bogonsinterval

        bypassstaticroutes = self.bypassstaticroutes

        checkaliasesurlcert = self.checkaliasesurlcert

        disablefilter = self.disablefilter

        disablenatreflection = self.disablenatreflection

        disablenegate = self.disablenegate

        disablereplyto = self.disablereplyto

        disablescrub = self.disablescrub

        disablevpnrules = self.disablevpnrules

        enablebinatreflection = self.enablebinatreflection

        enablenatreflectionhelper = self.enablenatreflectionhelper

        enablenatreflectionpurenat = self.enablenatreflectionpurenat

        icmperrortimeout = self.icmperrortimeout

        icmpfirsttimeout = self.icmpfirsttimeout

        maximumfrags = self.maximumfrags

        maximumstates = self.maximumstates

        maximumtableentries = self.maximumtableentries

        maxmss = self.maxmss

        maxmss_enable = self.maxmss_enable

        vpn_scrubenodf = self.vpn_scrubenodf

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

        tcpclosedtimeout = self.tcpclosedtimeout

        tcpclosingtimeout = self.tcpclosingtimeout

        tcpestablishedtimeout = self.tcpestablishedtimeout

        tcpfinwaittimeout = self.tcpfinwaittimeout

        tcpfirsttimeout = self.tcpfirsttimeout

        tcpopeningtimeout = self.tcpopeningtimeout

        tcptsdifftimeout = self.tcptsdifftimeout

        tftpinterface: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tftpinterface, Unset):
            tftpinterface = self.tftpinterface

        udpfirsttimeout = self.udpfirsttimeout

        udpmultipletimeout = self.udpmultipletimeout

        udpsingletimeout = self.udpsingletimeout

        field_dict: Dict[str, Any] = {}
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
        if disablenatreflection is not UNSET:
            field_dict["disablenatreflection"] = disablenatreflection
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
        if enablenatreflectionpurenat is not UNSET:
            field_dict["enablenatreflectionpurenat"] = enablenatreflectionpurenat
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
        if vpn_scrubenodf is not UNSET:
            field_dict["vpn_scrubenodf"] = vpn_scrubenodf
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        adaptiveend = d.pop("adaptiveend", UNSET)

        adaptivestart = d.pop("adaptivestart", UNSET)

        aliasesresolveinterval = d.pop("aliasesresolveinterval", UNSET)

        bogonsinterval = d.pop("bogonsinterval", UNSET)

        bypassstaticroutes = d.pop("bypassstaticroutes", UNSET)

        checkaliasesurlcert = d.pop("checkaliasesurlcert", UNSET)

        disablefilter = d.pop("disablefilter", UNSET)

        disablenatreflection = d.pop("disablenatreflection", UNSET)

        disablenegate = d.pop("disablenegate", UNSET)

        disablereplyto = d.pop("disablereplyto", UNSET)

        disablescrub = d.pop("disablescrub", UNSET)

        disablevpnrules = d.pop("disablevpnrules", UNSET)

        enablebinatreflection = d.pop("enablebinatreflection", UNSET)

        enablenatreflectionhelper = d.pop("enablenatreflectionhelper", UNSET)

        enablenatreflectionpurenat = d.pop("enablenatreflectionpurenat", UNSET)

        icmperrortimeout = d.pop("icmperrortimeout", UNSET)

        icmpfirsttimeout = d.pop("icmpfirsttimeout", UNSET)

        maximumfrags = d.pop("maximumfrags", UNSET)

        maximumstates = d.pop("maximumstates", UNSET)

        maximumtableentries = d.pop("maximumtableentries", UNSET)

        maxmss = d.pop("maxmss", UNSET)

        maxmss_enable = d.pop("maxmss_enable", UNSET)

        vpn_scrubenodf = d.pop("vpn_scrubenodf", UNSET)

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

        tcpclosedtimeout = d.pop("tcpclosedtimeout", UNSET)

        tcpclosingtimeout = d.pop("tcpclosingtimeout", UNSET)

        tcpestablishedtimeout = d.pop("tcpestablishedtimeout", UNSET)

        tcpfinwaittimeout = d.pop("tcpfinwaittimeout", UNSET)

        tcpfirsttimeout = d.pop("tcpfirsttimeout", UNSET)

        tcpopeningtimeout = d.pop("tcpopeningtimeout", UNSET)

        tcptsdifftimeout = d.pop("tcptsdifftimeout", UNSET)

        tftpinterface = cast(List[str], d.pop("tftpinterface", UNSET))

        udpfirsttimeout = d.pop("udpfirsttimeout", UNSET)

        udpmultipletimeout = d.pop("udpmultipletimeout", UNSET)

        udpsingletimeout = d.pop("udpsingletimeout", UNSET)

        adv_firewall = cls(
            adaptiveend=adaptiveend,
            adaptivestart=adaptivestart,
            aliasesresolveinterval=aliasesresolveinterval,
            bogonsinterval=bogonsinterval,
            bypassstaticroutes=bypassstaticroutes,
            checkaliasesurlcert=checkaliasesurlcert,
            disablefilter=disablefilter,
            disablenatreflection=disablenatreflection,
            disablenegate=disablenegate,
            disablereplyto=disablereplyto,
            disablescrub=disablescrub,
            disablevpnrules=disablevpnrules,
            enablebinatreflection=enablebinatreflection,
            enablenatreflectionhelper=enablenatreflectionhelper,
            enablenatreflectionpurenat=enablenatreflectionpurenat,
            icmperrortimeout=icmperrortimeout,
            icmpfirsttimeout=icmpfirsttimeout,
            maximumfrags=maximumfrags,
            maximumstates=maximumstates,
            maximumtableentries=maximumtableentries,
            maxmss=maxmss,
            maxmss_enable=maxmss_enable,
            vpn_scrubenodf=vpn_scrubenodf,
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
        )

        adv_firewall.additional_properties = d
        return adv_firewall

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
