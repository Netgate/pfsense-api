from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_alert import SnortAlert


T = TypeVar("T", bound="SnortAlerts")


@_attrs_define
class SnortAlerts:
    """
    Attributes:
        alerts (list[SnortAlert] | Unset):
    """

    alerts: list[SnortAlert] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alerts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item = alerts_item_data.to_dict()
                alerts.append(alerts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alerts is not UNSET:
            field_dict["alerts"] = alerts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_alert import SnortAlert

        d = dict(src_dict)
        _alerts = d.pop("alerts", UNSET)
        alerts: list[SnortAlert] | Unset = UNSET
        if _alerts is not UNSET:
            alerts = []
            for alerts_item_data in _alerts:
                alerts_item = SnortAlert.from_dict(alerts_item_data)

                alerts.append(alerts_item)

        snort_alerts = cls(
            alerts=alerts,
        )

        snort_alerts.additional_properties = d
        return snort_alerts

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
