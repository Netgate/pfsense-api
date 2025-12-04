from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSACLNetwork")


@_attrs_define
class DNSACLNetwork:
    """
    Attributes:
        acl_network (str):
        mask (str):
        description (str | Unset):
    """

    acl_network: str
    mask: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acl_network = self.acl_network

        mask = self.mask

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acl_network": acl_network,
                "mask": mask,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acl_network = d.pop("acl_network")

        mask = d.pop("mask")

        description = d.pop("description", UNSET)

        dnsacl_network = cls(
            acl_network=acl_network,
            mask=mask,
            description=description,
        )

        dnsacl_network.additional_properties = d
        return dnsacl_network

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
