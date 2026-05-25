from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspFileId")


@_attrs_define
class SnortInspFileId:
    """
    Attributes:
        type_depth (int | Unset): stop type ID at this point { 0:max53 }; default 1460
        signature_depth (int | Unset): stop signature at this point { 0:max53 }; default 10485760
        block_timeout (int | Unset): stop blocking after this many seconds { 0:max31 }; default 86400
        lookup_timeout (int | Unset): give up on lookup after this many seconds { 0:max31 }; default 2
        block_timeout_lookup (bool | Unset): block if lookup times out; default false
        capture_memcap (int | Unset): memcap for file capture in megabytes { 0:max53 }; default 100
        capture_max_size (int | Unset): stop file capture beyond this point { 0:max53 }; default 1048576
        capture_min_size (int | Unset): stop file capture if file size less than this { 0:max53 }; default 0
        capture_block_size (int | Unset): file capture block size in bytes { 8:max53 }; default 32768
        max_files_cached (int | Unset): maximal number of files cached in memory { 8:max53 }; default 65536
        max_files_per_flow (int | Unset): maximal number of files able to be concurrently processed per flow { 1:max53
            }; default 128
        show_data_depth (int | Unset): print this many octets { 0:max53 }; default 100
        rules_file (str | Unset): name of file with IPS rules for file identification
        trace_type (bool | Unset): enable runtime dump of type info; default false
        trace_signature (bool | Unset): enable runtime dump of signature info; default false
        trace_stream (bool | Unset): enable runtime dump of file data; default false
        decompress_buffer_size (int | Unset): file decompression buffer size { 1024:max31 }; default 100000
    """

    type_depth: int | Unset = UNSET
    signature_depth: int | Unset = UNSET
    block_timeout: int | Unset = UNSET
    lookup_timeout: int | Unset = UNSET
    block_timeout_lookup: bool | Unset = UNSET
    capture_memcap: int | Unset = UNSET
    capture_max_size: int | Unset = UNSET
    capture_min_size: int | Unset = UNSET
    capture_block_size: int | Unset = UNSET
    max_files_cached: int | Unset = UNSET
    max_files_per_flow: int | Unset = UNSET
    show_data_depth: int | Unset = UNSET
    rules_file: str | Unset = UNSET
    trace_type: bool | Unset = UNSET
    trace_signature: bool | Unset = UNSET
    trace_stream: bool | Unset = UNSET
    decompress_buffer_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_depth = self.type_depth

        signature_depth = self.signature_depth

        block_timeout = self.block_timeout

        lookup_timeout = self.lookup_timeout

        block_timeout_lookup = self.block_timeout_lookup

        capture_memcap = self.capture_memcap

        capture_max_size = self.capture_max_size

        capture_min_size = self.capture_min_size

        capture_block_size = self.capture_block_size

        max_files_cached = self.max_files_cached

        max_files_per_flow = self.max_files_per_flow

        show_data_depth = self.show_data_depth

        rules_file = self.rules_file

        trace_type = self.trace_type

        trace_signature = self.trace_signature

        trace_stream = self.trace_stream

        decompress_buffer_size = self.decompress_buffer_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_depth is not UNSET:
            field_dict["type_depth"] = type_depth
        if signature_depth is not UNSET:
            field_dict["signature_depth"] = signature_depth
        if block_timeout is not UNSET:
            field_dict["block_timeout"] = block_timeout
        if lookup_timeout is not UNSET:
            field_dict["lookup_timeout"] = lookup_timeout
        if block_timeout_lookup is not UNSET:
            field_dict["block_timeout_lookup"] = block_timeout_lookup
        if capture_memcap is not UNSET:
            field_dict["capture_memcap"] = capture_memcap
        if capture_max_size is not UNSET:
            field_dict["capture_max_size"] = capture_max_size
        if capture_min_size is not UNSET:
            field_dict["capture_min_size"] = capture_min_size
        if capture_block_size is not UNSET:
            field_dict["capture_block_size"] = capture_block_size
        if max_files_cached is not UNSET:
            field_dict["max_files_cached"] = max_files_cached
        if max_files_per_flow is not UNSET:
            field_dict["max_files_per_flow"] = max_files_per_flow
        if show_data_depth is not UNSET:
            field_dict["show_data_depth"] = show_data_depth
        if rules_file is not UNSET:
            field_dict["rules_file"] = rules_file
        if trace_type is not UNSET:
            field_dict["trace_type"] = trace_type
        if trace_signature is not UNSET:
            field_dict["trace_signature"] = trace_signature
        if trace_stream is not UNSET:
            field_dict["trace_stream"] = trace_stream
        if decompress_buffer_size is not UNSET:
            field_dict["decompress_buffer_size"] = decompress_buffer_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_depth = d.pop("type_depth", UNSET)

        signature_depth = d.pop("signature_depth", UNSET)

        block_timeout = d.pop("block_timeout", UNSET)

        lookup_timeout = d.pop("lookup_timeout", UNSET)

        block_timeout_lookup = d.pop("block_timeout_lookup", UNSET)

        capture_memcap = d.pop("capture_memcap", UNSET)

        capture_max_size = d.pop("capture_max_size", UNSET)

        capture_min_size = d.pop("capture_min_size", UNSET)

        capture_block_size = d.pop("capture_block_size", UNSET)

        max_files_cached = d.pop("max_files_cached", UNSET)

        max_files_per_flow = d.pop("max_files_per_flow", UNSET)

        show_data_depth = d.pop("show_data_depth", UNSET)

        rules_file = d.pop("rules_file", UNSET)

        trace_type = d.pop("trace_type", UNSET)

        trace_signature = d.pop("trace_signature", UNSET)

        trace_stream = d.pop("trace_stream", UNSET)

        decompress_buffer_size = d.pop("decompress_buffer_size", UNSET)

        snort_insp_file_id = cls(
            type_depth=type_depth,
            signature_depth=signature_depth,
            block_timeout=block_timeout,
            lookup_timeout=lookup_timeout,
            block_timeout_lookup=block_timeout_lookup,
            capture_memcap=capture_memcap,
            capture_max_size=capture_max_size,
            capture_min_size=capture_min_size,
            capture_block_size=capture_block_size,
            max_files_cached=max_files_cached,
            max_files_per_flow=max_files_per_flow,
            show_data_depth=show_data_depth,
            rules_file=rules_file,
            trace_type=trace_type,
            trace_signature=trace_signature,
            trace_stream=trace_stream,
            decompress_buffer_size=decompress_buffer_size,
        )

        snort_insp_file_id.additional_properties = d
        return snort_insp_file_id

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
