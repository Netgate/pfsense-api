from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dnsacl_network import DNSACLNetwork


T = TypeVar("T", bound="DNSACL")


@_attrs_define
class DNSACL:
    """
    Attributes:
        aclid (str):
        aclname (str):
        aclaction (str | Unset):
        description (str | Unset):
        row (list[DNSACLNetwork] | Unset):
    """

    aclid: str
    aclname: str
    aclaction: str | Unset = UNSET
    description: str | Unset = UNSET
    row: list[DNSACLNetwork] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aclid = self.aclid

        aclname = self.aclname

        aclaction = self.aclaction

        description = self.description

        row: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aclid": aclid,
                "aclname": aclname,
            }
        )
        if aclaction is not UNSET:
            field_dict["aclaction"] = aclaction
        if description is not UNSET:
            field_dict["description"] = description
        if row is not UNSET:
            field_dict["row"] = row

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dnsacl_network import DNSACLNetwork

        d = dict(src_dict)
        aclid = d.pop("aclid")

        aclname = d.pop("aclname")

        aclaction = d.pop("aclaction", UNSET)

        description = d.pop("description", UNSET)

        _row = d.pop("row", UNSET)
        row: list[DNSACLNetwork] | Unset = UNSET
        if _row is not UNSET:
            row = []
            for row_item_data in _row:
                row_item = DNSACLNetwork.from_dict(row_item_data)

                row.append(row_item)

        dnsacl = cls(
            aclid=aclid,
            aclname=aclname,
            aclaction=aclaction,
            description=description,
            row=row,
        )

        dnsacl.additional_properties = d
        return dnsacl

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
