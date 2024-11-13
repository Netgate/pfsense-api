from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        gateways (Union[Unset, List['GatewayPInfo']]):
        priorities (Union[Unset, List['GatewayPriority']]):
    """

    gateways: Union[Unset, List["GatewayPInfo"]] = UNSET
    priorities: Union[Unset, List["GatewayPriority"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gateways: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.gateways, Unset):
            gateways = []
            for gateways_item_data in self.gateways:
                gateways_item = gateways_item_data.to_dict()
                gateways.append(gateways_item)

        priorities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.priorities, Unset):
            priorities = []
            for priorities_item_data in self.priorities:
                priorities_item = priorities_item_data.to_dict()
                priorities.append(priorities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateways is not UNSET:
            field_dict["gateways"] = gateways
        if priorities is not UNSET:
            field_dict["priorities"] = priorities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gateway_p_info import GatewayPInfo
        from ..models.gateway_priority import GatewayPriority

        d = src_dict.copy()
        gateways = []
        _gateways = d.pop("gateways", UNSET)
        for gateways_item_data in _gateways or []:
            gateways_item = GatewayPInfo.from_dict(gateways_item_data)

            gateways.append(gateways_item)

        priorities = []
        _priorities = d.pop("priorities", UNSET)
        for priorities_item_data in _priorities or []:
            priorities_item = GatewayPriority.from_dict(priorities_item_data)

            priorities.append(priorities_item)

        gateway_priorities = cls(
            gateways=gateways,
            priorities=priorities,
        )

        gateway_priorities.additional_properties = d
        return gateway_priorities

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
