from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueStats")


@_attrs_define
class QueueStats:
    """
    Attributes:
        name (str | Unset):
        interface (str | Unset):
        shapertype (str | Unset):
        contains (list[str] | Unset):
        pkts (str | Unset):
        bytes_ (str | Unset):
        droppedpkts (str | Unset):
        droppedbytes (str | Unset):
        qlengthitems (str | Unset):
        qlengthsize (str | Unset):
        borrows (str | Unset):
        suspends (str | Unset):
    """

    name: str | Unset = UNSET
    interface: str | Unset = UNSET
    shapertype: str | Unset = UNSET
    contains: list[str] | Unset = UNSET
    pkts: str | Unset = UNSET
    bytes_: str | Unset = UNSET
    droppedpkts: str | Unset = UNSET
    droppedbytes: str | Unset = UNSET
    qlengthitems: str | Unset = UNSET
    qlengthsize: str | Unset = UNSET
    borrows: str | Unset = UNSET
    suspends: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        interface = self.interface

        shapertype = self.shapertype

        contains: list[str] | Unset = UNSET
        if not isinstance(self.contains, Unset):
            contains = self.contains

        pkts = self.pkts

        bytes_ = self.bytes_

        droppedpkts = self.droppedpkts

        droppedbytes = self.droppedbytes

        qlengthitems = self.qlengthitems

        qlengthsize = self.qlengthsize

        borrows = self.borrows

        suspends = self.suspends

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if interface is not UNSET:
            field_dict["interface"] = interface
        if shapertype is not UNSET:
            field_dict["shapertype"] = shapertype
        if contains is not UNSET:
            field_dict["contains"] = contains
        if pkts is not UNSET:
            field_dict["pkts"] = pkts
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if droppedpkts is not UNSET:
            field_dict["droppedpkts"] = droppedpkts
        if droppedbytes is not UNSET:
            field_dict["droppedbytes"] = droppedbytes
        if qlengthitems is not UNSET:
            field_dict["qlengthitems"] = qlengthitems
        if qlengthsize is not UNSET:
            field_dict["qlengthsize"] = qlengthsize
        if borrows is not UNSET:
            field_dict["borrows"] = borrows
        if suspends is not UNSET:
            field_dict["suspends"] = suspends

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        interface = d.pop("interface", UNSET)

        shapertype = d.pop("shapertype", UNSET)

        contains = cast(list[str], d.pop("contains", UNSET))

        pkts = d.pop("pkts", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        droppedpkts = d.pop("droppedpkts", UNSET)

        droppedbytes = d.pop("droppedbytes", UNSET)

        qlengthitems = d.pop("qlengthitems", UNSET)

        qlengthsize = d.pop("qlengthsize", UNSET)

        borrows = d.pop("borrows", UNSET)

        suspends = d.pop("suspends", UNSET)

        queue_stats = cls(
            name=name,
            interface=interface,
            shapertype=shapertype,
            contains=contains,
            pkts=pkts,
            bytes_=bytes_,
            droppedpkts=droppedpkts,
            droppedbytes=droppedbytes,
            qlengthitems=qlengthitems,
            qlengthsize=qlengthsize,
            borrows=borrows,
            suspends=suspends,
        )

        queue_stats.additional_properties = d
        return queue_stats

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
