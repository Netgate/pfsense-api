from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.os_socket_list import OsSocketList


T = TypeVar("T", bound="DiagSocketStats")


@_attrs_define
class DiagSocketStats:
    """
    Attributes:
        sockets (OsSocketList | Unset):
    """

    sockets: OsSocketList | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sockets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sockets, Unset):
            sockets = self.sockets.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sockets is not UNSET:
            field_dict["sockets"] = sockets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.os_socket_list import OsSocketList

        d = dict(src_dict)
        _sockets = d.pop("sockets", UNSET)
        sockets: OsSocketList | Unset
        if isinstance(_sockets, Unset):
            sockets = UNSET
        else:
            sockets = OsSocketList.from_dict(_sockets)

        diag_socket_stats = cls(
            sockets=sockets,
        )

        diag_socket_stats.additional_properties = d
        return diag_socket_stats

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
