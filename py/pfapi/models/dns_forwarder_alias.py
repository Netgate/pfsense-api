from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSForwarderAlias")


@_attrs_define
class DNSForwarderAlias:
    """
    Attributes:
        host (Union[Unset, str]):
        domain (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    host: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host

        domain = self.domain

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if domain is not UNSET:
            field_dict["domain"] = domain
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host", UNSET)

        domain = d.pop("domain", UNSET)

        description = d.pop("description", UNSET)

        dns_forwarder_alias = cls(
            host=host,
            domain=domain,
            description=description,
        )

        dns_forwarder_alias.additional_properties = d
        return dns_forwarder_alias

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
