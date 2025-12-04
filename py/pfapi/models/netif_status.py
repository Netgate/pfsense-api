from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetifStatus")


@_attrs_define
class NetifStatus:
    """
    Attributes:
        assigned_name (str | Unset):
        identity (str | Unset):
        device (str | Unset):
        state (str | Unset):
        addresses (list[str] | Unset):
    """

    assigned_name: str | Unset = UNSET
    identity: str | Unset = UNSET
    device: str | Unset = UNSET
    state: str | Unset = UNSET
    addresses: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_name = self.assigned_name

        identity = self.identity

        device = self.device

        state = self.state

        addresses: list[str] | Unset = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned_name is not UNSET:
            field_dict["assigned_name"] = assigned_name
        if identity is not UNSET:
            field_dict["identity"] = identity
        if device is not UNSET:
            field_dict["device"] = device
        if state is not UNSET:
            field_dict["state"] = state
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assigned_name = d.pop("assigned_name", UNSET)

        identity = d.pop("identity", UNSET)

        device = d.pop("device", UNSET)

        state = d.pop("state", UNSET)

        addresses = cast(list[str], d.pop("addresses", UNSET))

        netif_status = cls(
            assigned_name=assigned_name,
            identity=identity,
            device=device,
            state=state,
            addresses=addresses,
        )

        netif_status.additional_properties = d
        return netif_status

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
