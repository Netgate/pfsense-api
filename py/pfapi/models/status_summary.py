from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        status (Union[Unset, SystemStatus]):
        timestamp (Union[Unset, int]): millisecond timestamp of the system
        packages (Union[Unset, List['PackageStatus']]):
        dirty (Union[Unset, DirtySubsystems]):
        ui_features (Union[Unset, StatusSummaryUiFeatures]):
        alerts (Union[Unset, str]):
    """

    status: Union[Unset, "SystemStatus"] = UNSET
    timestamp: Union[Unset, int] = UNSET
    packages: Union[Unset, List["PackageStatus"]] = UNSET
    dirty: Union[Unset, "DirtySubsystems"] = UNSET
    ui_features: Union[Unset, "StatusSummaryUiFeatures"] = UNSET
    alerts: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        timestamp = self.timestamp

        packages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        dirty: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dirty, Unset):
            dirty = self.dirty.to_dict()

        ui_features: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ui_features, Unset):
            ui_features = self.ui_features.to_dict()

        alerts = self.alerts

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dirty_subsystems import DirtySubsystems
        from ..models.package_status import PackageStatus
        from ..models.status_summary_ui_features import StatusSummaryUiFeatures
        from ..models.system_status import SystemStatus

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, SystemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SystemStatus.from_dict(_status)

        timestamp = d.pop("timestamp", UNSET)

        packages = []
        _packages = d.pop("packages", UNSET)
        for packages_item_data in _packages or []:
            packages_item = PackageStatus.from_dict(packages_item_data)

            packages.append(packages_item)

        _dirty = d.pop("dirty", UNSET)
        dirty: Union[Unset, DirtySubsystems]
        if isinstance(_dirty, Unset):
            dirty = UNSET
        else:
            dirty = DirtySubsystems.from_dict(_dirty)

        _ui_features = d.pop("ui_features", UNSET)
        ui_features: Union[Unset, StatusSummaryUiFeatures]
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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
