from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dirty_subsystems import DirtySubsystems
    from ..models.package_status import PackageStatus
    from ..models.status_summary_ui_features import StatusSummaryUiFeatures
    from ..models.system_status import SystemStatus


T = TypeVar("T", bound="StatusSummary")


@_attrs_define
class StatusSummary:
    """
    Attributes:
        status (SystemStatus | Unset):
        timestamp (int | Unset): millisecond timestamp of the system
        packages (list[PackageStatus] | Unset):
        dirty (DirtySubsystems | Unset):
        ui_features (StatusSummaryUiFeatures | Unset):
        alerts (str | Unset):
    """

    status: SystemStatus | Unset = UNSET
    timestamp: int | Unset = UNSET
    packages: list[PackageStatus] | Unset = UNSET
    dirty: DirtySubsystems | Unset = UNSET
    ui_features: StatusSummaryUiFeatures | Unset = UNSET
    alerts: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        timestamp = self.timestamp

        packages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        dirty: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dirty, Unset):
            dirty = self.dirty.to_dict()

        ui_features: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ui_features, Unset):
            ui_features = self.ui_features.to_dict()

        alerts = self.alerts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if packages is not UNSET:
            field_dict["packages"] = packages
        if dirty is not UNSET:
            field_dict["dirty"] = dirty
        if ui_features is not UNSET:
            field_dict["ui_features"] = ui_features
        if alerts is not UNSET:
            field_dict["alerts"] = alerts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dirty_subsystems import DirtySubsystems
        from ..models.package_status import PackageStatus
        from ..models.status_summary_ui_features import StatusSummaryUiFeatures
        from ..models.system_status import SystemStatus

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: SystemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SystemStatus.from_dict(_status)

        timestamp = d.pop("timestamp", UNSET)

        _packages = d.pop("packages", UNSET)
        packages: list[PackageStatus] | Unset = UNSET
        if _packages is not UNSET:
            packages = []
            for packages_item_data in _packages:
                packages_item = PackageStatus.from_dict(packages_item_data)

                packages.append(packages_item)

        _dirty = d.pop("dirty", UNSET)
        dirty: DirtySubsystems | Unset
        if isinstance(_dirty, Unset):
            dirty = UNSET
        else:
            dirty = DirtySubsystems.from_dict(_dirty)

        _ui_features = d.pop("ui_features", UNSET)
        ui_features: StatusSummaryUiFeatures | Unset
        if isinstance(_ui_features, Unset):
            ui_features = UNSET
        else:
            ui_features = StatusSummaryUiFeatures.from_dict(_ui_features)

        alerts = d.pop("alerts", UNSET)

        status_summary = cls(
            status=status,
            timestamp=timestamp,
            packages=packages,
            dirty=dirty,
            ui_features=ui_features,
            alerts=alerts,
        )

        status_summary.additional_properties = d
        return status_summary

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
