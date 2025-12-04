from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controller_backup import ControllerBackup


T = TypeVar("T", bound="ControllerBackups")


@_attrs_define
class ControllerBackups:
    """
    Attributes:
        backups (list[ControllerBackup] | Unset):
    """

    backups: list[ControllerBackup] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.backups, Unset):
            backups = []
            for backups_item_data in self.backups:
                backups_item = backups_item_data.to_dict()
                backups.append(backups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backups is not UNSET:
            field_dict["backups"] = backups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.controller_backup import ControllerBackup

        d = dict(src_dict)
        _backups = d.pop("backups", UNSET)
        backups: list[ControllerBackup] | Unset = UNSET
        if _backups is not UNSET:
            backups = []
            for backups_item_data in _backups:
                backups_item = ControllerBackup.from_dict(backups_item_data)

                backups.append(backups_item)

        controller_backups = cls(
            backups=backups,
        )

        controller_backups.additional_properties = d
        return controller_backups

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
