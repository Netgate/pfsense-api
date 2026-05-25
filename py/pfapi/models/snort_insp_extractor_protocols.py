from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspExtractorProtocols")


@_attrs_define
class SnortInspExtractorProtocols:
    """
    Attributes:
        service (str | Unset): service to extract from { http | ftp | conn | dns | weird | notice }
        tenant_id (int | Unset): tenant_id of target tenant { 0:max32 }; default 0
        on_events (str | Unset): specify events to log
        fields (str | Unset): specify fields to log
    """

    service: str | Unset = UNSET
    tenant_id: int | Unset = UNSET
    on_events: str | Unset = UNSET
    fields: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service = self.service

        tenant_id = self.tenant_id

        on_events = self.on_events

        fields = self.fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service is not UNSET:
            field_dict["service"] = service
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if on_events is not UNSET:
            field_dict["on_events"] = on_events
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service = d.pop("service", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        on_events = d.pop("on_events", UNSET)

        fields = d.pop("fields", UNSET)

        snort_insp_extractor_protocols = cls(
            service=service,
            tenant_id=tenant_id,
            on_events=on_events,
            fields=fields,
        )

        snort_insp_extractor_protocols.additional_properties = d
        return snort_insp_extractor_protocols

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
