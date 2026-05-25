from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThreatGateBackgroundMessages")


@_attrs_define
class ThreatGateBackgroundMessages:
    """
    Attributes:
        status (list[str] | Unset):
        errors (list[str] | Unset):
        success (list[str] | Unset):
        information (list[str] | Unset):
    """

    status: list[str] | Unset = UNSET
    errors: list[str] | Unset = UNSET
    success: list[str] | Unset = UNSET
    information: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        success: list[str] | Unset = UNSET
        if not isinstance(self.success, Unset):
            success = self.success

        information: list[str] | Unset = UNSET
        if not isinstance(self.information, Unset):
            information = self.information

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if errors is not UNSET:
            field_dict["errors"] = errors
        if success is not UNSET:
            field_dict["success"] = success
        if information is not UNSET:
            field_dict["information"] = information

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = cast(list[str], d.pop("status", UNSET))

        errors = cast(list[str], d.pop("errors", UNSET))

        success = cast(list[str], d.pop("success", UNSET))

        information = cast(list[str], d.pop("information", UNSET))

        threat_gate_background_messages = cls(
            status=status,
            errors=errors,
            success=success,
            information=information,
        )

        threat_gate_background_messages.additional_properties = d
        return threat_gate_background_messages

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
