from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Package")


@_attrs_define
class Package:
    """
    Attributes:
        name (str | Unset):
        internal_name (str | Unset):
        info_link (str | Unset):
        descr (str | Unset):
        version (str | Unset):
        config_file (str | Unset):
        include_file (str | Unset):
        category (str | Unset):
        depedencies (list[str] | Unset):
    """

    name: str | Unset = UNSET
    internal_name: str | Unset = UNSET
    info_link: str | Unset = UNSET
    descr: str | Unset = UNSET
    version: str | Unset = UNSET
    config_file: str | Unset = UNSET
    include_file: str | Unset = UNSET
    category: str | Unset = UNSET
    depedencies: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        internal_name = self.internal_name

        info_link = self.info_link

        descr = self.descr

        version = self.version

        config_file = self.config_file

        include_file = self.include_file

        category = self.category

        depedencies: list[str] | Unset = UNSET
        if not isinstance(self.depedencies, Unset):
            depedencies = self.depedencies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if internal_name is not UNSET:
            field_dict["internal_name"] = internal_name
        if info_link is not UNSET:
            field_dict["info_link"] = info_link
        if descr is not UNSET:
            field_dict["descr"] = descr
        if version is not UNSET:
            field_dict["version"] = version
        if config_file is not UNSET:
            field_dict["config_file"] = config_file
        if include_file is not UNSET:
            field_dict["include_file"] = include_file
        if category is not UNSET:
            field_dict["category"] = category
        if depedencies is not UNSET:
            field_dict["depedencies"] = depedencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        internal_name = d.pop("internal_name", UNSET)

        info_link = d.pop("info_link", UNSET)

        descr = d.pop("descr", UNSET)

        version = d.pop("version", UNSET)

        config_file = d.pop("config_file", UNSET)

        include_file = d.pop("include_file", UNSET)

        category = d.pop("category", UNSET)

        depedencies = cast(list[str], d.pop("depedencies", UNSET))

        package = cls(
            name=name,
            internal_name=internal_name,
            info_link=info_link,
            descr=descr,
            version=version,
            config_file=config_file,
            include_file=include_file,
            category=category,
            depedencies=depedencies,
        )

        package.additional_properties = d
        return package

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
