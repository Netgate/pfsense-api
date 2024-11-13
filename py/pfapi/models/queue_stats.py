from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueStats")


@_attrs_define
class QueueStats:
    """
    Attributes:
        name (Union[Unset, str]):
        interface (Union[Unset, str]):
        shapertype (Union[Unset, str]):
        contains (Union[Unset, List[str]]):
        pkts (Union[Unset, str]):
        bytes_ (Union[Unset, str]):
        droppedpkts (Union[Unset, str]):
        droppedbytes (Union[Unset, str]):
        qlengthitems (Union[Unset, str]):
        qlengthsize (Union[Unset, str]):
        borrows (Union[Unset, str]):
        suspends (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    shapertype: Union[Unset, str] = UNSET
    contains: Union[Unset, List[str]] = UNSET
    pkts: Union[Unset, str] = UNSET
    bytes_: Union[Unset, str] = UNSET
    droppedpkts: Union[Unset, str] = UNSET
    droppedbytes: Union[Unset, str] = UNSET
    qlengthitems: Union[Unset, str] = UNSET
    qlengthsize: Union[Unset, str] = UNSET
    borrows: Union[Unset, str] = UNSET
    suspends: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        interface = self.interface

        shapertype = self.shapertype

        contains: Union[Unset, List[str]] = UNSET
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

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        interface = d.pop("interface", UNSET)

        shapertype = d.pop("shapertype", UNSET)

        contains = cast(List[str], d.pop("contains", UNSET))

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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
