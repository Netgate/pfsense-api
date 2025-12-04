from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_user_timestamp import FWUserTimestamp
    from ..models.nat_addr_port import NATAddrPort


T = TypeVar("T", bound="NATOutboundRule")


@_attrs_define
class NATOutboundRule:
    """
    Attributes:
        created (FWUserTimestamp | Unset):
        descr (str | Unset):
        disabled (bool | Unset):
        destination (NATAddrPort | Unset):
        id (str | Unset):
        interface (str | Unset):
        ipprotocol (str | Unset):
        nonat (bool | Unset):
        nosync (bool | Unset):
        protocol (str | Unset):
        poolopts (str | Unset):
        source (NATAddrPort | Unset):
        source_hash_key (str | Unset):
        staticnatport (bool | Unset):
        target (NATAddrPort | Unset):
        updated (FWUserTimestamp | Unset):
    """

    created: FWUserTimestamp | Unset = UNSET
    descr: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    destination: NATAddrPort | Unset = UNSET
    id: str | Unset = UNSET
    interface: str | Unset = UNSET
    ipprotocol: str | Unset = UNSET
    nonat: bool | Unset = UNSET
    nosync: bool | Unset = UNSET
    protocol: str | Unset = UNSET
    poolopts: str | Unset = UNSET
    source: NATAddrPort | Unset = UNSET
    source_hash_key: str | Unset = UNSET
    staticnatport: bool | Unset = UNSET
    target: NATAddrPort | Unset = UNSET
    updated: FWUserTimestamp | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        descr = self.descr

        disabled = self.disabled

        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        id = self.id

        interface = self.interface

        ipprotocol = self.ipprotocol

        nonat = self.nonat

        nosync = self.nosync

        protocol = self.protocol

        poolopts = self.poolopts

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        source_hash_key = self.source_hash_key

        staticnatport = self.staticnatport

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        updated: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if destination is not UNSET:
            field_dict["destination"] = destination
        if id is not UNSET:
            field_dict["id"] = id
        if interface is not UNSET:
            field_dict["interface"] = interface
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if nonat is not UNSET:
            field_dict["nonat"] = nonat
        if nosync is not UNSET:
            field_dict["nosync"] = nosync
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if poolopts is not UNSET:
            field_dict["poolopts"] = poolopts
        if source is not UNSET:
            field_dict["source"] = source
        if source_hash_key is not UNSET:
            field_dict["source-hash-key"] = source_hash_key
        if staticnatport is not UNSET:
            field_dict["staticnatport"] = staticnatport
        if target is not UNSET:
            field_dict["target"] = target
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fw_user_timestamp import FWUserTimestamp
        from ..models.nat_addr_port import NATAddrPort

        d = dict(src_dict)
        _created = d.pop("created", UNSET)
        created: FWUserTimestamp | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = FWUserTimestamp.from_dict(_created)

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        _destination = d.pop("destination", UNSET)
        destination: NATAddrPort | Unset
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = NATAddrPort.from_dict(_destination)

        id = d.pop("id", UNSET)

        interface = d.pop("interface", UNSET)

        ipprotocol = d.pop("ipprotocol", UNSET)

        nonat = d.pop("nonat", UNSET)

        nosync = d.pop("nosync", UNSET)

        protocol = d.pop("protocol", UNSET)

        poolopts = d.pop("poolopts", UNSET)

        _source = d.pop("source", UNSET)
        source: NATAddrPort | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NATAddrPort.from_dict(_source)

        source_hash_key = d.pop("source-hash-key", UNSET)

        staticnatport = d.pop("staticnatport", UNSET)

        _target = d.pop("target", UNSET)
        target: NATAddrPort | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = NATAddrPort.from_dict(_target)

        _updated = d.pop("updated", UNSET)
        updated: FWUserTimestamp | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = FWUserTimestamp.from_dict(_updated)

        nat_outbound_rule = cls(
            created=created,
            descr=descr,
            disabled=disabled,
            destination=destination,
            id=id,
            interface=interface,
            ipprotocol=ipprotocol,
            nonat=nonat,
            nosync=nosync,
            protocol=protocol,
            poolopts=poolopts,
            source=source,
            source_hash_key=source_hash_key,
            staticnatport=staticnatport,
            target=target,
            updated=updated,
        )

        nat_outbound_rule.additional_properties = d
        return nat_outbound_rule

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
