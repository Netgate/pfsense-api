from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceGatewayUpdate")


@_attrs_define
class InterfaceGatewayUpdate:
    """
    Attributes:
        gateway (Union[Unset, str]): name of IPv4 gateway
        gatewayv6 (Union[Unset, str]): name of IPv6 gateway
    """

    gateway: Union[Unset, str] = UNSET
    gatewayv6: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gateway = self.gateway

        gatewayv6 = self.gatewayv6

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if gatewayv6 is not UNSET:
            field_dict["gatewayv6"] = gatewayv6

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gateway = d.pop("gateway", UNSET)

        gatewayv6 = d.pop("gatewayv6", UNSET)

        interface_gateway_update = cls(
            gateway=gateway,
            gatewayv6=gatewayv6,
        )

        interface_gateway_update.additional_properties = d
        return interface_gateway_update

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
