from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_bgpadvanced_row import FrrBgpadvancedRow
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrBgpadvanced")


@_attrs_define
class FrrBgpadvanced:
    """
    Attributes:
        default_localpref (str | Unset): (Advanced Options) Default Local Preference

            Configure default Local Preference value (0-4294967295, higher=more preferred)
        tablemap (str | Unset): (Advanced Options) Table Map

            BGP table to RIB route download filter
        timers_coalesce (str | Unset): (Advanced Timers) Coalesce Timer

            Subgroup Coalesce Timer (1-4294967295, ms)
        timers_routemapdelay (str | Unset): (Advanced Timers) Route Map Delay

            Time to wait before processing route-map changes (0-600, seconds). 0 disables the timer (No route updates happen
            when route-maps change)
        dampening_halflife (str | Unset): (Advanced Timers) Dampening

            Time Penalty Half Life (1-45)
        dampening_reuse (str | Unset): (Advanced Timers) Reuse Route

            When to Reuse a Route (1-20000)
        dampening_suppress (str | Unset): (Advanced Timers) Suppress Route

            Start Suppressing Route (1-20000)
        dampening_suppressduration (str | Unset): (Advanced Timers) Suppress Duration

            Max Time to Suppress (1-255)
        fastexternalfailover (bool | Unset): (Advanced Routing Behavior) Disable Fast External Failover

            Do not immediately reset session if a link to a directly connected external peer goes down
        networkimportcheck (bool | Unset): (Advanced Routing Behavior) Network Import Check

            Check if the BGP network route exists in IGP
        rejcectassetasconfedset (bool | Unset): (Advanced Routing Behavior) Reject AS_SET/AS_CONFED_SET Routes

            Reject incoming and outgoing routes with AS_SET or AS_CONFED_SET type
        routereflectorallowoutboundpolicy (bool | Unset): (Route Reflecting) Route Reflector Outbound

            Allow modifications made by outbound route-map on ibgp neighbors
        routereflectorclusterid (str | Unset): (Route Reflecting) Cluster ID

            Route Reflector Cluster ID (1-4294967295 or IP address)
        routereflectorclienttoclient (bool | Unset): (Route Reflecting) Disable Client-To-Client

            Do not allow client-to-client route reflection
        row (list[FrrBgpadvancedRow] | Unset):
        meddeterministic (bool | Unset): (Multi-Exit Discriminator) Deterministic MED

            Pick the best-MED path among paths advertised from the neighboring AS
        medalwayscompare (bool | Unset): (Multi-Exit Discriminator) Always Compare MED

            Allow comparing MED from different neighbors
        maxmedadmin (bool | Unset): (Multi-Exit Discriminator) Max MED

            Administratively applied Max MED (indefinite)
        maxmedadminvalue (str | Unset): (Multi-Exit Discriminator) Definite Max MED

            Definite Admin Max MED value to be used (0-4294967294)
        maxmedstartup (str | Unset): (Multi-Exit Discriminator) Startup Max MED Time

            Time period for Max MED on startup (5-86400)
        maxmedstartupvalue (str | Unset): (Multi-Exit Discriminator) Startup Max Med Value

            Max MED value to be used during startup (0-4294967294)
        confedas (str | Unset): (Confederation) AS Confederation

            Routing domain confederation AS (1-4294967295)
        confedpeers (str | Unset): (Confederation) Confederation Peers

            Peer AS list in BGP confederation (space separated)
        distanceadmin (str | Unset): (Distance) Administrative Distance

            Define an administrative distance (1-255)
        distanceadminprefix (str | Unset): (Distance) IP Source Prefix

            IP Source Prefix for Admin Distance (x.x.x.x/yy)
        distanceadminacl (str | Unset): (Distance) Admin Distance ACL

            Access List for Admin Distance
        bgpdistanceext (str | Unset): (Distance) BGP Distance

            Distance for AS external routes (1-255)
        bgpdistanceint (str | Unset): (Distance) Internal BGP Distance

            Distance for AS internal routes (1-255)
        bgpdistancelocal (str | Unset): (Distance) Local BGP Distance

            Distance for local routes (1-255)
        bgpbestpathasconfed (bool | Unset): (Best Path Selection) Compare Path with Confederation

            Compare path lengths including confederation sets and sequences in selecting a route
        bgpbestpathasignore (bool | Unset): (Best Path Selection) Ignore AS Path

            Ignore AS path length in selecting a route
        bgpbestpathasmulti (bool | Unset): (Best Path Selection) Multipath Relax

            Allow load sharing across routes that have different AS paths (but same length)
        bgpbestpathasmultigenasset (bool | Unset): (Best Path Selection) Generate an AS_SET

            Generate an AS_SET
        bgpbestpathcomparerouterid (bool | Unset): (Best Path Selection) Compare Router ID

            Compare Router ID for identical EBGP paths
        bgpbestpathmedconfed (bool | Unset): (Best Path Selection) MED Confederation

            Compare MED among confederation paths
        bgpbestpathmedmissing (bool | Unset): (Best Path Selection) Missing MED

            Treat missing MED as the least preferred path
        disableebgpconnectedroutecheck (bool | Unset): (eBGP) eBGP Nexthop Connected

            Disable checking if nexthop is connected on eBGP sessions
        enforcefirstas (bool | Unset): (eBGP) Enforce First AS

            Enforce the first AS for eBGP routes
        disableebgprequirepolicy (bool | Unset): (eBGP) Disable eBGP Require Policy

            Disable the requirement to apply incoming and outgoing filter to eBGP sessions
        subgrouppktqueuemax (str | Unset): (Networking Behavior) Subgroup Packet Queue

            Default Subgroup Packet Queue Maximum (20-100)
        writequanta (str | Unset): (Networking Behavior) Write Quanta

            Number of packets to write to peer socket per run (1-10000)
        tablemap_options (list[TextValue] | Unset):
        distanceadminacl_options (list[TextValue] | Unset):
    """

    default_localpref: str | Unset = UNSET
    tablemap: str | Unset = UNSET
    timers_coalesce: str | Unset = UNSET
    timers_routemapdelay: str | Unset = UNSET
    dampening_halflife: str | Unset = UNSET
    dampening_reuse: str | Unset = UNSET
    dampening_suppress: str | Unset = UNSET
    dampening_suppressduration: str | Unset = UNSET
    fastexternalfailover: bool | Unset = UNSET
    networkimportcheck: bool | Unset = UNSET
    rejcectassetasconfedset: bool | Unset = UNSET
    routereflectorallowoutboundpolicy: bool | Unset = UNSET
    routereflectorclusterid: str | Unset = UNSET
    routereflectorclienttoclient: bool | Unset = UNSET
    row: list[FrrBgpadvancedRow] | Unset = UNSET
    meddeterministic: bool | Unset = UNSET
    medalwayscompare: bool | Unset = UNSET
    maxmedadmin: bool | Unset = UNSET
    maxmedadminvalue: str | Unset = UNSET
    maxmedstartup: str | Unset = UNSET
    maxmedstartupvalue: str | Unset = UNSET
    confedas: str | Unset = UNSET
    confedpeers: str | Unset = UNSET
    distanceadmin: str | Unset = UNSET
    distanceadminprefix: str | Unset = UNSET
    distanceadminacl: str | Unset = UNSET
    bgpdistanceext: str | Unset = UNSET
    bgpdistanceint: str | Unset = UNSET
    bgpdistancelocal: str | Unset = UNSET
    bgpbestpathasconfed: bool | Unset = UNSET
    bgpbestpathasignore: bool | Unset = UNSET
    bgpbestpathasmulti: bool | Unset = UNSET
    bgpbestpathasmultigenasset: bool | Unset = UNSET
    bgpbestpathcomparerouterid: bool | Unset = UNSET
    bgpbestpathmedconfed: bool | Unset = UNSET
    bgpbestpathmedmissing: bool | Unset = UNSET
    disableebgpconnectedroutecheck: bool | Unset = UNSET
    enforcefirstas: bool | Unset = UNSET
    disableebgprequirepolicy: bool | Unset = UNSET
    subgrouppktqueuemax: str | Unset = UNSET
    writequanta: str | Unset = UNSET
    tablemap_options: list[TextValue] | Unset = UNSET
    distanceadminacl_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_localpref = self.default_localpref

        tablemap = self.tablemap

        timers_coalesce = self.timers_coalesce

        timers_routemapdelay = self.timers_routemapdelay

        dampening_halflife = self.dampening_halflife

        dampening_reuse = self.dampening_reuse

        dampening_suppress = self.dampening_suppress

        dampening_suppressduration = self.dampening_suppressduration

        fastexternalfailover = self.fastexternalfailover

        networkimportcheck = self.networkimportcheck

        rejcectassetasconfedset = self.rejcectassetasconfedset

        routereflectorallowoutboundpolicy = self.routereflectorallowoutboundpolicy

        routereflectorclusterid = self.routereflectorclusterid

        routereflectorclienttoclient = self.routereflectorclienttoclient

        row: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        meddeterministic = self.meddeterministic

        medalwayscompare = self.medalwayscompare

        maxmedadmin = self.maxmedadmin

        maxmedadminvalue = self.maxmedadminvalue

        maxmedstartup = self.maxmedstartup

        maxmedstartupvalue = self.maxmedstartupvalue

        confedas = self.confedas

        confedpeers = self.confedpeers

        distanceadmin = self.distanceadmin

        distanceadminprefix = self.distanceadminprefix

        distanceadminacl = self.distanceadminacl

        bgpdistanceext = self.bgpdistanceext

        bgpdistanceint = self.bgpdistanceint

        bgpdistancelocal = self.bgpdistancelocal

        bgpbestpathasconfed = self.bgpbestpathasconfed

        bgpbestpathasignore = self.bgpbestpathasignore

        bgpbestpathasmulti = self.bgpbestpathasmulti

        bgpbestpathasmultigenasset = self.bgpbestpathasmultigenasset

        bgpbestpathcomparerouterid = self.bgpbestpathcomparerouterid

        bgpbestpathmedconfed = self.bgpbestpathmedconfed

        bgpbestpathmedmissing = self.bgpbestpathmedmissing

        disableebgpconnectedroutecheck = self.disableebgpconnectedroutecheck

        enforcefirstas = self.enforcefirstas

        disableebgprequirepolicy = self.disableebgprequirepolicy

        subgrouppktqueuemax = self.subgrouppktqueuemax

        writequanta = self.writequanta

        tablemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tablemap_options, Unset):
            tablemap_options = []
            for tablemap_options_item_data in self.tablemap_options:
                tablemap_options_item = tablemap_options_item_data.to_dict()
                tablemap_options.append(tablemap_options_item)

        distanceadminacl_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.distanceadminacl_options, Unset):
            distanceadminacl_options = []
            for distanceadminacl_options_item_data in self.distanceadminacl_options:
                distanceadminacl_options_item = distanceadminacl_options_item_data.to_dict()
                distanceadminacl_options.append(distanceadminacl_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_localpref is not UNSET:
            field_dict["default_localpref"] = default_localpref
        if tablemap is not UNSET:
            field_dict["tablemap"] = tablemap
        if timers_coalesce is not UNSET:
            field_dict["timers_coalesce"] = timers_coalesce
        if timers_routemapdelay is not UNSET:
            field_dict["timers_routemapdelay"] = timers_routemapdelay
        if dampening_halflife is not UNSET:
            field_dict["dampening_halflife"] = dampening_halflife
        if dampening_reuse is not UNSET:
            field_dict["dampening_reuse"] = dampening_reuse
        if dampening_suppress is not UNSET:
            field_dict["dampening_suppress"] = dampening_suppress
        if dampening_suppressduration is not UNSET:
            field_dict["dampening_suppressduration"] = dampening_suppressduration
        if fastexternalfailover is not UNSET:
            field_dict["fastexternalfailover"] = fastexternalfailover
        if networkimportcheck is not UNSET:
            field_dict["networkimportcheck"] = networkimportcheck
        if rejcectassetasconfedset is not UNSET:
            field_dict["rejcectassetasconfedset"] = rejcectassetasconfedset
        if routereflectorallowoutboundpolicy is not UNSET:
            field_dict["routereflectorallowoutboundpolicy"] = routereflectorallowoutboundpolicy
        if routereflectorclusterid is not UNSET:
            field_dict["routereflectorclusterid"] = routereflectorclusterid
        if routereflectorclienttoclient is not UNSET:
            field_dict["routereflectorclienttoclient"] = routereflectorclienttoclient
        if row is not UNSET:
            field_dict["row"] = row
        if meddeterministic is not UNSET:
            field_dict["meddeterministic"] = meddeterministic
        if medalwayscompare is not UNSET:
            field_dict["medalwayscompare"] = medalwayscompare
        if maxmedadmin is not UNSET:
            field_dict["maxmedadmin"] = maxmedadmin
        if maxmedadminvalue is not UNSET:
            field_dict["maxmedadminvalue"] = maxmedadminvalue
        if maxmedstartup is not UNSET:
            field_dict["maxmedstartup"] = maxmedstartup
        if maxmedstartupvalue is not UNSET:
            field_dict["maxmedstartupvalue"] = maxmedstartupvalue
        if confedas is not UNSET:
            field_dict["confedas"] = confedas
        if confedpeers is not UNSET:
            field_dict["confedpeers"] = confedpeers
        if distanceadmin is not UNSET:
            field_dict["distanceadmin"] = distanceadmin
        if distanceadminprefix is not UNSET:
            field_dict["distanceadminprefix"] = distanceadminprefix
        if distanceadminacl is not UNSET:
            field_dict["distanceadminacl"] = distanceadminacl
        if bgpdistanceext is not UNSET:
            field_dict["bgpdistanceext"] = bgpdistanceext
        if bgpdistanceint is not UNSET:
            field_dict["bgpdistanceint"] = bgpdistanceint
        if bgpdistancelocal is not UNSET:
            field_dict["bgpdistancelocal"] = bgpdistancelocal
        if bgpbestpathasconfed is not UNSET:
            field_dict["bgpbestpathasconfed"] = bgpbestpathasconfed
        if bgpbestpathasignore is not UNSET:
            field_dict["bgpbestpathasignore"] = bgpbestpathasignore
        if bgpbestpathasmulti is not UNSET:
            field_dict["bgpbestpathasmulti"] = bgpbestpathasmulti
        if bgpbestpathasmultigenasset is not UNSET:
            field_dict["bgpbestpathasmultigenasset"] = bgpbestpathasmultigenasset
        if bgpbestpathcomparerouterid is not UNSET:
            field_dict["bgpbestpathcomparerouterid"] = bgpbestpathcomparerouterid
        if bgpbestpathmedconfed is not UNSET:
            field_dict["bgpbestpathmedconfed"] = bgpbestpathmedconfed
        if bgpbestpathmedmissing is not UNSET:
            field_dict["bgpbestpathmedmissing"] = bgpbestpathmedmissing
        if disableebgpconnectedroutecheck is not UNSET:
            field_dict["disableebgpconnectedroutecheck"] = disableebgpconnectedroutecheck
        if enforcefirstas is not UNSET:
            field_dict["enforcefirstas"] = enforcefirstas
        if disableebgprequirepolicy is not UNSET:
            field_dict["disableebgprequirepolicy"] = disableebgprequirepolicy
        if subgrouppktqueuemax is not UNSET:
            field_dict["subgrouppktqueuemax"] = subgrouppktqueuemax
        if writequanta is not UNSET:
            field_dict["writequanta"] = writequanta
        if tablemap_options is not UNSET:
            field_dict["tablemap_options"] = tablemap_options
        if distanceadminacl_options is not UNSET:
            field_dict["distanceadminacl_options"] = distanceadminacl_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_bgpadvanced_row import FrrBgpadvancedRow
        from ..models.text_value import TextValue

        d = dict(src_dict)
        default_localpref = d.pop("default_localpref", UNSET)

        tablemap = d.pop("tablemap", UNSET)

        timers_coalesce = d.pop("timers_coalesce", UNSET)

        timers_routemapdelay = d.pop("timers_routemapdelay", UNSET)

        dampening_halflife = d.pop("dampening_halflife", UNSET)

        dampening_reuse = d.pop("dampening_reuse", UNSET)

        dampening_suppress = d.pop("dampening_suppress", UNSET)

        dampening_suppressduration = d.pop("dampening_suppressduration", UNSET)

        fastexternalfailover = d.pop("fastexternalfailover", UNSET)

        networkimportcheck = d.pop("networkimportcheck", UNSET)

        rejcectassetasconfedset = d.pop("rejcectassetasconfedset", UNSET)

        routereflectorallowoutboundpolicy = d.pop("routereflectorallowoutboundpolicy", UNSET)

        routereflectorclusterid = d.pop("routereflectorclusterid", UNSET)

        routereflectorclienttoclient = d.pop("routereflectorclienttoclient", UNSET)

        _row = d.pop("row", UNSET)
        row: list[FrrBgpadvancedRow] | Unset = UNSET
        if _row is not UNSET:
            row = []
            for row_item_data in _row:
                row_item = FrrBgpadvancedRow.from_dict(row_item_data)

                row.append(row_item)

        meddeterministic = d.pop("meddeterministic", UNSET)

        medalwayscompare = d.pop("medalwayscompare", UNSET)

        maxmedadmin = d.pop("maxmedadmin", UNSET)

        maxmedadminvalue = d.pop("maxmedadminvalue", UNSET)

        maxmedstartup = d.pop("maxmedstartup", UNSET)

        maxmedstartupvalue = d.pop("maxmedstartupvalue", UNSET)

        confedas = d.pop("confedas", UNSET)

        confedpeers = d.pop("confedpeers", UNSET)

        distanceadmin = d.pop("distanceadmin", UNSET)

        distanceadminprefix = d.pop("distanceadminprefix", UNSET)

        distanceadminacl = d.pop("distanceadminacl", UNSET)

        bgpdistanceext = d.pop("bgpdistanceext", UNSET)

        bgpdistanceint = d.pop("bgpdistanceint", UNSET)

        bgpdistancelocal = d.pop("bgpdistancelocal", UNSET)

        bgpbestpathasconfed = d.pop("bgpbestpathasconfed", UNSET)

        bgpbestpathasignore = d.pop("bgpbestpathasignore", UNSET)

        bgpbestpathasmulti = d.pop("bgpbestpathasmulti", UNSET)

        bgpbestpathasmultigenasset = d.pop("bgpbestpathasmultigenasset", UNSET)

        bgpbestpathcomparerouterid = d.pop("bgpbestpathcomparerouterid", UNSET)

        bgpbestpathmedconfed = d.pop("bgpbestpathmedconfed", UNSET)

        bgpbestpathmedmissing = d.pop("bgpbestpathmedmissing", UNSET)

        disableebgpconnectedroutecheck = d.pop("disableebgpconnectedroutecheck", UNSET)

        enforcefirstas = d.pop("enforcefirstas", UNSET)

        disableebgprequirepolicy = d.pop("disableebgprequirepolicy", UNSET)

        subgrouppktqueuemax = d.pop("subgrouppktqueuemax", UNSET)

        writequanta = d.pop("writequanta", UNSET)

        _tablemap_options = d.pop("tablemap_options", UNSET)
        tablemap_options: list[TextValue] | Unset = UNSET
        if _tablemap_options is not UNSET:
            tablemap_options = []
            for tablemap_options_item_data in _tablemap_options:
                tablemap_options_item = TextValue.from_dict(tablemap_options_item_data)

                tablemap_options.append(tablemap_options_item)

        _distanceadminacl_options = d.pop("distanceadminacl_options", UNSET)
        distanceadminacl_options: list[TextValue] | Unset = UNSET
        if _distanceadminacl_options is not UNSET:
            distanceadminacl_options = []
            for distanceadminacl_options_item_data in _distanceadminacl_options:
                distanceadminacl_options_item = TextValue.from_dict(distanceadminacl_options_item_data)

                distanceadminacl_options.append(distanceadminacl_options_item)

        frr_bgpadvanced = cls(
            default_localpref=default_localpref,
            tablemap=tablemap,
            timers_coalesce=timers_coalesce,
            timers_routemapdelay=timers_routemapdelay,
            dampening_halflife=dampening_halflife,
            dampening_reuse=dampening_reuse,
            dampening_suppress=dampening_suppress,
            dampening_suppressduration=dampening_suppressduration,
            fastexternalfailover=fastexternalfailover,
            networkimportcheck=networkimportcheck,
            rejcectassetasconfedset=rejcectassetasconfedset,
            routereflectorallowoutboundpolicy=routereflectorallowoutboundpolicy,
            routereflectorclusterid=routereflectorclusterid,
            routereflectorclienttoclient=routereflectorclienttoclient,
            row=row,
            meddeterministic=meddeterministic,
            medalwayscompare=medalwayscompare,
            maxmedadmin=maxmedadmin,
            maxmedadminvalue=maxmedadminvalue,
            maxmedstartup=maxmedstartup,
            maxmedstartupvalue=maxmedstartupvalue,
            confedas=confedas,
            confedpeers=confedpeers,
            distanceadmin=distanceadmin,
            distanceadminprefix=distanceadminprefix,
            distanceadminacl=distanceadminacl,
            bgpdistanceext=bgpdistanceext,
            bgpdistanceint=bgpdistanceint,
            bgpdistancelocal=bgpdistancelocal,
            bgpbestpathasconfed=bgpbestpathasconfed,
            bgpbestpathasignore=bgpbestpathasignore,
            bgpbestpathasmulti=bgpbestpathasmulti,
            bgpbestpathasmultigenasset=bgpbestpathasmultigenasset,
            bgpbestpathcomparerouterid=bgpbestpathcomparerouterid,
            bgpbestpathmedconfed=bgpbestpathmedconfed,
            bgpbestpathmedmissing=bgpbestpathmedmissing,
            disableebgpconnectedroutecheck=disableebgpconnectedroutecheck,
            enforcefirstas=enforcefirstas,
            disableebgprequirepolicy=disableebgprequirepolicy,
            subgrouppktqueuemax=subgrouppktqueuemax,
            writequanta=writequanta,
            tablemap_options=tablemap_options,
            distanceadminacl_options=distanceadminacl_options,
        )

        frr_bgpadvanced.additional_properties = d
        return frr_bgpadvanced

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
