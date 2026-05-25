from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.threat_gate_max_mind import ThreatGateMaxMind


T = TypeVar("T", bound="ThreatGateConfiguration")


@_attrs_define
class ThreatGateConfiguration:
    """
    Attributes:
        enable (bool | Unset):
        refresh_interval (str | Unset):
        maxmind (ThreatGateMaxMind | Unset):
    """

    enable: bool | Unset = UNSET
    refresh_interval: str | Unset = UNSET
    maxmind: ThreatGateMaxMind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        refresh_interval = self.refresh_interval

        maxmind: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maxmind, Unset):
            maxmind = self.maxmind.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if refresh_interval is not UNSET:
            field_dict["refresh_interval"] = refresh_interval
        if maxmind is not UNSET:
            field_dict["maxmind"] = maxmind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.threat_gate_max_mind import ThreatGateMaxMind

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        refresh_interval = d.pop("refresh_interval", UNSET)

        _maxmind = d.pop("maxmind", UNSET)
        maxmind: ThreatGateMaxMind | Unset
        if isinstance(_maxmind, Unset):
            maxmind = UNSET
        else:
            maxmind = ThreatGateMaxMind.from_dict(_maxmind)

        threat_gate_configuration = cls(
            enable=enable,
            refresh_interval=refresh_interval,
            maxmind=maxmind,
        )

        threat_gate_configuration.additional_properties = d
        return threat_gate_configuration

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
