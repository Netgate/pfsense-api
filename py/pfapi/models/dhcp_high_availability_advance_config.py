from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpHighAvailabilityAdvanceConfig")


@_attrs_define
class DhcpHighAvailabilityAdvanceConfig:
    """
    Attributes:
        heartbeat_delay (Union[Unset, int]):
        max_response_delay (Union[Unset, int]):
        max_ack_delay (Union[Unset, int]):
        max_unacked_clients (Union[Unset, int]):
        max_rejected_updates (Union[Unset, int]):
    """

    heartbeat_delay: Union[Unset, int] = UNSET
    max_response_delay: Union[Unset, int] = UNSET
    max_ack_delay: Union[Unset, int] = UNSET
    max_unacked_clients: Union[Unset, int] = UNSET
    max_rejected_updates: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        heartbeat_delay = self.heartbeat_delay

        max_response_delay = self.max_response_delay

        max_ack_delay = self.max_ack_delay

        max_unacked_clients = self.max_unacked_clients

        max_rejected_updates = self.max_rejected_updates

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if heartbeat_delay is not UNSET:
            field_dict["heartbeat_delay"] = heartbeat_delay
        if max_response_delay is not UNSET:
            field_dict["max_response_delay"] = max_response_delay
        if max_ack_delay is not UNSET:
            field_dict["max_ack_delay"] = max_ack_delay
        if max_unacked_clients is not UNSET:
            field_dict["max_unacked_clients"] = max_unacked_clients
        if max_rejected_updates is not UNSET:
            field_dict["max_rejected_updates"] = max_rejected_updates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        heartbeat_delay = d.pop("heartbeat_delay", UNSET)

        max_response_delay = d.pop("max_response_delay", UNSET)

        max_ack_delay = d.pop("max_ack_delay", UNSET)

        max_unacked_clients = d.pop("max_unacked_clients", UNSET)

        max_rejected_updates = d.pop("max_rejected_updates", UNSET)

        dhcp_high_availability_advance_config = cls(
            heartbeat_delay=heartbeat_delay,
            max_response_delay=max_response_delay,
            max_ack_delay=max_ack_delay,
            max_unacked_clients=max_unacked_clients,
            max_rejected_updates=max_rejected_updates,
        )

        dhcp_high_availability_advance_config.additional_properties = d
        return dhcp_high_availability_advance_config

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
