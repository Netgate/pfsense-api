from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSACLNetwork")


@_attrs_define
class DNSACLNetwork:
    """
    Attributes:
        acl_network (Union[Unset, str]):
        mask (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    acl_network: Union[Unset, str] = UNSET
    mask: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        acl_network = self.acl_network

        mask = self.mask

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acl_network is not UNSET:
            field_dict["acl_network"] = acl_network
        if mask is not UNSET:
            field_dict["mask"] = mask
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        acl_network = d.pop("acl_network", UNSET)

        mask = d.pop("mask", UNSET)

        description = d.pop("description", UNSET)

        dnsacl_network = cls(
            acl_network=acl_network,
            mask=mask,
            description=description,
        )

        dnsacl_network.additional_properties = d
        return dnsacl_network

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
