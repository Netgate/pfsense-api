from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FilterLogCARPInfo")


@_attrs_define
class FilterLogCARPInfo:
    """
    Attributes:
        type (str):
        ttl (int):
        vhid (int):
        version (int):
        adv_skew (int):
        adv_base (int):
    """

    type: str
    ttl: int
    vhid: int
    version: int
    adv_skew: int
    adv_base: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        ttl = self.ttl

        vhid = self.vhid

        version = self.version

        adv_skew = self.adv_skew

        adv_base = self.adv_base

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "ttl": ttl,
                "vhid": vhid,
                "version": version,
                "adv_skew": adv_skew,
                "adv_base": adv_base,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        ttl = d.pop("ttl")

        vhid = d.pop("vhid")

        version = d.pop("version")

        adv_skew = d.pop("adv_skew")

        adv_base = d.pop("adv_base")

        filter_log_carp_info = cls(
            type=type,
            ttl=ttl,
            vhid=vhid,
            version=version,
            adv_skew=adv_skew,
            adv_base=adv_base,
        )

        filter_log_carp_info.additional_properties = d
        return filter_log_carp_info

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
