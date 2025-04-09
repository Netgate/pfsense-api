from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_alias import FWAlias
    from ..models.fw_system_alias import FWSystemAlias
    from ..models.nat1_to_1_rule import NAT1To1Rule
    from ..models.simple_interface import SimpleInterface


T = TypeVar("T", bound="NAT1To1Rules")


@_attrs_define
class NAT1To1Rules:
    """
    Attributes:
        destlist (Union[Unset, List['SimpleInterface']]):
        interfacelist (Union[Unset, List['SimpleInterface']]):
        aliases (Union[Unset, List['FWAlias']]):
        sysaliases (Union[Unset, List['FWSystemAlias']]):
        rules (Union[Unset, List['NAT1To1Rule']]):
        extlist (Union[Unset, List['SimpleInterface']]):
        srclist (Union[Unset, List['SimpleInterface']]):
    """

    destlist: Union[Unset, List["SimpleInterface"]] = UNSET
    interfacelist: Union[Unset, List["SimpleInterface"]] = UNSET
    aliases: Union[Unset, List["FWAlias"]] = UNSET
    sysaliases: Union[Unset, List["FWSystemAlias"]] = UNSET
    rules: Union[Unset, List["NAT1To1Rule"]] = UNSET
    extlist: Union[Unset, List["SimpleInterface"]] = UNSET
    srclist: Union[Unset, List["SimpleInterface"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        destlist: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.destlist, Unset):
            destlist = []
            for destlist_item_data in self.destlist:
                destlist_item = destlist_item_data.to_dict()
                destlist.append(destlist_item)

        interfacelist: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfacelist, Unset):
            interfacelist = []
            for interfacelist_item_data in self.interfacelist:
                interfacelist_item = interfacelist_item_data.to_dict()
                interfacelist.append(interfacelist_item)

        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()
                aliases.append(aliases_item)

        sysaliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sysaliases, Unset):
            sysaliases = []
            for sysaliases_item_data in self.sysaliases:
                sysaliases_item = sysaliases_item_data.to_dict()
                sysaliases.append(sysaliases_item)

        rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        extlist: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extlist, Unset):
            extlist = []
            for extlist_item_data in self.extlist:
                extlist_item = extlist_item_data.to_dict()
                extlist.append(extlist_item)

        srclist: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.srclist, Unset):
            srclist = []
            for srclist_item_data in self.srclist:
                srclist_item = srclist_item_data.to_dict()
                srclist.append(srclist_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destlist is not UNSET:
            field_dict["destlist"] = destlist
        if interfacelist is not UNSET:
            field_dict["interfacelist"] = interfacelist
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if sysaliases is not UNSET:
            field_dict["sysaliases"] = sysaliases
        if rules is not UNSET:
            field_dict["rules"] = rules
        if extlist is not UNSET:
            field_dict["extlist"] = extlist
        if srclist is not UNSET:
            field_dict["srclist"] = srclist

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_alias import FWAlias
        from ..models.fw_system_alias import FWSystemAlias
        from ..models.nat1_to_1_rule import NAT1To1Rule
        from ..models.simple_interface import SimpleInterface

        d = src_dict.copy()
        destlist = []
        _destlist = d.pop("destlist", UNSET)
        for destlist_item_data in _destlist or []:
            destlist_item = SimpleInterface.from_dict(destlist_item_data)

            destlist.append(destlist_item)

        interfacelist = []
        _interfacelist = d.pop("interfacelist", UNSET)
        for interfacelist_item_data in _interfacelist or []:
            interfacelist_item = SimpleInterface.from_dict(interfacelist_item_data)

            interfacelist.append(interfacelist_item)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = FWAlias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        sysaliases = []
        _sysaliases = d.pop("sysaliases", UNSET)
        for sysaliases_item_data in _sysaliases or []:
            sysaliases_item = FWSystemAlias.from_dict(sysaliases_item_data)

            sysaliases.append(sysaliases_item)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = NAT1To1Rule.from_dict(rules_item_data)

            rules.append(rules_item)

        extlist = []
        _extlist = d.pop("extlist", UNSET)
        for extlist_item_data in _extlist or []:
            extlist_item = SimpleInterface.from_dict(extlist_item_data)

            extlist.append(extlist_item)

        srclist = []
        _srclist = d.pop("srclist", UNSET)
        for srclist_item_data in _srclist or []:
            srclist_item = SimpleInterface.from_dict(srclist_item_data)

            srclist.append(srclist_item)

        nat1_to_1_rules = cls(
            destlist=destlist,
            interfacelist=interfacelist,
            aliases=aliases,
            sysaliases=sysaliases,
            rules=rules,
            extlist=extlist,
            srclist=srclist,
        )

        nat1_to_1_rules.additional_properties = d
        return nat1_to_1_rules

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
