from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortRulesUploadReq")


@_attrs_define
class SnortRulesUploadReq:
    """
    Attributes:
        name (str | Unset): name to give to ruleset; can be empty if "url" is provided
        contents (str | Unset): if provided, then this should be a single rules text document
        url (str | Unset): alternative to file upload, provide the URL to download from
    """

    name: str | Unset = UNSET
    contents: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        contents = self.contents

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if contents is not UNSET:
            field_dict["contents"] = contents
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        contents = d.pop("contents", UNSET)

        url = d.pop("url", UNSET)

        snort_rules_upload_req = cls(
            name=name,
            contents=contents,
            url=url,
        )

        snort_rules_upload_req.additional_properties = d
        return snort_rules_upload_req

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
