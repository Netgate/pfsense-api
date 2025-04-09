from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_addr_port import FWAddrPort
    from ..models.fw_filter_rule_nat import FWFilterRuleNAT
    from ..models.fw_rule_state import FWRuleState
    from ..models.fw_user_timestamp import FWUserTimestamp
    from ..models.tcp_flags import TCPFlags


T = TypeVar("T", bound="FWFilterRule")


@_attrs_define
class FWFilterRule:
    """
    Attributes:
        id (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        readonly (Union[Unset, bool]):
        floating (Union[Unset, bool]): floating rule
        ethernet (Union[Unset, bool]): ethernet rule
        gateway (Union[Unset, str]):
        tracker (Union[Unset, str]):
        type (Union[Unset, str]): pass, block, reject (non-ethernet), match (floating)
        interface (Union[Unset, str]):
        ipprotocol (Union[Unset, str]):
        tag (Union[Unset, str]):
        tagged (Union[Unset, str]):
        max_ (Union[Unset, str]):
        max_src_nodes (Union[Unset, str]):
        max_src_conn (Union[Unset, str]):
        max_src_states (Union[Unset, str]):
        statetimeout (Union[Unset, str]):
        statepolicy (Union[Unset, str]): "" (global default), if-bound, floating
        statetype (Union[Unset, str]):
        state (Union[Unset, FWRuleState]):
        os (Union[Unset, str]):
        protocol (Union[Unset, str]):
        direction (Union[Unset, str]):
        quick (Union[Unset, bool]):
        log (Union[Unset, bool]):
        dscp (Union[Unset, str]):
        allowopts (Union[Unset, bool]):
        disablereplyto (Union[Unset, bool]):
        nottagged (Union[Unset, bool]):
        pflow (Union[Unset, str]): "" (global default), "enabled", "disabled"
        max_src_conn_rate (Union[Unset, str]):
        max_src_conn_rates (Union[Unset, str]):
        tcpflags1 (Union[Unset, str]):
        tcpflags2 (Union[Unset, str]):
        tcpflags1_struct (Union[Unset, TCPFlags]):
        tcpflags2_struct (Union[Unset, TCPFlags]):
        tcpflags_any (Union[Unset, bool]):
        icmptype (Union[Unset, str]):
        nopfsync (Union[Unset, bool]):
        nosync (Union[Unset, bool]):
        vlanprio (Union[Unset, str]):
        vlanprioset (Union[Unset, str]):
        dnpipe (Union[Unset, str]): inbound pipe limiter
        pdnpipe (Union[Unset, str]): outbound pipe limiter
        ackqueue (Union[Unset, str]): acknowledgement shaper queue
        defaultqueue (Union[Unset, str]): default shaper queue
        bridgeto (Union[Unset, str]): ethernet rule, bridge to interface
        source (Union[Unset, FWAddrPort]):
        sched (Union[Unset, str]):
        destination (Union[Unset, FWAddrPort]):
        descr (Union[Unset, str]):
        srcmac (Union[Unset, str]): source MAC address for ethernet rule
        dstmac (Union[Unset, str]): destination MAC address for ethernet rule
        nat (Union[Unset, FWFilterRuleNAT]):
        updated (Union[Unset, FWUserTimestamp]):
        created (Union[Unset, FWUserTimestamp]):
        associated_rule_id (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    readonly: Union[Unset, bool] = UNSET
    floating: Union[Unset, bool] = UNSET
    ethernet: Union[Unset, bool] = UNSET
    gateway: Union[Unset, str] = UNSET
    tracker: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    ipprotocol: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    tagged: Union[Unset, str] = UNSET
    max_: Union[Unset, str] = UNSET
    max_src_nodes: Union[Unset, str] = UNSET
    max_src_conn: Union[Unset, str] = UNSET
    max_src_states: Union[Unset, str] = UNSET
    statetimeout: Union[Unset, str] = UNSET
    statepolicy: Union[Unset, str] = UNSET
    statetype: Union[Unset, str] = UNSET
    state: Union[Unset, "FWRuleState"] = UNSET
    os: Union[Unset, str] = UNSET
    protocol: Union[Unset, str] = UNSET
    direction: Union[Unset, str] = UNSET
    quick: Union[Unset, bool] = UNSET
    log: Union[Unset, bool] = UNSET
    dscp: Union[Unset, str] = UNSET
    allowopts: Union[Unset, bool] = UNSET
    disablereplyto: Union[Unset, bool] = UNSET
    nottagged: Union[Unset, bool] = UNSET
    pflow: Union[Unset, str] = UNSET
    max_src_conn_rate: Union[Unset, str] = UNSET
    max_src_conn_rates: Union[Unset, str] = UNSET
    tcpflags1: Union[Unset, str] = UNSET
    tcpflags2: Union[Unset, str] = UNSET
    tcpflags1_struct: Union[Unset, "TCPFlags"] = UNSET
    tcpflags2_struct: Union[Unset, "TCPFlags"] = UNSET
    tcpflags_any: Union[Unset, bool] = UNSET
    icmptype: Union[Unset, str] = UNSET
    nopfsync: Union[Unset, bool] = UNSET
    nosync: Union[Unset, bool] = UNSET
    vlanprio: Union[Unset, str] = UNSET
    vlanprioset: Union[Unset, str] = UNSET
    dnpipe: Union[Unset, str] = UNSET
    pdnpipe: Union[Unset, str] = UNSET
    ackqueue: Union[Unset, str] = UNSET
    defaultqueue: Union[Unset, str] = UNSET
    bridgeto: Union[Unset, str] = UNSET
    source: Union[Unset, "FWAddrPort"] = UNSET
    sched: Union[Unset, str] = UNSET
    destination: Union[Unset, "FWAddrPort"] = UNSET
    descr: Union[Unset, str] = UNSET
    srcmac: Union[Unset, str] = UNSET
    dstmac: Union[Unset, str] = UNSET
    nat: Union[Unset, "FWFilterRuleNAT"] = UNSET
    updated: Union[Unset, "FWUserTimestamp"] = UNSET
    created: Union[Unset, "FWUserTimestamp"] = UNSET
    associated_rule_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        disabled = self.disabled

        readonly = self.readonly

        floating = self.floating

        ethernet = self.ethernet

        gateway = self.gateway

        tracker = self.tracker

        type = self.type

        interface = self.interface

        ipprotocol = self.ipprotocol

        tag = self.tag

        tagged = self.tagged

        max_ = self.max_

        max_src_nodes = self.max_src_nodes

        max_src_conn = self.max_src_conn

        max_src_states = self.max_src_states

        statetimeout = self.statetimeout

        statepolicy = self.statepolicy

        statetype = self.statetype

        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        os = self.os

        protocol = self.protocol

        direction = self.direction

        quick = self.quick

        log = self.log

        dscp = self.dscp

        allowopts = self.allowopts

        disablereplyto = self.disablereplyto

        nottagged = self.nottagged

        pflow = self.pflow

        max_src_conn_rate = self.max_src_conn_rate

        max_src_conn_rates = self.max_src_conn_rates

        tcpflags1 = self.tcpflags1

        tcpflags2 = self.tcpflags2

        tcpflags1_struct: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tcpflags1_struct, Unset):
            tcpflags1_struct = self.tcpflags1_struct.to_dict()

        tcpflags2_struct: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tcpflags2_struct, Unset):
            tcpflags2_struct = self.tcpflags2_struct.to_dict()

        tcpflags_any = self.tcpflags_any

        icmptype = self.icmptype

        nopfsync = self.nopfsync

        nosync = self.nosync

        vlanprio = self.vlanprio

        vlanprioset = self.vlanprioset

        dnpipe = self.dnpipe

        pdnpipe = self.pdnpipe

        ackqueue = self.ackqueue

        defaultqueue = self.defaultqueue

        bridgeto = self.bridgeto

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        sched = self.sched

        destination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        descr = self.descr

        srcmac = self.srcmac

        dstmac = self.dstmac

        nat: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nat, Unset):
            nat = self.nat.to_dict()

        updated: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        created: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        associated_rule_id = self.associated_rule_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if readonly is not UNSET:
            field_dict["readonly"] = readonly
        if floating is not UNSET:
            field_dict["floating"] = floating
        if ethernet is not UNSET:
            field_dict["ethernet"] = ethernet
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if tracker is not UNSET:
            field_dict["tracker"] = tracker
        if type is not UNSET:
            field_dict["type"] = type
        if interface is not UNSET:
            field_dict["interface"] = interface
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if tag is not UNSET:
            field_dict["tag"] = tag
        if tagged is not UNSET:
            field_dict["tagged"] = tagged
        if max_ is not UNSET:
            field_dict["max"] = max_
        if max_src_nodes is not UNSET:
            field_dict["max_src_nodes"] = max_src_nodes
        if max_src_conn is not UNSET:
            field_dict["max_src_conn"] = max_src_conn
        if max_src_states is not UNSET:
            field_dict["max_src_states"] = max_src_states
        if statetimeout is not UNSET:
            field_dict["statetimeout"] = statetimeout
        if statepolicy is not UNSET:
            field_dict["statepolicy"] = statepolicy
        if statetype is not UNSET:
            field_dict["statetype"] = statetype
        if state is not UNSET:
            field_dict["state"] = state
        if os is not UNSET:
            field_dict["os"] = os
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if direction is not UNSET:
            field_dict["direction"] = direction
        if quick is not UNSET:
            field_dict["quick"] = quick
        if log is not UNSET:
            field_dict["log"] = log
        if dscp is not UNSET:
            field_dict["dscp"] = dscp
        if allowopts is not UNSET:
            field_dict["allowopts"] = allowopts
        if disablereplyto is not UNSET:
            field_dict["disablereplyto"] = disablereplyto
        if nottagged is not UNSET:
            field_dict["nottagged"] = nottagged
        if pflow is not UNSET:
            field_dict["pflow"] = pflow
        if max_src_conn_rate is not UNSET:
            field_dict["max_src_conn_rate"] = max_src_conn_rate
        if max_src_conn_rates is not UNSET:
            field_dict["max_src_conn_rates"] = max_src_conn_rates
        if tcpflags1 is not UNSET:
            field_dict["tcpflags1"] = tcpflags1
        if tcpflags2 is not UNSET:
            field_dict["tcpflags2"] = tcpflags2
        if tcpflags1_struct is not UNSET:
            field_dict["tcpflags1_struct"] = tcpflags1_struct
        if tcpflags2_struct is not UNSET:
            field_dict["tcpflags2_struct"] = tcpflags2_struct
        if tcpflags_any is not UNSET:
            field_dict["tcpflags_any"] = tcpflags_any
        if icmptype is not UNSET:
            field_dict["icmptype"] = icmptype
        if nopfsync is not UNSET:
            field_dict["nopfsync"] = nopfsync
        if nosync is not UNSET:
            field_dict["nosync"] = nosync
        if vlanprio is not UNSET:
            field_dict["vlanprio"] = vlanprio
        if vlanprioset is not UNSET:
            field_dict["vlanprioset"] = vlanprioset
        if dnpipe is not UNSET:
            field_dict["dnpipe"] = dnpipe
        if pdnpipe is not UNSET:
            field_dict["pdnpipe"] = pdnpipe
        if ackqueue is not UNSET:
            field_dict["ackqueue"] = ackqueue
        if defaultqueue is not UNSET:
            field_dict["defaultqueue"] = defaultqueue
        if bridgeto is not UNSET:
            field_dict["bridgeto"] = bridgeto
        if source is not UNSET:
            field_dict["source"] = source
        if sched is not UNSET:
            field_dict["sched"] = sched
        if destination is not UNSET:
            field_dict["destination"] = destination
        if descr is not UNSET:
            field_dict["descr"] = descr
        if srcmac is not UNSET:
            field_dict["srcmac"] = srcmac
        if dstmac is not UNSET:
            field_dict["dstmac"] = dstmac
        if nat is not UNSET:
            field_dict["nat"] = nat
        if updated is not UNSET:
            field_dict["updated"] = updated
        if created is not UNSET:
            field_dict["created"] = created
        if associated_rule_id is not UNSET:
            field_dict["associated_rule_id"] = associated_rule_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_addr_port import FWAddrPort
        from ..models.fw_filter_rule_nat import FWFilterRuleNAT
        from ..models.fw_rule_state import FWRuleState
        from ..models.fw_user_timestamp import FWUserTimestamp
        from ..models.tcp_flags import TCPFlags

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        disabled = d.pop("disabled", UNSET)

        readonly = d.pop("readonly", UNSET)

        floating = d.pop("floating", UNSET)

        ethernet = d.pop("ethernet", UNSET)

        gateway = d.pop("gateway", UNSET)

        tracker = d.pop("tracker", UNSET)

        type = d.pop("type", UNSET)

        interface = d.pop("interface", UNSET)

        ipprotocol = d.pop("ipprotocol", UNSET)

        tag = d.pop("tag", UNSET)

        tagged = d.pop("tagged", UNSET)

        max_ = d.pop("max", UNSET)

        max_src_nodes = d.pop("max_src_nodes", UNSET)

        max_src_conn = d.pop("max_src_conn", UNSET)

        max_src_states = d.pop("max_src_states", UNSET)

        statetimeout = d.pop("statetimeout", UNSET)

        statepolicy = d.pop("statepolicy", UNSET)

        statetype = d.pop("statetype", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, FWRuleState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = FWRuleState.from_dict(_state)

        os = d.pop("os", UNSET)

        protocol = d.pop("protocol", UNSET)

        direction = d.pop("direction", UNSET)

        quick = d.pop("quick", UNSET)

        log = d.pop("log", UNSET)

        dscp = d.pop("dscp", UNSET)

        allowopts = d.pop("allowopts", UNSET)

        disablereplyto = d.pop("disablereplyto", UNSET)

        nottagged = d.pop("nottagged", UNSET)

        pflow = d.pop("pflow", UNSET)

        max_src_conn_rate = d.pop("max_src_conn_rate", UNSET)

        max_src_conn_rates = d.pop("max_src_conn_rates", UNSET)

        tcpflags1 = d.pop("tcpflags1", UNSET)

        tcpflags2 = d.pop("tcpflags2", UNSET)

        _tcpflags1_struct = d.pop("tcpflags1_struct", UNSET)
        tcpflags1_struct: Union[Unset, TCPFlags]
        if isinstance(_tcpflags1_struct, Unset):
            tcpflags1_struct = UNSET
        else:
            tcpflags1_struct = TCPFlags.from_dict(_tcpflags1_struct)

        _tcpflags2_struct = d.pop("tcpflags2_struct", UNSET)
        tcpflags2_struct: Union[Unset, TCPFlags]
        if isinstance(_tcpflags2_struct, Unset):
            tcpflags2_struct = UNSET
        else:
            tcpflags2_struct = TCPFlags.from_dict(_tcpflags2_struct)

        tcpflags_any = d.pop("tcpflags_any", UNSET)

        icmptype = d.pop("icmptype", UNSET)

        nopfsync = d.pop("nopfsync", UNSET)

        nosync = d.pop("nosync", UNSET)

        vlanprio = d.pop("vlanprio", UNSET)

        vlanprioset = d.pop("vlanprioset", UNSET)

        dnpipe = d.pop("dnpipe", UNSET)

        pdnpipe = d.pop("pdnpipe", UNSET)

        ackqueue = d.pop("ackqueue", UNSET)

        defaultqueue = d.pop("defaultqueue", UNSET)

        bridgeto = d.pop("bridgeto", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, FWAddrPort]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = FWAddrPort.from_dict(_source)

        sched = d.pop("sched", UNSET)

        _destination = d.pop("destination", UNSET)
        destination: Union[Unset, FWAddrPort]
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = FWAddrPort.from_dict(_destination)

        descr = d.pop("descr", UNSET)

        srcmac = d.pop("srcmac", UNSET)

        dstmac = d.pop("dstmac", UNSET)

        _nat = d.pop("nat", UNSET)
        nat: Union[Unset, FWFilterRuleNAT]
        if isinstance(_nat, Unset):
            nat = UNSET
        else:
            nat = FWFilterRuleNAT.from_dict(_nat)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, FWUserTimestamp]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = FWUserTimestamp.from_dict(_updated)

        _created = d.pop("created", UNSET)
        created: Union[Unset, FWUserTimestamp]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = FWUserTimestamp.from_dict(_created)

        associated_rule_id = d.pop("associated_rule_id", UNSET)

        fw_filter_rule = cls(
            id=id,
            disabled=disabled,
            readonly=readonly,
            floating=floating,
            ethernet=ethernet,
            gateway=gateway,
            tracker=tracker,
            type=type,
            interface=interface,
            ipprotocol=ipprotocol,
            tag=tag,
            tagged=tagged,
            max_=max_,
            max_src_nodes=max_src_nodes,
            max_src_conn=max_src_conn,
            max_src_states=max_src_states,
            statetimeout=statetimeout,
            statepolicy=statepolicy,
            statetype=statetype,
            state=state,
            os=os,
            protocol=protocol,
            direction=direction,
            quick=quick,
            log=log,
            dscp=dscp,
            allowopts=allowopts,
            disablereplyto=disablereplyto,
            nottagged=nottagged,
            pflow=pflow,
            max_src_conn_rate=max_src_conn_rate,
            max_src_conn_rates=max_src_conn_rates,
            tcpflags1=tcpflags1,
            tcpflags2=tcpflags2,
            tcpflags1_struct=tcpflags1_struct,
            tcpflags2_struct=tcpflags2_struct,
            tcpflags_any=tcpflags_any,
            icmptype=icmptype,
            nopfsync=nopfsync,
            nosync=nosync,
            vlanprio=vlanprio,
            vlanprioset=vlanprioset,
            dnpipe=dnpipe,
            pdnpipe=pdnpipe,
            ackqueue=ackqueue,
            defaultqueue=defaultqueue,
            bridgeto=bridgeto,
            source=source,
            sched=sched,
            destination=destination,
            descr=descr,
            srcmac=srcmac,
            dstmac=dstmac,
            nat=nat,
            updated=updated,
            created=created,
            associated_rule_id=associated_rule_id,
        )

        fw_filter_rule.additional_properties = d
        return fw_filter_rule

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
