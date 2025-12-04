from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NtpServer")


@_attrs_define
class NtpServer:
    """
    Attributes:
        addr (str):
        type_ (str): pool | peer | server
        prefer (bool | Unset):
        no_select (bool | Unset):
    """

    addr: str
    type_: str
    prefer: bool | Unset = UNSET
    no_select: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addr = self.addr

        type_ = self.type_

        prefer = self.prefer

        no_select = self.no_select

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addr": addr,
                "type": type_,
            }
        )
        if prefer is not UNSET:
            field_dict["prefer"] = prefer
        if no_select is not UNSET:
            field_dict["no_select"] = no_select

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        addr = d.pop("addr")

        type_ = d.pop("type")

        prefer = d.pop("prefer", UNSET)

        no_select = d.pop("no_select", UNSET)

        ntp_server = cls(
            addr=addr,
            type_=type_,
            prefer=prefer,
            no_select=no_select,
        )

        ntp_server.additional_properties = d
        return ntp_server

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
