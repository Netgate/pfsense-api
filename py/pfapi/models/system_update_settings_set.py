from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_update_boot_envs_settings import SystemUpdateBootEnvsSettings


T = TypeVar("T", bound="SystemUpdateSettingsSet")


@_attrs_define
class SystemUpdateSettingsSet:
    """
    Attributes:
        firmware_branch (Union[Unset, str]):
        disable_check (Union[Unset, bool]):
        boot_envs (Union[Unset, SystemUpdateBootEnvsSettings]):
    """

    firmware_branch: Union[Unset, str] = UNSET
    disable_check: Union[Unset, bool] = UNSET
    boot_envs: Union[Unset, "SystemUpdateBootEnvsSettings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        firmware_branch = self.firmware_branch

        disable_check = self.disable_check

        boot_envs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.boot_envs, Unset):
            boot_envs = self.boot_envs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if firmware_branch is not UNSET:
            field_dict["firmware_branch"] = firmware_branch
        if disable_check is not UNSET:
            field_dict["disable_check"] = disable_check
        if boot_envs is not UNSET:
            field_dict["boot_envs"] = boot_envs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_update_boot_envs_settings import SystemUpdateBootEnvsSettings

        d = src_dict.copy()
        firmware_branch = d.pop("firmware_branch", UNSET)

        disable_check = d.pop("disable_check", UNSET)

        _boot_envs = d.pop("boot_envs", UNSET)
        boot_envs: Union[Unset, SystemUpdateBootEnvsSettings]
        if isinstance(_boot_envs, Unset):
            boot_envs = UNSET
        else:
            boot_envs = SystemUpdateBootEnvsSettings.from_dict(_boot_envs)

        system_update_settings_set = cls(
            firmware_branch=firmware_branch,
            disable_check=disable_check,
            boot_envs=boot_envs,
        )

        system_update_settings_set.additional_properties = d
        return system_update_settings_set

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
