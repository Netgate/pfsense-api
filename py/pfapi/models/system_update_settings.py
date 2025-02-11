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
        firmware_branch (str):
        disable_check (bool):
        boot_envs (SystemUpdateBootEnvsSettings):
        git_sync (SystemGitSyncSettings):
        firmware_branches (Union[Unset, List['SystemUpdateFirmwareBranch']]):
    """

    firmware_branch: str
    disable_check: bool
    boot_envs: "SystemUpdateBootEnvsSettings"
    git_sync: "SystemGitSyncSettings"
    firmware_branches: Union[Unset, List["SystemUpdateFirmwareBranch"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        firmware_branch = self.firmware_branch

        disable_check = self.disable_check

        boot_envs = self.boot_envs.to_dict()

        git_sync = self.git_sync.to_dict()

        firmware_branches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.firmware_branches, Unset):
            firmware_branches = []
            for firmware_branches_item_data in self.firmware_branches:
                firmware_branches_item = firmware_branches_item_data.to_dict()
                firmware_branches.append(firmware_branches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firmware_branch": firmware_branch,
                "disable_check": disable_check,
                "boot_envs": boot_envs,
                "git_sync": git_sync,
            }
        )
        if firmware_branches is not UNSET:
            field_dict["firmware_branches"] = firmware_branches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_git_sync_settings import SystemGitSyncSettings
        from ..models.system_update_boot_envs_settings import SystemUpdateBootEnvsSettings
        from ..models.system_update_firmware_branch import SystemUpdateFirmwareBranch

        d = src_dict.copy()
        firmware_branch = d.pop("firmware_branch")

        disable_check = d.pop("disable_check")

        boot_envs = SystemUpdateBootEnvsSettings.from_dict(d.pop("boot_envs"))

        git_sync = SystemGitSyncSettings.from_dict(d.pop("git_sync"))

        firmware_branches = []
        _firmware_branches = d.pop("firmware_branches", UNSET)
        for firmware_branches_item_data in _firmware_branches or []:
            firmware_branches_item = SystemUpdateFirmwareBranch.from_dict(firmware_branches_item_data)

            firmware_branches.append(firmware_branches_item)

        system_update_settings = cls(
            firmware_branch=firmware_branch,
            disable_check=disable_check,
            boot_envs=boot_envs,
            git_sync=git_sync,
            firmware_branches=firmware_branches,
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
