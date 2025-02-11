from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemGitSyncSettings")


@_attrs_define
class SystemGitSyncSettings:
    """
    Attributes:
        sync_on_upgrade (bool):
        repo_url (str):
        minimal (bool):
        diff (bool):
        show_files (bool):
        show_command (bool):
        dry_run (bool):
        branches (Union[Unset, List[str]]):
    """

    sync_on_upgrade: bool
    repo_url: str
    minimal: bool
    diff: bool
    show_files: bool
    show_command: bool
    dry_run: bool
    branches: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sync_on_upgrade = self.sync_on_upgrade

        repo_url = self.repo_url

        minimal = self.minimal

        diff = self.diff

        show_files = self.show_files

        show_command = self.show_command

        dry_run = self.dry_run

        branches: Union[Unset, List[str]] = UNSET
        if not isinstance(self.branches, Unset):
            branches = self.branches

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_on_upgrade": sync_on_upgrade,
                "repo_url": repo_url,
                "minimal": minimal,
                "diff": diff,
                "show_files": show_files,
                "show_command": show_command,
                "dry_run": dry_run,
            }
        )
        if branches is not UNSET:
            field_dict["branches"] = branches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sync_on_upgrade = d.pop("sync_on_upgrade")

        repo_url = d.pop("repo_url")

        minimal = d.pop("minimal")

        diff = d.pop("diff")

        show_files = d.pop("show_files")

        show_command = d.pop("show_command")

        dry_run = d.pop("dry_run")

        branches = cast(List[str], d.pop("branches", UNSET))

        system_git_sync_settings = cls(
            sync_on_upgrade=sync_on_upgrade,
            repo_url=repo_url,
            minimal=minimal,
            diff=diff,
            show_files=show_files,
            show_command=show_command,
            dry_run=dry_run,
            branches=branches,
        )

        system_git_sync_settings.additional_properties = d
        return system_git_sync_settings

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
