from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.system_update_boot_envs_settings import SystemUpdateBootEnvsSettings


T = TypeVar("T", bound="SystemUpdateSettingsSet")


@_attrs_define
class SystemUpdateSettingsSet:
    """
    Attributes:
        firmware_branch (str):
        disable_check (bool):
        boot_envs (SystemUpdateBootEnvsSettings):
    """

    firmware_branch: str
    disable_check: bool
    boot_envs: "SystemUpdateBootEnvsSettings"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        firmware_branch = self.firmware_branch

        disable_check = self.disable_check

        boot_envs = self.boot_envs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firmware_branch": firmware_branch,
                "disable_check": disable_check,
                "boot_envs": boot_envs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_update_boot_envs_settings import SystemUpdateBootEnvsSettings

        d = src_dict.copy()
        firmware_branch = d.pop("firmware_branch")

        disable_check = d.pop("disable_check")

        boot_envs = SystemUpdateBootEnvsSettings.from_dict(d.pop("boot_envs"))

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
