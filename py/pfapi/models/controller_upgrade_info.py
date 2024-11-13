from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControllerUpgradeInfo")


@_attrs_define
class ControllerUpgradeInfo:
    """
    Attributes:
        current_version (Union[Unset, str]):
        new_version (Union[Unset, str]):
        changes (Union[Unset, str]):
    """

    current_version: Union[Unset, str] = UNSET
    new_version: Union[Unset, str] = UNSET
    changes: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_version = self.current_version

        new_version = self.new_version

        changes = self.changes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_version is not UNSET:
            field_dict["current_version"] = current_version
        if new_version is not UNSET:
            field_dict["new_version"] = new_version
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_version = d.pop("current_version", UNSET)

        new_version = d.pop("new_version", UNSET)

        changes = d.pop("changes", UNSET)

        controller_upgrade_info = cls(
            current_version=current_version,
            new_version=new_version,
            changes=changes,
        )

        controller_upgrade_info.additional_properties = d
        return controller_upgrade_info

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
