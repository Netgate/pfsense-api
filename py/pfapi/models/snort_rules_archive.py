from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortRulesArchive")


@_attrs_define
class SnortRulesArchive:
    """Archives are the bundles that contain the rulesets.
    For example, they are provided by Snort Talos subscription or
    from Emerging Threats.
    This object provides metadata about the contents of the archive.

        Attributes:
            files (list[str] | Unset):
            version (str | Unset): version encode in archive
            download_time (str | Unset): time (RFC-3339) of when downloaded
            download_location (str | Unset): address of source or uploaded if user provided
            in_progress (bool | Unset): is ruleset currently being downloaded
            percent_avail (int | Unset): if the ruleset is from a URL, then the percentage downloaded
    """

    files: list[str] | Unset = UNSET
    version: str | Unset = UNSET
    download_time: str | Unset = UNSET
    download_location: str | Unset = UNSET
    in_progress: bool | Unset = UNSET
    percent_avail: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: list[str] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files

        version = self.version

        download_time = self.download_time

        download_location = self.download_location

        in_progress = self.in_progress

        percent_avail = self.percent_avail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if version is not UNSET:
            field_dict["version"] = version
        if download_time is not UNSET:
            field_dict["download_time"] = download_time
        if download_location is not UNSET:
            field_dict["download_location"] = download_location
        if in_progress is not UNSET:
            field_dict["in_progress"] = in_progress
        if percent_avail is not UNSET:
            field_dict["percent_avail"] = percent_avail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        files = cast(list[str], d.pop("files", UNSET))

        version = d.pop("version", UNSET)

        download_time = d.pop("download_time", UNSET)

        download_location = d.pop("download_location", UNSET)

        in_progress = d.pop("in_progress", UNSET)

        percent_avail = d.pop("percent_avail", UNSET)

        snort_rules_archive = cls(
            files=files,
            version=version,
            download_time=download_time,
            download_location=download_location,
            in_progress=in_progress,
            percent_avail=percent_avail,
        )

        snort_rules_archive.additional_properties = d
        return snort_rules_archive

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
