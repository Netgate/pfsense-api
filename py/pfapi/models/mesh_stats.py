from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mesh_vpn_conns import MeshVpnConns


T = TypeVar("T", bound="MeshStats")


@_attrs_define
class MeshStats:
    """
    Attributes:
        devices_total (int | Unset): total number of devices
        devices_online (int | Unset): active devices
        vpn_conns (list[MeshVpnConns] | Unset):
    """

    devices_total: int | Unset = UNSET
    devices_online: int | Unset = UNSET
    vpn_conns: list[MeshVpnConns] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        devices_total = self.devices_total

        devices_online = self.devices_online

        vpn_conns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vpn_conns, Unset):
            vpn_conns = []
            for vpn_conns_item_data in self.vpn_conns:
                vpn_conns_item = vpn_conns_item_data.to_dict()
                vpn_conns.append(vpn_conns_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices_total is not UNSET:
            field_dict["devices_total"] = devices_total
        if devices_online is not UNSET:
            field_dict["devices_online"] = devices_online
        if vpn_conns is not UNSET:
            field_dict["vpn_conns"] = vpn_conns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mesh_vpn_conns import MeshVpnConns

        d = dict(src_dict)
        devices_total = d.pop("devices_total", UNSET)

        devices_online = d.pop("devices_online", UNSET)

        _vpn_conns = d.pop("vpn_conns", UNSET)
        vpn_conns: list[MeshVpnConns] | Unset = UNSET
        if _vpn_conns is not UNSET:
            vpn_conns = []
            for vpn_conns_item_data in _vpn_conns:
                vpn_conns_item = MeshVpnConns.from_dict(vpn_conns_item_data)

                vpn_conns.append(vpn_conns_item)

        mesh_stats = cls(
            devices_total=devices_total,
            devices_online=devices_online,
            vpn_conns=vpn_conns,
        )

        mesh_stats.additional_properties = d
        return mesh_stats

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
