from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.haproxy_resolver import HaproxyResolver


T = TypeVar("T", bound="HaproxyResolverList")


@_attrs_define
class HaproxyResolverList:
    """
    Attributes:
        resolvers (list[HaproxyResolver] | Unset):
    """

    resolvers: list[HaproxyResolver] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resolvers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resolvers, Unset):
            resolvers = []
            for resolvers_item_data in self.resolvers:
                resolvers_item = resolvers_item_data.to_dict()
                resolvers.append(resolvers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resolvers is not UNSET:
            field_dict["resolvers"] = resolvers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.haproxy_resolver import HaproxyResolver

        d = dict(src_dict)
        _resolvers = d.pop("resolvers", UNSET)
        resolvers: list[HaproxyResolver] | Unset = UNSET
        if _resolvers is not UNSET:
            resolvers = []
            for resolvers_item_data in _resolvers:
                resolvers_item = HaproxyResolver.from_dict(resolvers_item_data)

                resolvers.append(resolvers_item)

        haproxy_resolver_list = cls(
            resolvers=resolvers,
        )

        haproxy_resolver_list.additional_properties = d
        return haproxy_resolver_list

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
