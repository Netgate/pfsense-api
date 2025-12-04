from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_rules_aliases import FWRulesAliases
    from ..models.fw_rules_entry import FwRulesEntry
    from ..models.name_descr import NameDescr


T = TypeVar("T", bound="FWRules")


@_attrs_define
class FWRules:
    """
    Attributes:
        aliases (FWRulesAliases | Unset):
        nat_interfaces (list[str] | Unset):
        entries (list[FwRulesEntry] | Unset):
        schedules (list[NameDescr] | Unset):
        gateways4 (list[NameDescr] | Unset):
        gateways6 (list[NameDescr] | Unset):
        queues (list[str] | Unset):
        limiters (list[str] | Unset):
    """

    aliases: FWRulesAliases | Unset = UNSET
    nat_interfaces: list[str] | Unset = UNSET
    entries: list[FwRulesEntry] | Unset = UNSET
    schedules: list[NameDescr] | Unset = UNSET
    gateways4: list[NameDescr] | Unset = UNSET
    gateways6: list[NameDescr] | Unset = UNSET
    queues: list[str] | Unset = UNSET
    limiters: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aliases: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases.to_dict()

        nat_interfaces: list[str] | Unset = UNSET
        if not isinstance(self.nat_interfaces, Unset):
            nat_interfaces = self.nat_interfaces

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        schedules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.schedules, Unset):
            schedules = []
            for schedules_item_data in self.schedules:
                schedules_item = schedules_item_data.to_dict()
                schedules.append(schedules_item)

        gateways4: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gateways4, Unset):
            gateways4 = []
            for gateways4_item_data in self.gateways4:
                gateways4_item = gateways4_item_data.to_dict()
                gateways4.append(gateways4_item)

        gateways6: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gateways6, Unset):
            gateways6 = []
            for gateways6_item_data in self.gateways6:
                gateways6_item = gateways6_item_data.to_dict()
                gateways6.append(gateways6_item)

        queues: list[str] | Unset = UNSET
        if not isinstance(self.queues, Unset):
            queues = self.queues

        limiters: list[str] | Unset = UNSET
        if not isinstance(self.limiters, Unset):
            limiters = self.limiters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if nat_interfaces is not UNSET:
            field_dict["nat_interfaces"] = nat_interfaces
        if entries is not UNSET:
            field_dict["entries"] = entries
        if schedules is not UNSET:
            field_dict["schedules"] = schedules
        if gateways4 is not UNSET:
            field_dict["gateways4"] = gateways4
        if gateways6 is not UNSET:
            field_dict["gateways6"] = gateways6
        if queues is not UNSET:
            field_dict["queues"] = queues
        if limiters is not UNSET:
            field_dict["limiters"] = limiters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fw_rules_aliases import FWRulesAliases
        from ..models.fw_rules_entry import FwRulesEntry
        from ..models.name_descr import NameDescr

        d = dict(src_dict)
        _aliases = d.pop("aliases", UNSET)
        aliases: FWRulesAliases | Unset
        if isinstance(_aliases, Unset):
            aliases = UNSET
        else:
            aliases = FWRulesAliases.from_dict(_aliases)

        nat_interfaces = cast(list[str], d.pop("nat_interfaces", UNSET))

        _entries = d.pop("entries", UNSET)
        entries: list[FwRulesEntry] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = FwRulesEntry.from_dict(entries_item_data)

                entries.append(entries_item)

        _schedules = d.pop("schedules", UNSET)
        schedules: list[NameDescr] | Unset = UNSET
        if _schedules is not UNSET:
            schedules = []
            for schedules_item_data in _schedules:
                schedules_item = NameDescr.from_dict(schedules_item_data)

                schedules.append(schedules_item)

        _gateways4 = d.pop("gateways4", UNSET)
        gateways4: list[NameDescr] | Unset = UNSET
        if _gateways4 is not UNSET:
            gateways4 = []
            for gateways4_item_data in _gateways4:
                gateways4_item = NameDescr.from_dict(gateways4_item_data)

                gateways4.append(gateways4_item)

        _gateways6 = d.pop("gateways6", UNSET)
        gateways6: list[NameDescr] | Unset = UNSET
        if _gateways6 is not UNSET:
            gateways6 = []
            for gateways6_item_data in _gateways6:
                gateways6_item = NameDescr.from_dict(gateways6_item_data)

                gateways6.append(gateways6_item)

        queues = cast(list[str], d.pop("queues", UNSET))

        limiters = cast(list[str], d.pop("limiters", UNSET))

        fw_rules = cls(
            aliases=aliases,
            nat_interfaces=nat_interfaces,
            entries=entries,
            schedules=schedules,
            gateways4=gateways4,
            gateways6=gateways6,
            queues=queues,
            limiters=limiters,
        )

        fw_rules.additional_properties = d
        return fw_rules

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
