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
        name (str):
        idx (Union[Unset, int]):
        descr (Union[Unset, str]):
        gateway_priority (Union[Unset, List['GatewayGroupPriority']]):
        keep_failover_states (Union[Unset, str]):
        trigger (Union[Unset, str]):
        trigger_descr (Union[Unset, str]):
        keep_failover_states_descr (Union[Unset, str]):
    """

    name: str
    idx: Union[Unset, int] = UNSET
    descr: Union[Unset, str] = UNSET
    gateway_priority: Union[Unset, List["GatewayGroupPriority"]] = UNSET
    keep_failover_states: Union[Unset, str] = UNSET
    trigger: Union[Unset, str] = UNSET
    trigger_descr: Union[Unset, str] = UNSET
    keep_failover_states_descr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        idx = self.idx

        descr = self.descr

        gateway_priority: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.gateway_priority, Unset):
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gateway_group_priority import GatewayGroupPriority

        d = src_dict.copy()
        name = d.pop("name")

        idx = d.pop("idx", UNSET)

        descr = d.pop("descr", UNSET)

        gateway_priority = []
        _gateway_priority = d.pop("gateway_priority", UNSET)
        for gateway_priority_item_data in _gateway_priority or []:
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
