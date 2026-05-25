from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyFile")


@_attrs_define
class HaproxyFile:
    """
    Attributes:
        name (str | Unset): File Name

            Unique name for this file. Used to reference it from error file configurations.
        type_ (str | Unset): File Type (errorfile, luascript, writetodisk)

            Type of HAProxy file.
            - errorfile: Custom HTTP error response page
            - luascript: Lua script loaded by HAProxy
            - writetodisk: File written to disk for use in HAProxy configuration
            (Default: errorfile)
        content (str | Unset): File Content

            Content of the file. For error files, this should include the complete
            HTTP response including status line and headers.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    content: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        content = self.content

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if content is not UNSET:
            field_dict["content"] = content
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        content = d.pop("content", UNSET)

        id = d.pop("id", UNSET)

        haproxy_file = cls(
            name=name,
            type_=type_,
            content=content,
            id=id,
        )

        haproxy_file.additional_properties = d
        return haproxy_file

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
