from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IGMPProxy")


@_attrs_define
class IGMPProxy:
    """
    Attributes:
        ifname (str):
        address (str):
        threshold (Union[Unset, str]):
        descr (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    ifname: str
    address: str
    threshold: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ifname = self.ifname

        address = self.address

        threshold = self.threshold

        descr = self.descr

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ifname": ifname,
                "address": address,
            }
        )
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if descr is not UNSET:
            field_dict["descr"] = descr
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ifname = d.pop("ifname")

        address = d.pop("address")

        threshold = d.pop("threshold", UNSET)

        descr = d.pop("descr", UNSET)

        type = d.pop("type", UNSET)

        igmp_proxy = cls(
            ifname=ifname,
            address=address,
            threshold=threshold,
            descr=descr,
            type=type,
        )

        igmp_proxy.additional_properties = d
        return igmp_proxy

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
