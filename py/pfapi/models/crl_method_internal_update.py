from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.crl_method_internal_update_revoke_reason import CRLMethodInternalUpdateRevokeReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="CRLMethodInternalUpdate")


@_attrs_define
class CRLMethodInternalUpdate:
    """
    Attributes:
        lifetime (int | Unset):
        serial (int | Unset):
        revoke_reason (CRLMethodInternalUpdateRevokeReason | Unset):
        revoke_serials (list[int] | Unset):
        revoke_certref (list[str] | Unset):
    """

    lifetime: int | Unset = UNSET
    serial: int | Unset = UNSET
    revoke_reason: CRLMethodInternalUpdateRevokeReason | Unset = UNSET
    revoke_serials: list[int] | Unset = UNSET
    revoke_certref: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lifetime = self.lifetime

        serial = self.serial

        revoke_reason: str | Unset = UNSET
        if not isinstance(self.revoke_reason, Unset):
            revoke_reason = self.revoke_reason.value

        revoke_serials: list[int] | Unset = UNSET
        if not isinstance(self.revoke_serials, Unset):
            revoke_serials = self.revoke_serials

        revoke_certref: list[str] | Unset = UNSET
        if not isinstance(self.revoke_certref, Unset):
            revoke_certref = self.revoke_certref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if serial is not UNSET:
            field_dict["serial"] = serial
        if revoke_reason is not UNSET:
            field_dict["revoke_reason"] = revoke_reason
        if revoke_serials is not UNSET:
            field_dict["revoke_serials"] = revoke_serials
        if revoke_certref is not UNSET:
            field_dict["revoke_certref"] = revoke_certref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lifetime = d.pop("lifetime", UNSET)

        serial = d.pop("serial", UNSET)

        _revoke_reason = d.pop("revoke_reason", UNSET)
        revoke_reason: CRLMethodInternalUpdateRevokeReason | Unset
        if isinstance(_revoke_reason, Unset):
            revoke_reason = UNSET
        else:
            revoke_reason = CRLMethodInternalUpdateRevokeReason(_revoke_reason)

        revoke_serials = cast(list[int], d.pop("revoke_serials", UNSET))

        revoke_certref = cast(list[str], d.pop("revoke_certref", UNSET))

        crl_method_internal_update = cls(
            lifetime=lifetime,
            serial=serial,
            revoke_reason=revoke_reason,
            revoke_serials=revoke_serials,
            revoke_certref=revoke_certref,
        )

        crl_method_internal_update.additional_properties = d
        return crl_method_internal_update

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
