from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortAlert")


@_attrs_define
class SnortAlert:
    """
    Attributes:
        timestamp (int | Unset): Epoch microsecond timestamp of alert
        priority (int | Unset):
        protocol (str | Unset): udp, tcp, etc
        class_ (str | Unset): classification
        src_addr (str | Unset):
        src_port (int | Unset):
        dst_addr (str | Unset):
        dst_port (int | Unset):
        sid (int | Unset): sig id
        gid (int | Unset): sig generator
        descr (str | Unset):
        action (str | Unset): alert, drop, reject, sdrop, log, pass
    """

    timestamp: int | Unset = UNSET
    priority: int | Unset = UNSET
    protocol: str | Unset = UNSET
    class_: str | Unset = UNSET
    src_addr: str | Unset = UNSET
    src_port: int | Unset = UNSET
    dst_addr: str | Unset = UNSET
    dst_port: int | Unset = UNSET
    sid: int | Unset = UNSET
    gid: int | Unset = UNSET
    descr: str | Unset = UNSET
    action: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        priority = self.priority

        protocol = self.protocol

        class_ = self.class_

        src_addr = self.src_addr

        src_port = self.src_port

        dst_addr = self.dst_addr

        dst_port = self.dst_port

        sid = self.sid

        gid = self.gid

        descr = self.descr

        action = self.action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if priority is not UNSET:
            field_dict["priority"] = priority
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if class_ is not UNSET:
            field_dict["class"] = class_
        if src_addr is not UNSET:
            field_dict["src_addr"] = src_addr
        if src_port is not UNSET:
            field_dict["src_port"] = src_port
        if dst_addr is not UNSET:
            field_dict["dst_addr"] = dst_addr
        if dst_port is not UNSET:
            field_dict["dst_port"] = dst_port
        if sid is not UNSET:
            field_dict["sid"] = sid
        if gid is not UNSET:
            field_dict["gid"] = gid
        if descr is not UNSET:
            field_dict["descr"] = descr
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        priority = d.pop("priority", UNSET)

        protocol = d.pop("protocol", UNSET)

        class_ = d.pop("class", UNSET)

        src_addr = d.pop("src_addr", UNSET)

        src_port = d.pop("src_port", UNSET)

        dst_addr = d.pop("dst_addr", UNSET)

        dst_port = d.pop("dst_port", UNSET)

        sid = d.pop("sid", UNSET)

        gid = d.pop("gid", UNSET)

        descr = d.pop("descr", UNSET)

        action = d.pop("action", UNSET)

        snort_alert = cls(
            timestamp=timestamp,
            priority=priority,
            protocol=protocol,
            class_=class_,
            src_addr=src_addr,
            src_port=src_port,
            dst_addr=dst_addr,
            dst_port=dst_port,
            sid=sid,
            gid=gid,
            descr=descr,
            action=action,
        )

        snort_alert.additional_properties = d
        return snort_alert

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
