from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_status import GatewayStatus
    from ..models.group_status import GroupStatus


T = TypeVar("T", bound="GatewaysStatus")


@_attrs_define
class GatewaysStatus:
    """
    Attributes:
        gateways (Union[Unset, List['GatewayStatus']]):
        groups (Union[Unset, List['GroupStatus']]):
    """

    gateways: Union[Unset, List["GatewayStatus"]] = UNSET
    groups: Union[Unset, List["GroupStatus"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gateways: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.gateways, Unset):
            gateways = []
            for gateways_item_data in self.gateways:
                gateways_item = gateways_item_data.to_dict()
                gateways.append(gateways_item)

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateways is not UNSET:
            field_dict["gateways"] = gateways
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gateway_status import GatewayStatus
        from ..models.group_status import GroupStatus

        d = src_dict.copy()
        gateways = []
        _gateways = d.pop("gateways", UNSET)
        for gateways_item_data in _gateways or []:
            gateways_item = GatewayStatus.from_dict(gateways_item_data)

            gateways.append(gateways_item)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GroupStatus.from_dict(groups_item_data)

            groups.append(groups_item)

        gateways_status = cls(
            gateways=gateways,
            groups=groups,
        )

        gateways_status.additional_properties = d
        return gateways_status

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
