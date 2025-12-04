from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_user_timestamp import FWUserTimestamp
    from ..models.nat_addr_port import NATAddrPort


T = TypeVar("T", bound="NATRule")


@_attrs_define
class NATRule:
    """
    Attributes:
        id (str | Unset):
        associated_rule_id (str | Unset):
        created (FWUserTimestamp | Unset):
        descr (str | Unset):
        disabled (bool | Unset):
        destination (NATAddrPort | Unset):
        filter_rule_association (str | Unset):
        interface (str | Unset):
        target (NATAddrPort | Unset):
        natreflection (str | Unset):
        nordr (bool | Unset):
        protocol (str | Unset):
        ipprotocol (str | Unset):
        source (NATAddrPort | Unset):
        updated (FWUserTimestamp | Unset):
        nosync (bool | Unset):
    """

    id: str | Unset = UNSET
    associated_rule_id: str | Unset = UNSET
    created: FWUserTimestamp | Unset = UNSET
    descr: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    destination: NATAddrPort | Unset = UNSET
    filter_rule_association: str | Unset = UNSET
    interface: str | Unset = UNSET
    target: NATAddrPort | Unset = UNSET
    natreflection: str | Unset = UNSET
    nordr: bool | Unset = UNSET
    protocol: str | Unset = UNSET
    ipprotocol: str | Unset = UNSET
    source: NATAddrPort | Unset = UNSET
    updated: FWUserTimestamp | Unset = UNSET
    nosync: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        associated_rule_id = self.associated_rule_id

        created: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        descr = self.descr

        disabled = self.disabled

        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        filter_rule_association = self.filter_rule_association

        interface = self.interface

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        natreflection = self.natreflection

        nordr = self.nordr

        protocol = self.protocol

        ipprotocol = self.ipprotocol

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        updated: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        nosync = self.nosync

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if associated_rule_id is not UNSET:
            field_dict["associated_rule_id"] = associated_rule_id
        if created is not UNSET:
            field_dict["created"] = created
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if destination is not UNSET:
            field_dict["destination"] = destination
        if filter_rule_association is not UNSET:
            field_dict["filter_rule_association"] = filter_rule_association
        if interface is not UNSET:
            field_dict["interface"] = interface
        if target is not UNSET:
            field_dict["target"] = target
        if natreflection is not UNSET:
            field_dict["natreflection"] = natreflection
        if nordr is not UNSET:
            field_dict["nordr"] = nordr
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if source is not UNSET:
            field_dict["source"] = source
        if updated is not UNSET:
            field_dict["updated"] = updated
        if nosync is not UNSET:
            field_dict["nosync"] = nosync

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fw_user_timestamp import FWUserTimestamp
        from ..models.nat_addr_port import NATAddrPort

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        associated_rule_id = d.pop("associated_rule_id", UNSET)

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

        filter_rule_association = d.pop("filter_rule_association", UNSET)

        interface = d.pop("interface", UNSET)

        _target = d.pop("target", UNSET)
        target: NATAddrPort | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = NATAddrPort.from_dict(_target)

        natreflection = d.pop("natreflection", UNSET)

        nordr = d.pop("nordr", UNSET)

        protocol = d.pop("protocol", UNSET)

        ipprotocol = d.pop("ipprotocol", UNSET)

        _source = d.pop("source", UNSET)
        source: NATAddrPort | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NATAddrPort.from_dict(_source)

        _updated = d.pop("updated", UNSET)
        updated: FWUserTimestamp | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = FWUserTimestamp.from_dict(_updated)

        nosync = d.pop("nosync", UNSET)

        nat_rule = cls(
            id=id,
            associated_rule_id=associated_rule_id,
            created=created,
            descr=descr,
            disabled=disabled,
            destination=destination,
            filter_rule_association=filter_rule_association,
            interface=interface,
            target=target,
            natreflection=natreflection,
            nordr=nordr,
            protocol=protocol,
            ipprotocol=ipprotocol,
            source=source,
            updated=updated,
            nosync=nosync,
        )

        nat_rule.additional_properties = d
        return nat_rule

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
