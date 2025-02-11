from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeshVpnConns")


@_attrs_define
class MeshVpnConns:
    """
    Attributes:
        vpn_type (str):
        vpn_name (str):
        conns (str):
        subnets (Union[Unset, List[str]]):
    """

    vpn_type: str
    vpn_name: str
    conns: str
    subnets: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vpn_type = self.vpn_type

        vpn_name = self.vpn_name

        conns = self.conns

        subnets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subnets, Unset):
            subnets = self.subnets

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vpn_type": vpn_type,
                "vpn_name": vpn_name,
                "conns": conns,
            }
        )
        if subnets is not UNSET:
            field_dict["subnets"] = subnets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vpn_type = d.pop("vpn_type")

        vpn_name = d.pop("vpn_name")

        conns = d.pop("conns")

        subnets = cast(List[str], d.pop("subnets", UNSET))

        mesh_vpn_conns = cls(
            vpn_type=vpn_type,
            vpn_name=vpn_name,
            conns=conns,
            subnets=subnets,
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
