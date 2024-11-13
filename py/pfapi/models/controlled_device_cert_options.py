from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControlledDeviceCertOptions")


@_attrs_define
class ControlledDeviceCertOptions:
    """
    Attributes:
        organization (Union[Unset, str]):
        country (Union[Unset, str]):
        province (Union[Unset, str]):
        locality (Union[Unset, str]):
        street_addr (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        ip_addresses (Union[Unset, List[str]]):
        expiry_days (Union[Unset, int]):
    """

    organization: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    province: Union[Unset, str] = UNSET
    locality: Union[Unset, str] = UNSET
    street_addr: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    ip_addresses: Union[Unset, List[str]] = UNSET
    expiry_days: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization = self.organization

        country = self.country

        province = self.province

        locality = self.locality

        street_addr = self.street_addr

        postal_code = self.postal_code

        ip_addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = self.ip_addresses

        expiry_days = self.expiry_days

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization is not UNSET:
            field_dict["organization"] = organization
        if country is not UNSET:
            field_dict["country"] = country
        if province is not UNSET:
            field_dict["province"] = province
        if locality is not UNSET:
            field_dict["locality"] = locality
        if street_addr is not UNSET:
            field_dict["street_addr"] = street_addr
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if ip_addresses is not UNSET:
            field_dict["ip_addresses"] = ip_addresses
        if expiry_days is not UNSET:
            field_dict["expiry_days"] = expiry_days

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organization = d.pop("organization", UNSET)

        country = d.pop("country", UNSET)

        province = d.pop("province", UNSET)

        locality = d.pop("locality", UNSET)

        street_addr = d.pop("street_addr", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        ip_addresses = cast(List[str], d.pop("ip_addresses", UNSET))

        expiry_days = d.pop("expiry_days", UNSET)

        controlled_device_cert_options = cls(
            organization=organization,
            country=country,
            province=province,
            locality=locality,
            street_addr=street_addr,
            postal_code=postal_code,
            ip_addresses=ip_addresses,
            expiry_days=expiry_days,
        )

        controlled_device_cert_options.additional_properties = d
        return controlled_device_cert_options

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
