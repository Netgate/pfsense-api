from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenewCertOptions")


@_attrs_define
class RenewCertOptions:
    """Options for certificate renewal

    Attributes:
        reusekey (bool | Unset):
        reuseserial (bool | Unset):
        strictsecurity (bool | Unset):
    """

    reusekey: bool | Unset = UNSET
    reuseserial: bool | Unset = UNSET
    strictsecurity: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reusekey = self.reusekey

        reuseserial = self.reuseserial

        strictsecurity = self.strictsecurity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reusekey is not UNSET:
            field_dict["reusekey"] = reusekey
        if reuseserial is not UNSET:
            field_dict["reuseserial"] = reuseserial
        if strictsecurity is not UNSET:
            field_dict["strictsecurity"] = strictsecurity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reusekey = d.pop("reusekey", UNSET)

        reuseserial = d.pop("reuseserial", UNSET)

        strictsecurity = d.pop("strictsecurity", UNSET)

        renew_cert_options = cls(
            reusekey=reusekey,
            reuseserial=reuseserial,
            strictsecurity=strictsecurity,
        )

        renew_cert_options.additional_properties = d
        return renew_cert_options

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
