from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecWidgetMobile")


@_attrs_define
class IPSecWidgetMobile:
    """
    Attributes:
        user (str | Unset):
        ip (str | Unset):
        status (str | Unset):
    """

    user: str | Unset = UNSET
    ip: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        ip = self.ip

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if ip is not UNSET:
            field_dict["ip"] = ip
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = d.pop("user", UNSET)

        ip = d.pop("ip", UNSET)

        status = d.pop("status", UNSET)

        ip_sec_widget_mobile = cls(
            user=user,
            ip=ip,
            status=status,
        )

        ip_sec_widget_mobile.additional_properties = d
        return ip_sec_widget_mobile

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
