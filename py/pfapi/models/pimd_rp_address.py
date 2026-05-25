from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PimdRpAddress")


@_attrs_define
class PimdRpAddress:
    """
    Attributes:
        address (str | Unset): RP Address

            Static rendezvous point (RP) for a given group, or range or groups, to bypass elections.
            May be a unicast address or multicast group.
            All static RP entries are advertised with a priority of 1.
        descr (str | Unset): Description
        mcgroup (str | Unset): Multicast Group

            Optional group address and prefix for this static RP.
            Default group is 224.0.0.0/16.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    address: str | Unset = UNSET
    descr: str | Unset = UNSET
    mcgroup: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        descr = self.descr

        mcgroup = self.mcgroup

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if descr is not UNSET:
            field_dict["descr"] = descr
        if mcgroup is not UNSET:
            field_dict["mcgroup"] = mcgroup
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        descr = d.pop("descr", UNSET)

        mcgroup = d.pop("mcgroup", UNSET)

        id = d.pop("id", UNSET)

        pimd_rp_address = cls(
            address=address,
            descr=descr,
            mcgroup=mcgroup,
            id=id,
        )

        pimd_rp_address.additional_properties = d
        return pimd_rp_address

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
