from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FreeradiusConfigs")


@_attrs_define
class FreeradiusConfigs:
    """
    Attributes:
        configs (list[TextValue] | Unset):
    """

    configs: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configs, Unset):
            configs = []
            for configs_item_data in self.configs:
                configs_item = configs_item_data.to_dict()
                configs.append(configs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configs is not UNSET:
            field_dict["configs"] = configs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _configs = d.pop("configs", UNSET)
        configs: list[TextValue] | Unset = UNSET
        if _configs is not UNSET:
            configs = []
            for configs_item_data in _configs:
                configs_item = TextValue.from_dict(configs_item_data)

                configs.append(configs_item)

        freeradius_configs = cls(
            configs=configs,
        )

        freeradius_configs.additional_properties = d
        return freeradius_configs

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
