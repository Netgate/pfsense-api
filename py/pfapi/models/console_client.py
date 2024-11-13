from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsoleClient")


@_attrs_define
class ConsoleClient:
    """
    Attributes:
        addr (Union[Unset, str]):
        type (Union[Unset, str]):
        time (Union[Unset, int]):
    """

    addr: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        addr = self.addr

        type = self.type

        time = self.time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addr is not UNSET:
            field_dict["addr"] = addr
        if type is not UNSET:
            field_dict["type"] = type
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        addr = d.pop("addr", UNSET)

        type = d.pop("type", UNSET)

        time = d.pop("time", UNSET)

        console_client = cls(
            addr=addr,
            type=type,
            time=time,
        )

        console_client.additional_properties = d
        return console_client

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
