from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snmp_config import SNMPConfig


T = TypeVar("T", bound="ServicesSNMPConfigReq")


@_attrs_define
class ServicesSNMPConfigReq:
    """
    Attributes:
        config (SNMPConfig | Unset):
    """

    config: SNMPConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snmp_config import SNMPConfig

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: SNMPConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = SNMPConfig.from_dict(_config)

        services_snmp_config_req = cls(
            config=config,
        )

        services_snmp_config_req.additional_properties = d
        return services_snmp_config_req

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
