from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FWFirewallInterfaces")


@_attrs_define
class FWFirewallInterfaces:
    """
    Attributes:
        interfaces (Union[Unset, List[str]]):
        wan (Union[Unset, str]):
        lan (Union[Unset, str]):
        ethernet (Union[Unset, bool]): ethernet filter is enabled
    """

    interfaces: Union[Unset, List[str]] = UNSET
    wan: Union[Unset, str] = UNSET
    lan: Union[Unset, str] = UNSET
    ethernet: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        wan = self.wan

        lan = self.lan

        ethernet = self.ethernet

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if wan is not UNSET:
            field_dict["wan"] = wan
        if lan is not UNSET:
            field_dict["lan"] = lan
        if ethernet is not UNSET:
            field_dict["ethernet"] = ethernet

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interfaces = cast(List[str], d.pop("interfaces", UNSET))

        wan = d.pop("wan", UNSET)

        lan = d.pop("lan", UNSET)

        ethernet = d.pop("ethernet", UNSET)

        fw_firewall_interfaces = cls(
            interfaces=interfaces,
            wan=wan,
            lan=lan,
            ethernet=ethernet,
        )

        fw_firewall_interfaces.additional_properties = d
        return fw_firewall_interfaces

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
