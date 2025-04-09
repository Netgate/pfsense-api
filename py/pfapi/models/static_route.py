from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaticRoute")


@_attrs_define
class StaticRoute:
    """
    Attributes:
        network (str):
        gateway (str):
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        interface (Union[Unset, str]):
        network_encoded (Union[Unset, str]): base64 encoded network; read-only
        gateway_encoded (Union[Unset, str]): base64 encoded gateway; read-only
    """

    network: str
    gateway: str
    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    interface: Union[Unset, str] = UNSET
    network_encoded: Union[Unset, str] = UNSET
    gateway_encoded: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        network = self.network

        gateway = self.gateway

        descr = self.descr

        disabled = self.disabled

        interface = self.interface

        network_encoded = self.network_encoded

        gateway_encoded = self.gateway_encoded

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network": network,
                "gateway": gateway,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if interface is not UNSET:
            field_dict["interface"] = interface
        if network_encoded is not UNSET:
            field_dict["network_encoded"] = network_encoded
        if gateway_encoded is not UNSET:
            field_dict["gateway_encoded"] = gateway_encoded

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        network = d.pop("network")

        gateway = d.pop("gateway")

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        interface = d.pop("interface", UNSET)

        network_encoded = d.pop("network_encoded", UNSET)

        gateway_encoded = d.pop("gateway_encoded", UNSET)

        static_route = cls(
            network=network,
            gateway=gateway,
            descr=descr,
            disabled=disabled,
            interface=interface,
            network_encoded=network_encoded,
            gateway_encoded=gateway_encoded,
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
