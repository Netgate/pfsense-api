from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControllerBackupRequest")


@_attrs_define
class ControllerBackupRequest:
    """
    Attributes:
        label (Union[Unset, str]):
        description (Union[Unset, str]):
        auto_backup (Union[Unset, bool]):
        acb_password (Union[Unset, str]):
    """

    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    auto_backup: Union[Unset, bool] = UNSET
    acb_password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        description = self.description

        auto_backup = self.auto_backup

        acb_password = self.acb_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if auto_backup is not UNSET:
            field_dict["auto_backup"] = auto_backup
        if acb_password is not UNSET:
            field_dict["acb_password"] = acb_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        auto_backup = d.pop("auto_backup", UNSET)

        acb_password = d.pop("acb_password", UNSET)

        controller_backup_request = cls(
            label=label,
            description=description,
            auto_backup=auto_backup,
            acb_password=acb_password,
        )

        controller_backup_request.additional_properties = d
        return controller_backup_request

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
