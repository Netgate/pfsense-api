from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cert_authority import CertAuthority


T = TypeVar("T", bound="CertAuthorities")


@_attrs_define
class CertAuthorities:
    """
    Attributes:
        cas (list[CertAuthority] | Unset):
    """

    cas: list[CertAuthority] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cas, Unset):
            cas = []
            for cas_item_data in self.cas:
                cas_item = cas_item_data.to_dict()
                cas.append(cas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cas is not UNSET:
            field_dict["cas"] = cas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cert_authority import CertAuthority

        d = dict(src_dict)
        _cas = d.pop("cas", UNSET)
        cas: list[CertAuthority] | Unset = UNSET
        if _cas is not UNSET:
            cas = []
            for cas_item_data in _cas:
                cas_item = CertAuthority.from_dict(cas_item_data)

                cas.append(cas_item)

        cert_authorities = cls(
            cas=cas,
        )

        cert_authorities.additional_properties = d
        return cert_authorities

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
