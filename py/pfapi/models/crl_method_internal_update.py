from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.crl_method_internal_update_revoke_reason import CRLMethodInternalUpdateRevokeReason

T = TypeVar("T", bound="CRLMethodInternalUpdate")


@_attrs_define
class CRLMethodInternalUpdate:
    """
    Attributes:
        lifetime (int):
        serial (int):
        revoke_reason (CRLMethodInternalUpdateRevokeReason):
        revoke_serials (List[int]):
        revoke_certref (List[str]):
    """

    lifetime: int
    serial: int
    revoke_reason: CRLMethodInternalUpdateRevokeReason
    revoke_serials: List[int]
    revoke_certref: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lifetime = self.lifetime

        serial = self.serial

        revoke_reason = self.revoke_reason.value

        revoke_serials = self.revoke_serials

        revoke_certref = self.revoke_certref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lifetime": lifetime,
                "serial": serial,
                "revoke_reason": revoke_reason,
                "revoke_serials": revoke_serials,
                "revoke_certref": revoke_certref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lifetime = d.pop("lifetime")

        serial = d.pop("serial")

        revoke_reason = CRLMethodInternalUpdateRevokeReason(d.pop("revoke_reason"))

        revoke_serials = cast(List[int], d.pop("revoke_serials"))

        revoke_certref = cast(List[str], d.pop("revoke_certref"))

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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
