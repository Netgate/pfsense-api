from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemSummary")


@_attrs_define
class SystemSummary:
    """
    Attributes:
        name (Union[Unset, str]): system name
        os (Union[Unset, str]): operating system
        arch (Union[Unset, str]): hardware architecture
        api_version (Union[Unset, str]): API version supported by this sytem
    """

    name: Union[Unset, str] = UNSET
    os: Union[Unset, str] = UNSET
    arch: Union[Unset, str] = UNSET
    api_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        os = self.os

        arch = self.arch

        api_version = self.api_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if os is not UNSET:
            field_dict["os"] = os
        if arch is not UNSET:
            field_dict["arch"] = arch
        if api_version is not UNSET:
            field_dict["api_version"] = api_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        os = d.pop("os", UNSET)

        arch = d.pop("arch", UNSET)

        api_version = d.pop("api_version", UNSET)

        system_summary = cls(
            name=name,
            os=os,
            arch=arch,
            api_version=api_version,
        )

        system_summary.additional_properties = d
        return system_summary

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
