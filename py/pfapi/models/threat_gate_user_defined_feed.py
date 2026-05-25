from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.threat_class import ThreatClass


T = TypeVar("T", bound="ThreatGateUserDefinedFeed")


@_attrs_define
class ThreatGateUserDefinedFeed:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        enabled (bool | Unset):
        mode (str | Unset): block, alias
        threat_class (ThreatClass | Unset):
        cidrs (list[str] | Unset):
        domains (list[str] | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    mode: str | Unset = UNSET
    threat_class: ThreatClass | Unset = UNSET
    cidrs: list[str] | Unset = UNSET
    domains: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        enabled = self.enabled

        mode = self.mode

        threat_class: dict[str, Any] | Unset = UNSET
        if not isinstance(self.threat_class, Unset):
            threat_class = self.threat_class.to_dict()

        cidrs: list[str] | Unset = UNSET
        if not isinstance(self.cidrs, Unset):
            cidrs = self.cidrs

        domains: list[str] | Unset = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if mode is not UNSET:
            field_dict["mode"] = mode
        if threat_class is not UNSET:
            field_dict["threatClass"] = threat_class
        if cidrs is not UNSET:
            field_dict["cidrs"] = cidrs
        if domains is not UNSET:
            field_dict["domains"] = domains

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.threat_class import ThreatClass

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        mode = d.pop("mode", UNSET)

        _threat_class = d.pop("threatClass", UNSET)
        threat_class: ThreatClass | Unset
        if isinstance(_threat_class, Unset):
            threat_class = UNSET
        else:
            threat_class = ThreatClass.from_dict(_threat_class)

        cidrs = cast(list[str], d.pop("cidrs", UNSET))

        domains = cast(list[str], d.pop("domains", UNSET))

        threat_gate_user_defined_feed = cls(
            id=id,
            name=name,
            enabled=enabled,
            mode=mode,
            threat_class=threat_class,
            cidrs=cidrs,
            domains=domains,
        )

        threat_gate_user_defined_feed.additional_properties = d
        return threat_gate_user_defined_feed

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
