from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bridge_interface_paths import BridgeInterfacePaths
    from ..models.bridge_interface_priorities import BridgeInterfacePriorities


T = TypeVar("T", bound="BridgeInterface")


@_attrs_define
class BridgeInterface:
    """
    Attributes:
        members (Union[Unset, str]):
        enablestp (Union[Unset, bool]):
        descr (Union[Unset, str]):
        maxaddr (Union[Unset, str]):
        timeout (Union[Unset, str]):
        maxage (Union[Unset, str]):
        fwdelay (Union[Unset, str]):
        hellotime (Union[Unset, str]):
        priority (Union[Unset, str]):
        proto (Union[Unset, str]):
        holdcnt (Union[Unset, str]):
        ip6linklocal (Union[Unset, bool]):
        ifpriority (Union[Unset, str]):
        ifpathcost (Union[Unset, str]):
        paths (Union[Unset, BridgeInterfacePaths]):
        priorities (Union[Unset, BridgeInterfacePriorities]):
        static (Union[Unset, str]):
        private (Union[Unset, str]):
        stp (Union[Unset, str]):
        span (Union[Unset, str]):
        edge (Union[Unset, str]):
        autoedge (Union[Unset, str]):
        ptp (Union[Unset, str]):
        autoptp (Union[Unset, str]):
        bridgeif (Union[Unset, str]):
    """

    members: Union[Unset, str] = UNSET
    enablestp: Union[Unset, bool] = UNSET
    descr: Union[Unset, str] = UNSET
    maxaddr: Union[Unset, str] = UNSET
    timeout: Union[Unset, str] = UNSET
    maxage: Union[Unset, str] = UNSET
    fwdelay: Union[Unset, str] = UNSET
    hellotime: Union[Unset, str] = UNSET
    priority: Union[Unset, str] = UNSET
    proto: Union[Unset, str] = UNSET
    holdcnt: Union[Unset, str] = UNSET
    ip6linklocal: Union[Unset, bool] = UNSET
    ifpriority: Union[Unset, str] = UNSET
    ifpathcost: Union[Unset, str] = UNSET
    paths: Union[Unset, "BridgeInterfacePaths"] = UNSET
    priorities: Union[Unset, "BridgeInterfacePriorities"] = UNSET
    static: Union[Unset, str] = UNSET
    private: Union[Unset, str] = UNSET
    stp: Union[Unset, str] = UNSET
    span: Union[Unset, str] = UNSET
    edge: Union[Unset, str] = UNSET
    autoedge: Union[Unset, str] = UNSET
    ptp: Union[Unset, str] = UNSET
    autoptp: Union[Unset, str] = UNSET
    bridgeif: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        members = self.members

        enablestp = self.enablestp

        descr = self.descr

        maxaddr = self.maxaddr

        timeout = self.timeout

        maxage = self.maxage

        fwdelay = self.fwdelay

        hellotime = self.hellotime

        priority = self.priority

        proto = self.proto

        holdcnt = self.holdcnt

        ip6linklocal = self.ip6linklocal

        ifpriority = self.ifpriority

        ifpathcost = self.ifpathcost

        paths: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths.to_dict()

        priorities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.priorities, Unset):
            priorities = self.priorities.to_dict()

        static = self.static

        private = self.private

        stp = self.stp

        span = self.span

        edge = self.edge

        autoedge = self.autoedge

        ptp = self.ptp

        autoptp = self.autoptp

        bridgeif = self.bridgeif

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if members is not UNSET:
            field_dict["members"] = members
        if enablestp is not UNSET:
            field_dict["enablestp"] = enablestp
        if descr is not UNSET:
            field_dict["descr"] = descr
        if maxaddr is not UNSET:
            field_dict["maxaddr"] = maxaddr
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if maxage is not UNSET:
            field_dict["maxage"] = maxage
        if fwdelay is not UNSET:
            field_dict["fwdelay"] = fwdelay
        if hellotime is not UNSET:
            field_dict["hellotime"] = hellotime
        if priority is not UNSET:
            field_dict["priority"] = priority
        if proto is not UNSET:
            field_dict["proto"] = proto
        if holdcnt is not UNSET:
            field_dict["holdcnt"] = holdcnt
        if ip6linklocal is not UNSET:
            field_dict["ip6linklocal"] = ip6linklocal
        if ifpriority is not UNSET:
            field_dict["ifpriority"] = ifpriority
        if ifpathcost is not UNSET:
            field_dict["ifpathcost"] = ifpathcost
        if paths is not UNSET:
            field_dict["paths"] = paths
        if priorities is not UNSET:
            field_dict["priorities"] = priorities
        if static is not UNSET:
            field_dict["static"] = static
        if private is not UNSET:
            field_dict["private"] = private
        if stp is not UNSET:
            field_dict["stp"] = stp
        if span is not UNSET:
            field_dict["span"] = span
        if edge is not UNSET:
            field_dict["edge"] = edge
        if autoedge is not UNSET:
            field_dict["autoedge"] = autoedge
        if ptp is not UNSET:
            field_dict["ptp"] = ptp
        if autoptp is not UNSET:
            field_dict["autoptp"] = autoptp
        if bridgeif is not UNSET:
            field_dict["bridgeif"] = bridgeif

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bridge_interface_paths import BridgeInterfacePaths
        from ..models.bridge_interface_priorities import BridgeInterfacePriorities

        d = src_dict.copy()
        members = d.pop("members", UNSET)

        enablestp = d.pop("enablestp", UNSET)

        descr = d.pop("descr", UNSET)

        maxaddr = d.pop("maxaddr", UNSET)

        timeout = d.pop("timeout", UNSET)

        maxage = d.pop("maxage", UNSET)

        fwdelay = d.pop("fwdelay", UNSET)

        hellotime = d.pop("hellotime", UNSET)

        priority = d.pop("priority", UNSET)

        proto = d.pop("proto", UNSET)

        holdcnt = d.pop("holdcnt", UNSET)

        ip6linklocal = d.pop("ip6linklocal", UNSET)

        ifpriority = d.pop("ifpriority", UNSET)

        ifpathcost = d.pop("ifpathcost", UNSET)

        _paths = d.pop("paths", UNSET)
        paths: Union[Unset, BridgeInterfacePaths]
        if isinstance(_paths, Unset):
            paths = UNSET
        else:
            paths = BridgeInterfacePaths.from_dict(_paths)

        _priorities = d.pop("priorities", UNSET)
        priorities: Union[Unset, BridgeInterfacePriorities]
        if isinstance(_priorities, Unset):
            priorities = UNSET
        else:
            priorities = BridgeInterfacePriorities.from_dict(_priorities)

        static = d.pop("static", UNSET)

        private = d.pop("private", UNSET)

        stp = d.pop("stp", UNSET)

        span = d.pop("span", UNSET)

        edge = d.pop("edge", UNSET)

        autoedge = d.pop("autoedge", UNSET)

        ptp = d.pop("ptp", UNSET)

        autoptp = d.pop("autoptp", UNSET)

        bridgeif = d.pop("bridgeif", UNSET)

        bridge_interface = cls(
            members=members,
            enablestp=enablestp,
            descr=descr,
            maxaddr=maxaddr,
            timeout=timeout,
            maxage=maxage,
            fwdelay=fwdelay,
            hellotime=hellotime,
            priority=priority,
            proto=proto,
            holdcnt=holdcnt,
            ip6linklocal=ip6linklocal,
            ifpriority=ifpriority,
            ifpathcost=ifpathcost,
            paths=paths,
            priorities=priorities,
            static=static,
            private=private,
            stp=stp,
            span=span,
            edge=edge,
            autoedge=autoedge,
            ptp=ptp,
            autoptp=autoptp,
            bridgeif=bridgeif,
        )

        bridge_interface.additional_properties = d
        return bridge_interface

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
