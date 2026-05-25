from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspRnaUaFingerprintsLUserAgent")


@_attrs_define
class SnortInspRnaUaFingerprintsLUserAgent:
    """
    Attributes:
        substring (str | Unset): a substring of user agent string
    """

    substring: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        substring = self.substring

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if substring is not UNSET:
            field_dict["substring"] = substring

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        substring = d.pop("substring", UNSET)

        snort_insp_rna_ua_fingerprints_l_user_agent = cls(
            substring=substring,
        )

        snort_insp_rna_ua_fingerprints_l_user_agent.additional_properties = d
        return snort_insp_rna_ua_fingerprints_l_user_agent

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
