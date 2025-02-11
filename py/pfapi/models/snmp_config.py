from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.snmp_modules import SNMPModules


T = TypeVar("T", bound="SNMPConfig")


@_attrs_define
class SNMPConfig:
    """
    Attributes:
        syslocation (str):
        syscontact (str):
        rocommunity (str):
        modules (SNMPModules):
        enable (bool):
        pollport (str):
        trapenable (bool):
        trapserver (str):
        trapserverport (str):
        trapstring (str):
        bindip (str):
    """

    syslocation: str
    syscontact: str
    rocommunity: str
    modules: "SNMPModules"
    enable: bool
    pollport: str
    trapenable: bool
    trapserver: str
    trapserverport: str
    trapstring: str
    bindip: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        syslocation = self.syslocation

        syscontact = self.syscontact

        rocommunity = self.rocommunity

        modules = self.modules.to_dict()

        enable = self.enable

        pollport = self.pollport

        trapenable = self.trapenable

        trapserver = self.trapserver

        trapserverport = self.trapserverport

        trapstring = self.trapstring

        bindip = self.bindip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "syslocation": syslocation,
                "syscontact": syscontact,
                "rocommunity": rocommunity,
                "modules": modules,
                "enable": enable,
                "pollport": pollport,
                "trapenable": trapenable,
                "trapserver": trapserver,
                "trapserverport": trapserverport,
                "trapstring": trapstring,
                "bindip": bindip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.snmp_modules import SNMPModules

        d = src_dict.copy()
        syslocation = d.pop("syslocation")

        syscontact = d.pop("syscontact")

        rocommunity = d.pop("rocommunity")

        modules = SNMPModules.from_dict(d.pop("modules"))

        enable = d.pop("enable")

        pollport = d.pop("pollport")

        trapenable = d.pop("trapenable")

        trapserver = d.pop("trapserver")

        trapserverport = d.pop("trapserverport")

        trapstring = d.pop("trapstring")

        bindip = d.pop("bindip")

        snmp_config = cls(
            syslocation=syslocation,
            syscontact=syscontact,
            rocommunity=rocommunity,
            modules=modules,
            enable=enable,
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
