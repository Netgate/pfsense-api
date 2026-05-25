from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspSnortMl")


@_attrs_define
class SnortInspSnortMl:
    """
    Attributes:
        uri_depth (int | Unset): number of input HTTP URI bytes to scan (-1 unlimited) { -1:max31 }; default -1
        client_body_depth (int | Unset): number of input HTTP client body bytes to scan (-1 unlimited) { -1:max31 };
            default 0
        http_param_threshold (float | Unset): alert threshold for http_param_model { 0:1 }; default 0.95
    """

    uri_depth: int | Unset = UNSET
    client_body_depth: int | Unset = UNSET
    http_param_threshold: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri_depth = self.uri_depth

        client_body_depth = self.client_body_depth

        http_param_threshold = self.http_param_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uri_depth is not UNSET:
            field_dict["uri_depth"] = uri_depth
        if client_body_depth is not UNSET:
            field_dict["client_body_depth"] = client_body_depth
        if http_param_threshold is not UNSET:
            field_dict["http_param_threshold"] = http_param_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri_depth = d.pop("uri_depth", UNSET)

        client_body_depth = d.pop("client_body_depth", UNSET)

        http_param_threshold = d.pop("http_param_threshold", UNSET)

        snort_insp_snort_ml = cls(
            uri_depth=uri_depth,
            client_body_depth=client_body_depth,
            http_param_threshold=http_param_threshold,
        )

        snort_insp_snort_ml.additional_properties = d
        return snort_insp_snort_ml

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
