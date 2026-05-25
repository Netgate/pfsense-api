from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_global_prefix import FrrGlobalPrefix


T = TypeVar("T", bound="FrrGlobalPrefixesList")


@_attrs_define
class FrrGlobalPrefixesList:
    """
    Attributes:
        globalprefixes (list[FrrGlobalPrefix] | Unset):
    """

    globalprefixes: list[FrrGlobalPrefix] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        globalprefixes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.globalprefixes, Unset):
            globalprefixes = []
            for globalprefixes_item_data in self.globalprefixes:
                globalprefixes_item = globalprefixes_item_data.to_dict()
                globalprefixes.append(globalprefixes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if globalprefixes is not UNSET:
            field_dict["globalprefixes"] = globalprefixes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_global_prefix import FrrGlobalPrefix

        d = dict(src_dict)
        _globalprefixes = d.pop("globalprefixes", UNSET)
        globalprefixes: list[FrrGlobalPrefix] | Unset = UNSET
        if _globalprefixes is not UNSET:
            globalprefixes = []
            for globalprefixes_item_data in _globalprefixes:
                globalprefixes_item = FrrGlobalPrefix.from_dict(globalprefixes_item_data)

                globalprefixes.append(globalprefixes_item)

        frr_global_prefixes_list = cls(
            globalprefixes=globalprefixes,
        )

        frr_global_prefixes_list.additional_properties = d
        return frr_global_prefixes_list

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
