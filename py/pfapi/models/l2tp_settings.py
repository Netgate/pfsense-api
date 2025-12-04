from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.l2tp_config import L2TPConfig


T = TypeVar("T", bound="L2TPSettings")


@_attrs_define
class L2TPSettings:
    """
    Attributes:
        l2tp (L2TPConfig | Unset):
        interfaces (list[str] | Unset):
    """

    l2tp: L2TPConfig | Unset = UNSET
    interfaces: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        l2tp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.l2tp, Unset):
            l2tp = self.l2tp.to_dict()

        interfaces: list[str] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if l2tp is not UNSET:
            field_dict["l2tp"] = l2tp
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.l2tp_config import L2TPConfig

        d = dict(src_dict)
        _l2tp = d.pop("l2tp", UNSET)
        l2tp: L2TPConfig | Unset
        if isinstance(_l2tp, Unset):
            l2tp = UNSET
        else:
            l2tp = L2TPConfig.from_dict(_l2tp)

        interfaces = cast(list[str], d.pop("interfaces", UNSET))

        l2tp_settings = cls(
            l2tp=l2tp,
            interfaces=interfaces,
        )

        l2tp_settings.additional_properties = d
        return l2tp_settings

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
