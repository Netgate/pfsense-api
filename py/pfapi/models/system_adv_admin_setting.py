from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_adv_admin import SystemAdvAdmin


T = TypeVar("T", bound="SystemAdvAdminSetting")


@_attrs_define
class SystemAdvAdminSetting:
    """
    Attributes:
        admin (SystemAdvAdmin | Unset):
    """

    admin: SystemAdvAdmin | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.admin, Unset):
            admin = self.admin.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin is not UNSET:
            field_dict["admin"] = admin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_adv_admin import SystemAdvAdmin

        d = dict(src_dict)
        _admin = d.pop("admin", UNSET)
        admin: SystemAdvAdmin | Unset
        if isinstance(_admin, Unset):
            admin = UNSET
        else:
            admin = SystemAdvAdmin.from_dict(_admin)

        system_adv_admin_setting = cls(
            admin=admin,
        )

        system_adv_admin_setting.additional_properties = d
        return system_adv_admin_setting

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
