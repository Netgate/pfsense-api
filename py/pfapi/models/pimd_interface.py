from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PimdInterface")


@_attrs_define
class PimdInterface:
    """
    Attributes:
        intf_ident (str | Unset): (Interface Options) Interface

            Select the interface or address to bind.
            Multiple entries may be added for the same interface to specify multiple values
            for items such as Alternative Networks and Multicast Scope.
            Note: A firewall rule with enabled advanced option 'Allow IP options' must exist to allow multicast traffic.
        descr (str | Unset): (Interface Options) Description
        binding (str | Unset): (Interface Options) Interface Binding (default, enable, disable)

            Binding behavior for this interface. Combines with Default Bind setting on the
            General tab to determine whether or not this interface will be used by PIMD.
        igmpversion (str | Unset): (Interface Options) IGMP Version (default, 3, 2)

            The IGMP version to use on this interface.
        dr_priority (str | Unset): (Interface Options) DR Priority

            Priority to use for Designated Router (DR) election.
            Highest advertised priority wins the election.
            Ties are given to the router with the highest IP address in the subnet.
            (1-4294967294, Default: 1)
        ttl_threshold (str | Unset): (Interface Options) TTL Threshold

            The TTL threshold for multicast frames to be forwarded from this interface.
            (1-255, Default: 1)
        distance (str | Unset): (Interface Options) Route Distance

            Default administrative distance for routes on this interface.
            Overrides the global Default Route Distance value.
            (1-255, Default: Default Route Distance on General tab)
        metric (str | Unset): (Interface Options) Route Metric

            Default metric for routes on this interface.
            Overrides the global Default Route Metric value.
            (1-1024, Default: Default Route Metric on General tab)
        altnet (str | Unset): (Interface Options) Alternative Network

            Alternative host or network to accept as a locally attached multicast source.
        scoped (str | Unset): (Interface Options) Multicast Scope

            Multicast streams belonging to this scoped group will not be forwarded.
            Allows interfaces to be configured as an administrative boundary for the specified group.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    intf_ident: str | Unset = UNSET
    descr: str | Unset = UNSET
    binding: str | Unset = UNSET
    igmpversion: str | Unset = UNSET
    dr_priority: str | Unset = UNSET
    ttl_threshold: str | Unset = UNSET
    distance: str | Unset = UNSET
    metric: str | Unset = UNSET
    altnet: str | Unset = UNSET
    scoped: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        intf_ident = self.intf_ident

        descr = self.descr

        binding = self.binding

        igmpversion = self.igmpversion

        dr_priority = self.dr_priority

        ttl_threshold = self.ttl_threshold

        distance = self.distance

        metric = self.metric

        altnet = self.altnet

        scoped = self.scoped

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if intf_ident is not UNSET:
            field_dict["intf_ident"] = intf_ident
        if descr is not UNSET:
            field_dict["descr"] = descr
        if binding is not UNSET:
            field_dict["binding"] = binding
        if igmpversion is not UNSET:
            field_dict["igmpversion"] = igmpversion
        if dr_priority is not UNSET:
            field_dict["dr_priority"] = dr_priority
        if ttl_threshold is not UNSET:
            field_dict["ttl_threshold"] = ttl_threshold
        if distance is not UNSET:
            field_dict["distance"] = distance
        if metric is not UNSET:
            field_dict["metric"] = metric
        if altnet is not UNSET:
            field_dict["altnet"] = altnet
        if scoped is not UNSET:
            field_dict["scoped"] = scoped
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        intf_ident = d.pop("intf_ident", UNSET)

        descr = d.pop("descr", UNSET)

        binding = d.pop("binding", UNSET)

        igmpversion = d.pop("igmpversion", UNSET)

        dr_priority = d.pop("dr_priority", UNSET)

        ttl_threshold = d.pop("ttl_threshold", UNSET)

        distance = d.pop("distance", UNSET)

        metric = d.pop("metric", UNSET)

        altnet = d.pop("altnet", UNSET)

        scoped = d.pop("scoped", UNSET)

        id = d.pop("id", UNSET)

        pimd_interface = cls(
            intf_ident=intf_ident,
            descr=descr,
            binding=binding,
            igmpversion=igmpversion,
            dr_priority=dr_priority,
            ttl_threshold=ttl_threshold,
            distance=distance,
            metric=metric,
            altnet=altnet,
            scoped=scoped,
            id=id,
        )

        pimd_interface.additional_properties = d
        return pimd_interface

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
