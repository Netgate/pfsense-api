from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StaticRoute")


@_attrs_define
class StaticRoute:
    """
    Attributes:
        network (str):
        network_encoded (str):
        gateway (str):
        gateway_encoded (str):
        descr (str):
        disabled (bool):
        interface (str):
    """

    network: str
    network_encoded: str
    gateway: str
    gateway_encoded: str
    descr: str
    disabled: bool
    interface: str
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
        field_dict.update(
            {
                "network": network,
                "network_encoded": network_encoded,
                "gateway": gateway,
                "gateway_encoded": gateway_encoded,
                "descr": descr,
                "disabled": disabled,
                "interface": interface,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        network = d.pop("network")

        network_encoded = d.pop("network_encoded")

        gateway = d.pop("gateway")

        gateway_encoded = d.pop("gateway_encoded")

        descr = d.pop("descr")

        disabled = d.pop("disabled")

        interface = d.pop("interface")

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
