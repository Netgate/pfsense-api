from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_git_sync_settings import SystemGitSyncSettings
    from ..models.system_update_boot_envs_settings import SystemUpdateBootEnvsSettings
    from ..models.system_update_firmware_branch import SystemUpdateFirmwareBranch


T = TypeVar("T", bound="SystemUpdateSettings")


@_attrs_define
class SystemUpdateSettings:
    """
    Attributes:
        firmware_branch (Union[Unset, str]):
        firmware_branches (Union[Unset, List['SystemUpdateFirmwareBranch']]):
        disable_check (Union[Unset, bool]):
        boot_envs (Union[Unset, SystemUpdateBootEnvsSettings]):
        git_sync (Union[Unset, SystemGitSyncSettings]):
    """

    firmware_branch: Union[Unset, str] = UNSET
    firmware_branches: Union[Unset, List["SystemUpdateFirmwareBranch"]] = UNSET
    disable_check: Union[Unset, bool] = UNSET
    boot_envs: Union[Unset, "SystemUpdateBootEnvsSettings"] = UNSET
    git_sync: Union[Unset, "SystemGitSyncSettings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        firmware_branch = self.firmware_branch

        firmware_branches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.firmware_branches, Unset):
            firmware_branches = []
            for firmware_branches_item_data in self.firmware_branches:
                firmware_branches_item = firmware_branches_item_data.to_dict()
                firmware_branches.append(firmware_branches_item)

        disable_check = self.disable_check

        boot_envs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.boot_envs, Unset):
            boot_envs = self.boot_envs.to_dict()

        git_sync: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.git_sync, Unset):
            git_sync = self.git_sync.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if firmware_branch is not UNSET:
            field_dict["firmware_branch"] = firmware_branch
        if firmware_branches is not UNSET:
            field_dict["firmware_branches"] = firmware_branches
        if disable_check is not UNSET:
            field_dict["disable_check"] = disable_check
        if boot_envs is not UNSET:
            field_dict["boot_envs"] = boot_envs
        if git_sync is not UNSET:
            field_dict["git_sync"] = git_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_git_sync_settings import SystemGitSyncSettings
        from ..models.system_update_boot_envs_settings import SystemUpdateBootEnvsSettings
        from ..models.system_update_firmware_branch import SystemUpdateFirmwareBranch

        d = src_dict.copy()
        firmware_branch = d.pop("firmware_branch", UNSET)

        firmware_branches = []
        _firmware_branches = d.pop("firmware_branches", UNSET)
        for firmware_branches_item_data in _firmware_branches or []:
            firmware_branches_item = SystemUpdateFirmwareBranch.from_dict(firmware_branches_item_data)

            firmware_branches.append(firmware_branches_item)

        disable_check = d.pop("disable_check", UNSET)

        _boot_envs = d.pop("boot_envs", UNSET)
        boot_envs: Union[Unset, SystemUpdateBootEnvsSettings]
        if isinstance(_boot_envs, Unset):
            boot_envs = UNSET
        else:
            boot_envs = SystemUpdateBootEnvsSettings.from_dict(_boot_envs)

        _git_sync = d.pop("git_sync", UNSET)
        git_sync: Union[Unset, SystemGitSyncSettings]
        if isinstance(_git_sync, Unset):
            git_sync = UNSET
        else:
            git_sync = SystemGitSyncSettings.from_dict(_git_sync)

        system_update_settings = cls(
            firmware_branch=firmware_branch,
            firmware_branches=firmware_branches,
            disable_check=disable_check,
            boot_envs=boot_envs,
            git_sync=git_sync,
        )

        system_update_settings.additional_properties = d
        return system_update_settings

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
