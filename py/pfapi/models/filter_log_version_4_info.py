from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FilterLogVersion4Info")


@_attrs_define
class FilterLogVersion4Info:
    """
    Attributes:
        tos (str):
        ecn (str):
        ttl (str):
        id (str):
        offset (str):
        flags (str):
    """

    tos: str
    ecn: str
    ttl: str
    id: str
    offset: str
    flags: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tos = self.tos

        ecn = self.ecn

        ttl = self.ttl

        id = self.id

        offset = self.offset

        flags = self.flags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tos": tos,
                "ecn": ecn,
                "ttl": ttl,
                "id": id,
                "offset": offset,
                "flags": flags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tos = d.pop("tos")

        ecn = d.pop("ecn")

        ttl = d.pop("ttl")

        id = d.pop("id")

        offset = d.pop("offset")

        flags = d.pop("flags")

        filter_log_version_4_info = cls(
            tos=tos,
            ecn=ecn,
            ttl=ttl,
            id=id,
            offset=offset,
            flags=flags,
        )

        filter_log_version_4_info.additional_properties = d
        return filter_log_version_4_info

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
