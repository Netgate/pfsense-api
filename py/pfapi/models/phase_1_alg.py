from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.encryption_algorithm import EncryptionAlgorithm


T = TypeVar("T", bound="Phase1Alg")


@_attrs_define
class Phase1Alg:
    """
    Attributes:
        encryption_algorithm (EncryptionAlgorithm):
        hash_algorithm (str):
        prf_algorithm (str):
        dhgroup (str):
    """

    encryption_algorithm: "EncryptionAlgorithm"
    hash_algorithm: str
    prf_algorithm: str
    dhgroup: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encryption_algorithm = self.encryption_algorithm.to_dict()

        hash_algorithm = self.hash_algorithm

        prf_algorithm = self.prf_algorithm

        dhgroup = self.dhgroup

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encryption_algorithm": encryption_algorithm,
                "hash_algorithm": hash_algorithm,
                "prf_algorithm": prf_algorithm,
                "dhgroup": dhgroup,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.encryption_algorithm import EncryptionAlgorithm

        d = src_dict.copy()
        encryption_algorithm = EncryptionAlgorithm.from_dict(d.pop("encryption_algorithm"))

        hash_algorithm = d.pop("hash_algorithm")

        prf_algorithm = d.pop("prf_algorithm")

        dhgroup = d.pop("dhgroup")

        phase_1_alg = cls(
            encryption_algorithm=encryption_algorithm,
            hash_algorithm=hash_algorithm,
            prf_algorithm=prf_algorithm,
            dhgroup=dhgroup,
        )

        phase_1_alg.additional_properties = d
        return phase_1_alg

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
