from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueStats")


@_attrs_define
class QueueStats:
    """
    Attributes:
        name (str):
        interface (str):
        shapertype (str):
        pkts (str):
        bytes_ (str):
        droppedpkts (str):
        droppedbytes (str):
        qlengthitems (str):
        qlengthsize (str):
        borrows (str):
        suspends (str):
        contains (Union[Unset, List[str]]):
    """

    name: str
    interface: str
    shapertype: str
    pkts: str
    bytes_: str
    droppedpkts: str
    droppedbytes: str
    qlengthitems: str
    qlengthsize: str
    borrows: str
    suspends: str
    contains: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        interface = self.interface

        shapertype = self.shapertype

        pkts = self.pkts

        bytes_ = self.bytes_

        droppedpkts = self.droppedpkts

        droppedbytes = self.droppedbytes

        qlengthitems = self.qlengthitems

        qlengthsize = self.qlengthsize

        borrows = self.borrows

        suspends = self.suspends

        contains: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contains, Unset):
            contains = self.contains

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "interface": interface,
                "shapertype": shapertype,
                "pkts": pkts,
                "bytes": bytes_,
                "droppedpkts": droppedpkts,
                "droppedbytes": droppedbytes,
                "qlengthitems": qlengthitems,
                "qlengthsize": qlengthsize,
                "borrows": borrows,
                "suspends": suspends,
            }
        )
        if contains is not UNSET:
            field_dict["contains"] = contains

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        interface = d.pop("interface")

        shapertype = d.pop("shapertype")

        pkts = d.pop("pkts")

        bytes_ = d.pop("bytes")

        droppedpkts = d.pop("droppedpkts")

        droppedbytes = d.pop("droppedbytes")

        qlengthitems = d.pop("qlengthitems")

        qlengthsize = d.pop("qlengthsize")

        borrows = d.pop("borrows")

        suspends = d.pop("suspends")

        contains = cast(List[str], d.pop("contains", UNSET))

        queue_stats = cls(
            name=name,
            interface=interface,
            shapertype=shapertype,
            pkts=pkts,
            bytes_=bytes_,
            droppedpkts=droppedpkts,
            droppedbytes=droppedbytes,
            qlengthitems=qlengthitems,
            qlengthsize=qlengthsize,
            borrows=borrows,
            suspends=suspends,
            contains=contains,
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
