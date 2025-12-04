from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SysFirmwareUpgradeOpt")


@_attrs_define
class SysFirmwareUpgradeOpt:
    """
    Attributes:
        upgrade (bool | Unset): set to true to confirm upgrade
    """

    upgrade: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upgrade = self.upgrade

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upgrade is not UNSET:
            field_dict["upgrade"] = upgrade

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upgrade = d.pop("upgrade", UNSET)

        sys_firmware_upgrade_opt = cls(
            upgrade=upgrade,
        )

        sys_firmware_upgrade_opt.additional_properties = d
        return sys_firmware_upgrade_opt

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
