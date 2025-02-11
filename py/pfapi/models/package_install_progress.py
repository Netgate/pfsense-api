from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageInstallProgress")


@_attrs_define
class PackageInstallProgress:
    """
    Attributes:
        name (str):
        version (str):
        percent (int):
        error (str):
        action (str):
        messages (Union[Unset, List[str]]):
    """

    name: str
    version: str
    percent: int
    error: str
    action: str
    messages: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        version = self.version

        percent = self.percent

        error = self.error

        action = self.action

        messages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "version": version,
                "percent": percent,
                "error": error,
                "action": action,
            }
        )
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        version = d.pop("version")

        percent = d.pop("percent")

        error = d.pop("error")

        action = d.pop("action")

        messages = cast(List[str], d.pop("messages", UNSET))

        package_install_progress = cls(
            name=name,
            version=version,
            percent=percent,
            error=error,
            action=action,
            messages=messages,
        )

        package_install_progress.additional_properties = d
        return package_install_progress

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
