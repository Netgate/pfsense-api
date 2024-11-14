from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diag_backup_info import DiagBackupInfo


T = TypeVar("T", bound="DiagPriorBackupInfo")


@_attrs_define
class DiagPriorBackupInfo:
    """
    Attributes:
        backups (Union[Unset, List['DiagBackupInfo']]):
    """

    backups: Union[Unset, List["DiagBackupInfo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        backups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.backups, Unset):
            backups = []
            for backups_item_data in self.backups:
                backups_item = backups_item_data.to_dict()
                backups.append(backups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backups is not UNSET:
            field_dict["backups"] = backups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.diag_backup_info import DiagBackupInfo

        d = src_dict.copy()
        backups = []
        _backups = d.pop("backups", UNSET)
        for backups_item_data in _backups or []:
            backups_item = DiagBackupInfo.from_dict(backups_item_data)

            backups.append(backups_item)

        diag_prior_backup_info = cls(
            backups=backups,
        )

        diag_prior_backup_info.additional_properties = d
        return diag_prior_backup_info

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
