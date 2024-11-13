from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        firmware_branch (Union[Unset, str]):
        firmware_branches (Union[Unset, List['SystemUpdateFirmwareBranch']]):
        messages (Union[Unset, List[str]]):
        boot_env (Union[Unset, str]):
        curr_base_system (Union[Unset, str]):
        latest_base_system (Union[Unset, str]):
        status_message (Union[Unset, str]):
        update_messages (Union[Unset, List[str]]):
    """

    firmware_branch: Union[Unset, str] = UNSET
    firmware_branches: Union[Unset, List["SystemUpdateFirmwareBranch"]] = UNSET
    messages: Union[Unset, List[str]] = UNSET
    boot_env: Union[Unset, str] = UNSET
    curr_base_system: Union[Unset, str] = UNSET
    latest_base_system: Union[Unset, str] = UNSET
    status_message: Union[Unset, str] = UNSET
    update_messages: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        firmware_branch = self.firmware_branch

        firmware_branches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.firmware_branches, Unset):
            firmware_branches = []
            for firmware_branches_item_data in self.firmware_branches:
                firmware_branches_item = firmware_branches_item_data.to_dict()
                firmware_branches.append(firmware_branches_item)

        messages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages

        boot_env = self.boot_env

        curr_base_system = self.curr_base_system

        latest_base_system = self.latest_base_system

        status_message = self.status_message

        update_messages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.update_messages, Unset):
            update_messages = self.update_messages

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_update_firmware_branch import SystemUpdateFirmwareBranch

        d = src_dict.copy()
        firmware_branch = d.pop("firmware_branch", UNSET)

        firmware_branches = []
        _firmware_branches = d.pop("firmware_branches", UNSET)
        for firmware_branches_item_data in _firmware_branches or []:
            firmware_branches_item = SystemUpdateFirmwareBranch.from_dict(firmware_branches_item_data)

            firmware_branches.append(firmware_branches_item)

        messages = cast(List[str], d.pop("messages", UNSET))

        boot_env = d.pop("boot_env", UNSET)

        curr_base_system = d.pop("curr_base_system", UNSET)

        latest_base_system = d.pop("latest_base_system", UNSET)

        status_message = d.pop("status_message", UNSET)

        update_messages = cast(List[str], d.pop("update_messages", UNSET))

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
