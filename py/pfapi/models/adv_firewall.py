from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdvFirewall")


@_attrs_define
class AdvFirewall:
    """
    Attributes:
        adaptiveend (str):
        adaptivestart (str):
        aliasesresolveinterval (str):
        bogonsinterval (str):
        bypassstaticroutes (bool):
        checkaliasesurlcert (bool):
        disablefilter (bool):
        disablenatreflection (bool):
        disablenegate (bool):
        disablereplyto (bool):
        disablescrub (bool):
        disablevpnrules (bool):
        enablebinatreflection (bool):
        enablenatreflectionhelper (bool):
        enablenatreflectionpurenat (bool):
        icmperrortimeout (str):
        icmpfirsttimeout (str):
        maximumfrags (str):
        maximumstates (str):
        maximumtableentries (str):
        maxmss (str):
        maxmss_enable (bool):
        vpn_scrubenodf (bool):
        vpn_fragment_reassemble (bool):
        natreflection (str):
        no_apipa_block (bool):
        optimization (str):
        otherfirsttimeout (str):
        othermultipletimeout (str):
        othersingletimeout (str):
        reflectiontimeout (str):
        scrubnodf (bool):
        scrubrnid (bool):
        sctpfirsttimeout (str):
        sctpopeningtimeout (str):
        sctpestablishedtimeout (str):
        sctpclosingtimeout (str):
        sctpclosedtimeout (str):
        tcpclosedtimeout (str):
        tcpclosingtimeout (str):
        tcpestablishedtimeout (str):
        tcpfinwaittimeout (str):
        tcpfirsttimeout (str):
        tcpopeningtimeout (str):
        tcptsdifftimeout (str):
        tftpinterface (List[str]):
        udpfirsttimeout (str):
        udpmultipletimeout (str):
        udpsingletimeout (str):
    """

    adaptiveend: str
    adaptivestart: str
    aliasesresolveinterval: str
    bogonsinterval: str
    bypassstaticroutes: bool
    checkaliasesurlcert: bool
    disablefilter: bool
    disablenatreflection: bool
    disablenegate: bool
    disablereplyto: bool
    disablescrub: bool
    disablevpnrules: bool
    enablebinatreflection: bool
    enablenatreflectionhelper: bool
    enablenatreflectionpurenat: bool
    icmperrortimeout: str
    icmpfirsttimeout: str
    maximumfrags: str
    maximumstates: str
    maximumtableentries: str
    maxmss: str
    maxmss_enable: bool
    vpn_scrubenodf: bool
    vpn_fragment_reassemble: bool
    natreflection: str
    no_apipa_block: bool
    optimization: str
    otherfirsttimeout: str
    othermultipletimeout: str
    othersingletimeout: str
    reflectiontimeout: str
    scrubnodf: bool
    scrubrnid: bool
    sctpfirsttimeout: str
    sctpopeningtimeout: str
    sctpestablishedtimeout: str
    sctpclosingtimeout: str
    sctpclosedtimeout: str
    tcpclosedtimeout: str
    tcpclosingtimeout: str
    tcpestablishedtimeout: str
    tcpfinwaittimeout: str
    tcpfirsttimeout: str
    tcpopeningtimeout: str
    tcptsdifftimeout: str
    tftpinterface: List[str]
    udpfirsttimeout: str
    udpmultipletimeout: str
    udpsingletimeout: str
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

        tftpinterface = self.tftpinterface

        udpfirsttimeout = self.udpfirsttimeout

        udpmultipletimeout = self.udpmultipletimeout

        udpsingletimeout = self.udpsingletimeout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adaptiveend": adaptiveend,
                "adaptivestart": adaptivestart,
                "aliasesresolveinterval": aliasesresolveinterval,
                "bogonsinterval": bogonsinterval,
                "bypassstaticroutes": bypassstaticroutes,
                "checkaliasesurlcert": checkaliasesurlcert,
                "disablefilter": disablefilter,
                "disablenatreflection": disablenatreflection,
                "disablenegate": disablenegate,
                "disablereplyto": disablereplyto,
                "disablescrub": disablescrub,
                "disablevpnrules": disablevpnrules,
                "enablebinatreflection": enablebinatreflection,
                "enablenatreflectionhelper": enablenatreflectionhelper,
                "enablenatreflectionpurenat": enablenatreflectionpurenat,
                "icmperrortimeout": icmperrortimeout,
                "icmpfirsttimeout": icmpfirsttimeout,
                "maximumfrags": maximumfrags,
                "maximumstates": maximumstates,
                "maximumtableentries": maximumtableentries,
                "maxmss": maxmss,
                "maxmss_enable": maxmss_enable,
                "vpn_scrubenodf": vpn_scrubenodf,
                "vpn_fragment_reassemble": vpn_fragment_reassemble,
                "natreflection": natreflection,
                "no_apipa_block": no_apipa_block,
                "optimization": optimization,
                "otherfirsttimeout": otherfirsttimeout,
                "othermultipletimeout": othermultipletimeout,
                "othersingletimeout": othersingletimeout,
                "reflectiontimeout": reflectiontimeout,
                "scrubnodf": scrubnodf,
                "scrubrnid": scrubrnid,
                "sctpfirsttimeout": sctpfirsttimeout,
                "sctpopeningtimeout": sctpopeningtimeout,
                "sctpestablishedtimeout": sctpestablishedtimeout,
                "sctpclosingtimeout": sctpclosingtimeout,
                "sctpclosedtimeout": sctpclosedtimeout,
                "tcpclosedtimeout": tcpclosedtimeout,
                "tcpclosingtimeout": tcpclosingtimeout,
                "tcpestablishedtimeout": tcpestablishedtimeout,
                "tcpfinwaittimeout": tcpfinwaittimeout,
                "tcpfirsttimeout": tcpfirsttimeout,
                "tcpopeningtimeout": tcpopeningtimeout,
                "tcptsdifftimeout": tcptsdifftimeout,
                "tftpinterface": tftpinterface,
                "udpfirsttimeout": udpfirsttimeout,
                "udpmultipletimeout": udpmultipletimeout,
                "udpsingletimeout": udpsingletimeout,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        adaptiveend = d.pop("adaptiveend")

        adaptivestart = d.pop("adaptivestart")

        aliasesresolveinterval = d.pop("aliasesresolveinterval")

        bogonsinterval = d.pop("bogonsinterval")

        bypassstaticroutes = d.pop("bypassstaticroutes")

        checkaliasesurlcert = d.pop("checkaliasesurlcert")

        disablefilter = d.pop("disablefilter")

        disablenatreflection = d.pop("disablenatreflection")

        disablenegate = d.pop("disablenegate")

        disablereplyto = d.pop("disablereplyto")

        disablescrub = d.pop("disablescrub")

        disablevpnrules = d.pop("disablevpnrules")

        enablebinatreflection = d.pop("enablebinatreflection")

        enablenatreflectionhelper = d.pop("enablenatreflectionhelper")

        enablenatreflectionpurenat = d.pop("enablenatreflectionpurenat")

        icmperrortimeout = d.pop("icmperrortimeout")

        icmpfirsttimeout = d.pop("icmpfirsttimeout")

        maximumfrags = d.pop("maximumfrags")

        maximumstates = d.pop("maximumstates")

        maximumtableentries = d.pop("maximumtableentries")

        maxmss = d.pop("maxmss")

        maxmss_enable = d.pop("maxmss_enable")

        vpn_scrubenodf = d.pop("vpn_scrubenodf")

        vpn_fragment_reassemble = d.pop("vpn_fragment_reassemble")

        natreflection = d.pop("natreflection")

        no_apipa_block = d.pop("no_apipa_block")

        optimization = d.pop("optimization")

        otherfirsttimeout = d.pop("otherfirsttimeout")

        othermultipletimeout = d.pop("othermultipletimeout")

        othersingletimeout = d.pop("othersingletimeout")

        reflectiontimeout = d.pop("reflectiontimeout")

        scrubnodf = d.pop("scrubnodf")

        scrubrnid = d.pop("scrubrnid")

        sctpfirsttimeout = d.pop("sctpfirsttimeout")

        sctpopeningtimeout = d.pop("sctpopeningtimeout")

        sctpestablishedtimeout = d.pop("sctpestablishedtimeout")

        sctpclosingtimeout = d.pop("sctpclosingtimeout")

        sctpclosedtimeout = d.pop("sctpclosedtimeout")

        tcpclosedtimeout = d.pop("tcpclosedtimeout")

        tcpclosingtimeout = d.pop("tcpclosingtimeout")

        tcpestablishedtimeout = d.pop("tcpestablishedtimeout")

        tcpfinwaittimeout = d.pop("tcpfinwaittimeout")

        tcpfirsttimeout = d.pop("tcpfirsttimeout")

        tcpopeningtimeout = d.pop("tcpopeningtimeout")

        tcptsdifftimeout = d.pop("tcptsdifftimeout")

        tftpinterface = cast(List[str], d.pop("tftpinterface"))

        udpfirsttimeout = d.pop("udpfirsttimeout")

        udpmultipletimeout = d.pop("udpmultipletimeout")

        udpsingletimeout = d.pop("udpsingletimeout")

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
