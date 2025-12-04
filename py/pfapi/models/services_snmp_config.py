from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snmp_config import SNMPConfig
    from ..models.snmp_interface import SNMPInterface


T = TypeVar("T", bound="ServicesSNMPConfig")


@_attrs_define
class ServicesSNMPConfig:
    """
    Attributes:
        config (SNMPConfig | Unset):
        interfaces (list[SNMPInterface] | Unset):
    """

    config: SNMPConfig | Unset = UNSET
    interfaces: list[SNMPInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

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
        from ..models.snmp_config import SNMPConfig
        from ..models.snmp_interface import SNMPInterface

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: SNMPConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = SNMPConfig.from_dict(_config)

        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[SNMPInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = SNMPInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        services_snmp_config = cls(
            config=config,
            interfaces=interfaces,
        )

        services_snmp_config.additional_properties = d
        return services_snmp_config

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
