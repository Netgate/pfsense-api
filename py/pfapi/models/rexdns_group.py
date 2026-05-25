from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rexdns_group_forward import RexdnsGroupForward
    from ..models.rexdns_group_resolve import RexdnsGroupResolve


T = TypeVar("T", bound="RexdnsGroup")


@_attrs_define
class RexdnsGroup:
    """
    Attributes:
        allow_fallback (bool | Unset): This field should be ignored when assigning global. Permits the the group
            fallback to the global ruleset
        prefix (str | Unset): This field should be ignored when assigning global. Network prefix, the global group will
            never have this field populated
        defaults (list[str] | Unset):
        block (list[str] | Unset):
        forward (RexdnsGroupForward | Unset):
        resolve (RexdnsGroupResolve | Unset):
    """

    allow_fallback: bool | Unset = UNSET
    prefix: str | Unset = UNSET
    defaults: list[str] | Unset = UNSET
    block: list[str] | Unset = UNSET
    forward: RexdnsGroupForward | Unset = UNSET
    resolve: RexdnsGroupResolve | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_fallback = self.allow_fallback

        prefix = self.prefix

        defaults: list[str] | Unset = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults

        block: list[str] | Unset = UNSET
        if not isinstance(self.block, Unset):
            block = self.block

        forward: dict[str, Any] | Unset = UNSET
        if not isinstance(self.forward, Unset):
            forward = self.forward.to_dict()

        resolve: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolve, Unset):
            resolve = self.resolve.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_fallback is not UNSET:
            field_dict["allow_fallback"] = allow_fallback
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if block is not UNSET:
            field_dict["block"] = block
        if forward is not UNSET:
            field_dict["forward"] = forward
        if resolve is not UNSET:
            field_dict["resolve"] = resolve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rexdns_group_forward import RexdnsGroupForward
        from ..models.rexdns_group_resolve import RexdnsGroupResolve

        d = dict(src_dict)
        allow_fallback = d.pop("allow_fallback", UNSET)

        prefix = d.pop("prefix", UNSET)

        defaults = cast(list[str], d.pop("defaults", UNSET))

        block = cast(list[str], d.pop("block", UNSET))

        _forward = d.pop("forward", UNSET)
        forward: RexdnsGroupForward | Unset
        if isinstance(_forward, Unset):
            forward = UNSET
        else:
            forward = RexdnsGroupForward.from_dict(_forward)

        _resolve = d.pop("resolve", UNSET)
        resolve: RexdnsGroupResolve | Unset
        if isinstance(_resolve, Unset):
            resolve = UNSET
        else:
            resolve = RexdnsGroupResolve.from_dict(_resolve)

        rexdns_group = cls(
            allow_fallback=allow_fallback,
            prefix=prefix,
            defaults=defaults,
            block=block,
            forward=forward,
            resolve=resolve,
        )

        rexdns_group.additional_properties = d
        return rexdns_group

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
