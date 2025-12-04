from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecWidgetTunnel")


@_attrs_define
class IPSecWidgetTunnel:
    """
    Attributes:
        source (str | Unset):
        destination (str | Unset):
        description (str | Unset):
        status (str | Unset):
    """

    source: str | Unset = UNSET
    destination: str | Unset = UNSET
    description: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        destination = self.destination

        description = self.description

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if destination is not UNSET:
            field_dict["destination"] = destination
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source", UNSET)

        destination = d.pop("destination", UNSET)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        ip_sec_widget_tunnel = cls(
            source=source,
            destination=destination,
            description=description,
            status=status,
        )

        ip_sec_widget_tunnel.additional_properties = d
        return ip_sec_widget_tunnel

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
