from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeshVpnConns")


@_attrs_define
class MeshVpnConns:
    """
    Attributes:
        vpn_type (Union[Unset, str]): type of VPN
        vpn_name (Union[Unset, str]): name assigned to vpn
        subnets (Union[Unset, List[str]]):
        conns (Union[Unset, str]): number of connections
    """

    vpn_type: Union[Unset, str] = UNSET
    vpn_name: Union[Unset, str] = UNSET
    subnets: Union[Unset, List[str]] = UNSET
    conns: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vpn_type = self.vpn_type

        vpn_name = self.vpn_name

        subnets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subnets, Unset):
            subnets = self.subnets

        conns = self.conns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpn_type is not UNSET:
            field_dict["vpn_type"] = vpn_type
        if vpn_name is not UNSET:
            field_dict["vpn_name"] = vpn_name
        if subnets is not UNSET:
            field_dict["subnets"] = subnets
        if conns is not UNSET:
            field_dict["conns"] = conns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vpn_type = d.pop("vpn_type", UNSET)

        vpn_name = d.pop("vpn_name", UNSET)

        subnets = cast(List[str], d.pop("subnets", UNSET))

        conns = d.pop("conns", UNSET)

        mesh_vpn_conns = cls(
            vpn_type=vpn_type,
            vpn_name=vpn_name,
            subnets=subnets,
            conns=conns,
        )

        mesh_vpn_conns.additional_properties = d
        return mesh_vpn_conns

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
