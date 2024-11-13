import json
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
    from ..models.diag_backup_request import DiagBackupRequest


T = TypeVar("T", bound="DiagRestoreBackupBody")


@_attrs_define
class DiagRestoreBackupBody:
    """
    Attributes:
        backup (Union[Unset, DiagBackupRequest]):
        config (Union[Unset, File]):
    """

    backup: Union[Unset, "DiagBackupRequest"] = UNSET
    config: Union[Unset, File] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        backup: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.backup, Unset):
            backup = self.backup.to_dict()

        config: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup is not UNSET:
            field_dict["backup"] = backup
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        backup: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.backup, Unset):
            backup = (None, json.dumps(self.backup.to_dict()).encode(), "application/json")

        config: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_tuple()

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if backup is not UNSET:
            field_dict["backup"] = backup
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.diag_backup_request import DiagBackupRequest

        d = src_dict.copy()
        _backup = d.pop("backup", UNSET)
        backup: Union[Unset, DiagBackupRequest]
        if isinstance(_backup, Unset):
            backup = UNSET
        else:
            backup = DiagBackupRequest.from_dict(_backup)

        _config = d.pop("config", UNSET)
        config: Union[Unset, File]
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
