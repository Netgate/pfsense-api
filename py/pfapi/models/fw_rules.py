from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_rules_aliases import FWRulesAliases
    from ..models.fw_rules_entry import FwRulesEntry


T = TypeVar("T", bound="FWRules")


@_attrs_define
class FWRules:
    """
    Attributes:
        aliases (Union[Unset, FWRulesAliases]):
        entries (Union[Unset, List['FwRulesEntry']]):
    """

    aliases: Union[Unset, "FWRulesAliases"] = UNSET
    entries: Union[Unset, List["FwRulesEntry"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aliases: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases.to_dict()

        entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_rules_aliases import FWRulesAliases
        from ..models.fw_rules_entry import FwRulesEntry

        d = src_dict.copy()
        _aliases = d.pop("aliases", UNSET)
        aliases: Union[Unset, FWRulesAliases]
        if isinstance(_aliases, Unset):
            aliases = UNSET
        else:
            aliases = FWRulesAliases.from_dict(_aliases)

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = FwRulesEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        fw_rules = cls(
            aliases=aliases,
            entries=entries,
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
