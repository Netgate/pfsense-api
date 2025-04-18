from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptivePortalName")


@_attrs_define
class CaptivePortalName:
    """
    Attributes:
        zone (str):
        interface (str):
        descr (Union[Unset, str]):
        users (Union[Unset, int]):
    """

    zone: str
    interface: str
    descr: Union[Unset, str] = UNSET
    users: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        zone = self.zone

        interface = self.interface

        descr = self.descr

        users = self.users

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zone": zone,
                "interface": interface,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        zone = d.pop("zone")

        interface = d.pop("interface")

        descr = d.pop("descr", UNSET)

        users = d.pop("users", UNSET)

        captive_portal_name = cls(
            zone=zone,
            interface=interface,
            descr=descr,
            users=users,
        )

        captive_portal_name.additional_properties = d
        return captive_portal_name

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
