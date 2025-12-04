from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_sec_widget_mobile import IPSecWidgetMobile
    from ..models.ip_sec_widget_tunnel import IPSecWidgetTunnel


T = TypeVar("T", bound="IPSecWidget")


@_attrs_define
class IPSecWidget:
    """
    Attributes:
        phase1s_active (int | Unset):
        phase1s_total (int | Unset):
        phase2s_active (int | Unset):
        phase2s_total (int | Unset):
        total_active (int | Unset):
        total_inactive (int | Unset):
        mobile_users (int | Unset):
        mobile_active (int | Unset):
        mobile_total (int | Unset):
        tunnels (list[IPSecWidgetTunnel] | Unset):
        mobile (list[IPSecWidgetMobile] | Unset):
    """

    phase1s_active: int | Unset = UNSET
    phase1s_total: int | Unset = UNSET
    phase2s_active: int | Unset = UNSET
    phase2s_total: int | Unset = UNSET
    total_active: int | Unset = UNSET
    total_inactive: int | Unset = UNSET
    mobile_users: int | Unset = UNSET
    mobile_active: int | Unset = UNSET
    mobile_total: int | Unset = UNSET
    tunnels: list[IPSecWidgetTunnel] | Unset = UNSET
    mobile: list[IPSecWidgetMobile] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phase1s_active = self.phase1s_active

        phase1s_total = self.phase1s_total

        phase2s_active = self.phase2s_active

        phase2s_total = self.phase2s_total

        total_active = self.total_active

        total_inactive = self.total_inactive

        mobile_users = self.mobile_users

        mobile_active = self.mobile_active

        mobile_total = self.mobile_total

        tunnels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tunnels, Unset):
            tunnels = []
            for tunnels_item_data in self.tunnels:
                tunnels_item = tunnels_item_data.to_dict()
                tunnels.append(tunnels_item)

        mobile: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mobile, Unset):
            mobile = []
            for mobile_item_data in self.mobile:
                mobile_item = mobile_item_data.to_dict()
                mobile.append(mobile_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phase1s_active is not UNSET:
            field_dict["phase1s_active"] = phase1s_active
        if phase1s_total is not UNSET:
            field_dict["phase1s_total"] = phase1s_total
        if phase2s_active is not UNSET:
            field_dict["phase2s_active"] = phase2s_active
        if phase2s_total is not UNSET:
            field_dict["phase2s_total"] = phase2s_total
        if total_active is not UNSET:
            field_dict["total_active"] = total_active
        if total_inactive is not UNSET:
            field_dict["total_inactive"] = total_inactive
        if mobile_users is not UNSET:
            field_dict["mobile_users"] = mobile_users
        if mobile_active is not UNSET:
            field_dict["mobile_active"] = mobile_active
        if mobile_total is not UNSET:
            field_dict["mobile_total"] = mobile_total
        if tunnels is not UNSET:
            field_dict["tunnels"] = tunnels
        if mobile is not UNSET:
            field_dict["mobile"] = mobile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_sec_widget_mobile import IPSecWidgetMobile
        from ..models.ip_sec_widget_tunnel import IPSecWidgetTunnel

        d = dict(src_dict)
        phase1s_active = d.pop("phase1s_active", UNSET)

        phase1s_total = d.pop("phase1s_total", UNSET)

        phase2s_active = d.pop("phase2s_active", UNSET)

        phase2s_total = d.pop("phase2s_total", UNSET)

        total_active = d.pop("total_active", UNSET)

        total_inactive = d.pop("total_inactive", UNSET)

        mobile_users = d.pop("mobile_users", UNSET)

        mobile_active = d.pop("mobile_active", UNSET)

        mobile_total = d.pop("mobile_total", UNSET)

        _tunnels = d.pop("tunnels", UNSET)
        tunnels: list[IPSecWidgetTunnel] | Unset = UNSET
        if _tunnels is not UNSET:
            tunnels = []
            for tunnels_item_data in _tunnels:
                tunnels_item = IPSecWidgetTunnel.from_dict(tunnels_item_data)

                tunnels.append(tunnels_item)

        _mobile = d.pop("mobile", UNSET)
        mobile: list[IPSecWidgetMobile] | Unset = UNSET
        if _mobile is not UNSET:
            mobile = []
            for mobile_item_data in _mobile:
                mobile_item = IPSecWidgetMobile.from_dict(mobile_item_data)

                mobile.append(mobile_item)

        ip_sec_widget = cls(
            phase1s_active=phase1s_active,
            phase1s_total=phase1s_total,
            phase2s_active=phase2s_active,
            phase2s_total=phase2s_total,
            total_active=total_active,
            total_inactive=total_inactive,
            mobile_users=mobile_users,
            mobile_active=mobile_active,
            mobile_total=mobile_total,
            tunnels=tunnels,
            mobile=mobile,
        )

        ip_sec_widget.additional_properties = d
        return ip_sec_widget

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
