from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_global_settings import DhcpGlobalSettings
    from ..models.dhcp_service_config import DhcpServiceConfig


T = TypeVar("T", bound="DhcpdConfig")


@_attrs_define
class DhcpdConfig:
    """
    Attributes:
        service (Union[Unset, DhcpGlobalSettings]):
        dhcpd (Union[Unset, DhcpServiceConfig]): Per IP version DHCP service setting
        dhcpdv6 (Union[Unset, DhcpServiceConfig]): Per IP version DHCP service setting
    """

    service: Union[Unset, "DhcpGlobalSettings"] = UNSET
    dhcpd: Union[Unset, "DhcpServiceConfig"] = UNSET
    dhcpdv6: Union[Unset, "DhcpServiceConfig"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.to_dict()

        dhcpd: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dhcpd, Unset):
            dhcpd = self.dhcpd.to_dict()

        dhcpdv6: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dhcpdv6, Unset):
            dhcpdv6 = self.dhcpdv6.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service is not UNSET:
            field_dict["service"] = service
        if dhcpd is not UNSET:
            field_dict["dhcpd"] = dhcpd
        if dhcpdv6 is not UNSET:
            field_dict["dhcpdv6"] = dhcpdv6

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dhcp_global_settings import DhcpGlobalSettings
        from ..models.dhcp_service_config import DhcpServiceConfig

        d = src_dict.copy()
        _service = d.pop("service", UNSET)
        service: Union[Unset, DhcpGlobalSettings]
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = DhcpGlobalSettings.from_dict(_service)

        _dhcpd = d.pop("dhcpd", UNSET)
        dhcpd: Union[Unset, DhcpServiceConfig]
        if isinstance(_dhcpd, Unset):
            dhcpd = UNSET
        else:
            dhcpd = DhcpServiceConfig.from_dict(_dhcpd)

        _dhcpdv6 = d.pop("dhcpdv6", UNSET)
        dhcpdv6: Union[Unset, DhcpServiceConfig]
        if isinstance(_dhcpdv6, Unset):
            dhcpdv6 = UNSET
        else:
            dhcpdv6 = DhcpServiceConfig.from_dict(_dhcpdv6)

        dhcpd_config = cls(
            service=service,
            dhcpd=dhcpd,
            dhcpdv6=dhcpdv6,
        )

        dhcpd_config.additional_properties = d
        return dhcpd_config

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
