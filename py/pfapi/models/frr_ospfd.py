from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_ospfd_row import FrrOspfdRow
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrOspfd")


@_attrs_define
class FrrOspfd:
    """
    Attributes:
        enable (bool | Unset): Enable

            Enable OSPF Routing
        adjacencylog (bool | Unset): Log Adjacency Changes

            If set to yes, adjacency changes will be written via syslog.
        routerid (str | Unset): Router ID

            Override the default Router ID. RID is the highest logical (loopback) IP address configured on a router.
            For more information on router identifiers see http://en.wikipedia.org/wiki/Open_Shortest_Path_First.
        spfholdtime (str | Unset): SPF Hold Time

            Set the SPF holdtime in milliseconds. The minimum time between two consecutive shortest path first calculations.
            (0-60000, Default: 1000)
        spfdelay (str | Unset): SPF Delay

            Set SPF delay in milliseconds. The delay between receiving an update to the link state database and starting the
            shortest path first calculation.
            (0-600000, Default: 200)
        enablesnmpagentx (bool | Unset): (Modules) Enable SNMP AgentX

            Enable agentx support for accessing FRR Zebra data via SNMP with the net-snmp package.
        defaultarea (str | Unset): (Default Area) Default Area

            Default OSPF area for this instance of OSPF.
            Used when an area is required but not defined elsewhere.

            For more information on Areas see http://en.wikipedia.org/wiki/Open_Shortest_Path_First#Area_types.
        defaultareatype (str | Unset): (Default Area) Default Area Type (none, stub, nosum, nssa, nssanosum)

            Defines how the default area behaves
        row (list[FrrOspfdRow] | Unset):
        redistributeconnectedsubnets (bool | Unset): (Route Redistribution) Connected Networks

            Redistribute Connected Networks
        redistributeconnectedsubnets_metric (str | Unset): (Route Redistribution) Metric

            Metric
        redistributeconnectedsubnets_metrictype (str | Unset): (Route Redistribution) Metric Type

            Metric Type 1/2
        redistributeconnectedsubnets_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributeconnectedsubnets_distlist (str | Unset): (Route Redistribution) Distribute List

            Distribute List
        redistributekernel (bool | Unset): (Route Redistribution) pfSense Kernel Routes

            Redistribute pfSense Kernel
        redistributekernel_metric (str | Unset): (Route Redistribution) Metric

            Metric
        redistributekernel_metrictype (str | Unset): (Route Redistribution) Metric Type

            Metric Type 1/2
        redistributekernel_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributekernel_distlist (str | Unset): (Route Redistribution) Distribute List

            Distribute List
        redistributebgp (bool | Unset): (Route Redistribution) BGP Routes

            Redistribute BGP
        redistributebgp_metric (str | Unset): (Route Redistribution) Metric

            Metric
        redistributebgp_metrictype (str | Unset): (Route Redistribution) Metric Type

            Metric Type 1/2
        redistributebgp_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributebgp_distlist (str | Unset): (Route Redistribution) Distribute List

            Distribute List
        redistributerip (bool | Unset): (Route Redistribution) RIP Routes

            Redistribute RIP
        redistributerip_metric (str | Unset): (Route Redistribution) Metric

            Metric
        redistributerip_metrictype (str | Unset): (Route Redistribution) Metric Type

            Metric Type 1/2
        redistributerip_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributerip_distlist (str | Unset): (Route Redistribution) Distribute List

            Distribute List
        redistributestatic (bool | Unset): (Route Redistribution) FRR Static Routes

            Redistribute FRR Static
        redistributestatic_metric (str | Unset): (Route Redistribution) Metric

            Metric
        redistributestatic_metrictype (str | Unset): (Route Redistribution) Metric Type

            Metric Type 1/2
        redistributestatic_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributestatic_distlist (str | Unset): (Route Redistribution) Distribute List

            Distribute List
        redistributedefaultroute (bool | Unset): (Default Route Redistribution) Redistribute Default

            Redistribute a Default route to neighbors
        redistributedefaultroute_always (bool | Unset): (Default Route Redistribution) Always Redistribute

            Always distribute a default route, even if routing table contains no default.
        redistributedefaultroute_metric (str | Unset): (Default Route Redistribution) Default Metric

            Default route metric (0-16777214)
        redistributedefaultroute_metrictype (str | Unset): (Default Route Redistribution) Default Metric Type

            Default Metric Type (1 or 2)
        redistributedefaultroute_routemap (str | Unset): (Default Route Redistribution) Route Map

            Route Map used to filter default route redistribution.
        rfc1583 (bool | Unset): (Advanced) RFC 1583 Compatibility

            If enabled, decisions regarding AS-external routes are evaluated according to RFC 1583/RFC 2328 (Section G.2).
            The default is no.
        opaquelsa (bool | Unset): (Advanced) Opaque LSA

            Enables support for Opaque LSA messages.
        referencebandwidth (str | Unset): (Advanced) Reference Bandwidth

            Base value, in Mbit/s, used to calculate automatic interface costs. Must be set the same on all OSPF routers
            (1-4294967, default 100).
        max_metric_administrative (bool | Unset): (Advanced) Max Metric

            Administratively Enable Max Metric
        max_metric_startup (str | Unset): (Advanced) Startup Seconds

            Max Metric Seconds at Startup (5-86400, blank to disable)
        max_metric_shutdown (str | Unset): (Advanced) Shutdown Seconds

            Max Metric Seconds at Shutdown (5-86400, blank to disable)
        writemultiplier (str | Unset): (Advanced) Write Multiplier

            Interfaces to process per write, (1-100, default 20)
        abrtype (str | Unset): (Advanced) ABR type (cisco, ibm, shortcut, standard)

            Defines the standard used when acting as an ABR
        redistributeconnectedsubnets_routemap_options (list[TextValue] | Unset):
        redistributeconnectedsubnets_distlist_options (list[TextValue] | Unset):
        redistributekernel_routemap_options (list[TextValue] | Unset):
        redistributekernel_distlist_options (list[TextValue] | Unset):
        redistributebgp_routemap_options (list[TextValue] | Unset):
        redistributebgp_distlist_options (list[TextValue] | Unset):
        redistributerip_routemap_options (list[TextValue] | Unset):
        redistributerip_distlist_options (list[TextValue] | Unset):
        redistributestatic_routemap_options (list[TextValue] | Unset):
        redistributestatic_distlist_options (list[TextValue] | Unset):
        redistributedefaultroute_routemap_options (list[TextValue] | Unset):
    """

    enable: bool | Unset = UNSET
    adjacencylog: bool | Unset = UNSET
    routerid: str | Unset = UNSET
    spfholdtime: str | Unset = UNSET
    spfdelay: str | Unset = UNSET
    enablesnmpagentx: bool | Unset = UNSET
    defaultarea: str | Unset = UNSET
    defaultareatype: str | Unset = UNSET
    row: list[FrrOspfdRow] | Unset = UNSET
    redistributeconnectedsubnets: bool | Unset = UNSET
    redistributeconnectedsubnets_metric: str | Unset = UNSET
    redistributeconnectedsubnets_metrictype: str | Unset = UNSET
    redistributeconnectedsubnets_routemap: str | Unset = UNSET
    redistributeconnectedsubnets_distlist: str | Unset = UNSET
    redistributekernel: bool | Unset = UNSET
    redistributekernel_metric: str | Unset = UNSET
    redistributekernel_metrictype: str | Unset = UNSET
    redistributekernel_routemap: str | Unset = UNSET
    redistributekernel_distlist: str | Unset = UNSET
    redistributebgp: bool | Unset = UNSET
    redistributebgp_metric: str | Unset = UNSET
    redistributebgp_metrictype: str | Unset = UNSET
    redistributebgp_routemap: str | Unset = UNSET
    redistributebgp_distlist: str | Unset = UNSET
    redistributerip: bool | Unset = UNSET
    redistributerip_metric: str | Unset = UNSET
    redistributerip_metrictype: str | Unset = UNSET
    redistributerip_routemap: str | Unset = UNSET
    redistributerip_distlist: str | Unset = UNSET
    redistributestatic: bool | Unset = UNSET
    redistributestatic_metric: str | Unset = UNSET
    redistributestatic_metrictype: str | Unset = UNSET
    redistributestatic_routemap: str | Unset = UNSET
    redistributestatic_distlist: str | Unset = UNSET
    redistributedefaultroute: bool | Unset = UNSET
    redistributedefaultroute_always: bool | Unset = UNSET
    redistributedefaultroute_metric: str | Unset = UNSET
    redistributedefaultroute_metrictype: str | Unset = UNSET
    redistributedefaultroute_routemap: str | Unset = UNSET
    rfc1583: bool | Unset = UNSET
    opaquelsa: bool | Unset = UNSET
    referencebandwidth: str | Unset = UNSET
    max_metric_administrative: bool | Unset = UNSET
    max_metric_startup: str | Unset = UNSET
    max_metric_shutdown: str | Unset = UNSET
    writemultiplier: str | Unset = UNSET
    abrtype: str | Unset = UNSET
    redistributeconnectedsubnets_routemap_options: list[TextValue] | Unset = UNSET
    redistributeconnectedsubnets_distlist_options: list[TextValue] | Unset = UNSET
    redistributekernel_routemap_options: list[TextValue] | Unset = UNSET
    redistributekernel_distlist_options: list[TextValue] | Unset = UNSET
    redistributebgp_routemap_options: list[TextValue] | Unset = UNSET
    redistributebgp_distlist_options: list[TextValue] | Unset = UNSET
    redistributerip_routemap_options: list[TextValue] | Unset = UNSET
    redistributerip_distlist_options: list[TextValue] | Unset = UNSET
    redistributestatic_routemap_options: list[TextValue] | Unset = UNSET
    redistributestatic_distlist_options: list[TextValue] | Unset = UNSET
    redistributedefaultroute_routemap_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        adjacencylog = self.adjacencylog

        routerid = self.routerid

        spfholdtime = self.spfholdtime

        spfdelay = self.spfdelay

        enablesnmpagentx = self.enablesnmpagentx

        defaultarea = self.defaultarea

        defaultareatype = self.defaultareatype

        row: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        redistributeconnectedsubnets = self.redistributeconnectedsubnets

        redistributeconnectedsubnets_metric = self.redistributeconnectedsubnets_metric

        redistributeconnectedsubnets_metrictype = self.redistributeconnectedsubnets_metrictype

        redistributeconnectedsubnets_routemap = self.redistributeconnectedsubnets_routemap

        redistributeconnectedsubnets_distlist = self.redistributeconnectedsubnets_distlist

        redistributekernel = self.redistributekernel

        redistributekernel_metric = self.redistributekernel_metric

        redistributekernel_metrictype = self.redistributekernel_metrictype

        redistributekernel_routemap = self.redistributekernel_routemap

        redistributekernel_distlist = self.redistributekernel_distlist

        redistributebgp = self.redistributebgp

        redistributebgp_metric = self.redistributebgp_metric

        redistributebgp_metrictype = self.redistributebgp_metrictype

        redistributebgp_routemap = self.redistributebgp_routemap

        redistributebgp_distlist = self.redistributebgp_distlist

        redistributerip = self.redistributerip

        redistributerip_metric = self.redistributerip_metric

        redistributerip_metrictype = self.redistributerip_metrictype

        redistributerip_routemap = self.redistributerip_routemap

        redistributerip_distlist = self.redistributerip_distlist

        redistributestatic = self.redistributestatic

        redistributestatic_metric = self.redistributestatic_metric

        redistributestatic_metrictype = self.redistributestatic_metrictype

        redistributestatic_routemap = self.redistributestatic_routemap

        redistributestatic_distlist = self.redistributestatic_distlist

        redistributedefaultroute = self.redistributedefaultroute

        redistributedefaultroute_always = self.redistributedefaultroute_always

        redistributedefaultroute_metric = self.redistributedefaultroute_metric

        redistributedefaultroute_metrictype = self.redistributedefaultroute_metrictype

        redistributedefaultroute_routemap = self.redistributedefaultroute_routemap

        rfc1583 = self.rfc1583

        opaquelsa = self.opaquelsa

        referencebandwidth = self.referencebandwidth

        max_metric_administrative = self.max_metric_administrative

        max_metric_startup = self.max_metric_startup

        max_metric_shutdown = self.max_metric_shutdown

        writemultiplier = self.writemultiplier

        abrtype = self.abrtype

        redistributeconnectedsubnets_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributeconnectedsubnets_routemap_options, Unset):
            redistributeconnectedsubnets_routemap_options = []
            for (
                redistributeconnectedsubnets_routemap_options_item_data
            ) in self.redistributeconnectedsubnets_routemap_options:
                redistributeconnectedsubnets_routemap_options_item = (
                    redistributeconnectedsubnets_routemap_options_item_data.to_dict()
                )
                redistributeconnectedsubnets_routemap_options.append(redistributeconnectedsubnets_routemap_options_item)

        redistributeconnectedsubnets_distlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributeconnectedsubnets_distlist_options, Unset):
            redistributeconnectedsubnets_distlist_options = []
            for (
                redistributeconnectedsubnets_distlist_options_item_data
            ) in self.redistributeconnectedsubnets_distlist_options:
                redistributeconnectedsubnets_distlist_options_item = (
                    redistributeconnectedsubnets_distlist_options_item_data.to_dict()
                )
                redistributeconnectedsubnets_distlist_options.append(redistributeconnectedsubnets_distlist_options_item)

        redistributekernel_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributekernel_routemap_options, Unset):
            redistributekernel_routemap_options = []
            for redistributekernel_routemap_options_item_data in self.redistributekernel_routemap_options:
                redistributekernel_routemap_options_item = redistributekernel_routemap_options_item_data.to_dict()
                redistributekernel_routemap_options.append(redistributekernel_routemap_options_item)

        redistributekernel_distlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributekernel_distlist_options, Unset):
            redistributekernel_distlist_options = []
            for redistributekernel_distlist_options_item_data in self.redistributekernel_distlist_options:
                redistributekernel_distlist_options_item = redistributekernel_distlist_options_item_data.to_dict()
                redistributekernel_distlist_options.append(redistributekernel_distlist_options_item)

        redistributebgp_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributebgp_routemap_options, Unset):
            redistributebgp_routemap_options = []
            for redistributebgp_routemap_options_item_data in self.redistributebgp_routemap_options:
                redistributebgp_routemap_options_item = redistributebgp_routemap_options_item_data.to_dict()
                redistributebgp_routemap_options.append(redistributebgp_routemap_options_item)

        redistributebgp_distlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributebgp_distlist_options, Unset):
            redistributebgp_distlist_options = []
            for redistributebgp_distlist_options_item_data in self.redistributebgp_distlist_options:
                redistributebgp_distlist_options_item = redistributebgp_distlist_options_item_data.to_dict()
                redistributebgp_distlist_options.append(redistributebgp_distlist_options_item)

        redistributerip_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributerip_routemap_options, Unset):
            redistributerip_routemap_options = []
            for redistributerip_routemap_options_item_data in self.redistributerip_routemap_options:
                redistributerip_routemap_options_item = redistributerip_routemap_options_item_data.to_dict()
                redistributerip_routemap_options.append(redistributerip_routemap_options_item)

        redistributerip_distlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributerip_distlist_options, Unset):
            redistributerip_distlist_options = []
            for redistributerip_distlist_options_item_data in self.redistributerip_distlist_options:
                redistributerip_distlist_options_item = redistributerip_distlist_options_item_data.to_dict()
                redistributerip_distlist_options.append(redistributerip_distlist_options_item)

        redistributestatic_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributestatic_routemap_options, Unset):
            redistributestatic_routemap_options = []
            for redistributestatic_routemap_options_item_data in self.redistributestatic_routemap_options:
                redistributestatic_routemap_options_item = redistributestatic_routemap_options_item_data.to_dict()
                redistributestatic_routemap_options.append(redistributestatic_routemap_options_item)

        redistributestatic_distlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributestatic_distlist_options, Unset):
            redistributestatic_distlist_options = []
            for redistributestatic_distlist_options_item_data in self.redistributestatic_distlist_options:
                redistributestatic_distlist_options_item = redistributestatic_distlist_options_item_data.to_dict()
                redistributestatic_distlist_options.append(redistributestatic_distlist_options_item)

        redistributedefaultroute_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributedefaultroute_routemap_options, Unset):
            redistributedefaultroute_routemap_options = []
            for redistributedefaultroute_routemap_options_item_data in self.redistributedefaultroute_routemap_options:
                redistributedefaultroute_routemap_options_item = (
                    redistributedefaultroute_routemap_options_item_data.to_dict()
                )
                redistributedefaultroute_routemap_options.append(redistributedefaultroute_routemap_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if adjacencylog is not UNSET:
            field_dict["adjacencylog"] = adjacencylog
        if routerid is not UNSET:
            field_dict["routerid"] = routerid
        if spfholdtime is not UNSET:
            field_dict["spfholdtime"] = spfholdtime
        if spfdelay is not UNSET:
            field_dict["spfdelay"] = spfdelay
        if enablesnmpagentx is not UNSET:
            field_dict["enablesnmpagentx"] = enablesnmpagentx
        if defaultarea is not UNSET:
            field_dict["defaultarea"] = defaultarea
        if defaultareatype is not UNSET:
            field_dict["defaultareatype"] = defaultareatype
        if row is not UNSET:
            field_dict["row"] = row
        if redistributeconnectedsubnets is not UNSET:
            field_dict["redistributeconnectedsubnets"] = redistributeconnectedsubnets
        if redistributeconnectedsubnets_metric is not UNSET:
            field_dict["redistributeconnectedsubnets_metric"] = redistributeconnectedsubnets_metric
        if redistributeconnectedsubnets_metrictype is not UNSET:
            field_dict["redistributeconnectedsubnets_metrictype"] = redistributeconnectedsubnets_metrictype
        if redistributeconnectedsubnets_routemap is not UNSET:
            field_dict["redistributeconnectedsubnets_routemap"] = redistributeconnectedsubnets_routemap
        if redistributeconnectedsubnets_distlist is not UNSET:
            field_dict["redistributeconnectedsubnets_distlist"] = redistributeconnectedsubnets_distlist
        if redistributekernel is not UNSET:
            field_dict["redistributekernel"] = redistributekernel
        if redistributekernel_metric is not UNSET:
            field_dict["redistributekernel_metric"] = redistributekernel_metric
        if redistributekernel_metrictype is not UNSET:
            field_dict["redistributekernel_metrictype"] = redistributekernel_metrictype
        if redistributekernel_routemap is not UNSET:
            field_dict["redistributekernel_routemap"] = redistributekernel_routemap
        if redistributekernel_distlist is not UNSET:
            field_dict["redistributekernel_distlist"] = redistributekernel_distlist
        if redistributebgp is not UNSET:
            field_dict["redistributebgp"] = redistributebgp
        if redistributebgp_metric is not UNSET:
            field_dict["redistributebgp_metric"] = redistributebgp_metric
        if redistributebgp_metrictype is not UNSET:
            field_dict["redistributebgp_metrictype"] = redistributebgp_metrictype
        if redistributebgp_routemap is not UNSET:
            field_dict["redistributebgp_routemap"] = redistributebgp_routemap
        if redistributebgp_distlist is not UNSET:
            field_dict["redistributebgp_distlist"] = redistributebgp_distlist
        if redistributerip is not UNSET:
            field_dict["redistributerip"] = redistributerip
        if redistributerip_metric is not UNSET:
            field_dict["redistributerip_metric"] = redistributerip_metric
        if redistributerip_metrictype is not UNSET:
            field_dict["redistributerip_metrictype"] = redistributerip_metrictype
        if redistributerip_routemap is not UNSET:
            field_dict["redistributerip_routemap"] = redistributerip_routemap
        if redistributerip_distlist is not UNSET:
            field_dict["redistributerip_distlist"] = redistributerip_distlist
        if redistributestatic is not UNSET:
            field_dict["redistributestatic"] = redistributestatic
        if redistributestatic_metric is not UNSET:
            field_dict["redistributestatic_metric"] = redistributestatic_metric
        if redistributestatic_metrictype is not UNSET:
            field_dict["redistributestatic_metrictype"] = redistributestatic_metrictype
        if redistributestatic_routemap is not UNSET:
            field_dict["redistributestatic_routemap"] = redistributestatic_routemap
        if redistributestatic_distlist is not UNSET:
            field_dict["redistributestatic_distlist"] = redistributestatic_distlist
        if redistributedefaultroute is not UNSET:
            field_dict["redistributedefaultroute"] = redistributedefaultroute
        if redistributedefaultroute_always is not UNSET:
            field_dict["redistributedefaultroute_always"] = redistributedefaultroute_always
        if redistributedefaultroute_metric is not UNSET:
            field_dict["redistributedefaultroute_metric"] = redistributedefaultroute_metric
        if redistributedefaultroute_metrictype is not UNSET:
            field_dict["redistributedefaultroute_metrictype"] = redistributedefaultroute_metrictype
        if redistributedefaultroute_routemap is not UNSET:
            field_dict["redistributedefaultroute_routemap"] = redistributedefaultroute_routemap
        if rfc1583 is not UNSET:
            field_dict["rfc1583"] = rfc1583
        if opaquelsa is not UNSET:
            field_dict["opaquelsa"] = opaquelsa
        if referencebandwidth is not UNSET:
            field_dict["referencebandwidth"] = referencebandwidth
        if max_metric_administrative is not UNSET:
            field_dict["max_metric_administrative"] = max_metric_administrative
        if max_metric_startup is not UNSET:
            field_dict["max_metric_startup"] = max_metric_startup
        if max_metric_shutdown is not UNSET:
            field_dict["max_metric_shutdown"] = max_metric_shutdown
        if writemultiplier is not UNSET:
            field_dict["writemultiplier"] = writemultiplier
        if abrtype is not UNSET:
            field_dict["abrtype"] = abrtype
        if redistributeconnectedsubnets_routemap_options is not UNSET:
            field_dict["redistributeconnectedsubnets_routemap_options"] = redistributeconnectedsubnets_routemap_options
        if redistributeconnectedsubnets_distlist_options is not UNSET:
            field_dict["redistributeconnectedsubnets_distlist_options"] = redistributeconnectedsubnets_distlist_options
        if redistributekernel_routemap_options is not UNSET:
            field_dict["redistributekernel_routemap_options"] = redistributekernel_routemap_options
        if redistributekernel_distlist_options is not UNSET:
            field_dict["redistributekernel_distlist_options"] = redistributekernel_distlist_options
        if redistributebgp_routemap_options is not UNSET:
            field_dict["redistributebgp_routemap_options"] = redistributebgp_routemap_options
        if redistributebgp_distlist_options is not UNSET:
            field_dict["redistributebgp_distlist_options"] = redistributebgp_distlist_options
        if redistributerip_routemap_options is not UNSET:
            field_dict["redistributerip_routemap_options"] = redistributerip_routemap_options
        if redistributerip_distlist_options is not UNSET:
            field_dict["redistributerip_distlist_options"] = redistributerip_distlist_options
        if redistributestatic_routemap_options is not UNSET:
            field_dict["redistributestatic_routemap_options"] = redistributestatic_routemap_options
        if redistributestatic_distlist_options is not UNSET:
            field_dict["redistributestatic_distlist_options"] = redistributestatic_distlist_options
        if redistributedefaultroute_routemap_options is not UNSET:
            field_dict["redistributedefaultroute_routemap_options"] = redistributedefaultroute_routemap_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_ospfd_row import FrrOspfdRow
        from ..models.text_value import TextValue

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        adjacencylog = d.pop("adjacencylog", UNSET)

        routerid = d.pop("routerid", UNSET)

        spfholdtime = d.pop("spfholdtime", UNSET)

        spfdelay = d.pop("spfdelay", UNSET)

        enablesnmpagentx = d.pop("enablesnmpagentx", UNSET)

        defaultarea = d.pop("defaultarea", UNSET)

        defaultareatype = d.pop("defaultareatype", UNSET)

        _row = d.pop("row", UNSET)
        row: list[FrrOspfdRow] | Unset = UNSET
        if _row is not UNSET:
            row = []
            for row_item_data in _row:
                row_item = FrrOspfdRow.from_dict(row_item_data)

                row.append(row_item)

        redistributeconnectedsubnets = d.pop("redistributeconnectedsubnets", UNSET)

        redistributeconnectedsubnets_metric = d.pop("redistributeconnectedsubnets_metric", UNSET)

        redistributeconnectedsubnets_metrictype = d.pop("redistributeconnectedsubnets_metrictype", UNSET)

        redistributeconnectedsubnets_routemap = d.pop("redistributeconnectedsubnets_routemap", UNSET)

        redistributeconnectedsubnets_distlist = d.pop("redistributeconnectedsubnets_distlist", UNSET)

        redistributekernel = d.pop("redistributekernel", UNSET)

        redistributekernel_metric = d.pop("redistributekernel_metric", UNSET)

        redistributekernel_metrictype = d.pop("redistributekernel_metrictype", UNSET)

        redistributekernel_routemap = d.pop("redistributekernel_routemap", UNSET)

        redistributekernel_distlist = d.pop("redistributekernel_distlist", UNSET)

        redistributebgp = d.pop("redistributebgp", UNSET)

        redistributebgp_metric = d.pop("redistributebgp_metric", UNSET)

        redistributebgp_metrictype = d.pop("redistributebgp_metrictype", UNSET)

        redistributebgp_routemap = d.pop("redistributebgp_routemap", UNSET)

        redistributebgp_distlist = d.pop("redistributebgp_distlist", UNSET)

        redistributerip = d.pop("redistributerip", UNSET)

        redistributerip_metric = d.pop("redistributerip_metric", UNSET)

        redistributerip_metrictype = d.pop("redistributerip_metrictype", UNSET)

        redistributerip_routemap = d.pop("redistributerip_routemap", UNSET)

        redistributerip_distlist = d.pop("redistributerip_distlist", UNSET)

        redistributestatic = d.pop("redistributestatic", UNSET)

        redistributestatic_metric = d.pop("redistributestatic_metric", UNSET)

        redistributestatic_metrictype = d.pop("redistributestatic_metrictype", UNSET)

        redistributestatic_routemap = d.pop("redistributestatic_routemap", UNSET)

        redistributestatic_distlist = d.pop("redistributestatic_distlist", UNSET)

        redistributedefaultroute = d.pop("redistributedefaultroute", UNSET)

        redistributedefaultroute_always = d.pop("redistributedefaultroute_always", UNSET)

        redistributedefaultroute_metric = d.pop("redistributedefaultroute_metric", UNSET)

        redistributedefaultroute_metrictype = d.pop("redistributedefaultroute_metrictype", UNSET)

        redistributedefaultroute_routemap = d.pop("redistributedefaultroute_routemap", UNSET)

        rfc1583 = d.pop("rfc1583", UNSET)

        opaquelsa = d.pop("opaquelsa", UNSET)

        referencebandwidth = d.pop("referencebandwidth", UNSET)

        max_metric_administrative = d.pop("max_metric_administrative", UNSET)

        max_metric_startup = d.pop("max_metric_startup", UNSET)

        max_metric_shutdown = d.pop("max_metric_shutdown", UNSET)

        writemultiplier = d.pop("writemultiplier", UNSET)

        abrtype = d.pop("abrtype", UNSET)

        _redistributeconnectedsubnets_routemap_options = d.pop("redistributeconnectedsubnets_routemap_options", UNSET)
        redistributeconnectedsubnets_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributeconnectedsubnets_routemap_options is not UNSET:
            redistributeconnectedsubnets_routemap_options = []
            for (
                redistributeconnectedsubnets_routemap_options_item_data
            ) in _redistributeconnectedsubnets_routemap_options:
                redistributeconnectedsubnets_routemap_options_item = TextValue.from_dict(
                    redistributeconnectedsubnets_routemap_options_item_data
                )

                redistributeconnectedsubnets_routemap_options.append(redistributeconnectedsubnets_routemap_options_item)

        _redistributeconnectedsubnets_distlist_options = d.pop("redistributeconnectedsubnets_distlist_options", UNSET)
        redistributeconnectedsubnets_distlist_options: list[TextValue] | Unset = UNSET
        if _redistributeconnectedsubnets_distlist_options is not UNSET:
            redistributeconnectedsubnets_distlist_options = []
            for (
                redistributeconnectedsubnets_distlist_options_item_data
            ) in _redistributeconnectedsubnets_distlist_options:
                redistributeconnectedsubnets_distlist_options_item = TextValue.from_dict(
                    redistributeconnectedsubnets_distlist_options_item_data
                )

                redistributeconnectedsubnets_distlist_options.append(redistributeconnectedsubnets_distlist_options_item)

        _redistributekernel_routemap_options = d.pop("redistributekernel_routemap_options", UNSET)
        redistributekernel_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributekernel_routemap_options is not UNSET:
            redistributekernel_routemap_options = []
            for redistributekernel_routemap_options_item_data in _redistributekernel_routemap_options:
                redistributekernel_routemap_options_item = TextValue.from_dict(
                    redistributekernel_routemap_options_item_data
                )

                redistributekernel_routemap_options.append(redistributekernel_routemap_options_item)

        _redistributekernel_distlist_options = d.pop("redistributekernel_distlist_options", UNSET)
        redistributekernel_distlist_options: list[TextValue] | Unset = UNSET
        if _redistributekernel_distlist_options is not UNSET:
            redistributekernel_distlist_options = []
            for redistributekernel_distlist_options_item_data in _redistributekernel_distlist_options:
                redistributekernel_distlist_options_item = TextValue.from_dict(
                    redistributekernel_distlist_options_item_data
                )

                redistributekernel_distlist_options.append(redistributekernel_distlist_options_item)

        _redistributebgp_routemap_options = d.pop("redistributebgp_routemap_options", UNSET)
        redistributebgp_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributebgp_routemap_options is not UNSET:
            redistributebgp_routemap_options = []
            for redistributebgp_routemap_options_item_data in _redistributebgp_routemap_options:
                redistributebgp_routemap_options_item = TextValue.from_dict(redistributebgp_routemap_options_item_data)

                redistributebgp_routemap_options.append(redistributebgp_routemap_options_item)

        _redistributebgp_distlist_options = d.pop("redistributebgp_distlist_options", UNSET)
        redistributebgp_distlist_options: list[TextValue] | Unset = UNSET
        if _redistributebgp_distlist_options is not UNSET:
            redistributebgp_distlist_options = []
            for redistributebgp_distlist_options_item_data in _redistributebgp_distlist_options:
                redistributebgp_distlist_options_item = TextValue.from_dict(redistributebgp_distlist_options_item_data)

                redistributebgp_distlist_options.append(redistributebgp_distlist_options_item)

        _redistributerip_routemap_options = d.pop("redistributerip_routemap_options", UNSET)
        redistributerip_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributerip_routemap_options is not UNSET:
            redistributerip_routemap_options = []
            for redistributerip_routemap_options_item_data in _redistributerip_routemap_options:
                redistributerip_routemap_options_item = TextValue.from_dict(redistributerip_routemap_options_item_data)

                redistributerip_routemap_options.append(redistributerip_routemap_options_item)

        _redistributerip_distlist_options = d.pop("redistributerip_distlist_options", UNSET)
        redistributerip_distlist_options: list[TextValue] | Unset = UNSET
        if _redistributerip_distlist_options is not UNSET:
            redistributerip_distlist_options = []
            for redistributerip_distlist_options_item_data in _redistributerip_distlist_options:
                redistributerip_distlist_options_item = TextValue.from_dict(redistributerip_distlist_options_item_data)

                redistributerip_distlist_options.append(redistributerip_distlist_options_item)

        _redistributestatic_routemap_options = d.pop("redistributestatic_routemap_options", UNSET)
        redistributestatic_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributestatic_routemap_options is not UNSET:
            redistributestatic_routemap_options = []
            for redistributestatic_routemap_options_item_data in _redistributestatic_routemap_options:
                redistributestatic_routemap_options_item = TextValue.from_dict(
                    redistributestatic_routemap_options_item_data
                )

                redistributestatic_routemap_options.append(redistributestatic_routemap_options_item)

        _redistributestatic_distlist_options = d.pop("redistributestatic_distlist_options", UNSET)
        redistributestatic_distlist_options: list[TextValue] | Unset = UNSET
        if _redistributestatic_distlist_options is not UNSET:
            redistributestatic_distlist_options = []
            for redistributestatic_distlist_options_item_data in _redistributestatic_distlist_options:
                redistributestatic_distlist_options_item = TextValue.from_dict(
                    redistributestatic_distlist_options_item_data
                )

                redistributestatic_distlist_options.append(redistributestatic_distlist_options_item)

        _redistributedefaultroute_routemap_options = d.pop("redistributedefaultroute_routemap_options", UNSET)
        redistributedefaultroute_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributedefaultroute_routemap_options is not UNSET:
            redistributedefaultroute_routemap_options = []
            for redistributedefaultroute_routemap_options_item_data in _redistributedefaultroute_routemap_options:
                redistributedefaultroute_routemap_options_item = TextValue.from_dict(
                    redistributedefaultroute_routemap_options_item_data
                )

                redistributedefaultroute_routemap_options.append(redistributedefaultroute_routemap_options_item)

        frr_ospfd = cls(
            enable=enable,
            adjacencylog=adjacencylog,
            routerid=routerid,
            spfholdtime=spfholdtime,
            spfdelay=spfdelay,
            enablesnmpagentx=enablesnmpagentx,
            defaultarea=defaultarea,
            defaultareatype=defaultareatype,
            row=row,
            redistributeconnectedsubnets=redistributeconnectedsubnets,
            redistributeconnectedsubnets_metric=redistributeconnectedsubnets_metric,
            redistributeconnectedsubnets_metrictype=redistributeconnectedsubnets_metrictype,
            redistributeconnectedsubnets_routemap=redistributeconnectedsubnets_routemap,
            redistributeconnectedsubnets_distlist=redistributeconnectedsubnets_distlist,
            redistributekernel=redistributekernel,
            redistributekernel_metric=redistributekernel_metric,
            redistributekernel_metrictype=redistributekernel_metrictype,
            redistributekernel_routemap=redistributekernel_routemap,
            redistributekernel_distlist=redistributekernel_distlist,
            redistributebgp=redistributebgp,
            redistributebgp_metric=redistributebgp_metric,
            redistributebgp_metrictype=redistributebgp_metrictype,
            redistributebgp_routemap=redistributebgp_routemap,
            redistributebgp_distlist=redistributebgp_distlist,
            redistributerip=redistributerip,
            redistributerip_metric=redistributerip_metric,
            redistributerip_metrictype=redistributerip_metrictype,
            redistributerip_routemap=redistributerip_routemap,
            redistributerip_distlist=redistributerip_distlist,
            redistributestatic=redistributestatic,
            redistributestatic_metric=redistributestatic_metric,
            redistributestatic_metrictype=redistributestatic_metrictype,
            redistributestatic_routemap=redistributestatic_routemap,
            redistributestatic_distlist=redistributestatic_distlist,
            redistributedefaultroute=redistributedefaultroute,
            redistributedefaultroute_always=redistributedefaultroute_always,
            redistributedefaultroute_metric=redistributedefaultroute_metric,
            redistributedefaultroute_metrictype=redistributedefaultroute_metrictype,
            redistributedefaultroute_routemap=redistributedefaultroute_routemap,
            rfc1583=rfc1583,
            opaquelsa=opaquelsa,
            referencebandwidth=referencebandwidth,
            max_metric_administrative=max_metric_administrative,
            max_metric_startup=max_metric_startup,
            max_metric_shutdown=max_metric_shutdown,
            writemultiplier=writemultiplier,
            abrtype=abrtype,
            redistributeconnectedsubnets_routemap_options=redistributeconnectedsubnets_routemap_options,
            redistributeconnectedsubnets_distlist_options=redistributeconnectedsubnets_distlist_options,
            redistributekernel_routemap_options=redistributekernel_routemap_options,
            redistributekernel_distlist_options=redistributekernel_distlist_options,
            redistributebgp_routemap_options=redistributebgp_routemap_options,
            redistributebgp_distlist_options=redistributebgp_distlist_options,
            redistributerip_routemap_options=redistributerip_routemap_options,
            redistributerip_distlist_options=redistributerip_distlist_options,
            redistributestatic_routemap_options=redistributestatic_routemap_options,
            redistributestatic_distlist_options=redistributestatic_distlist_options,
            redistributedefaultroute_routemap_options=redistributedefaultroute_routemap_options,
        )

        frr_ospfd.additional_properties = d
        return frr_ospfd

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
