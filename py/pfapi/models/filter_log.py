from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_log_carp_info import FilterLogCARPInfo
    from ..models.filter_log_icmp_info import FilterLogICMPInfo
    from ..models.filter_log_tcp_info import FilterLogTCPInfo
    from ..models.filter_log_version_4_info import FilterLogVersion4Info
    from ..models.filter_log_version_6_info import FilterLogVersion6Info


T = TypeVar("T", bound="FilterLog")


@_attrs_define
class FilterLog:
    """
    Attributes:
        time_usec (int | Unset):
        time (str | Unset):
        rulenum (int | Unset):
        subrulenum (int | Unset):
        anchor (str | Unset):
        rule_descr (str | Unset):
        tracker (str | Unset):
        realint (str | Unset):
        friendly_interface (str | Unset):
        reason (str | Unset):
        action (str | Unset):
        direction (str | Unset):
        version (int | Unset):
        proto_id (int | Unset):
        proto (str | Unset):
        v4info (FilterLogVersion4Info | Unset):
        v6info (FilterLogVersion6Info | Unset):
        length (int | Unset):
        src (str | Unset):
        dst (str | Unset):
        src_ip (str | Unset):
        dst_ip (str | Unset):
        src_port (int | Unset):
        dst_port (int | Unset):
        tcp_info (FilterLogTCPInfo | Unset): proto_id = 6
        icmp_info (FilterLogICMPInfo | Unset): proto_id 1, 58
        carp_info (FilterLogCARPInfo | Unset):
    """

    time_usec: int | Unset = UNSET
    time: str | Unset = UNSET
    rulenum: int | Unset = UNSET
    subrulenum: int | Unset = UNSET
    anchor: str | Unset = UNSET
    rule_descr: str | Unset = UNSET
    tracker: str | Unset = UNSET
    realint: str | Unset = UNSET
    friendly_interface: str | Unset = UNSET
    reason: str | Unset = UNSET
    action: str | Unset = UNSET
    direction: str | Unset = UNSET
    version: int | Unset = UNSET
    proto_id: int | Unset = UNSET
    proto: str | Unset = UNSET
    v4info: FilterLogVersion4Info | Unset = UNSET
    v6info: FilterLogVersion6Info | Unset = UNSET
    length: int | Unset = UNSET
    src: str | Unset = UNSET
    dst: str | Unset = UNSET
    src_ip: str | Unset = UNSET
    dst_ip: str | Unset = UNSET
    src_port: int | Unset = UNSET
    dst_port: int | Unset = UNSET
    tcp_info: FilterLogTCPInfo | Unset = UNSET
    icmp_info: FilterLogICMPInfo | Unset = UNSET
    carp_info: FilterLogCARPInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_usec = self.time_usec

        time = self.time

        rulenum = self.rulenum

        subrulenum = self.subrulenum

        anchor = self.anchor

        rule_descr = self.rule_descr

        tracker = self.tracker

        realint = self.realint

        friendly_interface = self.friendly_interface

        reason = self.reason

        action = self.action

        direction = self.direction

        version = self.version

        proto_id = self.proto_id

        proto = self.proto

        v4info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.v4info, Unset):
            v4info = self.v4info.to_dict()

        v6info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.v6info, Unset):
            v6info = self.v6info.to_dict()

        length = self.length

        src = self.src

        dst = self.dst

        src_ip = self.src_ip

        dst_ip = self.dst_ip

        src_port = self.src_port

        dst_port = self.dst_port

        tcp_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp_info, Unset):
            tcp_info = self.tcp_info.to_dict()

        icmp_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.icmp_info, Unset):
            icmp_info = self.icmp_info.to_dict()

        carp_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.carp_info, Unset):
            carp_info = self.carp_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_usec is not UNSET:
            field_dict["time_usec"] = time_usec
        if time is not UNSET:
            field_dict["time"] = time
        if rulenum is not UNSET:
            field_dict["rulenum"] = rulenum
        if subrulenum is not UNSET:
            field_dict["subrulenum"] = subrulenum
        if anchor is not UNSET:
            field_dict["anchor"] = anchor
        if rule_descr is not UNSET:
            field_dict["rule_descr"] = rule_descr
        if tracker is not UNSET:
            field_dict["tracker"] = tracker
        if realint is not UNSET:
            field_dict["realint"] = realint
        if friendly_interface is not UNSET:
            field_dict["friendly_interface"] = friendly_interface
        if reason is not UNSET:
            field_dict["reason"] = reason
        if action is not UNSET:
            field_dict["action"] = action
        if direction is not UNSET:
            field_dict["direction"] = direction
        if version is not UNSET:
            field_dict["version"] = version
        if proto_id is not UNSET:
            field_dict["proto_id"] = proto_id
        if proto is not UNSET:
            field_dict["proto"] = proto
        if v4info is not UNSET:
            field_dict["v4info"] = v4info
        if v6info is not UNSET:
            field_dict["v6info"] = v6info
        if length is not UNSET:
            field_dict["length"] = length
        if src is not UNSET:
            field_dict["src"] = src
        if dst is not UNSET:
            field_dict["dst"] = dst
        if src_ip is not UNSET:
            field_dict["src_ip"] = src_ip
        if dst_ip is not UNSET:
            field_dict["dst_ip"] = dst_ip
        if src_port is not UNSET:
            field_dict["src_port"] = src_port
        if dst_port is not UNSET:
            field_dict["dst_port"] = dst_port
        if tcp_info is not UNSET:
            field_dict["tcp_info"] = tcp_info
        if icmp_info is not UNSET:
            field_dict["icmp_info"] = icmp_info
        if carp_info is not UNSET:
            field_dict["carp_info"] = carp_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_log_carp_info import FilterLogCARPInfo
        from ..models.filter_log_icmp_info import FilterLogICMPInfo
        from ..models.filter_log_tcp_info import FilterLogTCPInfo
        from ..models.filter_log_version_4_info import FilterLogVersion4Info
        from ..models.filter_log_version_6_info import FilterLogVersion6Info

        d = dict(src_dict)
        time_usec = d.pop("time_usec", UNSET)

        time = d.pop("time", UNSET)

        rulenum = d.pop("rulenum", UNSET)

        subrulenum = d.pop("subrulenum", UNSET)

        anchor = d.pop("anchor", UNSET)

        rule_descr = d.pop("rule_descr", UNSET)

        tracker = d.pop("tracker", UNSET)

        realint = d.pop("realint", UNSET)

        friendly_interface = d.pop("friendly_interface", UNSET)

        reason = d.pop("reason", UNSET)

        action = d.pop("action", UNSET)

        direction = d.pop("direction", UNSET)

        version = d.pop("version", UNSET)

        proto_id = d.pop("proto_id", UNSET)

        proto = d.pop("proto", UNSET)

        _v4info = d.pop("v4info", UNSET)
        v4info: FilterLogVersion4Info | Unset
        if isinstance(_v4info, Unset):
            v4info = UNSET
        else:
            v4info = FilterLogVersion4Info.from_dict(_v4info)

        _v6info = d.pop("v6info", UNSET)
        v6info: FilterLogVersion6Info | Unset
        if isinstance(_v6info, Unset):
            v6info = UNSET
        else:
            v6info = FilterLogVersion6Info.from_dict(_v6info)

        length = d.pop("length", UNSET)

        src = d.pop("src", UNSET)

        dst = d.pop("dst", UNSET)

        src_ip = d.pop("src_ip", UNSET)

        dst_ip = d.pop("dst_ip", UNSET)

        src_port = d.pop("src_port", UNSET)

        dst_port = d.pop("dst_port", UNSET)

        _tcp_info = d.pop("tcp_info", UNSET)
        tcp_info: FilterLogTCPInfo | Unset
        if isinstance(_tcp_info, Unset):
            tcp_info = UNSET
        else:
            tcp_info = FilterLogTCPInfo.from_dict(_tcp_info)

        _icmp_info = d.pop("icmp_info", UNSET)
        icmp_info: FilterLogICMPInfo | Unset
        if isinstance(_icmp_info, Unset):
            icmp_info = UNSET
        else:
            icmp_info = FilterLogICMPInfo.from_dict(_icmp_info)

        _carp_info = d.pop("carp_info", UNSET)
        carp_info: FilterLogCARPInfo | Unset
        if isinstance(_carp_info, Unset):
            carp_info = UNSET
        else:
            carp_info = FilterLogCARPInfo.from_dict(_carp_info)

        filter_log = cls(
            time_usec=time_usec,
            time=time,
            rulenum=rulenum,
            subrulenum=subrulenum,
            anchor=anchor,
            rule_descr=rule_descr,
            tracker=tracker,
            realint=realint,
            friendly_interface=friendly_interface,
            reason=reason,
            action=action,
            direction=direction,
            version=version,
            proto_id=proto_id,
            proto=proto,
            v4info=v4info,
            v6info=v6info,
            length=length,
            src=src,
            dst=dst,
            src_ip=src_ip,
            dst_ip=dst_ip,
            src_port=src_port,
            dst_port=dst_port,
            tcp_info=tcp_info,
            icmp_info=icmp_info,
            carp_info=carp_info,
        )

        filter_log.additional_properties = d
        return filter_log

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
