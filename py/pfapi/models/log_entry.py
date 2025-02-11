from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LogEntry")


@_attrs_define
class LogEntry:
    """
    Attributes:
        type (str):
        timestamp (int):
        device_name (str):
        device_address (str):
        class_ (str):
        message (str):
    """

    type: str
    timestamp: int
    device_name: str
    device_address: str
    class_: str
    message: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        timestamp = self.timestamp

        device_name = self.device_name

        device_address = self.device_address

        class_ = self.class_

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "timestamp": timestamp,
                "device_name": device_name,
                "device_address": device_address,
                "class": class_,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        timestamp = d.pop("timestamp")

        device_name = d.pop("device_name")

        device_address = d.pop("device_address")

        class_ = d.pop("class")

        message = d.pop("message")

        log_entry = cls(
            type=type,
            timestamp=timestamp,
            device_name=device_name,
            device_address=device_address,
            class_=class_,
            message=message,
        )

        log_entry.additional_properties = d
        return log_entry

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
