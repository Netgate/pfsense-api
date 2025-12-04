from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DHCPLease")


@_attrs_define
class DHCPLease:
    """
    Attributes:
        type_ (str | Unset): dynamic, static, ia-na, ia-pd, ia-ta
        host (str | Unset):
        lifetime (int | Unset):
        ip (str | Unset):
        mac (str | Unset):
        cltt (str | Unset):
        cid (str | Unset):
        state (str | Unset):
        start (str | Unset):
        end (str | Unset):
        iaid (str | Unset):
        duid (str | Unset):
        online_status (str | Unset):
        descr (str | Unset):
    """

    type_: str | Unset = UNSET
    host: str | Unset = UNSET
    lifetime: int | Unset = UNSET
    ip: str | Unset = UNSET
    mac: str | Unset = UNSET
    cltt: str | Unset = UNSET
    cid: str | Unset = UNSET
    state: str | Unset = UNSET
    start: str | Unset = UNSET
    end: str | Unset = UNSET
    iaid: str | Unset = UNSET
    duid: str | Unset = UNSET
    online_status: str | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        host = self.host

        lifetime = self.lifetime

        ip = self.ip

        mac = self.mac

        cltt = self.cltt

        cid = self.cid

        state = self.state

        start = self.start

        end = self.end

        iaid = self.iaid

        duid = self.duid

        online_status = self.online_status

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if host is not UNSET:
            field_dict["host"] = host
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if ip is not UNSET:
            field_dict["ip"] = ip
        if mac is not UNSET:
            field_dict["mac"] = mac
        if cltt is not UNSET:
            field_dict["cltt"] = cltt
        if cid is not UNSET:
            field_dict["cid"] = cid
        if state is not UNSET:
            field_dict["state"] = state
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if iaid is not UNSET:
            field_dict["iaid"] = iaid
        if duid is not UNSET:
            field_dict["duid"] = duid
        if online_status is not UNSET:
            field_dict["online_status"] = online_status
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        host = d.pop("host", UNSET)

        lifetime = d.pop("lifetime", UNSET)

        ip = d.pop("ip", UNSET)

        mac = d.pop("mac", UNSET)

        cltt = d.pop("cltt", UNSET)

        cid = d.pop("cid", UNSET)

        state = d.pop("state", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        iaid = d.pop("iaid", UNSET)

        duid = d.pop("duid", UNSET)

        online_status = d.pop("online_status", UNSET)

        descr = d.pop("descr", UNSET)

        dhcp_lease = cls(
            type_=type_,
            host=host,
            lifetime=lifetime,
            ip=ip,
            mac=mac,
            cltt=cltt,
            cid=cid,
            state=state,
            start=start,
            end=end,
            iaid=iaid,
            duid=duid,
            online_status=online_status,
            descr=descr,
        )

        dhcp_lease.additional_properties = d
        return dhcp_lease

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
