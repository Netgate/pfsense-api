from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogEntry")


@_attrs_define
class LogEntry:
    """
    Attributes:
        type (Union[Unset, str]):
        timestamp (Union[Unset, int]):
        timestr (Union[Unset, str]):
        device_name (Union[Unset, str]):
        device_address (Union[Unset, str]):
        class_ (Union[Unset, str]):
        message (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    timestamp: Union[Unset, int] = UNSET
    timestr: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    device_address: Union[Unset, str] = UNSET
    class_: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        timestamp = self.timestamp

        timestr = self.timestr

        device_name = self.device_name

        device_address = self.device_address

        class_ = self.class_

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if timestr is not UNSET:
            field_dict["timestr"] = timestr
        if device_name is not UNSET:
            field_dict["device_name"] = device_name
        if device_address is not UNSET:
            field_dict["device_address"] = device_address
        if class_ is not UNSET:
            field_dict["class"] = class_
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        timestr = d.pop("timestr", UNSET)

        device_name = d.pop("device_name", UNSET)

        device_address = d.pop("device_address", UNSET)

        class_ = d.pop("class", UNSET)

        message = d.pop("message", UNSET)

        log_entry = cls(
            type=type,
            timestamp=timestamp,
            timestr=timestr,
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
