from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        backups (Union[Unset, List['ControllerBackup']]):
    """

    backups: Union[Unset, List["ControllerBackup"]] = UNSET
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
        from ..models.controller_backup import ControllerBackup

        d = src_dict.copy()
        backups = []
        _backups = d.pop("backups", UNSET)
        for backups_item_data in _backups or []:
            backups_item = ControllerBackup.from_dict(backups_item_data)

            backups.append(backups_item)

        controller_backups = cls(
            backups=backups,
        )

        controller_backups.additional_properties = d
        return controller_backups

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
