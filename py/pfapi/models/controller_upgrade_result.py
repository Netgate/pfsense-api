from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControllerUpgradeResult")


@_attrs_define
class ControllerUpgradeResult:
    """
    Attributes:
        active_version (str):
        previous_version (str):
        restart_time (int):
        messages (str):
    """

    active_version: str
    previous_version: str
    restart_time: int
    messages: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active_version = self.active_version

        previous_version = self.previous_version

        restart_time = self.restart_time

        messages = self.messages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active_version": active_version,
                "previous_version": previous_version,
                "restart_time": restart_time,
                "messages": messages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active_version = d.pop("active_version")

        previous_version = d.pop("previous_version")

        restart_time = d.pop("restart_time")

        messages = d.pop("messages")

        controller_upgrade_result = cls(
            active_version=active_version,
            previous_version=previous_version,
            restart_time=restart_time,
            messages=messages,
        )

        controller_upgrade_result.additional_properties = d
        return controller_upgrade_result

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
