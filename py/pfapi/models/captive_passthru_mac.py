from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptivePassthruMac")


@_attrs_define
class CaptivePassthruMac:
    """
    Attributes:
        action (str | Unset):
        mac (str | Unset):
        bw_up (str | Unset):
        bw_down (str | Unset):
        descr (str | Unset):
    """

    action: str | Unset = UNSET
    mac: str | Unset = UNSET
    bw_up: str | Unset = UNSET
    bw_down: str | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        mac = self.mac

        bw_up = self.bw_up

        bw_down = self.bw_down

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if mac is not UNSET:
            field_dict["mac"] = mac
        if bw_up is not UNSET:
            field_dict["bw_up"] = bw_up
        if bw_down is not UNSET:
            field_dict["bw_down"] = bw_down
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        mac = d.pop("mac", UNSET)

        bw_up = d.pop("bw_up", UNSET)

        bw_down = d.pop("bw_down", UNSET)

        descr = d.pop("descr", UNSET)

        captive_passthru_mac = cls(
            action=action,
            mac=mac,
            bw_up=bw_up,
            bw_down=bw_down,
            descr=descr,
        )

        captive_passthru_mac.additional_properties = d
        return captive_passthru_mac

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
