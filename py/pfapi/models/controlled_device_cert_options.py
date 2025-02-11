from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControlledDeviceCertOptions")


@_attrs_define
class ControlledDeviceCertOptions:
    """
    Attributes:
        organization (str):
        country (str):
        province (str):
        locality (str):
        street_addr (str):
        postal_code (str):
        ip_addresses (List[str]):
        expiry_days (int):
    """

    organization: str
    country: str
    province: str
    locality: str
    street_addr: str
    postal_code: str
    ip_addresses: List[str]
    expiry_days: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization = self.organization

        country = self.country

        province = self.province

        locality = self.locality

        street_addr = self.street_addr

        postal_code = self.postal_code

        ip_addresses = self.ip_addresses

        expiry_days = self.expiry_days

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization": organization,
                "country": country,
                "province": province,
                "locality": locality,
                "street_addr": street_addr,
                "postal_code": postal_code,
                "ip_addresses": ip_addresses,
                "expiry_days": expiry_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organization = d.pop("organization")

        country = d.pop("country")

        province = d.pop("province")

        locality = d.pop("locality")

        street_addr = d.pop("street_addr")

        postal_code = d.pop("postal_code")

        ip_addresses = cast(List[str], d.pop("ip_addresses"))

        expiry_days = d.pop("expiry_days")

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
