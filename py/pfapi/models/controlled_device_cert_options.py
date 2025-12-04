from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControlledDeviceCertOptions")


@_attrs_define
class ControlledDeviceCertOptions:
    """
    Attributes:
        organization (str | Unset):
        country (str | Unset):
        province (str | Unset):
        locality (str | Unset):
        street_addr (str | Unset):
        postal_code (str | Unset):
        ip_addresses (list[str] | Unset):
        expiry_days (int | Unset):
    """

    organization: str | Unset = UNSET
    country: str | Unset = UNSET
    province: str | Unset = UNSET
    locality: str | Unset = UNSET
    street_addr: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    ip_addresses: list[str] | Unset = UNSET
    expiry_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization = self.organization

        country = self.country

        province = self.province

        locality = self.locality

        street_addr = self.street_addr

        postal_code = self.postal_code

        ip_addresses: list[str] | Unset = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = self.ip_addresses

        expiry_days = self.expiry_days

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization = d.pop("organization", UNSET)

        country = d.pop("country", UNSET)

        province = d.pop("province", UNSET)

        locality = d.pop("locality", UNSET)

        street_addr = d.pop("street_addr", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        ip_addresses = cast(list[str], d.pop("ip_addresses", UNSET))

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
