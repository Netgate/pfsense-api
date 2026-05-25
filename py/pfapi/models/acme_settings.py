from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ACMESettings")


@_attrs_define
class ACMESettings:
    """
    Attributes:
        renew_certs (bool | Unset): whether to auto renew acme certs
        write_certs (bool | Unset): write acme cert in various format
    """

    renew_certs: bool | Unset = UNSET
    write_certs: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        renew_certs = self.renew_certs

        write_certs = self.write_certs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if renew_certs is not UNSET:
            field_dict["renew_certs"] = renew_certs
        if write_certs is not UNSET:
            field_dict["write_certs"] = write_certs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        renew_certs = d.pop("renew_certs", UNSET)

        write_certs = d.pop("write_certs", UNSET)

        acme_settings = cls(
            renew_certs=renew_certs,
            write_certs=write_certs,
        )

        acme_settings.additional_properties = d
        return acme_settings

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
