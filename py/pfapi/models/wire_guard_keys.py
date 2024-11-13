from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WireGuardKeys")


@_attrs_define
class WireGuardKeys:
    """
    Attributes:
        privkey (Union[Unset, str]):
        privkey_clamped (Union[Unset, str]):
        pubkey (Union[Unset, str]):
        was_clamped (Union[Unset, bool]):
    """

    privkey: Union[Unset, str] = UNSET
    privkey_clamped: Union[Unset, str] = UNSET
    pubkey: Union[Unset, str] = UNSET
    was_clamped: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        privkey = self.privkey

        privkey_clamped = self.privkey_clamped

        pubkey = self.pubkey

        was_clamped = self.was_clamped

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if privkey is not UNSET:
            field_dict["privkey"] = privkey
        if privkey_clamped is not UNSET:
            field_dict["privkey_clamped"] = privkey_clamped
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if was_clamped is not UNSET:
            field_dict["was_clamped"] = was_clamped

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        privkey = d.pop("privkey", UNSET)

        privkey_clamped = d.pop("privkey_clamped", UNSET)

        pubkey = d.pop("pubkey", UNSET)

        was_clamped = d.pop("was_clamped", UNSET)

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
