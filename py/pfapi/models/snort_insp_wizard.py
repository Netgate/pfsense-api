from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_wizard_hexes import SnortInspWizardHexes
    from ..models.snort_insp_wizard_spells import SnortInspWizardSpells


T = TypeVar("T", bound="SnortInspWizard")


@_attrs_define
class SnortInspWizard:
    """
    Attributes:
        hexes (list[SnortInspWizardHexes] | Unset):
        spells (list[SnortInspWizardSpells] | Unset):
        curses (list[str] | Unset):
        max_search_depth (int | Unset): maximum scan depth per flow { 0:65535 }; default 8192
    """

    hexes: list[SnortInspWizardHexes] | Unset = UNSET
    spells: list[SnortInspWizardSpells] | Unset = UNSET
    curses: list[str] | Unset = UNSET
    max_search_depth: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hexes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hexes, Unset):
            hexes = []
            for hexes_item_data in self.hexes:
                hexes_item = hexes_item_data.to_dict()
                hexes.append(hexes_item)

        spells: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.spells, Unset):
            spells = []
            for spells_item_data in self.spells:
                spells_item = spells_item_data.to_dict()
                spells.append(spells_item)

        curses: list[str] | Unset = UNSET
        if not isinstance(self.curses, Unset):
            curses = self.curses

        max_search_depth = self.max_search_depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hexes is not UNSET:
            field_dict["hexes"] = hexes
        if spells is not UNSET:
            field_dict["spells"] = spells
        if curses is not UNSET:
            field_dict["curses"] = curses
        if max_search_depth is not UNSET:
            field_dict["max_search_depth"] = max_search_depth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_wizard_hexes import SnortInspWizardHexes
        from ..models.snort_insp_wizard_spells import SnortInspWizardSpells

        d = dict(src_dict)
        _hexes = d.pop("hexes", UNSET)
        hexes: list[SnortInspWizardHexes] | Unset = UNSET
        if _hexes is not UNSET:
            hexes = []
            for hexes_item_data in _hexes:
                hexes_item = SnortInspWizardHexes.from_dict(hexes_item_data)

                hexes.append(hexes_item)

        _spells = d.pop("spells", UNSET)
        spells: list[SnortInspWizardSpells] | Unset = UNSET
        if _spells is not UNSET:
            spells = []
            for spells_item_data in _spells:
                spells_item = SnortInspWizardSpells.from_dict(spells_item_data)

                spells.append(spells_item)

        curses = cast(list[str], d.pop("curses", UNSET))

        max_search_depth = d.pop("max_search_depth", UNSET)

        snort_insp_wizard = cls(
            hexes=hexes,
            spells=spells,
            curses=curses,
            max_search_depth=max_search_depth,
        )

        snort_insp_wizard.additional_properties = d
        return snort_insp_wizard

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
