from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CertOpts")


@_attrs_define
class CertOpts:
    """
    Attributes:
        key_type (List[str]):
        key_size (List[int]):
        key_opt (List[str]):
        digest (List[str]):
    """

    key_type: List[str]
    key_size: List[int]
    key_opt: List[str]
    digest: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_type = self.key_type

        key_size = self.key_size

        key_opt = self.key_opt

        digest = self.digest

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_type": key_type,
                "key_size": key_size,
                "key_opt": key_opt,
                "digest": digest,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_type = cast(List[str], d.pop("key_type"))

        key_size = cast(List[int], d.pop("key_size"))

        key_opt = cast(List[str], d.pop("key_opt"))

        digest = cast(List[str], d.pop("digest"))

        cert_opts = cls(
            key_type=key_type,
            key_size=key_size,
            key_opt=key_opt,
            digest=digest,
        )

        cert_opts.additional_properties = d
        return cert_opts

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
