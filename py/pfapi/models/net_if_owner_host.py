from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NetIfOwnerHost")


@_attrs_define
class NetIfOwnerHost:
    """
    Attributes:
        wol (bool):
        hw_flags (str): comma-separated flags configured on interface, e.g. TSO, LRO, etc
    """

    wol: bool
    hw_flags: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wol = self.wol

        hw_flags = self.hw_flags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wol": wol,
                "hw_flags": hw_flags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        wol = d.pop("wol")

        hw_flags = d.pop("hw_flags")

        net_if_owner_host = cls(
            wol=wol,
            hw_flags=hw_flags,
        )

        net_if_owner_host.additional_properties = d
        return net_if_owner_host

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
