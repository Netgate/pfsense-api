from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterReloadStatus")


@_attrs_define
class FilterReloadStatus:
    """
    Attributes:
        ongoing (bool | Unset):
        done (bool | Unset):
        status_lines (list[str] | Unset):
        ha_xmlrpc_enabled (bool | Unset):
    """

    ongoing: bool | Unset = UNSET
    done: bool | Unset = UNSET
    status_lines: list[str] | Unset = UNSET
    ha_xmlrpc_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ongoing = self.ongoing

        done = self.done

        status_lines: list[str] | Unset = UNSET
        if not isinstance(self.status_lines, Unset):
            status_lines = self.status_lines

        ha_xmlrpc_enabled = self.ha_xmlrpc_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ongoing is not UNSET:
            field_dict["ongoing"] = ongoing
        if done is not UNSET:
            field_dict["done"] = done
        if status_lines is not UNSET:
            field_dict["status_lines"] = status_lines
        if ha_xmlrpc_enabled is not UNSET:
            field_dict["ha_xmlrpc_enabled"] = ha_xmlrpc_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ongoing = d.pop("ongoing", UNSET)

        done = d.pop("done", UNSET)

        status_lines = cast(list[str], d.pop("status_lines", UNSET))

        ha_xmlrpc_enabled = d.pop("ha_xmlrpc_enabled", UNSET)

        filter_reload_status = cls(
            ongoing=ongoing,
            done=done,
            status_lines=status_lines,
            ha_xmlrpc_enabled=ha_xmlrpc_enabled,
        )

        filter_reload_status.additional_properties = d
        return filter_reload_status

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
