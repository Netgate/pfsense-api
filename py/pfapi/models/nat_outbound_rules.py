from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_alias import FWAlias
    from ..models.nat_auto_rule import NATAutoRule
    from ..models.nat_outbound_rule import NATOutboundRule
    from ..models.simple_interface import SimpleInterface


T = TypeVar("T", bound="NATOutboundRules")


@_attrs_define
class NATOutboundRules:
    """
    Attributes:
        destlist (Union[Unset, List['SimpleInterface']]):
        interfacelist (Union[Unset, List['SimpleInterface']]):
        locallist (Union[Unset, List['SimpleInterface']]):
        mode (Union[Unset, str]):
        aliases (Union[Unset, List['FWAlias']]):
        rules (Union[Unset, List['NATOutboundRule']]):
        automatic_rules (Union[Unset, List['NATAutoRule']]):
        srclist (Union[Unset, List['SimpleInterface']]):
    """

    destlist: Union[Unset, List["SimpleInterface"]] = UNSET
    interfacelist: Union[Unset, List["SimpleInterface"]] = UNSET
    locallist: Union[Unset, List["SimpleInterface"]] = UNSET
    mode: Union[Unset, str] = UNSET
    aliases: Union[Unset, List["FWAlias"]] = UNSET
    rules: Union[Unset, List["NATOutboundRule"]] = UNSET
    automatic_rules: Union[Unset, List["NATAutoRule"]] = UNSET
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

        locallist: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locallist, Unset):
            locallist = []
            for locallist_item_data in self.locallist:
                locallist_item = locallist_item_data.to_dict()
                locallist.append(locallist_item)

        mode = self.mode

        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()
                aliases.append(aliases_item)

        rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        automatic_rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.automatic_rules, Unset):
            automatic_rules = []
            for automatic_rules_item_data in self.automatic_rules:
                automatic_rules_item = automatic_rules_item_data.to_dict()
                automatic_rules.append(automatic_rules_item)

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
        if locallist is not UNSET:
            field_dict["locallist"] = locallist
        if mode is not UNSET:
            field_dict["mode"] = mode
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if rules is not UNSET:
            field_dict["rules"] = rules
        if automatic_rules is not UNSET:
            field_dict["automatic_rules"] = automatic_rules
        if srclist is not UNSET:
            field_dict["srclist"] = srclist

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_alias import FWAlias
        from ..models.nat_auto_rule import NATAutoRule
        from ..models.nat_outbound_rule import NATOutboundRule
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

        locallist = []
        _locallist = d.pop("locallist", UNSET)
        for locallist_item_data in _locallist or []:
            locallist_item = SimpleInterface.from_dict(locallist_item_data)

            locallist.append(locallist_item)

        mode = d.pop("mode", UNSET)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = FWAlias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = NATOutboundRule.from_dict(rules_item_data)

            rules.append(rules_item)

        automatic_rules = []
        _automatic_rules = d.pop("automatic_rules", UNSET)
        for automatic_rules_item_data in _automatic_rules or []:
            automatic_rules_item = NATAutoRule.from_dict(automatic_rules_item_data)

            automatic_rules.append(automatic_rules_item)

        srclist = []
        _srclist = d.pop("srclist", UNSET)
        for srclist_item_data in _srclist or []:
            srclist_item = SimpleInterface.from_dict(srclist_item_data)

            srclist.append(srclist_item)

        nat_outbound_rules = cls(
            destlist=destlist,
            interfacelist=interfacelist,
            locallist=locallist,
            mode=mode,
            aliases=aliases,
            rules=rules,
            automatic_rules=automatic_rules,
            srclist=srclist,
        )

        nat_outbound_rules.additional_properties = d
        return nat_outbound_rules

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
