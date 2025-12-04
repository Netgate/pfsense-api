from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dyn_dns_config import DynDNSConfig


T = TypeVar("T", bound="DynDnsList")


@_attrs_define
class DynDnsList:
    """
    Attributes:
        dyndnses (list[DynDNSConfig] | Unset):
    """

    dyndnses: list[DynDNSConfig] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dyndnses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dyndnses, Unset):
            dyndnses = []
            for dyndnses_item_data in self.dyndnses:
                dyndnses_item = dyndnses_item_data.to_dict()
                dyndnses.append(dyndnses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dyndnses is not UNSET:
            field_dict["dyndnses"] = dyndnses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dyn_dns_config import DynDNSConfig

        d = dict(src_dict)
        _dyndnses = d.pop("dyndnses", UNSET)
        dyndnses: list[DynDNSConfig] | Unset = UNSET
        if _dyndnses is not UNSET:
            dyndnses = []
            for dyndnses_item_data in _dyndnses:
                dyndnses_item = DynDNSConfig.from_dict(dyndnses_item_data)

                dyndnses.append(dyndnses_item)

        dyn_dns_list = cls(
            dyndnses=dyndnses,
        )

        dyn_dns_list.additional_properties = d
        return dyn_dns_list

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
