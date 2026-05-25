from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspTlvPdu")


@_attrs_define
class SnortInspTlvPdu:
    """
    Attributes:
        offset (int | Unset): index to first byte of length field { 0:65535 }; default 0
        size (int | Unset): number of bytes in length field { 1:4 }; default 4
        skip (int | Unset): bytes after length field to end of header { 0:65535 }; default 0
        relative (bool | Unset): extracted length follows field (instead of whole PDU); default false
    """

    offset: int | Unset = UNSET
    size: int | Unset = UNSET
    skip: int | Unset = UNSET
    relative: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        size = self.size

        skip = self.skip

        relative = self.relative

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offset is not UNSET:
            field_dict["offset"] = offset
        if size is not UNSET:
            field_dict["size"] = size
        if skip is not UNSET:
            field_dict["skip"] = skip
        if relative is not UNSET:
            field_dict["relative"] = relative

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offset = d.pop("offset", UNSET)

        size = d.pop("size", UNSET)

        skip = d.pop("skip", UNSET)

        relative = d.pop("relative", UNSET)

        snort_insp_tlv_pdu = cls(
            offset=offset,
            size=size,
            skip=skip,
            relative=relative,
        )

        snort_insp_tlv_pdu.additional_properties = d
        return snort_insp_tlv_pdu

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
