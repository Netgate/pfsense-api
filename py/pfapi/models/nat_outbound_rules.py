from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_alias import FWAlias
    from ..models.fw_system_alias import FWSystemAlias
    from ..models.nat_auto_rule import NATAutoRule
    from ..models.nat_outbound_rule import NATOutboundRule
    from ..models.simple_interface import SimpleInterface


T = TypeVar("T", bound="NATOutboundRules")


@_attrs_define
class NATOutboundRules:
    """
    Attributes:
        destlist (list[SimpleInterface] | Unset):
        interfacelist (list[SimpleInterface] | Unset):
        locallist (list[SimpleInterface] | Unset):
        mode (str | Unset):
        aliases (list[FWAlias] | Unset):
        sysaliases (list[FWSystemAlias] | Unset):
        rules (list[NATOutboundRule] | Unset):
        automatic_rules (list[NATAutoRule] | Unset):
        srclist (list[SimpleInterface] | Unset):
    """

    destlist: list[SimpleInterface] | Unset = UNSET
    interfacelist: list[SimpleInterface] | Unset = UNSET
    locallist: list[SimpleInterface] | Unset = UNSET
    mode: str | Unset = UNSET
    aliases: list[FWAlias] | Unset = UNSET
    sysaliases: list[FWSystemAlias] | Unset = UNSET
    rules: list[NATOutboundRule] | Unset = UNSET
    automatic_rules: list[NATAutoRule] | Unset = UNSET
    srclist: list[SimpleInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destlist: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.destlist, Unset):
            destlist = []
            for destlist_item_data in self.destlist:
                destlist_item = destlist_item_data.to_dict()
                destlist.append(destlist_item)

        interfacelist: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfacelist, Unset):
            interfacelist = []
            for interfacelist_item_data in self.interfacelist:
                interfacelist_item = interfacelist_item_data.to_dict()
                interfacelist.append(interfacelist_item)

        locallist: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.locallist, Unset):
            locallist = []
            for locallist_item_data in self.locallist:
                locallist_item = locallist_item_data.to_dict()
                locallist.append(locallist_item)

        mode = self.mode

        aliases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()
                aliases.append(aliases_item)

        sysaliases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sysaliases, Unset):
            sysaliases = []
            for sysaliases_item_data in self.sysaliases:
                sysaliases_item = sysaliases_item_data.to_dict()
                sysaliases.append(sysaliases_item)

        rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        automatic_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.automatic_rules, Unset):
            automatic_rules = []
            for automatic_rules_item_data in self.automatic_rules:
                automatic_rules_item = automatic_rules_item_data.to_dict()
                automatic_rules.append(automatic_rules_item)

        srclist: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.srclist, Unset):
            srclist = []
            for srclist_item_data in self.srclist:
                srclist_item = srclist_item_data.to_dict()
                srclist.append(srclist_item)

        field_dict: dict[str, Any] = {}
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
        if sysaliases is not UNSET:
            field_dict["sysaliases"] = sysaliases
        if rules is not UNSET:
            field_dict["rules"] = rules
        if automatic_rules is not UNSET:
            field_dict["automatic_rules"] = automatic_rules
        if srclist is not UNSET:
            field_dict["srclist"] = srclist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fw_alias import FWAlias
        from ..models.fw_system_alias import FWSystemAlias
        from ..models.nat_auto_rule import NATAutoRule
        from ..models.nat_outbound_rule import NATOutboundRule
        from ..models.simple_interface import SimpleInterface

        d = dict(src_dict)
        _destlist = d.pop("destlist", UNSET)
        destlist: list[SimpleInterface] | Unset = UNSET
        if _destlist is not UNSET:
            destlist = []
            for destlist_item_data in _destlist:
                destlist_item = SimpleInterface.from_dict(destlist_item_data)

                destlist.append(destlist_item)

        _interfacelist = d.pop("interfacelist", UNSET)
        interfacelist: list[SimpleInterface] | Unset = UNSET
        if _interfacelist is not UNSET:
            interfacelist = []
            for interfacelist_item_data in _interfacelist:
                interfacelist_item = SimpleInterface.from_dict(interfacelist_item_data)

                interfacelist.append(interfacelist_item)

        _locallist = d.pop("locallist", UNSET)
        locallist: list[SimpleInterface] | Unset = UNSET
        if _locallist is not UNSET:
            locallist = []
            for locallist_item_data in _locallist:
                locallist_item = SimpleInterface.from_dict(locallist_item_data)

                locallist.append(locallist_item)

        mode = d.pop("mode", UNSET)

        _aliases = d.pop("aliases", UNSET)
        aliases: list[FWAlias] | Unset = UNSET
        if _aliases is not UNSET:
            aliases = []
            for aliases_item_data in _aliases:
                aliases_item = FWAlias.from_dict(aliases_item_data)

                aliases.append(aliases_item)

        _sysaliases = d.pop("sysaliases", UNSET)
        sysaliases: list[FWSystemAlias] | Unset = UNSET
        if _sysaliases is not UNSET:
            sysaliases = []
            for sysaliases_item_data in _sysaliases:
                sysaliases_item = FWSystemAlias.from_dict(sysaliases_item_data)

                sysaliases.append(sysaliases_item)

        _rules = d.pop("rules", UNSET)
        rules: list[NATOutboundRule] | Unset = UNSET
        if _rules is not UNSET:
            rules = []
            for rules_item_data in _rules:
                rules_item = NATOutboundRule.from_dict(rules_item_data)

                rules.append(rules_item)

        _automatic_rules = d.pop("automatic_rules", UNSET)
        automatic_rules: list[NATAutoRule] | Unset = UNSET
        if _automatic_rules is not UNSET:
            automatic_rules = []
            for automatic_rules_item_data in _automatic_rules:
                automatic_rules_item = NATAutoRule.from_dict(automatic_rules_item_data)

                automatic_rules.append(automatic_rules_item)

        _srclist = d.pop("srclist", UNSET)
        srclist: list[SimpleInterface] | Unset = UNSET
        if _srclist is not UNSET:
            srclist = []
            for srclist_item_data in _srclist:
                srclist_item = SimpleInterface.from_dict(srclist_item_data)

                srclist.append(srclist_item)

        nat_outbound_rules = cls(
            destlist=destlist,
            interfacelist=interfacelist,
            locallist=locallist,
            mode=mode,
            aliases=aliases,
            sysaliases=sysaliases,
            rules=rules,
            automatic_rules=automatic_rules,
            srclist=srclist,
        )

        nat_outbound_rules.additional_properties = d
        return nat_outbound_rules

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
