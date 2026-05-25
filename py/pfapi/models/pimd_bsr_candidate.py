from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PimdBsrCandidate")


@_attrs_define
class PimdBsrCandidate:
    """
    Attributes:
        intf_ident (str | Unset): Interface

            The interface or address on which to enable Bootstrap Router (BSR) candidate
            election participation.
            When set to "default", the feature is enabled without a specific interface,
            which will default to the highest available IP address.
        descr (str | Unset): Description
        priority (str | Unset): Priority

            Priority of this router when electing a BSR.
            Higher values are preferred by participating routers.
            (0-255, Default: 0)
        id (str | Unset): (readonly) ID assigned to this entry
    """

    intf_ident: str | Unset = UNSET
    descr: str | Unset = UNSET
    priority: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        intf_ident = self.intf_ident

        descr = self.descr

        priority = self.priority

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if intf_ident is not UNSET:
            field_dict["intf_ident"] = intf_ident
        if descr is not UNSET:
            field_dict["descr"] = descr
        if priority is not UNSET:
            field_dict["priority"] = priority
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        intf_ident = d.pop("intf_ident", UNSET)

        descr = d.pop("descr", UNSET)

        priority = d.pop("priority", UNSET)

        id = d.pop("id", UNSET)

        pimd_bsr_candidate = cls(
            intf_ident=intf_ident,
            descr=descr,
            priority=priority,
            id=id,
        )

        pimd_bsr_candidate.additional_properties = d
        return pimd_bsr_candidate

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
