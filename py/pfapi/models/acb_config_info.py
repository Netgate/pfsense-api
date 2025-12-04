from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acb_config import ACBConfig


T = TypeVar("T", bound="ACBConfigInfo")


@_attrs_define
class ACBConfigInfo:
    """
    Attributes:
        config (ACBConfig | Unset): valid values:
            frequency = "cron", "every"
            reverse = "yes", "no"
        userkey (str | Unset):
    """

    config: ACBConfig | Unset = UNSET
    userkey: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        userkey = self.userkey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if userkey is not UNSET:
            field_dict["userkey"] = userkey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acb_config import ACBConfig

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: ACBConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ACBConfig.from_dict(_config)

        userkey = d.pop("userkey", UNSET)

        acb_config_info = cls(
            config=config,
            userkey=userkey,
        )

        acb_config_info.additional_properties = d
        return acb_config_info

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
