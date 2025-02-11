from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WireGuardKeys")


@_attrs_define
class WireGuardKeys:
    """
    Attributes:
        privkey (str):
        privkey_clamped (str):
        pubkey (str):
        was_clamped (bool):
    """

    privkey: str
    privkey_clamped: str
    pubkey: str
    was_clamped: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        privkey = self.privkey

        privkey_clamped = self.privkey_clamped

        pubkey = self.pubkey

        was_clamped = self.was_clamped

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "privkey": privkey,
                "privkey_clamped": privkey_clamped,
                "pubkey": pubkey,
                "was_clamped": was_clamped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        privkey = d.pop("privkey")

        privkey_clamped = d.pop("privkey_clamped")

        pubkey = d.pop("pubkey")

        was_clamped = d.pop("was_clamped")

        wire_guard_keys = cls(
            privkey=privkey,
            privkey_clamped=privkey_clamped,
            pubkey=pubkey,
            was_clamped=was_clamped,
        )

        wire_guard_keys.additional_properties = d
        return wire_guard_keys

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
