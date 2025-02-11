from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        devices_total (int):
        devices_online (int):
        vpn_conns (Union[Unset, List['MeshVpnConns']]):
    """

    devices_total: int
    devices_online: int
    vpn_conns: Union[Unset, List["MeshVpnConns"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        devices_total = self.devices_total

        devices_online = self.devices_online

        vpn_conns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vpn_conns, Unset):
            vpn_conns = []
            for vpn_conns_item_data in self.vpn_conns:
                vpn_conns_item = vpn_conns_item_data.to_dict()
                vpn_conns.append(vpn_conns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "devices_total": devices_total,
                "devices_online": devices_online,
            }
        )
        if vpn_conns is not UNSET:
            field_dict["vpn_conns"] = vpn_conns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mesh_vpn_conns import MeshVpnConns

        d = src_dict.copy()
        devices_total = d.pop("devices_total")

        devices_online = d.pop("devices_online")

        vpn_conns = []
        _vpn_conns = d.pop("vpn_conns", UNSET)
        for vpn_conns_item_data in _vpn_conns or []:
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
