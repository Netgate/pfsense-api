from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortRuleFileContents")


@_attrs_define
class SnortRuleFileContents:
    """
    Attributes:
        filename (str | Unset): path of file
        ruleset (str | Unset): name of ruleset
        contents (str | Unset): contents of file
        content_type (str | Unset): type of file
    """

    filename: str | Unset = UNSET
    ruleset: str | Unset = UNSET
    contents: str | Unset = UNSET
    content_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        ruleset = self.ruleset

        contents = self.contents

        content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filename is not UNSET:
            field_dict["filename"] = filename
        if ruleset is not UNSET:
            field_dict["ruleset"] = ruleset
        if contents is not UNSET:
            field_dict["contents"] = contents
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename", UNSET)

        ruleset = d.pop("ruleset", UNSET)

        contents = d.pop("contents", UNSET)

        content_type = d.pop("content_type", UNSET)

        snort_rule_file_contents = cls(
            filename=filename,
            ruleset=ruleset,
            contents=contents,
            content_type=content_type,
        )

        snort_rule_file_contents.additional_properties = d
        return snort_rule_file_contents

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
