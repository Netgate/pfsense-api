from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adv_notification_setting import AdvNotificationSetting


T = TypeVar("T", bound="AdvNotifications")


@_attrs_define
class AdvNotifications:
    """
    Attributes:
        notifications (AdvNotificationSetting | Unset):
    """

    notifications: AdvNotificationSetting | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notifications: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = self.notifications.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notifications is not UNSET:
            field_dict["notifications"] = notifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adv_notification_setting import AdvNotificationSetting

        d = dict(src_dict)
        _notifications = d.pop("notifications", UNSET)
        notifications: AdvNotificationSetting | Unset
        if isinstance(_notifications, Unset):
            notifications = UNSET
        else:
            notifications = AdvNotificationSetting.from_dict(_notifications)

        adv_notifications = cls(
            notifications=notifications,
        )

        adv_notifications.additional_properties = d
        return adv_notifications

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
