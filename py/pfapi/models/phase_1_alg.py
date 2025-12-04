from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.encryption_algorithm import EncryptionAlgorithm


T = TypeVar("T", bound="Phase1Alg")


@_attrs_define
class Phase1Alg:
    """
    Attributes:
        encryption_algorithm (EncryptionAlgorithm | Unset):
        hash_algorithm (str | Unset):
        prf_algorithm (str | Unset):
        dhgroup (str | Unset):
    """

    encryption_algorithm: EncryptionAlgorithm | Unset = UNSET
    hash_algorithm: str | Unset = UNSET
    prf_algorithm: str | Unset = UNSET
    dhgroup: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encryption_algorithm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.encryption_algorithm, Unset):
            encryption_algorithm = self.encryption_algorithm.to_dict()

        hash_algorithm = self.hash_algorithm

        prf_algorithm = self.prf_algorithm

        dhgroup = self.dhgroup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encryption_algorithm is not UNSET:
            field_dict["encryption_algorithm"] = encryption_algorithm
        if hash_algorithm is not UNSET:
            field_dict["hash_algorithm"] = hash_algorithm
        if prf_algorithm is not UNSET:
            field_dict["prf_algorithm"] = prf_algorithm
        if dhgroup is not UNSET:
            field_dict["dhgroup"] = dhgroup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encryption_algorithm import EncryptionAlgorithm

        d = dict(src_dict)
        _encryption_algorithm = d.pop("encryption_algorithm", UNSET)
        encryption_algorithm: EncryptionAlgorithm | Unset
        if isinstance(_encryption_algorithm, Unset):
            encryption_algorithm = UNSET
        else:
            encryption_algorithm = EncryptionAlgorithm.from_dict(_encryption_algorithm)

        hash_algorithm = d.pop("hash_algorithm", UNSET)

        prf_algorithm = d.pop("prf_algorithm", UNSET)

        dhgroup = d.pop("dhgroup", UNSET)

        phase_1_alg = cls(
            encryption_algorithm=encryption_algorithm,
            hash_algorithm=hash_algorithm,
            prf_algorithm=prf_algorithm,
            dhgroup=dhgroup,
        )

        phase_1_alg.additional_properties = d
        return phase_1_alg

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
