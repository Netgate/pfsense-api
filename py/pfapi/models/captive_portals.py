from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.captive_portal_name import CaptivePortalName


T = TypeVar("T", bound="CaptivePortals")


@_attrs_define
class CaptivePortals:
    """
    Attributes:
        config (list[CaptivePortalName] | Unset):
    """

    config: list[CaptivePortalName] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = []
            for config_item_data in self.config:
                config_item = config_item_data.to_dict()
                config.append(config_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.captive_portal_name import CaptivePortalName

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: list[CaptivePortalName] | Unset = UNSET
        if _config is not UNSET:
            config = []
            for config_item_data in _config:
                config_item = CaptivePortalName.from_dict(config_item_data)

                config.append(config_item)

        captive_portals = cls(
            config=config,
        )

        captive_portals.additional_properties = d
        return captive_portals

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
