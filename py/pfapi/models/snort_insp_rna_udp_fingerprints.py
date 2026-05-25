from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_rna_udp_fingerprints_l_user_agent import SnortInspRnaUdpFingerprintsLUserAgent


T = TypeVar("T", bound="SnortInspRnaUdpFingerprints")


@_attrs_define
class SnortInspRnaUdpFingerprints:
    """
    Attributes:
        fpid (int | Unset): fingerprint id { 0:max32 }; default 0
        type_ (int | Unset): fingerprint type { 0:max32 }; default 0
        uuid (str | Unset): fingerprint uuid
        ttl (int | Unset): fingerprint ttl { 0:255 }; default 0
        tcp_window (str | Unset): fingerprint tcp window
        mss (str | Unset): fingerprint mss; default X
        id (str | Unset): id; default X
        topts (str | Unset): fingerprint tcp options
        ws (str | Unset): fingerprint window size; default X
        df (bool | Unset): fingerprint don’t fragment flag; default false
        ua_type (str | Unset): type of user agent fingerprints { os | device | jail-broken | jail-broken-host }; default
            os
        user_agent (list[SnortInspRnaUdpFingerprintsLUserAgent] | Unset):
        host_name (str | Unset): host name information
        device (str | Unset): device information
        dhcp55 (str | Unset): dhcp option 55 values
        dhcp60 (str | Unset): dhcp option 60 values
        major (int | Unset): smb major version { 0:max31 }
        minor (int | Unset): smb minor version { 0:max31 }
        flags (int | Unset): smb flags { 0:max32 }
    """

    fpid: int | Unset = UNSET
    type_: int | Unset = UNSET
    uuid: str | Unset = UNSET
    ttl: int | Unset = UNSET
    tcp_window: str | Unset = UNSET
    mss: str | Unset = UNSET
    id: str | Unset = UNSET
    topts: str | Unset = UNSET
    ws: str | Unset = UNSET
    df: bool | Unset = UNSET
    ua_type: str | Unset = UNSET
    user_agent: list[SnortInspRnaUdpFingerprintsLUserAgent] | Unset = UNSET
    host_name: str | Unset = UNSET
    device: str | Unset = UNSET
    dhcp55: str | Unset = UNSET
    dhcp60: str | Unset = UNSET
    major: int | Unset = UNSET
    minor: int | Unset = UNSET
    flags: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fpid = self.fpid

        type_ = self.type_

        uuid = self.uuid

        ttl = self.ttl

        tcp_window = self.tcp_window

        mss = self.mss

        id = self.id

        topts = self.topts

        ws = self.ws

        df = self.df

        ua_type = self.ua_type

        user_agent: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_agent, Unset):
            user_agent = []
            for user_agent_item_data in self.user_agent:
                user_agent_item = user_agent_item_data.to_dict()
                user_agent.append(user_agent_item)

        host_name = self.host_name

        device = self.device

        dhcp55 = self.dhcp55

        dhcp60 = self.dhcp60

        major = self.major

        minor = self.minor

        flags = self.flags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fpid is not UNSET:
            field_dict["fpid"] = fpid
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if tcp_window is not UNSET:
            field_dict["tcp_window"] = tcp_window
        if mss is not UNSET:
            field_dict["mss"] = mss
        if id is not UNSET:
            field_dict["id"] = id
        if topts is not UNSET:
            field_dict["topts"] = topts
        if ws is not UNSET:
            field_dict["ws"] = ws
        if df is not UNSET:
            field_dict["df"] = df
        if ua_type is not UNSET:
            field_dict["ua_type"] = ua_type
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if device is not UNSET:
            field_dict["device"] = device
        if dhcp55 is not UNSET:
            field_dict["dhcp55"] = dhcp55
        if dhcp60 is not UNSET:
            field_dict["dhcp60"] = dhcp60
        if major is not UNSET:
            field_dict["major"] = major
        if minor is not UNSET:
            field_dict["minor"] = minor
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_rna_udp_fingerprints_l_user_agent import SnortInspRnaUdpFingerprintsLUserAgent

        d = dict(src_dict)
        fpid = d.pop("fpid", UNSET)

        type_ = d.pop("type", UNSET)

        uuid = d.pop("uuid", UNSET)

        ttl = d.pop("ttl", UNSET)

        tcp_window = d.pop("tcp_window", UNSET)

        mss = d.pop("mss", UNSET)

        id = d.pop("id", UNSET)

        topts = d.pop("topts", UNSET)

        ws = d.pop("ws", UNSET)

        df = d.pop("df", UNSET)

        ua_type = d.pop("ua_type", UNSET)

        _user_agent = d.pop("user_agent", UNSET)
        user_agent: list[SnortInspRnaUdpFingerprintsLUserAgent] | Unset = UNSET
        if _user_agent is not UNSET:
            user_agent = []
            for user_agent_item_data in _user_agent:
                user_agent_item = SnortInspRnaUdpFingerprintsLUserAgent.from_dict(user_agent_item_data)

                user_agent.append(user_agent_item)

        host_name = d.pop("host_name", UNSET)

        device = d.pop("device", UNSET)

        dhcp55 = d.pop("dhcp55", UNSET)

        dhcp60 = d.pop("dhcp60", UNSET)

        major = d.pop("major", UNSET)

        minor = d.pop("minor", UNSET)

        flags = d.pop("flags", UNSET)

        snort_insp_rna_udp_fingerprints = cls(
            fpid=fpid,
            type_=type_,
            uuid=uuid,
            ttl=ttl,
            tcp_window=tcp_window,
            mss=mss,
            id=id,
            topts=topts,
            ws=ws,
            df=df,
            ua_type=ua_type,
            user_agent=user_agent,
            host_name=host_name,
            device=device,
            dhcp55=dhcp55,
            dhcp60=dhcp60,
            major=major,
            minor=minor,
            flags=flags,
        )

        snort_insp_rna_udp_fingerprints.additional_properties = d
        return snort_insp_rna_udp_fingerprints

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
