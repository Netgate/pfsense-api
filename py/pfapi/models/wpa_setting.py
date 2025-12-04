from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WPASetting")


@_attrs_define
class WPASetting:
    """
    Attributes:
        macaddr_acl (str | Unset):
        wpa_mode (str | Unset):
        wpa_key_mgmt (str | Unset):
        wpa_pairwise (str | Unset):
        wpa_group_rekey (str | Unset):
        wpa_gmk_rekey (str | Unset):
        passphrase (str | Unset):
        ext_wpa_sw (str | Unset):
    """

    macaddr_acl: str | Unset = UNSET
    wpa_mode: str | Unset = UNSET
    wpa_key_mgmt: str | Unset = UNSET
    wpa_pairwise: str | Unset = UNSET
    wpa_group_rekey: str | Unset = UNSET
    wpa_gmk_rekey: str | Unset = UNSET
    passphrase: str | Unset = UNSET
    ext_wpa_sw: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        macaddr_acl = self.macaddr_acl

        wpa_mode = self.wpa_mode

        wpa_key_mgmt = self.wpa_key_mgmt

        wpa_pairwise = self.wpa_pairwise

        wpa_group_rekey = self.wpa_group_rekey

        wpa_gmk_rekey = self.wpa_gmk_rekey

        passphrase = self.passphrase

        ext_wpa_sw = self.ext_wpa_sw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if macaddr_acl is not UNSET:
            field_dict["macaddr_acl"] = macaddr_acl
        if wpa_mode is not UNSET:
            field_dict["wpa_mode"] = wpa_mode
        if wpa_key_mgmt is not UNSET:
            field_dict["wpa_key_mgmt"] = wpa_key_mgmt
        if wpa_pairwise is not UNSET:
            field_dict["wpa_pairwise"] = wpa_pairwise
        if wpa_group_rekey is not UNSET:
            field_dict["wpa_group_rekey"] = wpa_group_rekey
        if wpa_gmk_rekey is not UNSET:
            field_dict["wpa_gmk_rekey"] = wpa_gmk_rekey
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase
        if ext_wpa_sw is not UNSET:
            field_dict["ext_wpa_sw"] = ext_wpa_sw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        macaddr_acl = d.pop("macaddr_acl", UNSET)

        wpa_mode = d.pop("wpa_mode", UNSET)

        wpa_key_mgmt = d.pop("wpa_key_mgmt", UNSET)

        wpa_pairwise = d.pop("wpa_pairwise", UNSET)

        wpa_group_rekey = d.pop("wpa_group_rekey", UNSET)

        wpa_gmk_rekey = d.pop("wpa_gmk_rekey", UNSET)

        passphrase = d.pop("passphrase", UNSET)

        ext_wpa_sw = d.pop("ext_wpa_sw", UNSET)

        wpa_setting = cls(
            macaddr_acl=macaddr_acl,
            wpa_mode=wpa_mode,
            wpa_key_mgmt=wpa_key_mgmt,
            wpa_pairwise=wpa_pairwise,
            wpa_group_rekey=wpa_group_rekey,
            wpa_gmk_rekey=wpa_gmk_rekey,
            passphrase=passphrase,
            ext_wpa_sw=ext_wpa_sw,
        )

        wpa_setting.additional_properties = d
        return wpa_setting

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
