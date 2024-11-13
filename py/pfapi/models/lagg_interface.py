from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LAGGInterface")


@_attrs_define
class LAGGInterface:
    """
    Attributes:
        members (Union[Unset, str]):
        descr (Union[Unset, str]):
        laggif (Union[Unset, str]):
        proto (Union[Unset, str]):
        failovermaster (Union[Unset, str]):
        lacptimeout (Union[Unset, str]):
    """

    members: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    laggif: Union[Unset, str] = UNSET
    proto: Union[Unset, str] = UNSET
    failovermaster: Union[Unset, str] = UNSET
    lacptimeout: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        members = self.members

        descr = self.descr

        laggif = self.laggif

        proto = self.proto

        failovermaster = self.failovermaster

        lacptimeout = self.lacptimeout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if members is not UNSET:
            field_dict["members"] = members
        if descr is not UNSET:
            field_dict["descr"] = descr
        if laggif is not UNSET:
            field_dict["laggif"] = laggif
        if proto is not UNSET:
            field_dict["proto"] = proto
        if failovermaster is not UNSET:
            field_dict["failovermaster"] = failovermaster
        if lacptimeout is not UNSET:
            field_dict["lacptimeout"] = lacptimeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        members = d.pop("members", UNSET)

        descr = d.pop("descr", UNSET)

        laggif = d.pop("laggif", UNSET)

        proto = d.pop("proto", UNSET)

        failovermaster = d.pop("failovermaster", UNSET)

        lacptimeout = d.pop("lacptimeout", UNSET)

        lagg_interface = cls(
            members=members,
            descr=descr,
            laggif=laggif,
            proto=proto,
            failovermaster=failovermaster,
            lacptimeout=lacptimeout,
        )

        lagg_interface.additional_properties = d
        return lagg_interface

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
