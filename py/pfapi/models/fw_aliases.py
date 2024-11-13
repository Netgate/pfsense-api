from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_alias import FWAlias
    from ..models.fw_system_alias import FWSystemAlias


T = TypeVar("T", bound="FWAliases")


@_attrs_define
class FWAliases:
    """
    Attributes:
        aliases (Union[Unset, List['FWAlias']]):
        system_aliases (Union[Unset, List['FWSystemAlias']]):
    """

    aliases: Union[Unset, List["FWAlias"]] = UNSET
    system_aliases: Union[Unset, List["FWSystemAlias"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()
                aliases.append(aliases_item)

        system_aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.system_aliases, Unset):
            system_aliases = []
            for system_aliases_item_data in self.system_aliases:
                system_aliases_item = system_aliases_item_data.to_dict()
                system_aliases.append(system_aliases_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if system_aliases is not UNSET:
            field_dict["system_aliases"] = system_aliases

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_alias import FWAlias
        from ..models.fw_system_alias import FWSystemAlias

        d = src_dict.copy()
        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = FWAlias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        system_aliases = []
        _system_aliases = d.pop("system_aliases", UNSET)
        for system_aliases_item_data in _system_aliases or []:
            system_aliases_item = FWSystemAlias.from_dict(system_aliases_item_data)

            system_aliases.append(system_aliases_item)

        fw_aliases = cls(
            aliases=aliases,
            system_aliases=system_aliases,
        )

        fw_aliases.additional_properties = d
        return fw_aliases

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
