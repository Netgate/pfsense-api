from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_p_info import GatewayPInfo
    from ..models.gateway_priority import GatewayPriority


T = TypeVar("T", bound="GatewayPriorities")


@_attrs_define
class GatewayPriorities:
    """
    Attributes:
        gateways (list[GatewayPInfo] | Unset):
        priorities (list[GatewayPriority] | Unset):
    """

    gateways: list[GatewayPInfo] | Unset = UNSET
    priorities: list[GatewayPriority] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateways: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gateways, Unset):
            gateways = []
            for gateways_item_data in self.gateways:
                gateways_item = gateways_item_data.to_dict()
                gateways.append(gateways_item)

        priorities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.priorities, Unset):
            priorities = []
            for priorities_item_data in self.priorities:
                priorities_item = priorities_item_data.to_dict()
                priorities.append(priorities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateways is not UNSET:
            field_dict["gateways"] = gateways
        if priorities is not UNSET:
            field_dict["priorities"] = priorities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_p_info import GatewayPInfo
        from ..models.gateway_priority import GatewayPriority

        d = dict(src_dict)
        _gateways = d.pop("gateways", UNSET)
        gateways: list[GatewayPInfo] | Unset = UNSET
        if _gateways is not UNSET:
            gateways = []
            for gateways_item_data in _gateways:
                gateways_item = GatewayPInfo.from_dict(gateways_item_data)

                gateways.append(gateways_item)

        _priorities = d.pop("priorities", UNSET)
        priorities: list[GatewayPriority] | Unset = UNSET
        if _priorities is not UNSET:
            priorities = []
            for priorities_item_data in _priorities:
                priorities_item = GatewayPriority.from_dict(priorities_item_data)

                priorities.append(priorities_item)

        gateway_priorities = cls(
            gateways=gateways,
            priorities=priorities,
        )

        gateway_priorities.additional_properties = d
        return gateway_priorities

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
