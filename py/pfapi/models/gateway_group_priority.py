from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayGroupPriority")


@_attrs_define
class GatewayGroupPriority:
    """
    Attributes:
        gateway (Union[Unset, str]):
        priority (Union[Unset, str]):
        vaddress (Union[Unset, str]):
    """

    gateway: Union[Unset, str] = UNSET
    priority: Union[Unset, str] = UNSET
    vaddress: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gateway = self.gateway

        priority = self.priority

        vaddress = self.vaddress

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if priority is not UNSET:
            field_dict["priority"] = priority
        if vaddress is not UNSET:
            field_dict["vaddress"] = vaddress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gateway = d.pop("gateway", UNSET)

        priority = d.pop("priority", UNSET)

        vaddress = d.pop("vaddress", UNSET)

        gateway_group_priority = cls(
            gateway=gateway,
            priority=priority,
            vaddress=vaddress,
        )

        gateway_group_priority.additional_properties = d
        return gateway_group_priority

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
