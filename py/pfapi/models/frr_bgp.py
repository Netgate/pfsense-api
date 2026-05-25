from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_bgp_row import FrrBgpRow
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrBgp")


@_attrs_define
class FrrBgp:
    """
    Attributes:
        enable (bool | Unset): (BGP Router Options) Enable

            Enable BGP Routing
        adjacencylog (bool | Unset): (BGP Router Options) Log Adjacency Changes

            If set to yes, adjacency changes will be written via syslog.
        asnum (str | Unset): (BGP Router Options) Local AS

            Autonomous System (AS) Number for this router. May be an integer from 1-4294967295.
        routerid (str | Unset): (BGP Router Options) Router ID

            Specify the Router ID, if it is not the default.
        timers_keepalive (str | Unset): (BGP Router Options) Timers

            Keep Alive Interval (0-65535)
        timers_holdtime (str | Unset): (BGP Router Options) Hold Time

            Hold Time (0-65535)
        timers_updatedelay (str | Unset): (BGP Router Options) Update Delay

            Update Delay (0-3600, s)
        timers_peerwait (str | Unset): (BGP Router Options) Peer Wait

            Peer Wait (1-3600, s)
        nodefipv4unicast (bool | Unset): (BGP Router Options) Disable Default IPv4 Unicast

            If checked, BGP will not assume IPv4 unicast by default.
        enablesnmpagentx (bool | Unset): (Modules) Enable SNMP AgentX

            Enable agentx support for accessing FRR Zebra data via SNMP with the net-snmp package.
        enablerpki (bool | Unset): (Modules) Enable BGP RPKI

            Enable BGP Resource Public Key Infrastructure.
        shutdown (bool | Unset): (Global Neighbor Shutdown) Global Neighbor Shutdown

            Administratively shutdown ALL neighbors
        shutdownmessage (str | Unset): (Global Neighbor Shutdown) Message

            Shutdown message (optional)
        grglobaldisable (bool | Unset): (Graceful Restart/Shutdown) Disable BGP Graceful Restart

            Globally disable graceful restart functionality in both restart and helper mode.
        disablepreservefwstate (bool | Unset): (Graceful Restart/Shutdown) Preserve FW State

            If checked, sets F-bit indication that fib is preserved while doing Graceful Restart.
        grstalepathtime (str | Unset): (Graceful Restart/Shutdown) Timers

            Stale Path Time (1-4095, s)
        grrestarttimetime (str | Unset): (Graceful Restart/Shutdown) Restart Time

            Restart Time (1-4095, s)
        grselectdefertime (str | Unset): (Graceful Restart/Shutdown) Select Defer Time

            Select Defer Time (0-3600, s)
        grribstaletime (str | Unset): (Graceful Restart/Shutdown) RIB Stale Time

            RIB Stale Time (1-3600, s)
        gsenable (bool | Unset): (Graceful Restart/Shutdown) Enable BGP Graceful Shutdown

            If checked, enable BGP graceful shutdown.
        rpkipollingperiod (str | Unset): (RPKI Timers) Timers

            Polling Period (1-86400, s)
        rpkiexpireinterval (str | Unset): (RPKI Timers) Expire Interval

            Expire Interval (600-172800, s)
        rpkiretryinterval (str | Unset): (RPKI Timers) Retry Interval

            Retry Interval (1-7200, s)
        redistributeconnected (str | Unset): (Network Distribution) Redistribute Local

            Redistribute connected networks
        redistributestatic (str | Unset): (Network Distribution) Redistribute Static

            Redistribute FRR static routes
        redistributekernel (str | Unset): (Network Distribution) Redistribute Kernel

            Redistribute Kernel routing table/pfSense static routes
        redistributeospf (str | Unset): (Network Distribution) Redistribute OSPF

            Redistribute OSPF routes to BGP Neighbors
        redistributeospf6 (str | Unset): (Network Distribution) Redistribute OSPFv3

            Redistribute OSPFv3 routes to BGP Neighbors
        redistributerip (str | Unset): (Network Distribution) Redistribute RIP

            Redistribute RIP routes to BGP Neighbors
        row (list[FrrBgpRow] | Unset):
        redistributeconnected_options (list[TextValue] | Unset):
        redistributestatic_options (list[TextValue] | Unset):
        redistributekernel_options (list[TextValue] | Unset):
        redistributeospf_options (list[TextValue] | Unset):
        redistributeospf6_options (list[TextValue] | Unset):
        redistributerip_options (list[TextValue] | Unset):
    """

    enable: bool | Unset = UNSET
    adjacencylog: bool | Unset = UNSET
    asnum: str | Unset = UNSET
    routerid: str | Unset = UNSET
    timers_keepalive: str | Unset = UNSET
    timers_holdtime: str | Unset = UNSET
    timers_updatedelay: str | Unset = UNSET
    timers_peerwait: str | Unset = UNSET
    nodefipv4unicast: bool | Unset = UNSET
    enablesnmpagentx: bool | Unset = UNSET
    enablerpki: bool | Unset = UNSET
    shutdown: bool | Unset = UNSET
    shutdownmessage: str | Unset = UNSET
    grglobaldisable: bool | Unset = UNSET
    disablepreservefwstate: bool | Unset = UNSET
    grstalepathtime: str | Unset = UNSET
    grrestarttimetime: str | Unset = UNSET
    grselectdefertime: str | Unset = UNSET
    grribstaletime: str | Unset = UNSET
    gsenable: bool | Unset = UNSET
    rpkipollingperiod: str | Unset = UNSET
    rpkiexpireinterval: str | Unset = UNSET
    rpkiretryinterval: str | Unset = UNSET
    redistributeconnected: str | Unset = UNSET
    redistributestatic: str | Unset = UNSET
    redistributekernel: str | Unset = UNSET
    redistributeospf: str | Unset = UNSET
    redistributeospf6: str | Unset = UNSET
    redistributerip: str | Unset = UNSET
    row: list[FrrBgpRow] | Unset = UNSET
    redistributeconnected_options: list[TextValue] | Unset = UNSET
    redistributestatic_options: list[TextValue] | Unset = UNSET
    redistributekernel_options: list[TextValue] | Unset = UNSET
    redistributeospf_options: list[TextValue] | Unset = UNSET
    redistributeospf6_options: list[TextValue] | Unset = UNSET
    redistributerip_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        adjacencylog = self.adjacencylog

        asnum = self.asnum

        routerid = self.routerid

        timers_keepalive = self.timers_keepalive

        timers_holdtime = self.timers_holdtime

        timers_updatedelay = self.timers_updatedelay

        timers_peerwait = self.timers_peerwait

        nodefipv4unicast = self.nodefipv4unicast

        enablesnmpagentx = self.enablesnmpagentx

        enablerpki = self.enablerpki

        shutdown = self.shutdown

        shutdownmessage = self.shutdownmessage

        grglobaldisable = self.grglobaldisable

        disablepreservefwstate = self.disablepreservefwstate

        grstalepathtime = self.grstalepathtime

        grrestarttimetime = self.grrestarttimetime

        grselectdefertime = self.grselectdefertime

        grribstaletime = self.grribstaletime

        gsenable = self.gsenable

        rpkipollingperiod = self.rpkipollingperiod

        rpkiexpireinterval = self.rpkiexpireinterval

        rpkiretryinterval = self.rpkiretryinterval

        redistributeconnected = self.redistributeconnected

        redistributestatic = self.redistributestatic

        redistributekernel = self.redistributekernel

        redistributeospf = self.redistributeospf

        redistributeospf6 = self.redistributeospf6

        redistributerip = self.redistributerip

        row: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        redistributeconnected_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributeconnected_options, Unset):
            redistributeconnected_options = []
            for redistributeconnected_options_item_data in self.redistributeconnected_options:
                redistributeconnected_options_item = redistributeconnected_options_item_data.to_dict()
                redistributeconnected_options.append(redistributeconnected_options_item)

        redistributestatic_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributestatic_options, Unset):
            redistributestatic_options = []
            for redistributestatic_options_item_data in self.redistributestatic_options:
                redistributestatic_options_item = redistributestatic_options_item_data.to_dict()
                redistributestatic_options.append(redistributestatic_options_item)

        redistributekernel_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributekernel_options, Unset):
            redistributekernel_options = []
            for redistributekernel_options_item_data in self.redistributekernel_options:
                redistributekernel_options_item = redistributekernel_options_item_data.to_dict()
                redistributekernel_options.append(redistributekernel_options_item)

        redistributeospf_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributeospf_options, Unset):
            redistributeospf_options = []
            for redistributeospf_options_item_data in self.redistributeospf_options:
                redistributeospf_options_item = redistributeospf_options_item_data.to_dict()
                redistributeospf_options.append(redistributeospf_options_item)

        redistributeospf6_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributeospf6_options, Unset):
            redistributeospf6_options = []
            for redistributeospf6_options_item_data in self.redistributeospf6_options:
                redistributeospf6_options_item = redistributeospf6_options_item_data.to_dict()
                redistributeospf6_options.append(redistributeospf6_options_item)

        redistributerip_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributerip_options, Unset):
            redistributerip_options = []
            for redistributerip_options_item_data in self.redistributerip_options:
                redistributerip_options_item = redistributerip_options_item_data.to_dict()
                redistributerip_options.append(redistributerip_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if adjacencylog is not UNSET:
            field_dict["adjacencylog"] = adjacencylog
        if asnum is not UNSET:
            field_dict["asnum"] = asnum
        if routerid is not UNSET:
            field_dict["routerid"] = routerid
        if timers_keepalive is not UNSET:
            field_dict["timers_keepalive"] = timers_keepalive
        if timers_holdtime is not UNSET:
            field_dict["timers_holdtime"] = timers_holdtime
        if timers_updatedelay is not UNSET:
            field_dict["timers_updatedelay"] = timers_updatedelay
        if timers_peerwait is not UNSET:
            field_dict["timers_peerwait"] = timers_peerwait
        if nodefipv4unicast is not UNSET:
            field_dict["nodefipv4unicast"] = nodefipv4unicast
        if enablesnmpagentx is not UNSET:
            field_dict["enablesnmpagentx"] = enablesnmpagentx
        if enablerpki is not UNSET:
            field_dict["enablerpki"] = enablerpki
        if shutdown is not UNSET:
            field_dict["shutdown"] = shutdown
        if shutdownmessage is not UNSET:
            field_dict["shutdownmessage"] = shutdownmessage
        if grglobaldisable is not UNSET:
            field_dict["grglobaldisable"] = grglobaldisable
        if disablepreservefwstate is not UNSET:
            field_dict["disablepreservefwstate"] = disablepreservefwstate
        if grstalepathtime is not UNSET:
            field_dict["grstalepathtime"] = grstalepathtime
        if grrestarttimetime is not UNSET:
            field_dict["grrestarttimetime"] = grrestarttimetime
        if grselectdefertime is not UNSET:
            field_dict["grselectdefertime"] = grselectdefertime
        if grribstaletime is not UNSET:
            field_dict["grribstaletime"] = grribstaletime
        if gsenable is not UNSET:
            field_dict["gsenable"] = gsenable
        if rpkipollingperiod is not UNSET:
            field_dict["rpkipollingperiod"] = rpkipollingperiod
        if rpkiexpireinterval is not UNSET:
            field_dict["rpkiexpireinterval"] = rpkiexpireinterval
        if rpkiretryinterval is not UNSET:
            field_dict["rpkiretryinterval"] = rpkiretryinterval
        if redistributeconnected is not UNSET:
            field_dict["redistributeconnected"] = redistributeconnected
        if redistributestatic is not UNSET:
            field_dict["redistributestatic"] = redistributestatic
        if redistributekernel is not UNSET:
            field_dict["redistributekernel"] = redistributekernel
        if redistributeospf is not UNSET:
            field_dict["redistributeospf"] = redistributeospf
        if redistributeospf6 is not UNSET:
            field_dict["redistributeospf6"] = redistributeospf6
        if redistributerip is not UNSET:
            field_dict["redistributerip"] = redistributerip
        if row is not UNSET:
            field_dict["row"] = row
        if redistributeconnected_options is not UNSET:
            field_dict["redistributeconnected_options"] = redistributeconnected_options
        if redistributestatic_options is not UNSET:
            field_dict["redistributestatic_options"] = redistributestatic_options
        if redistributekernel_options is not UNSET:
            field_dict["redistributekernel_options"] = redistributekernel_options
        if redistributeospf_options is not UNSET:
            field_dict["redistributeospf_options"] = redistributeospf_options
        if redistributeospf6_options is not UNSET:
            field_dict["redistributeospf6_options"] = redistributeospf6_options
        if redistributerip_options is not UNSET:
            field_dict["redistributerip_options"] = redistributerip_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_bgp_row import FrrBgpRow
        from ..models.text_value import TextValue

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        adjacencylog = d.pop("adjacencylog", UNSET)

        asnum = d.pop("asnum", UNSET)

        routerid = d.pop("routerid", UNSET)

        timers_keepalive = d.pop("timers_keepalive", UNSET)

        timers_holdtime = d.pop("timers_holdtime", UNSET)

        timers_updatedelay = d.pop("timers_updatedelay", UNSET)

        timers_peerwait = d.pop("timers_peerwait", UNSET)

        nodefipv4unicast = d.pop("nodefipv4unicast", UNSET)

        enablesnmpagentx = d.pop("enablesnmpagentx", UNSET)

        enablerpki = d.pop("enablerpki", UNSET)

        shutdown = d.pop("shutdown", UNSET)

        shutdownmessage = d.pop("shutdownmessage", UNSET)

        grglobaldisable = d.pop("grglobaldisable", UNSET)

        disablepreservefwstate = d.pop("disablepreservefwstate", UNSET)

        grstalepathtime = d.pop("grstalepathtime", UNSET)

        grrestarttimetime = d.pop("grrestarttimetime", UNSET)

        grselectdefertime = d.pop("grselectdefertime", UNSET)

        grribstaletime = d.pop("grribstaletime", UNSET)

        gsenable = d.pop("gsenable", UNSET)

        rpkipollingperiod = d.pop("rpkipollingperiod", UNSET)

        rpkiexpireinterval = d.pop("rpkiexpireinterval", UNSET)

        rpkiretryinterval = d.pop("rpkiretryinterval", UNSET)

        redistributeconnected = d.pop("redistributeconnected", UNSET)

        redistributestatic = d.pop("redistributestatic", UNSET)

        redistributekernel = d.pop("redistributekernel", UNSET)

        redistributeospf = d.pop("redistributeospf", UNSET)

        redistributeospf6 = d.pop("redistributeospf6", UNSET)

        redistributerip = d.pop("redistributerip", UNSET)

        _row = d.pop("row", UNSET)
        row: list[FrrBgpRow] | Unset = UNSET
        if _row is not UNSET:
            row = []
            for row_item_data in _row:
                row_item = FrrBgpRow.from_dict(row_item_data)

                row.append(row_item)

        _redistributeconnected_options = d.pop("redistributeconnected_options", UNSET)
        redistributeconnected_options: list[TextValue] | Unset = UNSET
        if _redistributeconnected_options is not UNSET:
            redistributeconnected_options = []
            for redistributeconnected_options_item_data in _redistributeconnected_options:
                redistributeconnected_options_item = TextValue.from_dict(redistributeconnected_options_item_data)

                redistributeconnected_options.append(redistributeconnected_options_item)

        _redistributestatic_options = d.pop("redistributestatic_options", UNSET)
        redistributestatic_options: list[TextValue] | Unset = UNSET
        if _redistributestatic_options is not UNSET:
            redistributestatic_options = []
            for redistributestatic_options_item_data in _redistributestatic_options:
                redistributestatic_options_item = TextValue.from_dict(redistributestatic_options_item_data)

                redistributestatic_options.append(redistributestatic_options_item)

        _redistributekernel_options = d.pop("redistributekernel_options", UNSET)
        redistributekernel_options: list[TextValue] | Unset = UNSET
        if _redistributekernel_options is not UNSET:
            redistributekernel_options = []
            for redistributekernel_options_item_data in _redistributekernel_options:
                redistributekernel_options_item = TextValue.from_dict(redistributekernel_options_item_data)

                redistributekernel_options.append(redistributekernel_options_item)

        _redistributeospf_options = d.pop("redistributeospf_options", UNSET)
        redistributeospf_options: list[TextValue] | Unset = UNSET
        if _redistributeospf_options is not UNSET:
            redistributeospf_options = []
            for redistributeospf_options_item_data in _redistributeospf_options:
                redistributeospf_options_item = TextValue.from_dict(redistributeospf_options_item_data)

                redistributeospf_options.append(redistributeospf_options_item)

        _redistributeospf6_options = d.pop("redistributeospf6_options", UNSET)
        redistributeospf6_options: list[TextValue] | Unset = UNSET
        if _redistributeospf6_options is not UNSET:
            redistributeospf6_options = []
            for redistributeospf6_options_item_data in _redistributeospf6_options:
                redistributeospf6_options_item = TextValue.from_dict(redistributeospf6_options_item_data)

                redistributeospf6_options.append(redistributeospf6_options_item)

        _redistributerip_options = d.pop("redistributerip_options", UNSET)
        redistributerip_options: list[TextValue] | Unset = UNSET
        if _redistributerip_options is not UNSET:
            redistributerip_options = []
            for redistributerip_options_item_data in _redistributerip_options:
                redistributerip_options_item = TextValue.from_dict(redistributerip_options_item_data)

                redistributerip_options.append(redistributerip_options_item)

        frr_bgp = cls(
            enable=enable,
            adjacencylog=adjacencylog,
            asnum=asnum,
            routerid=routerid,
            timers_keepalive=timers_keepalive,
            timers_holdtime=timers_holdtime,
            timers_updatedelay=timers_updatedelay,
            timers_peerwait=timers_peerwait,
            nodefipv4unicast=nodefipv4unicast,
            enablesnmpagentx=enablesnmpagentx,
            enablerpki=enablerpki,
            shutdown=shutdown,
            shutdownmessage=shutdownmessage,
            grglobaldisable=grglobaldisable,
            disablepreservefwstate=disablepreservefwstate,
            grstalepathtime=grstalepathtime,
            grrestarttimetime=grrestarttimetime,
            grselectdefertime=grselectdefertime,
            grribstaletime=grribstaletime,
            gsenable=gsenable,
            rpkipollingperiod=rpkipollingperiod,
            rpkiexpireinterval=rpkiexpireinterval,
            rpkiretryinterval=rpkiretryinterval,
            redistributeconnected=redistributeconnected,
            redistributestatic=redistributestatic,
            redistributekernel=redistributekernel,
            redistributeospf=redistributeospf,
            redistributeospf6=redistributeospf6,
            redistributerip=redistributerip,
            row=row,
            redistributeconnected_options=redistributeconnected_options,
            redistributestatic_options=redistributestatic_options,
            redistributekernel_options=redistributekernel_options,
            redistributeospf_options=redistributeospf_options,
            redistributeospf6_options=redistributeospf6_options,
            redistributerip_options=redistributerip_options,
        )

        frr_bgp.additional_properties = d
        return frr_bgp

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
