from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

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
        branches (list[str] | Unset):
        minimal (bool | Unset):
        diff (bool | Unset):
        show_files (bool | Unset):
        show_command (bool | Unset):
        dry_run (bool | Unset):
    """

    sync_on_upgrade: bool
    repo_url: str
    branches: list[str] | Unset = UNSET
    minimal: bool | Unset = UNSET
    diff: bool | Unset = UNSET
    show_files: bool | Unset = UNSET
    show_command: bool | Unset = UNSET
    dry_run: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_on_upgrade = self.sync_on_upgrade

        repo_url = self.repo_url

        branches: list[str] | Unset = UNSET
        if not isinstance(self.branches, Unset):
            branches = self.branches

        minimal = self.minimal

        diff = self.diff

        show_files = self.show_files

        show_command = self.show_command

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_on_upgrade": sync_on_upgrade,
                "repo_url": repo_url,
            }
        )
        if branches is not UNSET:
            field_dict["branches"] = branches
        if minimal is not UNSET:
            field_dict["minimal"] = minimal
        if diff is not UNSET:
            field_dict["diff"] = diff
        if show_files is not UNSET:
            field_dict["show_files"] = show_files
        if show_command is not UNSET:
            field_dict["show_command"] = show_command
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_on_upgrade = d.pop("sync_on_upgrade")

        repo_url = d.pop("repo_url")

        branches = cast(list[str], d.pop("branches", UNSET))

        minimal = d.pop("minimal", UNSET)

        diff = d.pop("diff", UNSET)

        show_files = d.pop("show_files", UNSET)

        show_command = d.pop("show_command", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        system_git_sync_settings = cls(
            sync_on_upgrade=sync_on_upgrade,
            repo_url=repo_url,
            branches=branches,
            minimal=minimal,
            diff=diff,
            show_files=show_files,
            show_command=show_command,
            dry_run=dry_run,
        )

        system_git_sync_settings.additional_properties = d
        return system_git_sync_settings

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
