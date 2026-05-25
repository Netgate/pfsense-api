from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrGlobalRoutemap")


@_attrs_define
class FrrGlobalRoutemap:
    """
    Attributes:
        name (str | Unset): Name

            The name of this Route Map entry.
        descr (str | Unset): Description
        action (str | Unset): Action (deny, permit)

            Permit or deny access
        seq (str | Unset): Sequence
        call (str | Unset): (Logic Control) Call Route Map

            Used to stop processing and call another route-map, then return.
        exitaction (str | Unset): (Logic Control) Exit Action

            Used to control what happens after processing this route-map.
        acl_match (str | Unset): (Access Lists) Match ACL

            Match a specific access list.
        prefix_match (str | Unset): (Prefix Lists) Match Prefix List

            Match a specific Prefix List.
        nexthop_action (str | Unset): (Next Hop) Next Hop Action (none, match-peer, match-acl, match-pl, set)

            Set or Match
        nexthop_peer (str | Unset): (Next Hop) Peer

            The peer to match or set
        nexthop_acl (str | Unset): (Next Hop) ACL

            The ACL to match
        nexthop_pl (str | Unset): (Next Hop) Prefix List

            The Prefix List to match
        metric_action (str | Unset): (Metric) Metric Action (none, match, set, settype1, settype2)

            Set or Match Metric
        metric_value (str | Unset): (Metric) Metric Value

            The metric value to match or apply. When setting a metric, the value may also be +rtt, -rtt, + or - value
            offset, or a specific metric.
        weight (str | Unset): (Weight) Weight

            A specific weight to set. Leave blank for default.
        localpref_action (str | Unset): (Local Preference) Local Pref Action (none, match, set)

            Set or Match Local Preference
        localpref_value (str | Unset): (Local Preference) Local Preference

            The Local Preference value to match or apply.
        aspath_action (str | Unset): (BGP AS Paths) AS Path Action (none, match, setexclude, setprepend, setprependlast)

            Set or Match
        aspath_match (str | Unset): (BGP AS Paths) Match AS Path

            The AS Path list to match, when Match AS Path is the Action.
        aspath_value (str | Unset): (BGP AS Paths) Set AS List
        community_action (str | Unset): (BGP Communities) Community Action (none, match, matchexact, set)

            Set or Match
        community_match (str | Unset): (BGP Communities) Match Community

            The existing community list to match.
        community_set (str | Unset): (BGP Communities) Set Community

            When setting a community, this is a space-separated list of communities in AS:VAL format, or a well-known
            community:
            internet, no-export, no-advertise, or local-as.
        community_additive (bool | Unset): (BGP Communities) Additive

            Indicates that when setting a community, it will be appended to any existing communities rather than replacing
            them.
        origin_action (str | Unset): (Origin) Origin Action (none, match, set)

            Set or Match
        origin_value (str | Unset): (Origin) Origin Name (none, egp, igp, incomplete)

            Origin value to match or set
        source_proto (str | Unset): (Source Protocol) Match Source Protocol (none, bgp, ospf, ospf6, connected, kernel,
            static, system, rip, ripng, isis)

            Source Protocol to match or set
        tag_action (str | Unset): (Tags) Tag Action (none, match, set)

            Set or Match Tag Value
        tag_value (str | Unset): (Tags) Tag Value

            The tag number to set or match, an integer 1-4294967295.
        rpki_state (str | Unset): (RPKI) Validate BGP Updates (none, notfound, invalid, valid)

            Match RKPI State
        id (str | Unset): (readonly) ID assigned to this entry
    """

    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    action: str | Unset = UNSET
    seq: str | Unset = UNSET
    call: str | Unset = UNSET
    exitaction: str | Unset = UNSET
    acl_match: str | Unset = UNSET
    prefix_match: str | Unset = UNSET
    nexthop_action: str | Unset = UNSET
    nexthop_peer: str | Unset = UNSET
    nexthop_acl: str | Unset = UNSET
    nexthop_pl: str | Unset = UNSET
    metric_action: str | Unset = UNSET
    metric_value: str | Unset = UNSET
    weight: str | Unset = UNSET
    localpref_action: str | Unset = UNSET
    localpref_value: str | Unset = UNSET
    aspath_action: str | Unset = UNSET
    aspath_match: str | Unset = UNSET
    aspath_value: str | Unset = UNSET
    community_action: str | Unset = UNSET
    community_match: str | Unset = UNSET
    community_set: str | Unset = UNSET
    community_additive: bool | Unset = UNSET
    origin_action: str | Unset = UNSET
    origin_value: str | Unset = UNSET
    source_proto: str | Unset = UNSET
    tag_action: str | Unset = UNSET
    tag_value: str | Unset = UNSET
    rpki_state: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descr = self.descr

        action = self.action

        seq = self.seq

        call = self.call

        exitaction = self.exitaction

        acl_match = self.acl_match

        prefix_match = self.prefix_match

        nexthop_action = self.nexthop_action

        nexthop_peer = self.nexthop_peer

        nexthop_acl = self.nexthop_acl

        nexthop_pl = self.nexthop_pl

        metric_action = self.metric_action

        metric_value = self.metric_value

        weight = self.weight

        localpref_action = self.localpref_action

        localpref_value = self.localpref_value

        aspath_action = self.aspath_action

        aspath_match = self.aspath_match

        aspath_value = self.aspath_value

        community_action = self.community_action

        community_match = self.community_match

        community_set = self.community_set

        community_additive = self.community_additive

        origin_action = self.origin_action

        origin_value = self.origin_value

        source_proto = self.source_proto

        tag_action = self.tag_action

        tag_value = self.tag_value

        rpki_state = self.rpki_state

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if action is not UNSET:
            field_dict["action"] = action
        if seq is not UNSET:
            field_dict["seq"] = seq
        if call is not UNSET:
            field_dict["call"] = call
        if exitaction is not UNSET:
            field_dict["exitaction"] = exitaction
        if acl_match is not UNSET:
            field_dict["acl_match"] = acl_match
        if prefix_match is not UNSET:
            field_dict["prefix_match"] = prefix_match
        if nexthop_action is not UNSET:
            field_dict["nexthop_action"] = nexthop_action
        if nexthop_peer is not UNSET:
            field_dict["nexthop_peer"] = nexthop_peer
        if nexthop_acl is not UNSET:
            field_dict["nexthop_acl"] = nexthop_acl
        if nexthop_pl is not UNSET:
            field_dict["nexthop_pl"] = nexthop_pl
        if metric_action is not UNSET:
            field_dict["metric_action"] = metric_action
        if metric_value is not UNSET:
            field_dict["metric_value"] = metric_value
        if weight is not UNSET:
            field_dict["weight"] = weight
        if localpref_action is not UNSET:
            field_dict["localpref_action"] = localpref_action
        if localpref_value is not UNSET:
            field_dict["localpref_value"] = localpref_value
        if aspath_action is not UNSET:
            field_dict["aspath_action"] = aspath_action
        if aspath_match is not UNSET:
            field_dict["aspath_match"] = aspath_match
        if aspath_value is not UNSET:
            field_dict["aspath_value"] = aspath_value
        if community_action is not UNSET:
            field_dict["community_action"] = community_action
        if community_match is not UNSET:
            field_dict["community_match"] = community_match
        if community_set is not UNSET:
            field_dict["community_set"] = community_set
        if community_additive is not UNSET:
            field_dict["community_additive"] = community_additive
        if origin_action is not UNSET:
            field_dict["origin_action"] = origin_action
        if origin_value is not UNSET:
            field_dict["origin_value"] = origin_value
        if source_proto is not UNSET:
            field_dict["source_proto"] = source_proto
        if tag_action is not UNSET:
            field_dict["tag_action"] = tag_action
        if tag_value is not UNSET:
            field_dict["tag_value"] = tag_value
        if rpki_state is not UNSET:
            field_dict["rpki_state"] = rpki_state
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        action = d.pop("action", UNSET)

        seq = d.pop("seq", UNSET)

        call = d.pop("call", UNSET)

        exitaction = d.pop("exitaction", UNSET)

        acl_match = d.pop("acl_match", UNSET)

        prefix_match = d.pop("prefix_match", UNSET)

        nexthop_action = d.pop("nexthop_action", UNSET)

        nexthop_peer = d.pop("nexthop_peer", UNSET)

        nexthop_acl = d.pop("nexthop_acl", UNSET)

        nexthop_pl = d.pop("nexthop_pl", UNSET)

        metric_action = d.pop("metric_action", UNSET)

        metric_value = d.pop("metric_value", UNSET)

        weight = d.pop("weight", UNSET)

        localpref_action = d.pop("localpref_action", UNSET)

        localpref_value = d.pop("localpref_value", UNSET)

        aspath_action = d.pop("aspath_action", UNSET)

        aspath_match = d.pop("aspath_match", UNSET)

        aspath_value = d.pop("aspath_value", UNSET)

        community_action = d.pop("community_action", UNSET)

        community_match = d.pop("community_match", UNSET)

        community_set = d.pop("community_set", UNSET)

        community_additive = d.pop("community_additive", UNSET)

        origin_action = d.pop("origin_action", UNSET)

        origin_value = d.pop("origin_value", UNSET)

        source_proto = d.pop("source_proto", UNSET)

        tag_action = d.pop("tag_action", UNSET)

        tag_value = d.pop("tag_value", UNSET)

        rpki_state = d.pop("rpki_state", UNSET)

        id = d.pop("id", UNSET)

        frr_global_routemap = cls(
            name=name,
            descr=descr,
            action=action,
            seq=seq,
            call=call,
            exitaction=exitaction,
            acl_match=acl_match,
            prefix_match=prefix_match,
            nexthop_action=nexthop_action,
            nexthop_peer=nexthop_peer,
            nexthop_acl=nexthop_acl,
            nexthop_pl=nexthop_pl,
            metric_action=metric_action,
            metric_value=metric_value,
            weight=weight,
            localpref_action=localpref_action,
            localpref_value=localpref_value,
            aspath_action=aspath_action,
            aspath_match=aspath_match,
            aspath_value=aspath_value,
            community_action=community_action,
            community_match=community_match,
            community_set=community_set,
            community_additive=community_additive,
            origin_action=origin_action,
            origin_value=origin_value,
            source_proto=source_proto,
            tag_action=tag_action,
            tag_value=tag_value,
            rpki_state=rpki_state,
            id=id,
        )

        frr_global_routemap.additional_properties = d
        return frr_global_routemap

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
