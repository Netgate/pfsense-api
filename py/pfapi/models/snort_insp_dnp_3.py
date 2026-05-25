from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspDnp3")


@_attrs_define
class SnortInspDnp3:
    """
    Attributes:
        check_crc (bool | Unset): validate checksums in DNP3 link layer frames; default false
    """

    check_crc: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_crc = self.check_crc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_crc is not UNSET:
            field_dict["check_crc"] = check_crc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        check_crc = d.pop("check_crc", UNSET)

        snort_insp_dnp_3 = cls(
            check_crc=check_crc,
        )

        snort_insp_dnp_3.additional_properties = d
        return snort_insp_dnp_3

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
