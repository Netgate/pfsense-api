from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrBgpRow")


@_attrs_define
class FrrBgpRow:
    """
    Attributes:
        distributeroutevalue (str | Unset): Subnet to Route
        distributeroutemap (str | Unset): Route Map
        distributeroutemap_options (list[TextValue] | Unset):
    """

    distributeroutevalue: str | Unset = UNSET
    distributeroutemap: str | Unset = UNSET
    distributeroutemap_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        distributeroutevalue = self.distributeroutevalue

        distributeroutemap = self.distributeroutemap

        distributeroutemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.distributeroutemap_options, Unset):
            distributeroutemap_options = []
            for distributeroutemap_options_item_data in self.distributeroutemap_options:
                distributeroutemap_options_item = distributeroutemap_options_item_data.to_dict()
                distributeroutemap_options.append(distributeroutemap_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distributeroutevalue is not UNSET:
            field_dict["distributeroutevalue"] = distributeroutevalue
        if distributeroutemap is not UNSET:
            field_dict["distributeroutemap"] = distributeroutemap
        if distributeroutemap_options is not UNSET:
            field_dict["distributeroutemap_options"] = distributeroutemap_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_value import TextValue

        d = dict(src_dict)
        distributeroutevalue = d.pop("distributeroutevalue", UNSET)

        distributeroutemap = d.pop("distributeroutemap", UNSET)

        _distributeroutemap_options = d.pop("distributeroutemap_options", UNSET)
        distributeroutemap_options: list[TextValue] | Unset = UNSET
        if _distributeroutemap_options is not UNSET:
            distributeroutemap_options = []
            for distributeroutemap_options_item_data in _distributeroutemap_options:
                distributeroutemap_options_item = TextValue.from_dict(distributeroutemap_options_item_data)

                distributeroutemap_options.append(distributeroutemap_options_item)

        frr_bgp_row = cls(
            distributeroutevalue=distributeroutevalue,
            distributeroutemap=distributeroutemap,
            distributeroutemap_options=distributeroutemap_options,
        )

        frr_bgp_row.additional_properties = d
        return frr_bgp_row

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
