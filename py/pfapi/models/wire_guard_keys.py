from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WireGuardKeys")


@_attrs_define
class WireGuardKeys:
    """
    Attributes:
        privkey (str | Unset):
        privkey_clamped (str | Unset):
        pubkey (str | Unset):
        was_clamped (bool | Unset):
    """

    privkey: str | Unset = UNSET
    privkey_clamped: str | Unset = UNSET
    pubkey: str | Unset = UNSET
    was_clamped: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        privkey = self.privkey

        privkey_clamped = self.privkey_clamped

        pubkey = self.pubkey

        was_clamped = self.was_clamped

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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
