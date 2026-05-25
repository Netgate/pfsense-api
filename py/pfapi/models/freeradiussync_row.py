from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FreeradiussyncRow")


@_attrs_define
class FreeradiussyncRow:
    """
    Attributes:
        syncdestinenable (str | Unset): Enable
        syncprotocol (str | Unset): Protocol (http, https)
        syncipaddress (str | Unset): IP Address/Hostname
        syncport (str | Unset): Port
        syncusername (str | Unset): Username
        syncpassword (str | Unset): Password
    """

    syncdestinenable: str | Unset = UNSET
    syncprotocol: str | Unset = UNSET
    syncipaddress: str | Unset = UNSET
    syncport: str | Unset = UNSET
    syncusername: str | Unset = UNSET
    syncpassword: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        syncdestinenable = self.syncdestinenable

        syncprotocol = self.syncprotocol

        syncipaddress = self.syncipaddress

        syncport = self.syncport

        syncusername = self.syncusername

        syncpassword = self.syncpassword

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if syncdestinenable is not UNSET:
            field_dict["syncdestinenable"] = syncdestinenable
        if syncprotocol is not UNSET:
            field_dict["syncprotocol"] = syncprotocol
        if syncipaddress is not UNSET:
            field_dict["syncipaddress"] = syncipaddress
        if syncport is not UNSET:
            field_dict["syncport"] = syncport
        if syncusername is not UNSET:
            field_dict["syncusername"] = syncusername
        if syncpassword is not UNSET:
            field_dict["syncpassword"] = syncpassword

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        syncdestinenable = d.pop("syncdestinenable", UNSET)

        syncprotocol = d.pop("syncprotocol", UNSET)

        syncipaddress = d.pop("syncipaddress", UNSET)

        syncport = d.pop("syncport", UNSET)

        syncusername = d.pop("syncusername", UNSET)

        syncpassword = d.pop("syncpassword", UNSET)

        freeradiussync_row = cls(
            syncdestinenable=syncdestinenable,
            syncprotocol=syncprotocol,
            syncipaddress=syncipaddress,
            syncport=syncport,
            syncusername=syncusername,
            syncpassword=syncpassword,
        )

        freeradiussync_row.additional_properties = d
        return freeradiussync_row

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
