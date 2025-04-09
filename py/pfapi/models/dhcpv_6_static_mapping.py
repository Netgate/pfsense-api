from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dhcpv6StaticMapping")


@_attrs_define
class Dhcpv6StaticMapping:
    """
    Attributes:
        id (Union[Unset, str]): read-only (index)
        backend (Union[Unset, str]): read-only
        duid (Union[Unset, str]):
        ipv6_address (Union[Unset, str]):
        hostname (Union[Unset, str]):
        description (Union[Unset, str]):
        early_dns_reg (Union[Unset, str]): default (track) | enable | disable
    """

    id: Union[Unset, str] = UNSET
    backend: Union[Unset, str] = UNSET
    duid: Union[Unset, str] = UNSET
    ipv6_address: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    early_dns_reg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        backend = self.backend

        duid = self.duid

        ipv6_address = self.ipv6_address

        hostname = self.hostname

        description = self.description

        early_dns_reg = self.early_dns_reg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if backend is not UNSET:
            field_dict["backend"] = backend
        if duid is not UNSET:
            field_dict["duid"] = duid
        if ipv6_address is not UNSET:
            field_dict["ipv6_address"] = ipv6_address
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if description is not UNSET:
            field_dict["description"] = description
        if early_dns_reg is not UNSET:
            field_dict["early_dns_reg"] = early_dns_reg

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        backend = d.pop("backend", UNSET)

        duid = d.pop("duid", UNSET)

        ipv6_address = d.pop("ipv6_address", UNSET)

        hostname = d.pop("hostname", UNSET)

        description = d.pop("description", UNSET)

        early_dns_reg = d.pop("early_dns_reg", UNSET)

        dhcpv_6_static_mapping = cls(
            id=id,
            backend=backend,
            duid=duid,
            ipv6_address=ipv6_address,
            hostname=hostname,
            description=description,
            early_dns_reg=early_dns_reg,
        )

        dhcpv_6_static_mapping.additional_properties = d
        return dhcpv_6_static_mapping

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
