from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.limiter import Limiter


T = TypeVar("T", bound="Limiters")


@_attrs_define
class Limiters:
    """
    Attributes:
        limiter (list[Limiter] | Unset):
    """

    limiter: list[Limiter] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limiter: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.limiter, Unset):
            limiter = []
            for limiter_item_data in self.limiter:
                limiter_item = limiter_item_data.to_dict()
                limiter.append(limiter_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limiter is not UNSET:
            field_dict["limiter"] = limiter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.limiter import Limiter

        d = dict(src_dict)
        _limiter = d.pop("limiter", UNSET)
        limiter: list[Limiter] | Unset = UNSET
        if _limiter is not UNSET:
            limiter = []
            for limiter_item_data in _limiter:
                limiter_item = Limiter.from_dict(limiter_item_data)

                limiter.append(limiter_item)

        limiters = cls(
            limiter=limiter,
        )

        limiters.additional_properties = d
        return limiters

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
