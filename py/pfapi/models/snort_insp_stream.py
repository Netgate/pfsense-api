from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_stream_allowlist_cache import SnortInspStreamAllowlistCache
    from ..models.snort_insp_stream_file_cache import SnortInspStreamFileCache
    from ..models.snort_insp_stream_icmp_cache import SnortInspStreamIcmpCache
    from ..models.snort_insp_stream_ip_cache import SnortInspStreamIpCache
    from ..models.snort_insp_stream_tcp_cache import SnortInspStreamTcpCache
    from ..models.snort_insp_stream_udp_cache import SnortInspStreamUdpCache
    from ..models.snort_insp_stream_user_cache import SnortInspStreamUserCache


T = TypeVar("T", bound="SnortInspStream")


@_attrs_define
class SnortInspStream:
    """
    Attributes:
        held_packet_timeout (int | Unset): timeout in milliseconds for held packets { 1:max32 }; default 1000
        ip_frags_only (bool | Unset): don’t process non-frag flows; default false
        max_flows (int | Unset): maximum simultaneous flows tracked before pruning { 2:max32 }; default 476288
        prune_flows (int | Unset): maximum flows to prune at one time { 1:max32 }; default 10
        pruning_timeout (int | Unset): minimum inactive time before being eligible for pruning { 1:max32 }; default 30
        require_3whs (int | Unset): don’t track midstream TCP sessions after given seconds from start up; -1 tracks all
            { -1:max31 }; default -1
        allowlist_cache (SnortInspStreamAllowlistCache | Unset):
        drop_stale_packets (bool | Unset): enable dropping of packets with stale timestamp; default false
        ip_cache (SnortInspStreamIpCache | Unset):
        icmp_cache (SnortInspStreamIcmpCache | Unset):
        tcp_cache (SnortInspStreamTcpCache | Unset):
        udp_cache (SnortInspStreamUdpCache | Unset):
        user_cache (SnortInspStreamUserCache | Unset):
        file_cache (SnortInspStreamFileCache | Unset):
    """

    held_packet_timeout: int | Unset = UNSET
    ip_frags_only: bool | Unset = UNSET
    max_flows: int | Unset = UNSET
    prune_flows: int | Unset = UNSET
    pruning_timeout: int | Unset = UNSET
    require_3whs: int | Unset = UNSET
    allowlist_cache: SnortInspStreamAllowlistCache | Unset = UNSET
    drop_stale_packets: bool | Unset = UNSET
    ip_cache: SnortInspStreamIpCache | Unset = UNSET
    icmp_cache: SnortInspStreamIcmpCache | Unset = UNSET
    tcp_cache: SnortInspStreamTcpCache | Unset = UNSET
    udp_cache: SnortInspStreamUdpCache | Unset = UNSET
    user_cache: SnortInspStreamUserCache | Unset = UNSET
    file_cache: SnortInspStreamFileCache | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        held_packet_timeout = self.held_packet_timeout

        ip_frags_only = self.ip_frags_only

        max_flows = self.max_flows

        prune_flows = self.prune_flows

        pruning_timeout = self.pruning_timeout

        require_3whs = self.require_3whs

        allowlist_cache: dict[str, Any] | Unset = UNSET
        if not isinstance(self.allowlist_cache, Unset):
            allowlist_cache = self.allowlist_cache.to_dict()

        drop_stale_packets = self.drop_stale_packets

        ip_cache: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_cache, Unset):
            ip_cache = self.ip_cache.to_dict()

        icmp_cache: dict[str, Any] | Unset = UNSET
        if not isinstance(self.icmp_cache, Unset):
            icmp_cache = self.icmp_cache.to_dict()

        tcp_cache: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp_cache, Unset):
            tcp_cache = self.tcp_cache.to_dict()

        udp_cache: dict[str, Any] | Unset = UNSET
        if not isinstance(self.udp_cache, Unset):
            udp_cache = self.udp_cache.to_dict()

        user_cache: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_cache, Unset):
            user_cache = self.user_cache.to_dict()

        file_cache: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_cache, Unset):
            file_cache = self.file_cache.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if held_packet_timeout is not UNSET:
            field_dict["held_packet_timeout"] = held_packet_timeout
        if ip_frags_only is not UNSET:
            field_dict["ip_frags_only"] = ip_frags_only
        if max_flows is not UNSET:
            field_dict["max_flows"] = max_flows
        if prune_flows is not UNSET:
            field_dict["prune_flows"] = prune_flows
        if pruning_timeout is not UNSET:
            field_dict["pruning_timeout"] = pruning_timeout
        if require_3whs is not UNSET:
            field_dict["require_3whs"] = require_3whs
        if allowlist_cache is not UNSET:
            field_dict["allowlist_cache"] = allowlist_cache
        if drop_stale_packets is not UNSET:
            field_dict["drop_stale_packets"] = drop_stale_packets
        if ip_cache is not UNSET:
            field_dict["ip_cache"] = ip_cache
        if icmp_cache is not UNSET:
            field_dict["icmp_cache"] = icmp_cache
        if tcp_cache is not UNSET:
            field_dict["tcp_cache"] = tcp_cache
        if udp_cache is not UNSET:
            field_dict["udp_cache"] = udp_cache
        if user_cache is not UNSET:
            field_dict["user_cache"] = user_cache
        if file_cache is not UNSET:
            field_dict["file_cache"] = file_cache

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_stream_allowlist_cache import SnortInspStreamAllowlistCache
        from ..models.snort_insp_stream_file_cache import SnortInspStreamFileCache
        from ..models.snort_insp_stream_icmp_cache import SnortInspStreamIcmpCache
        from ..models.snort_insp_stream_ip_cache import SnortInspStreamIpCache
        from ..models.snort_insp_stream_tcp_cache import SnortInspStreamTcpCache
        from ..models.snort_insp_stream_udp_cache import SnortInspStreamUdpCache
        from ..models.snort_insp_stream_user_cache import SnortInspStreamUserCache

        d = dict(src_dict)
        held_packet_timeout = d.pop("held_packet_timeout", UNSET)

        ip_frags_only = d.pop("ip_frags_only", UNSET)

        max_flows = d.pop("max_flows", UNSET)

        prune_flows = d.pop("prune_flows", UNSET)

        pruning_timeout = d.pop("pruning_timeout", UNSET)

        require_3whs = d.pop("require_3whs", UNSET)

        _allowlist_cache = d.pop("allowlist_cache", UNSET)
        allowlist_cache: SnortInspStreamAllowlistCache | Unset
        if isinstance(_allowlist_cache, Unset):
            allowlist_cache = UNSET
        else:
            allowlist_cache = SnortInspStreamAllowlistCache.from_dict(_allowlist_cache)

        drop_stale_packets = d.pop("drop_stale_packets", UNSET)

        _ip_cache = d.pop("ip_cache", UNSET)
        ip_cache: SnortInspStreamIpCache | Unset
        if isinstance(_ip_cache, Unset):
            ip_cache = UNSET
        else:
            ip_cache = SnortInspStreamIpCache.from_dict(_ip_cache)

        _icmp_cache = d.pop("icmp_cache", UNSET)
        icmp_cache: SnortInspStreamIcmpCache | Unset
        if isinstance(_icmp_cache, Unset):
            icmp_cache = UNSET
        else:
            icmp_cache = SnortInspStreamIcmpCache.from_dict(_icmp_cache)

        _tcp_cache = d.pop("tcp_cache", UNSET)
        tcp_cache: SnortInspStreamTcpCache | Unset
        if isinstance(_tcp_cache, Unset):
            tcp_cache = UNSET
        else:
            tcp_cache = SnortInspStreamTcpCache.from_dict(_tcp_cache)

        _udp_cache = d.pop("udp_cache", UNSET)
        udp_cache: SnortInspStreamUdpCache | Unset
        if isinstance(_udp_cache, Unset):
            udp_cache = UNSET
        else:
            udp_cache = SnortInspStreamUdpCache.from_dict(_udp_cache)

        _user_cache = d.pop("user_cache", UNSET)
        user_cache: SnortInspStreamUserCache | Unset
        if isinstance(_user_cache, Unset):
            user_cache = UNSET
        else:
            user_cache = SnortInspStreamUserCache.from_dict(_user_cache)

        _file_cache = d.pop("file_cache", UNSET)
        file_cache: SnortInspStreamFileCache | Unset
        if isinstance(_file_cache, Unset):
            file_cache = UNSET
        else:
            file_cache = SnortInspStreamFileCache.from_dict(_file_cache)

        snort_insp_stream = cls(
            held_packet_timeout=held_packet_timeout,
            ip_frags_only=ip_frags_only,
            max_flows=max_flows,
            prune_flows=prune_flows,
            pruning_timeout=pruning_timeout,
            require_3whs=require_3whs,
            allowlist_cache=allowlist_cache,
            drop_stale_packets=drop_stale_packets,
            ip_cache=ip_cache,
            icmp_cache=icmp_cache,
            tcp_cache=tcp_cache,
            udp_cache=udp_cache,
            user_cache=user_cache,
            file_cache=file_cache,
        )

        snort_insp_stream.additional_properties = d
        return snort_insp_stream

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
