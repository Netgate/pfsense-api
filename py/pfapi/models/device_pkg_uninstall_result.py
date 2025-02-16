from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DevicePkgUninstallResult")


@_attrs_define
class DevicePkgUninstallResult:
    """
    Attributes:
        device_id (str):
        uninstall_messages (str):
        result (str):
    """

    device_id: str
    uninstall_messages: str
    result: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_id = self.device_id

        uninstall_messages = self.uninstall_messages

        result = self.result

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "device_id": device_id,
                "uninstall_messages": uninstall_messages,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("device_id")

        uninstall_messages = d.pop("uninstall_messages")

        result = d.pop("result")

        device_pkg_uninstall_result = cls(
            device_id=device_id,
            uninstall_messages=uninstall_messages,
            result=result,
        )

        device_pkg_uninstall_result.additional_properties = d
        return device_pkg_uninstall_result

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
