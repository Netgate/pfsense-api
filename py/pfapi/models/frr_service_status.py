from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_daemon_status import FrrDaemonStatus


T = TypeVar("T", bound="FrrServiceStatus")


@_attrs_define
class FrrServiceStatus:
    """
    Attributes:
        running (bool | Unset): true if any FRR daemon is currently running
        status (str | Unset): human-readable service status ("running" or "stopped")
        daemons (list[FrrDaemonStatus] | Unset):
    """

    running: bool | Unset = UNSET
    status: str | Unset = UNSET
    daemons: list[FrrDaemonStatus] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        running = self.running

        status = self.status

        daemons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.daemons, Unset):
            daemons = []
            for daemons_item_data in self.daemons:
                daemons_item = daemons_item_data.to_dict()
                daemons.append(daemons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if running is not UNSET:
            field_dict["running"] = running
        if status is not UNSET:
            field_dict["status"] = status
        if daemons is not UNSET:
            field_dict["daemons"] = daemons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_daemon_status import FrrDaemonStatus

        d = dict(src_dict)
        running = d.pop("running", UNSET)

        status = d.pop("status", UNSET)

        _daemons = d.pop("daemons", UNSET)
        daemons: list[FrrDaemonStatus] | Unset = UNSET
        if _daemons is not UNSET:
            daemons = []
            for daemons_item_data in _daemons:
                daemons_item = FrrDaemonStatus.from_dict(daemons_item_data)

                daemons.append(daemons_item)

        frr_service_status = cls(
            running=running,
            status=status,
            daemons=daemons,
        )

        frr_service_status.additional_properties = d
        return frr_service_status

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
