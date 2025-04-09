from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        syslocation (Union[Unset, str]):
        syscontact (Union[Unset, str]):
        modules (Union[Unset, SNMPModules]):
        pollport (Union[Unset, str]):
        trapenable (Union[Unset, bool]):
        trapserver (Union[Unset, str]):
        trapserverport (Union[Unset, str]):
        trapstring (Union[Unset, str]):
        bindip (Union[Unset, str]):
    """

    rocommunity: str
    enable: bool
    syslocation: Union[Unset, str] = UNSET
    syscontact: Union[Unset, str] = UNSET
    modules: Union[Unset, "SNMPModules"] = UNSET
    pollport: Union[Unset, str] = UNSET
    trapenable: Union[Unset, bool] = UNSET
    trapserver: Union[Unset, str] = UNSET
    trapserverport: Union[Unset, str] = UNSET
    trapstring: Union[Unset, str] = UNSET
    bindip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rocommunity = self.rocommunity

        enable = self.enable

        syslocation = self.syslocation

        syscontact = self.syscontact

        modules: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.modules, Unset):
            modules = self.modules.to_dict()

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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.snmp_modules import SNMPModules

        d = src_dict.copy()
        rocommunity = d.pop("rocommunity")

        enable = d.pop("enable")

        syslocation = d.pop("syslocation", UNSET)

        syscontact = d.pop("syscontact", UNSET)

        _modules = d.pop("modules", UNSET)
        modules: Union[Unset, SNMPModules]
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
