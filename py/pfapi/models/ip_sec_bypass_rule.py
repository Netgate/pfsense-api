from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecBypassRule")


@_attrs_define
class IPSecBypassRule:
    """
    Attributes:
        source (Union[Unset, str]):
        sourcemask (Union[Unset, str]):
        destination (Union[Unset, str]):
        dstmask (Union[Unset, str]):
    """

    source: Union[Unset, str] = UNSET
    sourcemask: Union[Unset, str] = UNSET
    destination: Union[Unset, str] = UNSET
    dstmask: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source

        sourcemask = self.sourcemask

        destination = self.destination

        dstmask = self.dstmask

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if sourcemask is not UNSET:
            field_dict["sourcemask"] = sourcemask
        if destination is not UNSET:
            field_dict["destination"] = destination
        if dstmask is not UNSET:
            field_dict["dstmask"] = dstmask

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source = d.pop("source", UNSET)

        sourcemask = d.pop("sourcemask", UNSET)

        destination = d.pop("destination", UNSET)

        dstmask = d.pop("dstmask", UNSET)

        ip_sec_bypass_rule = cls(
            source=source,
            sourcemask=sourcemask,
            destination=destination,
            dstmask=dstmask,
        )

        ip_sec_bypass_rule.additional_properties = d
        return ip_sec_bypass_rule

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
