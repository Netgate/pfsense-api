from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_ospf_6d_row import FrrOspf6DRow
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrOspf6D")


@_attrs_define
class FrrOspf6D:
    """
    Attributes:
        enable (bool | Unset): Enable

            Enable OSPF6 Routing
        adjacencylog (bool | Unset): Log Adjacency Changes

            If set to yes, adjacency changes will be written via syslog.
        routerid (str | Unset): Router ID

            Override the default Router ID. RID is the highest logical (loopback) IP address configured on a router.
            For more information on router identifiers see http://en.wikipedia.org/wiki/Open_Shortest_Path_First
        updatefib (str | Unset): Disable FIB updates (Routing table) (none, stub)

            Disables the updating of the host routing table (turns into stub router).
        spfholdtime (str | Unset): SPF Hold Time

            Set the SPF holdtime in milliseconds. The minimum time between two consecutive shortest path first calculations.
            The default value is 5 seconds; the valid range is 1-5 seconds.
        spfdelay (str | Unset): SPF Delay

            Set SPF delay in milliseconds. The delay between receiving an update to the link state database and starting the
            shortest path first calculation.
            The default value is 1; valid range is 1-10 seconds.
        enablesnmpagentx (bool | Unset): (Modules) Enable SNMP AgentX

            Enable agentx support for accessing FRR OSPF6 data via SNMP with the net-snmp package.
        defaultarea (str | Unset): (Default Area) Default Area

            Default OSPF6 area for this instance of OSPF6.
            Used when an area is required but not defined elsewhere.
            For more information on Areas see http://en.wikipedia.org/wiki/Open_Shortest_Path_First#Area_types
        defaultareatype (str | Unset): (Default Area) Default Area Type (none, stub, nosum)

            Defines how the default area behaves
        row (list[FrrOspf6DRow] | Unset):
        redistributeconnectedsubnets (bool | Unset): (Route Redistribution) Connected Networks

            Redistribute Connected Networks
        redistributeconnectedsubnets_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributekernel (bool | Unset): (Route Redistribution) pfSense Kernel Routes

            Redistribute pfSense Kernel
        redistributekernel_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributebgp (bool | Unset): (Route Redistribution) BGP Routes

            Redistribute BGP
        redistributebgp_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributestatic (bool | Unset): (Route Redistribution) FRR Static Routes

            Redistribute FRR Static
        redistributestatic_routemap (str | Unset): (Route Redistribution)

            Route Map
        exportlist (str | Unset): (Route Filtering) Export List

            Uses this access list to filter route information transmitted to OSPF peers
        importlist (str | Unset): (Route Filtering) Import List

            Uses this access list to filter route information received from OSPF peers
        filterlist_out (str | Unset): (Route Filtering) Filter List (Out)

            Uses a prefix list to filter route information transmitted to OSPF peers
        filterlist_in (str | Unset): (Route Filtering) Filter List (In)

            Uses a prefix list to filter route information received from OSPF peers
        referencebandwidth (str | Unset): (Advanced) Reference Bandwidth

            Base value, in Mbit/s, used to calculate automatic interface costs. Must be set the same on all OSPF routers
            (1-4294967, default 100).
        distance (str | Unset): (Advanced) Distance

            Administrative distance (1-255).
        distance_external (str | Unset): (Advanced) External Distance

            External route distance (1-255).
        distance_interarea (str | Unset): (Advanced) Inter-area Distance

            Inter-area route distance (1-255).
        distance_intraarea (str | Unset): (Advanced) Intra-area Distance

            Intra-area route distance (1-255).
        redistributeconnectedsubnets_routemap_options (list[TextValue] | Unset):
        redistributekernel_routemap_options (list[TextValue] | Unset):
        redistributebgp_routemap_options (list[TextValue] | Unset):
        redistributestatic_routemap_options (list[TextValue] | Unset):
        exportlist_options (list[TextValue] | Unset):
        importlist_options (list[TextValue] | Unset):
        filterlist_out_options (list[TextValue] | Unset):
        filterlist_in_options (list[TextValue] | Unset):
    """

    enable: bool | Unset = UNSET
    adjacencylog: bool | Unset = UNSET
    routerid: str | Unset = UNSET
    updatefib: str | Unset = UNSET
    spfholdtime: str | Unset = UNSET
    spfdelay: str | Unset = UNSET
    enablesnmpagentx: bool | Unset = UNSET
    defaultarea: str | Unset = UNSET
    defaultareatype: str | Unset = UNSET
    row: list[FrrOspf6DRow] | Unset = UNSET
    redistributeconnectedsubnets: bool | Unset = UNSET
    redistributeconnectedsubnets_routemap: str | Unset = UNSET
    redistributekernel: bool | Unset = UNSET
    redistributekernel_routemap: str | Unset = UNSET
    redistributebgp: bool | Unset = UNSET
    redistributebgp_routemap: str | Unset = UNSET
    redistributestatic: bool | Unset = UNSET
    redistributestatic_routemap: str | Unset = UNSET
    exportlist: str | Unset = UNSET
    importlist: str | Unset = UNSET
    filterlist_out: str | Unset = UNSET
    filterlist_in: str | Unset = UNSET
    referencebandwidth: str | Unset = UNSET
    distance: str | Unset = UNSET
    distance_external: str | Unset = UNSET
    distance_interarea: str | Unset = UNSET
    distance_intraarea: str | Unset = UNSET
    redistributeconnectedsubnets_routemap_options: list[TextValue] | Unset = UNSET
    redistributekernel_routemap_options: list[TextValue] | Unset = UNSET
    redistributebgp_routemap_options: list[TextValue] | Unset = UNSET
    redistributestatic_routemap_options: list[TextValue] | Unset = UNSET
    exportlist_options: list[TextValue] | Unset = UNSET
    importlist_options: list[TextValue] | Unset = UNSET
    filterlist_out_options: list[TextValue] | Unset = UNSET
    filterlist_in_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        adjacencylog = self.adjacencylog

        routerid = self.routerid

        updatefib = self.updatefib

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

        redistributeconnectedsubnets_routemap = self.redistributeconnectedsubnets_routemap

        redistributekernel = self.redistributekernel

        redistributekernel_routemap = self.redistributekernel_routemap

        redistributebgp = self.redistributebgp

        redistributebgp_routemap = self.redistributebgp_routemap

        redistributestatic = self.redistributestatic

        redistributestatic_routemap = self.redistributestatic_routemap

        exportlist = self.exportlist

        importlist = self.importlist

        filterlist_out = self.filterlist_out

        filterlist_in = self.filterlist_in

        referencebandwidth = self.referencebandwidth

        distance = self.distance

        distance_external = self.distance_external

        distance_interarea = self.distance_interarea

        distance_intraarea = self.distance_intraarea

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

        redistributekernel_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributekernel_routemap_options, Unset):
            redistributekernel_routemap_options = []
            for redistributekernel_routemap_options_item_data in self.redistributekernel_routemap_options:
                redistributekernel_routemap_options_item = redistributekernel_routemap_options_item_data.to_dict()
                redistributekernel_routemap_options.append(redistributekernel_routemap_options_item)

        redistributebgp_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributebgp_routemap_options, Unset):
            redistributebgp_routemap_options = []
            for redistributebgp_routemap_options_item_data in self.redistributebgp_routemap_options:
                redistributebgp_routemap_options_item = redistributebgp_routemap_options_item_data.to_dict()
                redistributebgp_routemap_options.append(redistributebgp_routemap_options_item)

        redistributestatic_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributestatic_routemap_options, Unset):
            redistributestatic_routemap_options = []
            for redistributestatic_routemap_options_item_data in self.redistributestatic_routemap_options:
                redistributestatic_routemap_options_item = redistributestatic_routemap_options_item_data.to_dict()
                redistributestatic_routemap_options.append(redistributestatic_routemap_options_item)

        exportlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exportlist_options, Unset):
            exportlist_options = []
            for exportlist_options_item_data in self.exportlist_options:
                exportlist_options_item = exportlist_options_item_data.to_dict()
                exportlist_options.append(exportlist_options_item)

        importlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.importlist_options, Unset):
            importlist_options = []
            for importlist_options_item_data in self.importlist_options:
                importlist_options_item = importlist_options_item_data.to_dict()
                importlist_options.append(importlist_options_item)

        filterlist_out_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filterlist_out_options, Unset):
            filterlist_out_options = []
            for filterlist_out_options_item_data in self.filterlist_out_options:
                filterlist_out_options_item = filterlist_out_options_item_data.to_dict()
                filterlist_out_options.append(filterlist_out_options_item)

        filterlist_in_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filterlist_in_options, Unset):
            filterlist_in_options = []
            for filterlist_in_options_item_data in self.filterlist_in_options:
                filterlist_in_options_item = filterlist_in_options_item_data.to_dict()
                filterlist_in_options.append(filterlist_in_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if adjacencylog is not UNSET:
            field_dict["adjacencylog"] = adjacencylog
        if routerid is not UNSET:
            field_dict["routerid"] = routerid
        if updatefib is not UNSET:
            field_dict["updatefib"] = updatefib
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
        if redistributeconnectedsubnets_routemap is not UNSET:
            field_dict["redistributeconnectedsubnets_routemap"] = redistributeconnectedsubnets_routemap
        if redistributekernel is not UNSET:
            field_dict["redistributekernel"] = redistributekernel
        if redistributekernel_routemap is not UNSET:
            field_dict["redistributekernel_routemap"] = redistributekernel_routemap
        if redistributebgp is not UNSET:
            field_dict["redistributebgp"] = redistributebgp
        if redistributebgp_routemap is not UNSET:
            field_dict["redistributebgp_routemap"] = redistributebgp_routemap
        if redistributestatic is not UNSET:
            field_dict["redistributestatic"] = redistributestatic
        if redistributestatic_routemap is not UNSET:
            field_dict["redistributestatic_routemap"] = redistributestatic_routemap
        if exportlist is not UNSET:
            field_dict["exportlist"] = exportlist
        if importlist is not UNSET:
            field_dict["importlist"] = importlist
        if filterlist_out is not UNSET:
            field_dict["filterlist_out"] = filterlist_out
        if filterlist_in is not UNSET:
            field_dict["filterlist_in"] = filterlist_in
        if referencebandwidth is not UNSET:
            field_dict["referencebandwidth"] = referencebandwidth
        if distance is not UNSET:
            field_dict["distance"] = distance
        if distance_external is not UNSET:
            field_dict["distance_external"] = distance_external
        if distance_interarea is not UNSET:
            field_dict["distance_interarea"] = distance_interarea
        if distance_intraarea is not UNSET:
            field_dict["distance_intraarea"] = distance_intraarea
        if redistributeconnectedsubnets_routemap_options is not UNSET:
            field_dict["redistributeconnectedsubnets_routemap_options"] = redistributeconnectedsubnets_routemap_options
        if redistributekernel_routemap_options is not UNSET:
            field_dict["redistributekernel_routemap_options"] = redistributekernel_routemap_options
        if redistributebgp_routemap_options is not UNSET:
            field_dict["redistributebgp_routemap_options"] = redistributebgp_routemap_options
        if redistributestatic_routemap_options is not UNSET:
            field_dict["redistributestatic_routemap_options"] = redistributestatic_routemap_options
        if exportlist_options is not UNSET:
            field_dict["exportlist_options"] = exportlist_options
        if importlist_options is not UNSET:
            field_dict["importlist_options"] = importlist_options
        if filterlist_out_options is not UNSET:
            field_dict["filterlist_out_options"] = filterlist_out_options
        if filterlist_in_options is not UNSET:
            field_dict["filterlist_in_options"] = filterlist_in_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_ospf_6d_row import FrrOspf6DRow
        from ..models.text_value import TextValue

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        adjacencylog = d.pop("adjacencylog", UNSET)

        routerid = d.pop("routerid", UNSET)

        updatefib = d.pop("updatefib", UNSET)

        spfholdtime = d.pop("spfholdtime", UNSET)

        spfdelay = d.pop("spfdelay", UNSET)

        enablesnmpagentx = d.pop("enablesnmpagentx", UNSET)

        defaultarea = d.pop("defaultarea", UNSET)

        defaultareatype = d.pop("defaultareatype", UNSET)

        _row = d.pop("row", UNSET)
        row: list[FrrOspf6DRow] | Unset = UNSET
        if _row is not UNSET:
            row = []
            for row_item_data in _row:
                row_item = FrrOspf6DRow.from_dict(row_item_data)

                row.append(row_item)

        redistributeconnectedsubnets = d.pop("redistributeconnectedsubnets", UNSET)

        redistributeconnectedsubnets_routemap = d.pop("redistributeconnectedsubnets_routemap", UNSET)

        redistributekernel = d.pop("redistributekernel", UNSET)

        redistributekernel_routemap = d.pop("redistributekernel_routemap", UNSET)

        redistributebgp = d.pop("redistributebgp", UNSET)

        redistributebgp_routemap = d.pop("redistributebgp_routemap", UNSET)

        redistributestatic = d.pop("redistributestatic", UNSET)

        redistributestatic_routemap = d.pop("redistributestatic_routemap", UNSET)

        exportlist = d.pop("exportlist", UNSET)

        importlist = d.pop("importlist", UNSET)

        filterlist_out = d.pop("filterlist_out", UNSET)

        filterlist_in = d.pop("filterlist_in", UNSET)

        referencebandwidth = d.pop("referencebandwidth", UNSET)

        distance = d.pop("distance", UNSET)

        distance_external = d.pop("distance_external", UNSET)

        distance_interarea = d.pop("distance_interarea", UNSET)

        distance_intraarea = d.pop("distance_intraarea", UNSET)

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

        _redistributekernel_routemap_options = d.pop("redistributekernel_routemap_options", UNSET)
        redistributekernel_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributekernel_routemap_options is not UNSET:
            redistributekernel_routemap_options = []
            for redistributekernel_routemap_options_item_data in _redistributekernel_routemap_options:
                redistributekernel_routemap_options_item = TextValue.from_dict(
                    redistributekernel_routemap_options_item_data
                )

                redistributekernel_routemap_options.append(redistributekernel_routemap_options_item)

        _redistributebgp_routemap_options = d.pop("redistributebgp_routemap_options", UNSET)
        redistributebgp_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributebgp_routemap_options is not UNSET:
            redistributebgp_routemap_options = []
            for redistributebgp_routemap_options_item_data in _redistributebgp_routemap_options:
                redistributebgp_routemap_options_item = TextValue.from_dict(redistributebgp_routemap_options_item_data)

                redistributebgp_routemap_options.append(redistributebgp_routemap_options_item)

        _redistributestatic_routemap_options = d.pop("redistributestatic_routemap_options", UNSET)
        redistributestatic_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributestatic_routemap_options is not UNSET:
            redistributestatic_routemap_options = []
            for redistributestatic_routemap_options_item_data in _redistributestatic_routemap_options:
                redistributestatic_routemap_options_item = TextValue.from_dict(
                    redistributestatic_routemap_options_item_data
                )

                redistributestatic_routemap_options.append(redistributestatic_routemap_options_item)

        _exportlist_options = d.pop("exportlist_options", UNSET)
        exportlist_options: list[TextValue] | Unset = UNSET
        if _exportlist_options is not UNSET:
            exportlist_options = []
            for exportlist_options_item_data in _exportlist_options:
                exportlist_options_item = TextValue.from_dict(exportlist_options_item_data)

                exportlist_options.append(exportlist_options_item)

        _importlist_options = d.pop("importlist_options", UNSET)
        importlist_options: list[TextValue] | Unset = UNSET
        if _importlist_options is not UNSET:
            importlist_options = []
            for importlist_options_item_data in _importlist_options:
                importlist_options_item = TextValue.from_dict(importlist_options_item_data)

                importlist_options.append(importlist_options_item)

        _filterlist_out_options = d.pop("filterlist_out_options", UNSET)
        filterlist_out_options: list[TextValue] | Unset = UNSET
        if _filterlist_out_options is not UNSET:
            filterlist_out_options = []
            for filterlist_out_options_item_data in _filterlist_out_options:
                filterlist_out_options_item = TextValue.from_dict(filterlist_out_options_item_data)

                filterlist_out_options.append(filterlist_out_options_item)

        _filterlist_in_options = d.pop("filterlist_in_options", UNSET)
        filterlist_in_options: list[TextValue] | Unset = UNSET
        if _filterlist_in_options is not UNSET:
            filterlist_in_options = []
            for filterlist_in_options_item_data in _filterlist_in_options:
                filterlist_in_options_item = TextValue.from_dict(filterlist_in_options_item_data)

                filterlist_in_options.append(filterlist_in_options_item)

        frr_ospf_6d = cls(
            enable=enable,
            adjacencylog=adjacencylog,
            routerid=routerid,
            updatefib=updatefib,
            spfholdtime=spfholdtime,
            spfdelay=spfdelay,
            enablesnmpagentx=enablesnmpagentx,
            defaultarea=defaultarea,
            defaultareatype=defaultareatype,
            row=row,
            redistributeconnectedsubnets=redistributeconnectedsubnets,
            redistributeconnectedsubnets_routemap=redistributeconnectedsubnets_routemap,
            redistributekernel=redistributekernel,
            redistributekernel_routemap=redistributekernel_routemap,
            redistributebgp=redistributebgp,
            redistributebgp_routemap=redistributebgp_routemap,
            redistributestatic=redistributestatic,
            redistributestatic_routemap=redistributestatic_routemap,
            exportlist=exportlist,
            importlist=importlist,
            filterlist_out=filterlist_out,
            filterlist_in=filterlist_in,
            referencebandwidth=referencebandwidth,
            distance=distance,
            distance_external=distance_external,
            distance_interarea=distance_interarea,
            distance_intraarea=distance_intraarea,
            redistributeconnectedsubnets_routemap_options=redistributeconnectedsubnets_routemap_options,
            redistributekernel_routemap_options=redistributekernel_routemap_options,
            redistributebgp_routemap_options=redistributebgp_routemap_options,
            redistributestatic_routemap_options=redistributestatic_routemap_options,
            exportlist_options=exportlist_options,
            importlist_options=importlist_options,
            filterlist_out_options=filterlist_out_options,
            filterlist_in_options=filterlist_in_options,
        )

        frr_ospf_6d.additional_properties = d
        return frr_ospf_6d

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
