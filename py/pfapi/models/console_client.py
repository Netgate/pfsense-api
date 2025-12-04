from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsoleClient")


@_attrs_define
class ConsoleClient:
    """
    Attributes:
        addr (str | Unset):
        type_ (str | Unset):
        time (int | Unset):
    """

    addr: str | Unset = UNSET
    type_: str | Unset = UNSET
    time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addr = self.addr

        type_ = self.type_

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addr is not UNSET:
            field_dict["addr"] = addr
        if type_ is not UNSET:
            field_dict["type"] = type_
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        addr = d.pop("addr", UNSET)

        type_ = d.pop("type", UNSET)

        time = d.pop("time", UNSET)

        console_client = cls(
            addr=addr,
            type_=type_,
            time=time,
        )

        console_client.additional_properties = d
        return console_client

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
