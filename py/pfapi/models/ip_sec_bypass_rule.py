from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecBypassRule")


@_attrs_define
class IPSecBypassRule:
    """
    Attributes:
        source (str | Unset):
        sourcemask (str | Unset):
        destination (str | Unset):
        dstmask (str | Unset):
    """

    source: str | Unset = UNSET
    sourcemask: str | Unset = UNSET
    destination: str | Unset = UNSET
    dstmask: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        sourcemask = self.sourcemask

        destination = self.destination

        dstmask = self.dstmask

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if sourcemask is not UNSET:
            field_dict["sourcemask"] = sourcemask
        if destination is not UNSET:
            field_dict["destination"] = destination
        if dstmask is not UNSET:
            field_dict["dstmask"] = dstmask

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source", UNSET)

        sourcemask = d.pop("sourcemask", UNSET)

        destination = d.pop("destination", UNSET)

        dstmask = d.pop("dstmask", UNSET)

        ip_sec_bypass_rule = cls(
            source=source,
            sourcemask=sourcemask,
            destination=destination,
            dstmask=dstmask,
        )

        ip_sec_bypass_rule.additional_properties = d
        return ip_sec_bypass_rule

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
