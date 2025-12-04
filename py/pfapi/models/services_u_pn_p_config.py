from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.u_pn_p_config import UPnPConfig


T = TypeVar("T", bound="ServicesUPnPConfig")


@_attrs_define
class ServicesUPnPConfig:
    """
    Attributes:
        config (UPnPConfig | Unset):
        interfaces (list[str] | Unset):
    """

    config: UPnPConfig | Unset = UNSET
    interfaces: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        interfaces: list[str] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.u_pn_p_config import UPnPConfig

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: UPnPConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = UPnPConfig.from_dict(_config)

        interfaces = cast(list[str], d.pop("interfaces", UNSET))

        services_u_pn_p_config = cls(
            config=config,
            interfaces=interfaces,
        )

        services_u_pn_p_config.additional_properties = d
        return services_u_pn_p_config

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
