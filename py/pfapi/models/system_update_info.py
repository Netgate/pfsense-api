from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_update_firmware_branch import SystemUpdateFirmwareBranch


T = TypeVar("T", bound="SystemUpdateInfo")


@_attrs_define
class SystemUpdateInfo:
    """
    Attributes:
        firmware_branch (str | Unset):
        firmware_branches (list[SystemUpdateFirmwareBranch] | Unset):
        messages (list[str] | Unset):
        boot_env (str | Unset):
        curr_base_system (str | Unset):
        latest_base_system (str | Unset):
        status_message (str | Unset):
        update_messages (list[str] | Unset):
    """

    firmware_branch: str | Unset = UNSET
    firmware_branches: list[SystemUpdateFirmwareBranch] | Unset = UNSET
    messages: list[str] | Unset = UNSET
    boot_env: str | Unset = UNSET
    curr_base_system: str | Unset = UNSET
    latest_base_system: str | Unset = UNSET
    status_message: str | Unset = UNSET
    update_messages: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        firmware_branch = self.firmware_branch

        firmware_branches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.firmware_branches, Unset):
            firmware_branches = []
            for firmware_branches_item_data in self.firmware_branches:
                firmware_branches_item = firmware_branches_item_data.to_dict()
                firmware_branches.append(firmware_branches_item)

        messages: list[str] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages

        boot_env = self.boot_env

        curr_base_system = self.curr_base_system

        latest_base_system = self.latest_base_system

        status_message = self.status_message

        update_messages: list[str] | Unset = UNSET
        if not isinstance(self.update_messages, Unset):
            update_messages = self.update_messages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if firmware_branch is not UNSET:
            field_dict["firmware_branch"] = firmware_branch
        if firmware_branches is not UNSET:
            field_dict["firmware_branches"] = firmware_branches
        if messages is not UNSET:
            field_dict["messages"] = messages
        if boot_env is not UNSET:
            field_dict["boot_env"] = boot_env
        if curr_base_system is not UNSET:
            field_dict["curr_base_system"] = curr_base_system
        if latest_base_system is not UNSET:
            field_dict["latest_base_system"] = latest_base_system
        if status_message is not UNSET:
            field_dict["status_message"] = status_message
        if update_messages is not UNSET:
            field_dict["update_messages"] = update_messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_update_firmware_branch import SystemUpdateFirmwareBranch

        d = dict(src_dict)
        firmware_branch = d.pop("firmware_branch", UNSET)

        _firmware_branches = d.pop("firmware_branches", UNSET)
        firmware_branches: list[SystemUpdateFirmwareBranch] | Unset = UNSET
        if _firmware_branches is not UNSET:
            firmware_branches = []
            for firmware_branches_item_data in _firmware_branches:
                firmware_branches_item = SystemUpdateFirmwareBranch.from_dict(firmware_branches_item_data)

                firmware_branches.append(firmware_branches_item)

        messages = cast(list[str], d.pop("messages", UNSET))

        boot_env = d.pop("boot_env", UNSET)

        curr_base_system = d.pop("curr_base_system", UNSET)

        latest_base_system = d.pop("latest_base_system", UNSET)

        status_message = d.pop("status_message", UNSET)

        update_messages = cast(list[str], d.pop("update_messages", UNSET))

        system_update_info = cls(
            firmware_branch=firmware_branch,
            firmware_branches=firmware_branches,
            messages=messages,
            boot_env=boot_env,
            curr_base_system=curr_base_system,
            latest_base_system=latest_base_system,
            status_message=status_message,
            update_messages=update_messages,
        )

        system_update_info.additional_properties = d
        return system_update_info

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
