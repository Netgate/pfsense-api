from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tunable import Tunable


T = TypeVar("T", bound="Tunables")


@_attrs_define
class Tunables:
    """
    Attributes:
        tunables (list[Tunable] | Unset):
    """

    tunables: list[Tunable] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tunables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tunables, Unset):
            tunables = []
            for tunables_item_data in self.tunables:
                tunables_item = tunables_item_data.to_dict()
                tunables.append(tunables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tunables is not UNSET:
            field_dict["tunables"] = tunables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tunable import Tunable

        d = dict(src_dict)
        _tunables = d.pop("tunables", UNSET)
        tunables: list[Tunable] | Unset = UNSET
        if _tunables is not UNSET:
            tunables = []
            for tunables_item_data in _tunables:
                tunables_item = Tunable.from_dict(tunables_item_data)

                tunables.append(tunables_item)

        tunables = cls(
            tunables=tunables,
        )

        tunables.additional_properties = d
        return tunables

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
