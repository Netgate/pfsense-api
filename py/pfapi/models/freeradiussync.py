from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.freeradiussync_row import FreeradiussyncRow


T = TypeVar("T", bound="Freeradiussync")


@_attrs_define
class Freeradiussync:
    """
    Attributes:
        syncenablexmlrpc (str | Unset): (FreeRADIUS XMLRPC Sync) Enable Sync (auto, manual, disabled)

            Select a sync method for FreeRADIUS.

            Important: While using "Sync to host(s) defined below",
            only sync from host A to B, A to C but do not enable XMLRPC sync to A. This will result in a loop!
        synctimeout (str | Unset): (FreeRADIUS XMLRPC Sync) XMLRPC timeout

            Timeout in seconds for the XMLRPC timeout.
            Default: 150
        row (list[FreeradiussyncRow] | Unset):
    """

    syncenablexmlrpc: str | Unset = UNSET
    synctimeout: str | Unset = UNSET
    row: list[FreeradiussyncRow] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        syncenablexmlrpc = self.syncenablexmlrpc

        synctimeout = self.synctimeout

        row: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if syncenablexmlrpc is not UNSET:
            field_dict["syncenablexmlrpc"] = syncenablexmlrpc
        if synctimeout is not UNSET:
            field_dict["synctimeout"] = synctimeout
        if row is not UNSET:
            field_dict["row"] = row

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.freeradiussync_row import FreeradiussyncRow

        d = dict(src_dict)
        syncenablexmlrpc = d.pop("syncenablexmlrpc", UNSET)

        synctimeout = d.pop("synctimeout", UNSET)

        _row = d.pop("row", UNSET)
        row: list[FreeradiussyncRow] | Unset = UNSET
        if _row is not UNSET:
            row = []
            for row_item_data in _row:
                row_item = FreeradiussyncRow.from_dict(row_item_data)

                row.append(row_item)

        freeradiussync = cls(
            syncenablexmlrpc=syncenablexmlrpc,
            synctimeout=synctimeout,
            row=row,
        )

        freeradiussync.additional_properties = d
        return freeradiussync

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
