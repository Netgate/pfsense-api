from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        gateways (list[GatewayStatus] | Unset):
        groups (list[GroupStatus] | Unset):
    """

    gateways: list[GatewayStatus] | Unset = UNSET
    groups: list[GroupStatus] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateways: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gateways, Unset):
            gateways = []
            for gateways_item_data in self.gateways:
                gateways_item = gateways_item_data.to_dict()
                gateways.append(gateways_item)

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateways is not UNSET:
            field_dict["gateways"] = gateways
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_status import GatewayStatus
        from ..models.group_status import GroupStatus

        d = dict(src_dict)
        _gateways = d.pop("gateways", UNSET)
        gateways: list[GatewayStatus] | Unset = UNSET
        if _gateways is not UNSET:
            gateways = []
            for gateways_item_data in _gateways:
                gateways_item = GatewayStatus.from_dict(gateways_item_data)

                gateways.append(gateways_item)

        _groups = d.pop("groups", UNSET)
        groups: list[GroupStatus] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = GroupStatus.from_dict(groups_item_data)

                groups.append(groups_item)

        gateways_status = cls(
            gateways=gateways,
            groups=groups,
        )

        gateways_status.additional_properties = d
        return gateways_status

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
