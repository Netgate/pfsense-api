from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_group_priority import GatewayGroupPriority


T = TypeVar("T", bound="GatewayGroup")


@_attrs_define
class GatewayGroup:
    """
    Attributes:
        name (str):
        idx (int | Unset):
        descr (str | Unset):
        gateway_priority (list[GatewayGroupPriority] | Unset):
        keep_failover_states (str | Unset):
        trigger (str | Unset):
        trigger_descr (str | Unset):
        keep_failover_states_descr (str | Unset):
    """

    name: str
    idx: int | Unset = UNSET
    descr: str | Unset = UNSET
    gateway_priority: list[GatewayGroupPriority] | Unset = UNSET
    keep_failover_states: str | Unset = UNSET
    trigger: str | Unset = UNSET
    trigger_descr: str | Unset = UNSET
    keep_failover_states_descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        idx = self.idx

        descr = self.descr

        gateway_priority: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gateway_priority, Unset):
            gateway_priority = []
            for gateway_priority_item_data in self.gateway_priority:
                gateway_priority_item = gateway_priority_item_data.to_dict()
                gateway_priority.append(gateway_priority_item)

        keep_failover_states = self.keep_failover_states

        trigger = self.trigger

        trigger_descr = self.trigger_descr

        keep_failover_states_descr = self.keep_failover_states_descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if idx is not UNSET:
            field_dict["idx"] = idx
        if descr is not UNSET:
            field_dict["descr"] = descr
        if gateway_priority is not UNSET:
            field_dict["gateway_priority"] = gateway_priority
        if keep_failover_states is not UNSET:
            field_dict["keep_failover_states"] = keep_failover_states
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if trigger_descr is not UNSET:
            field_dict["trigger_descr"] = trigger_descr
        if keep_failover_states_descr is not UNSET:
            field_dict["keep_failover_states_descr"] = keep_failover_states_descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_group_priority import GatewayGroupPriority

        d = dict(src_dict)
        name = d.pop("name")

        idx = d.pop("idx", UNSET)

        descr = d.pop("descr", UNSET)

        _gateway_priority = d.pop("gateway_priority", UNSET)
        gateway_priority: list[GatewayGroupPriority] | Unset = UNSET
        if _gateway_priority is not UNSET:
            gateway_priority = []
            for gateway_priority_item_data in _gateway_priority:
                gateway_priority_item = GatewayGroupPriority.from_dict(gateway_priority_item_data)

                gateway_priority.append(gateway_priority_item)

        keep_failover_states = d.pop("keep_failover_states", UNSET)

        trigger = d.pop("trigger", UNSET)

        trigger_descr = d.pop("trigger_descr", UNSET)

        keep_failover_states_descr = d.pop("keep_failover_states_descr", UNSET)

        gateway_group = cls(
            name=name,
            idx=idx,
            descr=descr,
            gateway_priority=gateway_priority,
            keep_failover_states=keep_failover_states,
            trigger=trigger,
            trigger_descr=trigger_descr,
            keep_failover_states_descr=keep_failover_states_descr,
        )

        gateway_group.additional_properties = d
        return gateway_group

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
