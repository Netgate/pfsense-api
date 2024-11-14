from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_high_availability_config import DhcpHighAvailabilityConfig
    from ..models.dhcp_service_config_interfaces import DhcpServiceConfigInterfaces


T = TypeVar("T", bound="DhcpServiceConfig")


@_attrs_define
class DhcpServiceConfig:
    """Per IP version DHCP service setting

    Attributes:
        high_availability (Union[Unset, DhcpHighAvailabilityConfig]): High-availability configuration for Kea DHCP
            service.
        dns_reg (Union[Unset, bool]):
        early_dns_reg (Union[Unset, bool]):
        interfaces (Union[Unset, DhcpServiceConfigInterfaces]):
    """

    high_availability: Union[Unset, "DhcpHighAvailabilityConfig"] = UNSET
    dns_reg: Union[Unset, bool] = UNSET
    early_dns_reg: Union[Unset, bool] = UNSET
    interfaces: Union[Unset, "DhcpServiceConfigInterfaces"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        high_availability: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.high_availability, Unset):
            high_availability = self.high_availability.to_dict()

        dns_reg = self.dns_reg

        early_dns_reg = self.early_dns_reg

        interfaces: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if high_availability is not UNSET:
            field_dict["high_availability"] = high_availability
        if dns_reg is not UNSET:
            field_dict["dns_reg"] = dns_reg
        if early_dns_reg is not UNSET:
            field_dict["early_dns_reg"] = early_dns_reg
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dhcp_high_availability_config import DhcpHighAvailabilityConfig
        from ..models.dhcp_service_config_interfaces import DhcpServiceConfigInterfaces

        d = src_dict.copy()
        _high_availability = d.pop("high_availability", UNSET)
        high_availability: Union[Unset, DhcpHighAvailabilityConfig]
        if isinstance(_high_availability, Unset):
            high_availability = UNSET
        else:
            high_availability = DhcpHighAvailabilityConfig.from_dict(_high_availability)

        dns_reg = d.pop("dns_reg", UNSET)

        early_dns_reg = d.pop("early_dns_reg", UNSET)

        _interfaces = d.pop("interfaces", UNSET)
        interfaces: Union[Unset, DhcpServiceConfigInterfaces]
        if isinstance(_interfaces, Unset):
            interfaces = UNSET
        else:
            interfaces = DhcpServiceConfigInterfaces.from_dict(_interfaces)

        dhcp_service_config = cls(
            high_availability=high_availability,
            dns_reg=dns_reg,
            early_dns_reg=early_dns_reg,
            interfaces=interfaces,
        )

        dhcp_service_config.additional_properties = d
        return dhcp_service_config

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
