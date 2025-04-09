from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        aliases (Union[Unset, FWRulesAliases]):
        nat_interfaces (Union[Unset, List[str]]):
        entries (Union[Unset, List['FwRulesEntry']]):
        schedules (Union[Unset, List['NameDescr']]):
        gateways4 (Union[Unset, List['NameDescr']]):
        gateways6 (Union[Unset, List['NameDescr']]):
        queues (Union[Unset, List[str]]):
        limiters (Union[Unset, List[str]]):
    """

    aliases: Union[Unset, "FWRulesAliases"] = UNSET
    nat_interfaces: Union[Unset, List[str]] = UNSET
    entries: Union[Unset, List["FwRulesEntry"]] = UNSET
    schedules: Union[Unset, List["NameDescr"]] = UNSET
    gateways4: Union[Unset, List["NameDescr"]] = UNSET
    gateways6: Union[Unset, List["NameDescr"]] = UNSET
    queues: Union[Unset, List[str]] = UNSET
    limiters: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aliases: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases.to_dict()

        nat_interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.nat_interfaces, Unset):
            nat_interfaces = self.nat_interfaces

        entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        schedules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.schedules, Unset):
            schedules = []
            for schedules_item_data in self.schedules:
                schedules_item = schedules_item_data.to_dict()
                schedules.append(schedules_item)

        gateways4: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.gateways4, Unset):
            gateways4 = []
            for gateways4_item_data in self.gateways4:
                gateways4_item = gateways4_item_data.to_dict()
                gateways4.append(gateways4_item)

        gateways6: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.gateways6, Unset):
            gateways6 = []
            for gateways6_item_data in self.gateways6:
                gateways6_item = gateways6_item_data.to_dict()
                gateways6.append(gateways6_item)

        queues: Union[Unset, List[str]] = UNSET
        if not isinstance(self.queues, Unset):
            queues = self.queues

        limiters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.limiters, Unset):
            limiters = self.limiters

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_rules_aliases import FWRulesAliases
        from ..models.fw_rules_entry import FwRulesEntry
        from ..models.name_descr import NameDescr

        d = src_dict.copy()
        _aliases = d.pop("aliases", UNSET)
        aliases: Union[Unset, FWRulesAliases]
        if isinstance(_aliases, Unset):
            aliases = UNSET
        else:
            aliases = FWRulesAliases.from_dict(_aliases)

        nat_interfaces = cast(List[str], d.pop("nat_interfaces", UNSET))

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = FwRulesEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        schedules = []
        _schedules = d.pop("schedules", UNSET)
        for schedules_item_data in _schedules or []:
            schedules_item = NameDescr.from_dict(schedules_item_data)

            schedules.append(schedules_item)

        gateways4 = []
        _gateways4 = d.pop("gateways4", UNSET)
        for gateways4_item_data in _gateways4 or []:
            gateways4_item = NameDescr.from_dict(gateways4_item_data)

            gateways4.append(gateways4_item)

        gateways6 = []
        _gateways6 = d.pop("gateways6", UNSET)
        for gateways6_item_data in _gateways6 or []:
            gateways6_item = NameDescr.from_dict(gateways6_item_data)

            gateways6.append(gateways6_item)

        queues = cast(List[str], d.pop("queues", UNSET))

        limiters = cast(List[str], d.pop("limiters", UNSET))

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
