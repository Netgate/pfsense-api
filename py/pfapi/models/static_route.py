from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaticRoute")


@_attrs_define
class StaticRoute:
    """
    Attributes:
        network (Union[Unset, str]):
        network_encoded (Union[Unset, str]):
        gateway (Union[Unset, str]):
        gateway_encoded (Union[Unset, str]):
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        interface (Union[Unset, str]):
    """

    network: Union[Unset, str] = UNSET
    network_encoded: Union[Unset, str] = UNSET
    gateway: Union[Unset, str] = UNSET
    gateway_encoded: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    interface: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        network = self.network

        network_encoded = self.network_encoded

        gateway = self.gateway

        gateway_encoded = self.gateway_encoded

        descr = self.descr

        disabled = self.disabled

        interface = self.interface

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network is not UNSET:
            field_dict["network"] = network
        if network_encoded is not UNSET:
            field_dict["network_encoded"] = network_encoded
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if gateway_encoded is not UNSET:
            field_dict["gateway_encoded"] = gateway_encoded
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if interface is not UNSET:
            field_dict["interface"] = interface

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        network = d.pop("network", UNSET)

        network_encoded = d.pop("network_encoded", UNSET)

        gateway = d.pop("gateway", UNSET)

        gateway_encoded = d.pop("gateway_encoded", UNSET)

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        interface = d.pop("interface", UNSET)

        static_route = cls(
            network=network,
            network_encoded=network_encoded,
            gateway=gateway,
            gateway_encoded=gateway_encoded,
            descr=descr,
            disabled=disabled,
            interface=interface,
        )

        static_route.additional_properties = d
        return static_route

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
