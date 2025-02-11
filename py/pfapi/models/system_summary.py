from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SystemSummary")


@_attrs_define
class SystemSummary:
    """
    Attributes:
        name (str):
        os (str):
        arch (str):
        api_version (str):
    """

    name: str
    os: str
    arch: str
    api_version: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        os = self.os

        arch = self.arch

        api_version = self.api_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "os": os,
                "arch": arch,
                "api_version": api_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        os = d.pop("os")

        arch = d.pop("arch")

        api_version = d.pop("api_version")

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
