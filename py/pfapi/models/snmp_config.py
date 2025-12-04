from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snmp_modules import SNMPModules


T = TypeVar("T", bound="SNMPConfig")


@_attrs_define
class SNMPConfig:
    """
    Attributes:
        rocommunity (str):
        enable (bool):
        syslocation (str | Unset):
        syscontact (str | Unset):
        modules (SNMPModules | Unset):
        pollport (str | Unset):
        trapenable (bool | Unset):
        trapserver (str | Unset):
        trapserverport (str | Unset):
        trapstring (str | Unset):
        bindip (str | Unset):
    """

    rocommunity: str
    enable: bool
    syslocation: str | Unset = UNSET
    syscontact: str | Unset = UNSET
    modules: SNMPModules | Unset = UNSET
    pollport: str | Unset = UNSET
    trapenable: bool | Unset = UNSET
    trapserver: str | Unset = UNSET
    trapserverport: str | Unset = UNSET
    trapstring: str | Unset = UNSET
    bindip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rocommunity = self.rocommunity

        enable = self.enable

        syslocation = self.syslocation

        syscontact = self.syscontact

        modules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modules, Unset):
            modules = self.modules.to_dict()

        pollport = self.pollport

        trapenable = self.trapenable

        trapserver = self.trapserver

        trapserverport = self.trapserverport

        trapstring = self.trapstring

        bindip = self.bindip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rocommunity": rocommunity,
                "enable": enable,
            }
        )
        if syslocation is not UNSET:
            field_dict["syslocation"] = syslocation
        if syscontact is not UNSET:
            field_dict["syscontact"] = syscontact
        if modules is not UNSET:
            field_dict["modules"] = modules
        if pollport is not UNSET:
            field_dict["pollport"] = pollport
        if trapenable is not UNSET:
            field_dict["trapenable"] = trapenable
        if trapserver is not UNSET:
            field_dict["trapserver"] = trapserver
        if trapserverport is not UNSET:
            field_dict["trapserverport"] = trapserverport
        if trapstring is not UNSET:
            field_dict["trapstring"] = trapstring
        if bindip is not UNSET:
            field_dict["bindip"] = bindip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snmp_modules import SNMPModules

        d = dict(src_dict)
        rocommunity = d.pop("rocommunity")

        enable = d.pop("enable")

        syslocation = d.pop("syslocation", UNSET)

        syscontact = d.pop("syscontact", UNSET)

        _modules = d.pop("modules", UNSET)
        modules: SNMPModules | Unset
        if isinstance(_modules, Unset):
            modules = UNSET
        else:
            modules = SNMPModules.from_dict(_modules)

        pollport = d.pop("pollport", UNSET)

        trapenable = d.pop("trapenable", UNSET)

        trapserver = d.pop("trapserver", UNSET)

        trapserverport = d.pop("trapserverport", UNSET)

        trapstring = d.pop("trapstring", UNSET)

        bindip = d.pop("bindip", UNSET)

        snmp_config = cls(
            rocommunity=rocommunity,
            enable=enable,
            syslocation=syslocation,
            syscontact=syscontact,
            modules=modules,
            pollport=pollport,
            trapenable=trapenable,
            trapserver=trapserver,
            trapserverport=trapserverport,
            trapstring=trapstring,
            bindip=bindip,
        )

        snmp_config.additional_properties = d
        return snmp_config

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
