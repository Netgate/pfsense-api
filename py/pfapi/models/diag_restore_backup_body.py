from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

if TYPE_CHECKING:
    from ..models.diag_backup_request import DiagBackupRequest


T = TypeVar("T", bound="DiagRestoreBackupBody")


@_attrs_define
class DiagRestoreBackupBody:
    """
    Attributes:
        backup (DiagBackupRequest | Unset):
        config (File | Unset):
    """

    backup: DiagBackupRequest | Unset = UNSET
    config: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup, Unset):
            backup = self.backup.to_dict()

        config: FileTypes | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup is not UNSET:
            field_dict["backup"] = backup
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.backup, Unset):
            files.append(("backup", (None, json.dumps(self.backup.to_dict()).encode(), "application/json")))

        if not isinstance(self.config, Unset):
            files.append(("config", self.config.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diag_backup_request import DiagBackupRequest

        d = dict(src_dict)
        _backup = d.pop("backup", UNSET)
        backup: DiagBackupRequest | Unset
        if isinstance(_backup, Unset):
            backup = UNSET
        else:
            backup = DiagBackupRequest.from_dict(_backup)

        _config = d.pop("config", UNSET)
        config: File | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = File(payload=BytesIO(_config))

        diag_restore_backup_body = cls(
            backup=backup,
            config=config,
        )

        diag_restore_backup_body.additional_properties = d
        return diag_restore_backup_body

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
