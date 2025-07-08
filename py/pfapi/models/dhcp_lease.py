from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DHCPLease")


@_attrs_define
class DHCPLease:
    """
    Attributes:
        type (Union[Unset, str]): dynamic, static, ia-na, ia-pd, ia-ta
        host (Union[Unset, str]):
        lifetime (Union[Unset, int]):
        ip (Union[Unset, str]):
        mac (Union[Unset, str]):
        cltt (Union[Unset, str]):
        cid (Union[Unset, str]):
        state (Union[Unset, str]):
        start (Union[Unset, str]):
        end (Union[Unset, str]):
        iaid (Union[Unset, str]):
        duid (Union[Unset, str]):
        online_status (Union[Unset, str]):
        descr (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    lifetime: Union[Unset, int] = UNSET
    ip: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    cltt: Union[Unset, str] = UNSET
    cid: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    start: Union[Unset, str] = UNSET
    end: Union[Unset, str] = UNSET
    iaid: Union[Unset, str] = UNSET
    duid: Union[Unset, str] = UNSET
    online_status: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

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
            type=type,
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
