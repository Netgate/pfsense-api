from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mdns_record import MDNSRecord


T = TypeVar("T", bound="MDNSState")


@_attrs_define
class MDNSState:
    """
    Attributes:
        enabled (bool | Unset):
        instance (str | Unset):
        service (str | Unset):
        domain (str | Unset):
        hostname (str | Unset):
        port (int | Unset):
        ips (list[str] | Unset):
        txt (list[str] | Unset):
        records (list[MDNSRecord] | Unset):
    """

    enabled: bool | Unset = UNSET
    instance: str | Unset = UNSET
    service: str | Unset = UNSET
    domain: str | Unset = UNSET
    hostname: str | Unset = UNSET
    port: int | Unset = UNSET
    ips: list[str] | Unset = UNSET
    txt: list[str] | Unset = UNSET
    records: list[MDNSRecord] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        instance = self.instance

        service = self.service

        domain = self.domain

        hostname = self.hostname

        port = self.port

        ips: list[str] | Unset = UNSET
        if not isinstance(self.ips, Unset):
            ips = self.ips

        txt: list[str] | Unset = UNSET
        if not isinstance(self.txt, Unset):
            txt = self.txt

        records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if instance is not UNSET:
            field_dict["instance"] = instance
        if service is not UNSET:
            field_dict["service"] = service
        if domain is not UNSET:
            field_dict["domain"] = domain
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if port is not UNSET:
            field_dict["port"] = port
        if ips is not UNSET:
            field_dict["ips"] = ips
        if txt is not UNSET:
            field_dict["txt"] = txt
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mdns_record import MDNSRecord

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        instance = d.pop("instance", UNSET)

        service = d.pop("service", UNSET)

        domain = d.pop("domain", UNSET)

        hostname = d.pop("hostname", UNSET)

        port = d.pop("port", UNSET)

        ips = cast(list[str], d.pop("ips", UNSET))

        txt = cast(list[str], d.pop("txt", UNSET))

        _records = d.pop("records", UNSET)
        records: list[MDNSRecord] | Unset = UNSET
        if _records is not UNSET:
            records = []
            for records_item_data in _records:
                records_item = MDNSRecord.from_dict(records_item_data)

                records.append(records_item)

        mdns_state = cls(
            enabled=enabled,
            instance=instance,
            service=service,
            domain=domain,
            hostname=hostname,
            port=port,
            ips=ips,
            txt=txt,
            records=records,
        )

        mdns_state.additional_properties = d
        return mdns_state

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
