from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.carpvip_status import CARPVIPStatus


T = TypeVar("T", bound="CARPStatus")


@_attrs_define
class CARPStatus:
    """
    Attributes:
        enabled (bool | Unset):
        maintenancemode_enabled (bool | Unset):
        my_hostid (str | Unset): this system's host-id
        state_sync_hostids (list[str] | Unset):
        vips (list[CARPVIPStatus] | Unset):
    """

    enabled: bool | Unset = UNSET
    maintenancemode_enabled: bool | Unset = UNSET
    my_hostid: str | Unset = UNSET
    state_sync_hostids: list[str] | Unset = UNSET
    vips: list[CARPVIPStatus] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        maintenancemode_enabled = self.maintenancemode_enabled

        my_hostid = self.my_hostid

        state_sync_hostids: list[str] | Unset = UNSET
        if not isinstance(self.state_sync_hostids, Unset):
            state_sync_hostids = self.state_sync_hostids

        vips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vips, Unset):
            vips = []
            for vips_item_data in self.vips:
                vips_item = vips_item_data.to_dict()
                vips.append(vips_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if maintenancemode_enabled is not UNSET:
            field_dict["maintenancemode_enabled"] = maintenancemode_enabled
        if my_hostid is not UNSET:
            field_dict["my_hostid"] = my_hostid
        if state_sync_hostids is not UNSET:
            field_dict["state_sync_hostids"] = state_sync_hostids
        if vips is not UNSET:
            field_dict["vips"] = vips

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.carpvip_status import CARPVIPStatus

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        maintenancemode_enabled = d.pop("maintenancemode_enabled", UNSET)

        my_hostid = d.pop("my_hostid", UNSET)

        state_sync_hostids = cast(list[str], d.pop("state_sync_hostids", UNSET))

        _vips = d.pop("vips", UNSET)
        vips: list[CARPVIPStatus] | Unset = UNSET
        if _vips is not UNSET:
            vips = []
            for vips_item_data in _vips:
                vips_item = CARPVIPStatus.from_dict(vips_item_data)

                vips.append(vips_item)

        carp_status = cls(
            enabled=enabled,
            maintenancemode_enabled=maintenancemode_enabled,
            my_hostid=my_hostid,
            state_sync_hostids=state_sync_hostids,
            vips=vips,
        )

        carp_status.additional_properties = d
        return carp_status

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
