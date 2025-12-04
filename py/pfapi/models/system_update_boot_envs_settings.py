from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemUpdateBootEnvsSettings")


@_attrs_define
class SystemUpdateBootEnvsSettings:
    """
    Attributes:
        deferred_boot (bool | Unset):
        verify (bool | Unset):
        verify_timeout (int | Unset):
    """

    deferred_boot: bool | Unset = UNSET
    verify: bool | Unset = UNSET
    verify_timeout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deferred_boot = self.deferred_boot

        verify = self.verify

        verify_timeout = self.verify_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deferred_boot is not UNSET:
            field_dict["deferred_boot"] = deferred_boot
        if verify is not UNSET:
            field_dict["verify"] = verify
        if verify_timeout is not UNSET:
            field_dict["verify_timeout"] = verify_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deferred_boot = d.pop("deferred_boot", UNSET)

        verify = d.pop("verify", UNSET)

        verify_timeout = d.pop("verify_timeout", UNSET)

        system_update_boot_envs_settings = cls(
            deferred_boot=deferred_boot,
            verify=verify,
            verify_timeout=verify_timeout,
        )

        system_update_boot_envs_settings.additional_properties = d
        return system_update_boot_envs_settings

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
