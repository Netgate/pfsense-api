from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.snort_download_action_action import SnortDownloadActionAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortDownloadAction")


@_attrs_define
class SnortDownloadAction:
    """
    Attributes:
        action (SnortDownloadActionAction | Unset): start, stop, suspend or resume downloading from the service
    """

    action: SnortDownloadActionAction | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: SnortDownloadActionAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = SnortDownloadActionAction(_action)

        snort_download_action = cls(
            action=action,
        )

        snort_download_action.additional_properties = d
        return snort_download_action

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
