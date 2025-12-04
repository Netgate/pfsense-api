from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nat_auto_addr import NATAutoAddr


T = TypeVar("T", bound="NATAutoRule")


@_attrs_define
class NATAutoRule:
    """
    Attributes:
        id (str | Unset):
        interface (str | Unset):
        dstport (str | Unset):
        target (str | Unset):
        destination (NATAutoAddr | Unset):
        dstaddr (str | Unset):
        source (NATAutoAddr | Unset):
        dstany (bool | Unset):
        srcany (bool | Unset):
        srcaddr (str | Unset):
        staticnatport (bool | Unset):
        descr (str | Unset):
    """

    id: str | Unset = UNSET
    interface: str | Unset = UNSET
    dstport: str | Unset = UNSET
    target: str | Unset = UNSET
    destination: NATAutoAddr | Unset = UNSET
    dstaddr: str | Unset = UNSET
    source: NATAutoAddr | Unset = UNSET
    dstany: bool | Unset = UNSET
    srcany: bool | Unset = UNSET
    srcaddr: str | Unset = UNSET
    staticnatport: bool | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        interface = self.interface

        dstport = self.dstport

        target = self.target

        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        dstaddr = self.dstaddr

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        dstany = self.dstany

        srcany = self.srcany

        srcaddr = self.srcaddr

        staticnatport = self.staticnatport

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if interface is not UNSET:
            field_dict["interface"] = interface
        if dstport is not UNSET:
            field_dict["dstport"] = dstport
        if target is not UNSET:
            field_dict["target"] = target
        if destination is not UNSET:
            field_dict["destination"] = destination
        if dstaddr is not UNSET:
            field_dict["dstaddr"] = dstaddr
        if source is not UNSET:
            field_dict["source"] = source
        if dstany is not UNSET:
            field_dict["dstany"] = dstany
        if srcany is not UNSET:
            field_dict["srcany"] = srcany
        if srcaddr is not UNSET:
            field_dict["srcaddr"] = srcaddr
        if staticnatport is not UNSET:
            field_dict["staticnatport"] = staticnatport
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nat_auto_addr import NATAutoAddr

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        interface = d.pop("interface", UNSET)

        dstport = d.pop("dstport", UNSET)

        target = d.pop("target", UNSET)

        _destination = d.pop("destination", UNSET)
        destination: NATAutoAddr | Unset
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = NATAutoAddr.from_dict(_destination)

        dstaddr = d.pop("dstaddr", UNSET)

        _source = d.pop("source", UNSET)
        source: NATAutoAddr | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NATAutoAddr.from_dict(_source)

        dstany = d.pop("dstany", UNSET)

        srcany = d.pop("srcany", UNSET)

        srcaddr = d.pop("srcaddr", UNSET)

        staticnatport = d.pop("staticnatport", UNSET)

        descr = d.pop("descr", UNSET)

        nat_auto_rule = cls(
            id=id,
            interface=interface,
            dstport=dstport,
            target=target,
            destination=destination,
            dstaddr=dstaddr,
            source=source,
            dstany=dstany,
            srcany=srcany,
            srcaddr=srcaddr,
            staticnatport=staticnatport,
            descr=descr,
        )

        nat_auto_rule.additional_properties = d
        return nat_auto_rule

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
