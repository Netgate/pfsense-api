from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SysFirmwareInfo")


@_attrs_define
class SysFirmwareInfo:
    """
    Attributes:
        current_version (str): current firmware of the system
        latest_version (str): firmware version for upgrading to
        status (str): status message, if the firmware upgrade is in progress
        message (str): message to display, e.g. error or expectation after upgrading
    """

    current_version: str
    latest_version: str
    status: str
    message: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_version = self.current_version

        latest_version = self.latest_version

        status = self.status

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_version": current_version,
                "latest_version": latest_version,
                "status": status,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_version = d.pop("current_version")

        latest_version = d.pop("latest_version")

        status = d.pop("status")

        message = d.pop("message")

        sys_firmware_info = cls(
            current_version=current_version,
            latest_version=latest_version,
            status=status,
            message=message,
        )

        sys_firmware_info.additional_properties = d
        return sys_firmware_info

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
