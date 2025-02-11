from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        idx (int):
        name (str):
        descr (str):
        gateway_priority (List['GatewayGroupPriority']):
        keep_failover_states (str):
        trigger (str):
        trigger_descr (Union[Unset, str]):
        keep_failover_states_descr (Union[Unset, str]):
    """

    idx: int
    name: str
    descr: str
    gateway_priority: List["GatewayGroupPriority"]
    keep_failover_states: str
    trigger: str
    trigger_descr: Union[Unset, str] = UNSET
    keep_failover_states_descr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        idx = self.idx

        name = self.name

        descr = self.descr

        gateway_priority = []
        for gateway_priority_item_data in self.gateway_priority:
            gateway_priority_item = gateway_priority_item_data.to_dict()
            gateway_priority.append(gateway_priority_item)

        keep_failover_states = self.keep_failover_states

        trigger = self.trigger

        trigger_descr = self.trigger_descr

        keep_failover_states_descr = self.keep_failover_states_descr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idx": idx,
                "name": name,
                "descr": descr,
                "gateway_priority": gateway_priority,
                "keep_failover_states": keep_failover_states,
                "trigger": trigger,
            }
        )
        if trigger_descr is not UNSET:
            field_dict["trigger_descr"] = trigger_descr
        if keep_failover_states_descr is not UNSET:
            field_dict["keep_failover_states_descr"] = keep_failover_states_descr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gateway_group_priority import GatewayGroupPriority

        d = src_dict.copy()
        idx = d.pop("idx")

        name = d.pop("name")

        descr = d.pop("descr")

        gateway_priority = []
        _gateway_priority = d.pop("gateway_priority")
        for gateway_priority_item_data in _gateway_priority:
            gateway_priority_item = GatewayGroupPriority.from_dict(gateway_priority_item_data)

            gateway_priority.append(gateway_priority_item)

        keep_failover_states = d.pop("keep_failover_states")

        trigger = d.pop("trigger")

        trigger_descr = d.pop("trigger_descr", UNSET)

        keep_failover_states_descr = d.pop("keep_failover_states_descr", UNSET)

        gateway_group = cls(
            idx=idx,
            name=name,
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
