from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertOpts")


@_attrs_define
class CertOpts:
    """
    Attributes:
        key_type (list[str] | Unset):
        key_size (list[int] | Unset):
        key_opt (list[str] | Unset):
        digest (list[str] | Unset):
    """

    key_type: list[str] | Unset = UNSET
    key_size: list[int] | Unset = UNSET
    key_opt: list[str] | Unset = UNSET
    digest: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_type: list[str] | Unset = UNSET
        if not isinstance(self.key_type, Unset):
            key_type = self.key_type

        key_size: list[int] | Unset = UNSET
        if not isinstance(self.key_size, Unset):
            key_size = self.key_size

        key_opt: list[str] | Unset = UNSET
        if not isinstance(self.key_opt, Unset):
            key_opt = self.key_opt

        digest: list[str] | Unset = UNSET
        if not isinstance(self.digest, Unset):
            digest = self.digest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if key_size is not UNSET:
            field_dict["key_size"] = key_size
        if key_opt is not UNSET:
            field_dict["key_opt"] = key_opt
        if digest is not UNSET:
            field_dict["digest"] = digest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_type = cast(list[str], d.pop("key_type", UNSET))

        key_size = cast(list[int], d.pop("key_size", UNSET))

        key_opt = cast(list[str], d.pop("key_opt", UNSET))

        digest = cast(list[str], d.pop("digest", UNSET))

        cert_opts = cls(
            key_type=key_type,
            key_size=key_size,
            key_opt=key_opt,
            digest=digest,
        )

        cert_opts.additional_properties = d
        return cert_opts

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
