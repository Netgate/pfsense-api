from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrBgpNeighbor")


@_attrs_define
class FrrBgpNeighbor:
    """
    Attributes:
        peer (str | Unset): Name/Address

            The name of a peer group, or IP address of a neighbor.
            Provide a text name to define a Peer Group. Enter an IP Address to define a Peer.
        descr (str | Unset): Description
        peergroup (str | Unset): Peer Group

            When defining a Neighbor by IP address, select a group to which it belongs, if any.
        password (str | Unset): Password

            Password for this BGP Neighbor
        password_type (str | Unset): Password Type (none, both, both-bidir, frr, setkey, setkey-bidir)

            Type of Password
        shutdown (bool | Unset): (Shutdown) Shutdown

            Neighbor administrative shutdown
        shutdownmessage (str | Unset): (Shutdown) Shutdown Message

            Shutdown message (optional)
        shutdownautortt (str | Unset): (Shutdown) Auto-Shutdown

            RTT in milliseconds to automatically shutdown the peer if exceeded.
        shutdownautokeepalive (str | Unset): (Shutdown) Auto-Shutdown Keepalive Count

            Number of keepalive messages to count before shutting down the peer when round-trip-time exceeds the set
            threshold.
        asnum (str | Unset): (Basic Options) Remote AS

            Autonomous System (AS) Number for this neighbor. May be an integer from 1-4294967295, "external", or "internal".
        updatesource_type (str | Unset): (Basic Options) Update Source (ipv4, ipv6)

            IP type for BGP Updates
        updatesource (str | Unset): (Basic Options) Update Source

            Local source of BGP Updates
        bothaf (bool | Unset): (Basic Options) Address Family

            Allow neighbor to advertise and receive routes for both IPv4 and IPv6
        defaultoriginate (str | Unset): (Basic Options) Default Originate (no, ipv4, ipv6, yes)

            Originate default route to this neighbor.
        defaultoriginateroutemap (str | Unset): (Basic Options) Default Originate Route Map

            Choose a Route Map to restrict origination.
        sendcommunity (str | Unset): (Basic Options) Send Community (disabled, enabled, standard, extended, both)

            Send Community attribute to this neighbor
        nexthopself (str | Unset): (Basic Options) Next Hop Self (disabled, enabled, force)

            Disable the next hop calculation for this neighbor
        softreconfigurationinbound (bool | Unset): (Basic Options) Inbound Soft Reconfiguration

            Per-neighbor Inbound Soft Reconfiguration
        timers_keepalive (str | Unset): (Basic Options) Timers

            Keep Alive Interval (0-65535)
        timers_holdtime (str | Unset): (Basic Options) Hold Time

            Hold Time (1-65535)
        timers_connect (str | Unset): (Basic Options) Connect Timer

            Connect Timer (1-65535)
        distribute_in (str | Unset): (Peer Filtering) Distribute List Filter

            Inbound Distribution ACL Filter
        distribute_out (str | Unset): (Peer Filtering) Distribute List Filter

            Outbound Distribution ACL Filter
        prefixfilter_in (str | Unset): (Peer Filtering) Prefix List Filter

            Inbound Prefix List Filter
        prefixfilter_out (str | Unset): (Peer Filtering) Prefix List Filter

            Outbound Prefix List Filter
        aspathfilter_in (str | Unset): (Peer Filtering) AS Path Filter

            Inbound AS Path Filter
        aspathfilter_out (str | Unset): (Peer Filtering) AS Path Filter

            Outbound AS Path Filter
        routemap_in (str | Unset): (Peer Filtering) Route Map Filters

            Inbound Route Map Filter
        routemap_out (str | Unset): (Peer Filtering) Route Map Filters

            Outbound Route Map Filter
        unsuppressmap (str | Unset): (Peer Filtering) Unsuppress Route Map

            Route Map to selectively unsuppress suppressed routes
        bfdenable (bool | Unset): (BFD) BFD

            BFD Enable
        bfd_check_control_plane_failure (bool | Unset): (BFD) BFD Check Control Plane Failure

            BFD Check Control Plane Failure
        bfd_peer (str | Unset): (BFD) BFD Peer

            Select a BFD peer to subscribe, default is to use the neighbor address
        grmode (str | Unset): (Graceful Restart) Graceful Restart Mode (default, restart, helper, disable)

            Neighbor graceful restart mode
        weight (str | Unset): (Advanced Options) Weight

            Default weight for routes from this neighbor, 0-65535
        passive (bool | Unset): (Advanced Options) Passive

            Do not send open messages to this neighbor
        addpathtxallpaths (bool | Unset): (Advanced Options) Path Advertise

            All Paths to Neighbor
        addpathtxbestpathperas (bool | Unset): (Advanced Options) Path Transmit

            Best Path per each neighboring AS
        advertisementinterval (str | Unset): (Advanced Options) Advertisement Interval

            Minimum interval, in seconds, between sending BGP routing updates. (0-600)
        allowasin (str | Unset): (Advanced Options) Allow AS Inbound (disabled, enabled, origin, 1, 2, 3, 4, 5, 6, 7, 8,
            9, 10)

            Accept as-path with this local router's own AS present in it.
        asoverride (bool | Unset): (Advanced Options) AS Override

            Override ASNs in outbound updates if the AS Path is the same as the Remote AS
        attributeunchanged (bool | Unset): (Advanced Options) Attribute Unchanged

            Propagate BGP Attribute Unchanged
        attributeunchanged_aspath (bool | Unset): (Advanced Options) AS Path

            AS Path Attribute
        attributeunchanged_med (bool | Unset): (Advanced Options) Med

            Med Attribute
        attributeunchanged_nexthop (bool | Unset): (Advanced Options) Next Hop

            Next Hop Attribute
        capability (bool | Unset): (Advanced Options) Advertise Capability

            Advertise Dynamic capability
        capability_nexthop (bool | Unset): (Advanced Options) Advertise Capability Nexthop

            Advertise Extended Next-Hop capability. This is automatically enabled when peering with IPv6 link-local
            addresses.
        capability_orf (str | Unset): (Advanced Options) Advertise Capability (disabled, send, receive, both)

            Advertise Outbound Route Filter capability
        dontcapabilitynegotiate (bool | Unset): (Advanced Options) Disable Capability Negotiation

            Do not perform capability negotiation with the neighbor
        overridecapability (bool | Unset): (Advanced Options) Override Capability Negotiation

            Override capability negotiation result
        ttlsecurityhops (str | Unset): (Advanced Options) TTL Security Hops

            The maximum hop count to allow for BGP neighbors (1-254)

            Leave blank to disable
        disableconnectedcheck (bool | Unset): (Advanced Options) Disable Connected Check

            One-hop away EBGP peer using loopback address
        ebgpmultihop (str | Unset): (Advanced Options) EBGP Multi-Hop

            The maximum hop count to allow for EBGP neighbors not on directly connected networks (1-255)

            Leave blank to disable
        enforcemultihop (bool | Unset): (Advanced Options) Enforce EBGP Multi-Hop

            Enforce EBGP neighbors perform multihop
        localas_num (str | Unset): (Advanced Options) Local AS

            Local AS Number
        localas_noprepend (bool | Unset): (Advanced Options) No Prepend

            Do not prepend Local AS to updates from EBGP peers
        localas_replaceas (bool | Unset): (Advanced Options) Replace AS

            Do not prepend Local AS to updates from IBGP peers
        maximumprefix_num (str | Unset): (Advanced Options) Maximum Prefix

            Maximum Prefix to Accept (1-4294967295)
        maximumprefix_threshold (str | Unset): (Advanced Options) Warning Threshold

            % at which to warn (1-100)
        maximumprefix_warnonly (bool | Unset): (Advanced Options) Warn Only

            Warn Only (No Restart)
        maximumprefix_restart (str | Unset): (Advanced Options) Restart Interval

            Restart BGP after X warned minutes (1-65535)
        maximumprefixout_num (str | Unset): (Advanced Options) Maximum Prefix Out

            Maximum Prefix to Send (1-4294967295)
        removeprivateas (bool | Unset): (Advanced Options) Remove Private AS

            Remove private ASNs in outbound updates
        removeprivateas_all (bool | Unset): (Advanced Options) Apply to All

            Apply to all AS Numbers
        removeprivateas_replace (bool | Unset): (Advanced Options) Replace AS

            Replace Private with Local AS
        routeclient_reflector (bool | Unset): (Advanced Options) Route Client

            Neighbor is Route Reflector Client
        routeclient_server (bool | Unset): (Advanced Options) Route Client

            Neighbor is Route Server Client
        solo (bool | Unset): (Advanced Options) Solo Peer

            Neighbor is part of its own update group
        id (str | Unset): (readonly) ID assigned to this entry
    """

    peer: str | Unset = UNSET
    descr: str | Unset = UNSET
    peergroup: str | Unset = UNSET
    password: str | Unset = UNSET
    password_type: str | Unset = UNSET
    shutdown: bool | Unset = UNSET
    shutdownmessage: str | Unset = UNSET
    shutdownautortt: str | Unset = UNSET
    shutdownautokeepalive: str | Unset = UNSET
    asnum: str | Unset = UNSET
    updatesource_type: str | Unset = UNSET
    updatesource: str | Unset = UNSET
    bothaf: bool | Unset = UNSET
    defaultoriginate: str | Unset = UNSET
    defaultoriginateroutemap: str | Unset = UNSET
    sendcommunity: str | Unset = UNSET
    nexthopself: str | Unset = UNSET
    softreconfigurationinbound: bool | Unset = UNSET
    timers_keepalive: str | Unset = UNSET
    timers_holdtime: str | Unset = UNSET
    timers_connect: str | Unset = UNSET
    distribute_in: str | Unset = UNSET
    distribute_out: str | Unset = UNSET
    prefixfilter_in: str | Unset = UNSET
    prefixfilter_out: str | Unset = UNSET
    aspathfilter_in: str | Unset = UNSET
    aspathfilter_out: str | Unset = UNSET
    routemap_in: str | Unset = UNSET
    routemap_out: str | Unset = UNSET
    unsuppressmap: str | Unset = UNSET
    bfdenable: bool | Unset = UNSET
    bfd_check_control_plane_failure: bool | Unset = UNSET
    bfd_peer: str | Unset = UNSET
    grmode: str | Unset = UNSET
    weight: str | Unset = UNSET
    passive: bool | Unset = UNSET
    addpathtxallpaths: bool | Unset = UNSET
    addpathtxbestpathperas: bool | Unset = UNSET
    advertisementinterval: str | Unset = UNSET
    allowasin: str | Unset = UNSET
    asoverride: bool | Unset = UNSET
    attributeunchanged: bool | Unset = UNSET
    attributeunchanged_aspath: bool | Unset = UNSET
    attributeunchanged_med: bool | Unset = UNSET
    attributeunchanged_nexthop: bool | Unset = UNSET
    capability: bool | Unset = UNSET
    capability_nexthop: bool | Unset = UNSET
    capability_orf: str | Unset = UNSET
    dontcapabilitynegotiate: bool | Unset = UNSET
    overridecapability: bool | Unset = UNSET
    ttlsecurityhops: str | Unset = UNSET
    disableconnectedcheck: bool | Unset = UNSET
    ebgpmultihop: str | Unset = UNSET
    enforcemultihop: bool | Unset = UNSET
    localas_num: str | Unset = UNSET
    localas_noprepend: bool | Unset = UNSET
    localas_replaceas: bool | Unset = UNSET
    maximumprefix_num: str | Unset = UNSET
    maximumprefix_threshold: str | Unset = UNSET
    maximumprefix_warnonly: bool | Unset = UNSET
    maximumprefix_restart: str | Unset = UNSET
    maximumprefixout_num: str | Unset = UNSET
    removeprivateas: bool | Unset = UNSET
    removeprivateas_all: bool | Unset = UNSET
    removeprivateas_replace: bool | Unset = UNSET
    routeclient_reflector: bool | Unset = UNSET
    routeclient_server: bool | Unset = UNSET
    solo: bool | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        peer = self.peer

        descr = self.descr

        peergroup = self.peergroup

        password = self.password

        password_type = self.password_type

        shutdown = self.shutdown

        shutdownmessage = self.shutdownmessage

        shutdownautortt = self.shutdownautortt

        shutdownautokeepalive = self.shutdownautokeepalive

        asnum = self.asnum

        updatesource_type = self.updatesource_type

        updatesource = self.updatesource

        bothaf = self.bothaf

        defaultoriginate = self.defaultoriginate

        defaultoriginateroutemap = self.defaultoriginateroutemap

        sendcommunity = self.sendcommunity

        nexthopself = self.nexthopself

        softreconfigurationinbound = self.softreconfigurationinbound

        timers_keepalive = self.timers_keepalive

        timers_holdtime = self.timers_holdtime

        timers_connect = self.timers_connect

        distribute_in = self.distribute_in

        distribute_out = self.distribute_out

        prefixfilter_in = self.prefixfilter_in

        prefixfilter_out = self.prefixfilter_out

        aspathfilter_in = self.aspathfilter_in

        aspathfilter_out = self.aspathfilter_out

        routemap_in = self.routemap_in

        routemap_out = self.routemap_out

        unsuppressmap = self.unsuppressmap

        bfdenable = self.bfdenable

        bfd_check_control_plane_failure = self.bfd_check_control_plane_failure

        bfd_peer = self.bfd_peer

        grmode = self.grmode

        weight = self.weight

        passive = self.passive

        addpathtxallpaths = self.addpathtxallpaths

        addpathtxbestpathperas = self.addpathtxbestpathperas

        advertisementinterval = self.advertisementinterval

        allowasin = self.allowasin

        asoverride = self.asoverride

        attributeunchanged = self.attributeunchanged

        attributeunchanged_aspath = self.attributeunchanged_aspath

        attributeunchanged_med = self.attributeunchanged_med

        attributeunchanged_nexthop = self.attributeunchanged_nexthop

        capability = self.capability

        capability_nexthop = self.capability_nexthop

        capability_orf = self.capability_orf

        dontcapabilitynegotiate = self.dontcapabilitynegotiate

        overridecapability = self.overridecapability

        ttlsecurityhops = self.ttlsecurityhops

        disableconnectedcheck = self.disableconnectedcheck

        ebgpmultihop = self.ebgpmultihop

        enforcemultihop = self.enforcemultihop

        localas_num = self.localas_num

        localas_noprepend = self.localas_noprepend

        localas_replaceas = self.localas_replaceas

        maximumprefix_num = self.maximumprefix_num

        maximumprefix_threshold = self.maximumprefix_threshold

        maximumprefix_warnonly = self.maximumprefix_warnonly

        maximumprefix_restart = self.maximumprefix_restart

        maximumprefixout_num = self.maximumprefixout_num

        removeprivateas = self.removeprivateas

        removeprivateas_all = self.removeprivateas_all

        removeprivateas_replace = self.removeprivateas_replace

        routeclient_reflector = self.routeclient_reflector

        routeclient_server = self.routeclient_server

        solo = self.solo

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if peer is not UNSET:
            field_dict["peer"] = peer
        if descr is not UNSET:
            field_dict["descr"] = descr
        if peergroup is not UNSET:
            field_dict["peergroup"] = peergroup
        if password is not UNSET:
            field_dict["password"] = password
        if password_type is not UNSET:
            field_dict["password_type"] = password_type
        if shutdown is not UNSET:
            field_dict["shutdown"] = shutdown
        if shutdownmessage is not UNSET:
            field_dict["shutdownmessage"] = shutdownmessage
        if shutdownautortt is not UNSET:
            field_dict["shutdownautortt"] = shutdownautortt
        if shutdownautokeepalive is not UNSET:
            field_dict["shutdownautokeepalive"] = shutdownautokeepalive
        if asnum is not UNSET:
            field_dict["asnum"] = asnum
        if updatesource_type is not UNSET:
            field_dict["updatesource_type"] = updatesource_type
        if updatesource is not UNSET:
            field_dict["updatesource"] = updatesource
        if bothaf is not UNSET:
            field_dict["bothaf"] = bothaf
        if defaultoriginate is not UNSET:
            field_dict["defaultoriginate"] = defaultoriginate
        if defaultoriginateroutemap is not UNSET:
            field_dict["defaultoriginateroutemap"] = defaultoriginateroutemap
        if sendcommunity is not UNSET:
            field_dict["sendcommunity"] = sendcommunity
        if nexthopself is not UNSET:
            field_dict["nexthopself"] = nexthopself
        if softreconfigurationinbound is not UNSET:
            field_dict["softreconfigurationinbound"] = softreconfigurationinbound
        if timers_keepalive is not UNSET:
            field_dict["timers_keepalive"] = timers_keepalive
        if timers_holdtime is not UNSET:
            field_dict["timers_holdtime"] = timers_holdtime
        if timers_connect is not UNSET:
            field_dict["timers_connect"] = timers_connect
        if distribute_in is not UNSET:
            field_dict["distribute_in"] = distribute_in
        if distribute_out is not UNSET:
            field_dict["distribute_out"] = distribute_out
        if prefixfilter_in is not UNSET:
            field_dict["prefixfilter_in"] = prefixfilter_in
        if prefixfilter_out is not UNSET:
            field_dict["prefixfilter_out"] = prefixfilter_out
        if aspathfilter_in is not UNSET:
            field_dict["aspathfilter_in"] = aspathfilter_in
        if aspathfilter_out is not UNSET:
            field_dict["aspathfilter_out"] = aspathfilter_out
        if routemap_in is not UNSET:
            field_dict["routemap_in"] = routemap_in
        if routemap_out is not UNSET:
            field_dict["routemap_out"] = routemap_out
        if unsuppressmap is not UNSET:
            field_dict["unsuppressmap"] = unsuppressmap
        if bfdenable is not UNSET:
            field_dict["bfdenable"] = bfdenable
        if bfd_check_control_plane_failure is not UNSET:
            field_dict["bfd_check_control_plane_failure"] = bfd_check_control_plane_failure
        if bfd_peer is not UNSET:
            field_dict["bfd_peer"] = bfd_peer
        if grmode is not UNSET:
            field_dict["grmode"] = grmode
        if weight is not UNSET:
            field_dict["weight"] = weight
        if passive is not UNSET:
            field_dict["passive"] = passive
        if addpathtxallpaths is not UNSET:
            field_dict["addpathtxallpaths"] = addpathtxallpaths
        if addpathtxbestpathperas is not UNSET:
            field_dict["addpathtxbestpathperas"] = addpathtxbestpathperas
        if advertisementinterval is not UNSET:
            field_dict["advertisementinterval"] = advertisementinterval
        if allowasin is not UNSET:
            field_dict["allowasin"] = allowasin
        if asoverride is not UNSET:
            field_dict["asoverride"] = asoverride
        if attributeunchanged is not UNSET:
            field_dict["attributeunchanged"] = attributeunchanged
        if attributeunchanged_aspath is not UNSET:
            field_dict["attributeunchanged_aspath"] = attributeunchanged_aspath
        if attributeunchanged_med is not UNSET:
            field_dict["attributeunchanged_med"] = attributeunchanged_med
        if attributeunchanged_nexthop is not UNSET:
            field_dict["attributeunchanged_nexthop"] = attributeunchanged_nexthop
        if capability is not UNSET:
            field_dict["capability"] = capability
        if capability_nexthop is not UNSET:
            field_dict["capability_nexthop"] = capability_nexthop
        if capability_orf is not UNSET:
            field_dict["capability_orf"] = capability_orf
        if dontcapabilitynegotiate is not UNSET:
            field_dict["dontcapabilitynegotiate"] = dontcapabilitynegotiate
        if overridecapability is not UNSET:
            field_dict["overridecapability"] = overridecapability
        if ttlsecurityhops is not UNSET:
            field_dict["ttlsecurityhops"] = ttlsecurityhops
        if disableconnectedcheck is not UNSET:
            field_dict["disableconnectedcheck"] = disableconnectedcheck
        if ebgpmultihop is not UNSET:
            field_dict["ebgpmultihop"] = ebgpmultihop
        if enforcemultihop is not UNSET:
            field_dict["enforcemultihop"] = enforcemultihop
        if localas_num is not UNSET:
            field_dict["localas_num"] = localas_num
        if localas_noprepend is not UNSET:
            field_dict["localas_noprepend"] = localas_noprepend
        if localas_replaceas is not UNSET:
            field_dict["localas_replaceas"] = localas_replaceas
        if maximumprefix_num is not UNSET:
            field_dict["maximumprefix_num"] = maximumprefix_num
        if maximumprefix_threshold is not UNSET:
            field_dict["maximumprefix_threshold"] = maximumprefix_threshold
        if maximumprefix_warnonly is not UNSET:
            field_dict["maximumprefix_warnonly"] = maximumprefix_warnonly
        if maximumprefix_restart is not UNSET:
            field_dict["maximumprefix_restart"] = maximumprefix_restart
        if maximumprefixout_num is not UNSET:
            field_dict["maximumprefixout_num"] = maximumprefixout_num
        if removeprivateas is not UNSET:
            field_dict["removeprivateas"] = removeprivateas
        if removeprivateas_all is not UNSET:
            field_dict["removeprivateas_all"] = removeprivateas_all
        if removeprivateas_replace is not UNSET:
            field_dict["removeprivateas_replace"] = removeprivateas_replace
        if routeclient_reflector is not UNSET:
            field_dict["routeclient_reflector"] = routeclient_reflector
        if routeclient_server is not UNSET:
            field_dict["routeclient_server"] = routeclient_server
        if solo is not UNSET:
            field_dict["solo"] = solo
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        peer = d.pop("peer", UNSET)

        descr = d.pop("descr", UNSET)

        peergroup = d.pop("peergroup", UNSET)

        password = d.pop("password", UNSET)

        password_type = d.pop("password_type", UNSET)

        shutdown = d.pop("shutdown", UNSET)

        shutdownmessage = d.pop("shutdownmessage", UNSET)

        shutdownautortt = d.pop("shutdownautortt", UNSET)

        shutdownautokeepalive = d.pop("shutdownautokeepalive", UNSET)

        asnum = d.pop("asnum", UNSET)

        updatesource_type = d.pop("updatesource_type", UNSET)

        updatesource = d.pop("updatesource", UNSET)

        bothaf = d.pop("bothaf", UNSET)

        defaultoriginate = d.pop("defaultoriginate", UNSET)

        defaultoriginateroutemap = d.pop("defaultoriginateroutemap", UNSET)

        sendcommunity = d.pop("sendcommunity", UNSET)

        nexthopself = d.pop("nexthopself", UNSET)

        softreconfigurationinbound = d.pop("softreconfigurationinbound", UNSET)

        timers_keepalive = d.pop("timers_keepalive", UNSET)

        timers_holdtime = d.pop("timers_holdtime", UNSET)

        timers_connect = d.pop("timers_connect", UNSET)

        distribute_in = d.pop("distribute_in", UNSET)

        distribute_out = d.pop("distribute_out", UNSET)

        prefixfilter_in = d.pop("prefixfilter_in", UNSET)

        prefixfilter_out = d.pop("prefixfilter_out", UNSET)

        aspathfilter_in = d.pop("aspathfilter_in", UNSET)

        aspathfilter_out = d.pop("aspathfilter_out", UNSET)

        routemap_in = d.pop("routemap_in", UNSET)

        routemap_out = d.pop("routemap_out", UNSET)

        unsuppressmap = d.pop("unsuppressmap", UNSET)

        bfdenable = d.pop("bfdenable", UNSET)

        bfd_check_control_plane_failure = d.pop("bfd_check_control_plane_failure", UNSET)

        bfd_peer = d.pop("bfd_peer", UNSET)

        grmode = d.pop("grmode", UNSET)

        weight = d.pop("weight", UNSET)

        passive = d.pop("passive", UNSET)

        addpathtxallpaths = d.pop("addpathtxallpaths", UNSET)

        addpathtxbestpathperas = d.pop("addpathtxbestpathperas", UNSET)

        advertisementinterval = d.pop("advertisementinterval", UNSET)

        allowasin = d.pop("allowasin", UNSET)

        asoverride = d.pop("asoverride", UNSET)

        attributeunchanged = d.pop("attributeunchanged", UNSET)

        attributeunchanged_aspath = d.pop("attributeunchanged_aspath", UNSET)

        attributeunchanged_med = d.pop("attributeunchanged_med", UNSET)

        attributeunchanged_nexthop = d.pop("attributeunchanged_nexthop", UNSET)

        capability = d.pop("capability", UNSET)

        capability_nexthop = d.pop("capability_nexthop", UNSET)

        capability_orf = d.pop("capability_orf", UNSET)

        dontcapabilitynegotiate = d.pop("dontcapabilitynegotiate", UNSET)

        overridecapability = d.pop("overridecapability", UNSET)

        ttlsecurityhops = d.pop("ttlsecurityhops", UNSET)

        disableconnectedcheck = d.pop("disableconnectedcheck", UNSET)

        ebgpmultihop = d.pop("ebgpmultihop", UNSET)

        enforcemultihop = d.pop("enforcemultihop", UNSET)

        localas_num = d.pop("localas_num", UNSET)

        localas_noprepend = d.pop("localas_noprepend", UNSET)

        localas_replaceas = d.pop("localas_replaceas", UNSET)

        maximumprefix_num = d.pop("maximumprefix_num", UNSET)

        maximumprefix_threshold = d.pop("maximumprefix_threshold", UNSET)

        maximumprefix_warnonly = d.pop("maximumprefix_warnonly", UNSET)

        maximumprefix_restart = d.pop("maximumprefix_restart", UNSET)

        maximumprefixout_num = d.pop("maximumprefixout_num", UNSET)

        removeprivateas = d.pop("removeprivateas", UNSET)

        removeprivateas_all = d.pop("removeprivateas_all", UNSET)

        removeprivateas_replace = d.pop("removeprivateas_replace", UNSET)

        routeclient_reflector = d.pop("routeclient_reflector", UNSET)

        routeclient_server = d.pop("routeclient_server", UNSET)

        solo = d.pop("solo", UNSET)

        id = d.pop("id", UNSET)

        frr_bgp_neighbor = cls(
            peer=peer,
            descr=descr,
            peergroup=peergroup,
            password=password,
            password_type=password_type,
            shutdown=shutdown,
            shutdownmessage=shutdownmessage,
            shutdownautortt=shutdownautortt,
            shutdownautokeepalive=shutdownautokeepalive,
            asnum=asnum,
            updatesource_type=updatesource_type,
            updatesource=updatesource,
            bothaf=bothaf,
            defaultoriginate=defaultoriginate,
            defaultoriginateroutemap=defaultoriginateroutemap,
            sendcommunity=sendcommunity,
            nexthopself=nexthopself,
            softreconfigurationinbound=softreconfigurationinbound,
            timers_keepalive=timers_keepalive,
            timers_holdtime=timers_holdtime,
            timers_connect=timers_connect,
            distribute_in=distribute_in,
            distribute_out=distribute_out,
            prefixfilter_in=prefixfilter_in,
            prefixfilter_out=prefixfilter_out,
            aspathfilter_in=aspathfilter_in,
            aspathfilter_out=aspathfilter_out,
            routemap_in=routemap_in,
            routemap_out=routemap_out,
            unsuppressmap=unsuppressmap,
            bfdenable=bfdenable,
            bfd_check_control_plane_failure=bfd_check_control_plane_failure,
            bfd_peer=bfd_peer,
            grmode=grmode,
            weight=weight,
            passive=passive,
            addpathtxallpaths=addpathtxallpaths,
            addpathtxbestpathperas=addpathtxbestpathperas,
            advertisementinterval=advertisementinterval,
            allowasin=allowasin,
            asoverride=asoverride,
            attributeunchanged=attributeunchanged,
            attributeunchanged_aspath=attributeunchanged_aspath,
            attributeunchanged_med=attributeunchanged_med,
            attributeunchanged_nexthop=attributeunchanged_nexthop,
            capability=capability,
            capability_nexthop=capability_nexthop,
            capability_orf=capability_orf,
            dontcapabilitynegotiate=dontcapabilitynegotiate,
            overridecapability=overridecapability,
            ttlsecurityhops=ttlsecurityhops,
            disableconnectedcheck=disableconnectedcheck,
            ebgpmultihop=ebgpmultihop,
            enforcemultihop=enforcemultihop,
            localas_num=localas_num,
            localas_noprepend=localas_noprepend,
            localas_replaceas=localas_replaceas,
            maximumprefix_num=maximumprefix_num,
            maximumprefix_threshold=maximumprefix_threshold,
            maximumprefix_warnonly=maximumprefix_warnonly,
            maximumprefix_restart=maximumprefix_restart,
            maximumprefixout_num=maximumprefixout_num,
            removeprivateas=removeprivateas,
            removeprivateas_all=removeprivateas_all,
            removeprivateas_replace=removeprivateas_replace,
            routeclient_reflector=routeclient_reflector,
            routeclient_server=routeclient_server,
            solo=solo,
            id=id,
        )

        frr_bgp_neighbor.additional_properties = d
        return frr_bgp_neighbor

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
