from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.os_socket import OsSocket


T = TypeVar("T", bound="OsSocketList")


@_attrs_define
class OsSocketList:
    """
    Attributes:
        ipv4 (list[OsSocket] | Unset):
        ipv6 (list[OsSocket] | Unset):
    """

    ipv4: list[OsSocket] | Unset = UNSET
    ipv6: list[OsSocket] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv4: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ipv4, Unset):
            ipv4 = []
            for ipv4_item_data in self.ipv4:
                ipv4_item = ipv4_item_data.to_dict()
                ipv4.append(ipv4_item)

        ipv6: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ipv6, Unset):
            ipv6 = []
            for ipv6_item_data in self.ipv6:
                ipv6_item = ipv6_item_data.to_dict()
                ipv6.append(ipv6_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipv4 is not UNSET:
            field_dict["ipv4"] = ipv4
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.os_socket import OsSocket

        d = dict(src_dict)
        _ipv4 = d.pop("ipv4", UNSET)
        ipv4: list[OsSocket] | Unset = UNSET
        if _ipv4 is not UNSET:
            ipv4 = []
            for ipv4_item_data in _ipv4:
                ipv4_item = OsSocket.from_dict(ipv4_item_data)

                ipv4.append(ipv4_item)

        _ipv6 = d.pop("ipv6", UNSET)
        ipv6: list[OsSocket] | Unset = UNSET
        if _ipv6 is not UNSET:
            ipv6 = []
            for ipv6_item_data in _ipv6:
                ipv6_item = OsSocket.from_dict(ipv6_item_data)

                ipv6.append(ipv6_item)

        os_socket_list = cls(
            ipv4=ipv4,
            ipv6=ipv6,
        )

        os_socket_list.additional_properties = d
        return os_socket_list

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
