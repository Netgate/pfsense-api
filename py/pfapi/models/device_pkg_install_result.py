from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DevicePkgInstallResult")


@_attrs_define
class DevicePkgInstallResult:
    """
    Attributes:
        device_id (str):
        previous_version (str):
        active_version (str):
        install_messages (str):
        result (str):
    """

    device_id: str
    previous_version: str
    active_version: str
    install_messages: str
    result: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_id = self.device_id

        previous_version = self.previous_version

        active_version = self.active_version

        install_messages = self.install_messages

        result = self.result

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "device_id": device_id,
                "previous_version": previous_version,
                "active_version": active_version,
                "install_messages": install_messages,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("device_id")

        previous_version = d.pop("previous_version")

        active_version = d.pop("active_version")

        install_messages = d.pop("install_messages")

        result = d.pop("result")

        device_pkg_install_result = cls(
            device_id=device_id,
            previous_version=previous_version,
            active_version=active_version,
            install_messages=install_messages,
            result=result,
        )

        device_pkg_install_result.additional_properties = d
        return device_pkg_install_result

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
