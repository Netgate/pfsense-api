from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspWizardSpellsLToClient")


@_attrs_define
class SnortInspWizardSpellsLToClient:
    """
    Attributes:
        spell (str | Unset): sequence of data with wild cards (*)
    """

    spell: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spell = self.spell

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spell is not UNSET:
            field_dict["spell"] = spell

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        spell = d.pop("spell", UNSET)

        snort_insp_wizard_spells_l_to_client = cls(
            spell=spell,
        )

        snort_insp_wizard_spells_l_to_client.additional_properties = d
        return snort_insp_wizard_spells_l_to_client

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
