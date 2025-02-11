from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        time_usec (int):
        time (str):
        rulenum (int):
        subrulenum (int):
        anchor (str):
        rule_descr (str):
        tracker (str):
        realint (str):
        friendly_interface (str):
        reason (str):
        action (str):
        direction (str):
        version (int):
        proto_id (int):
        proto (str):
        v4info (FilterLogVersion4Info):
        v6info (FilterLogVersion6Info):
        length (int):
        src (str):
        dst (str):
        src_ip (str):
        dst_ip (str):
        src_port (int):
        dst_port (int):
        tcp_info (FilterLogTCPInfo): proto_id = 6
        icmp_info (FilterLogICMPInfo): proto_id 1, 58
        carp_info (FilterLogCARPInfo):
    """

    time_usec: int
    time: str
    rulenum: int
    subrulenum: int
    anchor: str
    rule_descr: str
    tracker: str
    realint: str
    friendly_interface: str
    reason: str
    action: str
    direction: str
    version: int
    proto_id: int
    proto: str
    v4info: "FilterLogVersion4Info"
    v6info: "FilterLogVersion6Info"
    length: int
    src: str
    dst: str
    src_ip: str
    dst_ip: str
    src_port: int
    dst_port: int
    tcp_info: "FilterLogTCPInfo"
    icmp_info: "FilterLogICMPInfo"
    carp_info: "FilterLogCARPInfo"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        v4info = self.v4info.to_dict()

        v6info = self.v6info.to_dict()

        length = self.length

        src = self.src

        dst = self.dst

        src_ip = self.src_ip

        dst_ip = self.dst_ip

        src_port = self.src_port

        dst_port = self.dst_port

        tcp_info = self.tcp_info.to_dict()

        icmp_info = self.icmp_info.to_dict()

        carp_info = self.carp_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time_usec": time_usec,
                "time": time,
                "rulenum": rulenum,
                "subrulenum": subrulenum,
                "anchor": anchor,
                "rule_descr": rule_descr,
                "tracker": tracker,
                "realint": realint,
                "friendly_interface": friendly_interface,
                "reason": reason,
                "action": action,
                "direction": direction,
                "version": version,
                "proto_id": proto_id,
                "proto": proto,
                "v4info": v4info,
                "v6info": v6info,
                "length": length,
                "src": src,
                "dst": dst,
                "src_ip": src_ip,
                "dst_ip": dst_ip,
                "src_port": src_port,
                "dst_port": dst_port,
                "tcp_info": tcp_info,
                "icmp_info": icmp_info,
                "carp_info": carp_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_log_carp_info import FilterLogCARPInfo
        from ..models.filter_log_icmp_info import FilterLogICMPInfo
        from ..models.filter_log_tcp_info import FilterLogTCPInfo
        from ..models.filter_log_version_4_info import FilterLogVersion4Info
        from ..models.filter_log_version_6_info import FilterLogVersion6Info

        d = src_dict.copy()
        time_usec = d.pop("time_usec")

        time = d.pop("time")

        rulenum = d.pop("rulenum")

        subrulenum = d.pop("subrulenum")

        anchor = d.pop("anchor")

        rule_descr = d.pop("rule_descr")

        tracker = d.pop("tracker")

        realint = d.pop("realint")

        friendly_interface = d.pop("friendly_interface")

        reason = d.pop("reason")

        action = d.pop("action")

        direction = d.pop("direction")

        version = d.pop("version")

        proto_id = d.pop("proto_id")

        proto = d.pop("proto")

        v4info = FilterLogVersion4Info.from_dict(d.pop("v4info"))

        v6info = FilterLogVersion6Info.from_dict(d.pop("v6info"))

        length = d.pop("length")

        src = d.pop("src")

        dst = d.pop("dst")

        src_ip = d.pop("src_ip")

        dst_ip = d.pop("dst_ip")

        src_port = d.pop("src_port")

        dst_port = d.pop("dst_port")

        tcp_info = FilterLogTCPInfo.from_dict(d.pop("tcp_info"))

        icmp_info = FilterLogICMPInfo.from_dict(d.pop("icmp_info"))

        carp_info = FilterLogCARPInfo.from_dict(d.pop("carp_info"))

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
