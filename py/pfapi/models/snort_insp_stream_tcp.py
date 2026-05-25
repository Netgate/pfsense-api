from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_stream_tcp_queue_limit import SnortInspStreamTcpQueueLimit
    from ..models.snort_insp_stream_tcp_small_segments import SnortInspStreamTcpSmallSegments


T = TypeVar("T", bound="SnortInspStreamTcp")


@_attrs_define
class SnortInspStreamTcp:
    """
    Attributes:
        flush_factor (int | Unset): flush upon seeing a drop in segment size after given number of non-decreasing
            segments { 0:65535 }; default 0
        max_window (int | Unset): maximum allowed TCP window { 0:1073725440 }; default 0
        overlap_limit (int | Unset): maximum number of allowed overlapping segments per session { 0:max32 }; default 0
        max_pdu (int | Unset): maximum reassembled PDU size { 1460:32768 }; default 16384
        no_ack (bool | Unset): received data is implicitly acked immediately; default false
        policy (str | Unset): determines operating system characteristics like reassembly { first | last | linux |
            old_linux | bsd | macos | solaris | irix | hpux11 | hpux10 | windows | win_2003 | vista }; default bsd
        reassemble_async (bool | Unset): queue data for reassembly before traffic is seen in both directions; default
            true
        show_rebuilt_packets (bool | Unset): enable cmg like output of reassembled packets; default false
        queue_limit (SnortInspStreamTcpQueueLimit | Unset):
        small_segments (SnortInspStreamTcpSmallSegments | Unset):
        session_timeout (int | Unset): session tracking timeout { 1:max31 }; default 180
        track_only (bool | Unset): disable reassembly if true; default false
        embryonic_timeout (int | Unset): Non-established connection timeout { 1:max31 }; default 30
        idle_timeout (int | Unset): session deletion on idle { 1:max31 }; default 3600
    """

    flush_factor: int | Unset = UNSET
    max_window: int | Unset = UNSET
    overlap_limit: int | Unset = UNSET
    max_pdu: int | Unset = UNSET
    no_ack: bool | Unset = UNSET
    policy: str | Unset = UNSET
    reassemble_async: bool | Unset = UNSET
    show_rebuilt_packets: bool | Unset = UNSET
    queue_limit: SnortInspStreamTcpQueueLimit | Unset = UNSET
    small_segments: SnortInspStreamTcpSmallSegments | Unset = UNSET
    session_timeout: int | Unset = UNSET
    track_only: bool | Unset = UNSET
    embryonic_timeout: int | Unset = UNSET
    idle_timeout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flush_factor = self.flush_factor

        max_window = self.max_window

        overlap_limit = self.overlap_limit

        max_pdu = self.max_pdu

        no_ack = self.no_ack

        policy = self.policy

        reassemble_async = self.reassemble_async

        show_rebuilt_packets = self.show_rebuilt_packets

        queue_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queue_limit, Unset):
            queue_limit = self.queue_limit.to_dict()

        small_segments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.small_segments, Unset):
            small_segments = self.small_segments.to_dict()

        session_timeout = self.session_timeout

        track_only = self.track_only

        embryonic_timeout = self.embryonic_timeout

        idle_timeout = self.idle_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flush_factor is not UNSET:
            field_dict["flush_factor"] = flush_factor
        if max_window is not UNSET:
            field_dict["max_window"] = max_window
        if overlap_limit is not UNSET:
            field_dict["overlap_limit"] = overlap_limit
        if max_pdu is not UNSET:
            field_dict["max_pdu"] = max_pdu
        if no_ack is not UNSET:
            field_dict["no_ack"] = no_ack
        if policy is not UNSET:
            field_dict["policy"] = policy
        if reassemble_async is not UNSET:
            field_dict["reassemble_async"] = reassemble_async
        if show_rebuilt_packets is not UNSET:
            field_dict["show_rebuilt_packets"] = show_rebuilt_packets
        if queue_limit is not UNSET:
            field_dict["queue_limit"] = queue_limit
        if small_segments is not UNSET:
            field_dict["small_segments"] = small_segments
        if session_timeout is not UNSET:
            field_dict["session_timeout"] = session_timeout
        if track_only is not UNSET:
            field_dict["track_only"] = track_only
        if embryonic_timeout is not UNSET:
            field_dict["embryonic_timeout"] = embryonic_timeout
        if idle_timeout is not UNSET:
            field_dict["idle_timeout"] = idle_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_stream_tcp_queue_limit import SnortInspStreamTcpQueueLimit
        from ..models.snort_insp_stream_tcp_small_segments import SnortInspStreamTcpSmallSegments

        d = dict(src_dict)
        flush_factor = d.pop("flush_factor", UNSET)

        max_window = d.pop("max_window", UNSET)

        overlap_limit = d.pop("overlap_limit", UNSET)

        max_pdu = d.pop("max_pdu", UNSET)

        no_ack = d.pop("no_ack", UNSET)

        policy = d.pop("policy", UNSET)

        reassemble_async = d.pop("reassemble_async", UNSET)

        show_rebuilt_packets = d.pop("show_rebuilt_packets", UNSET)

        _queue_limit = d.pop("queue_limit", UNSET)
        queue_limit: SnortInspStreamTcpQueueLimit | Unset
        if isinstance(_queue_limit, Unset):
            queue_limit = UNSET
        else:
            queue_limit = SnortInspStreamTcpQueueLimit.from_dict(_queue_limit)

        _small_segments = d.pop("small_segments", UNSET)
        small_segments: SnortInspStreamTcpSmallSegments | Unset
        if isinstance(_small_segments, Unset):
            small_segments = UNSET
        else:
            small_segments = SnortInspStreamTcpSmallSegments.from_dict(_small_segments)

        session_timeout = d.pop("session_timeout", UNSET)

        track_only = d.pop("track_only", UNSET)

        embryonic_timeout = d.pop("embryonic_timeout", UNSET)

        idle_timeout = d.pop("idle_timeout", UNSET)

        snort_insp_stream_tcp = cls(
            flush_factor=flush_factor,
            max_window=max_window,
            overlap_limit=overlap_limit,
            max_pdu=max_pdu,
            no_ack=no_ack,
            policy=policy,
            reassemble_async=reassemble_async,
            show_rebuilt_packets=show_rebuilt_packets,
            queue_limit=queue_limit,
            small_segments=small_segments,
            session_timeout=session_timeout,
            track_only=track_only,
            embryonic_timeout=embryonic_timeout,
            idle_timeout=idle_timeout,
        )

        snort_insp_stream_tcp.additional_properties = d
        return snort_insp_stream_tcp

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
