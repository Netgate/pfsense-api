from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecSPD")


@_attrs_define
class IPSecSPD:
    """
    Attributes:
        dir_ (Union[Unset, str]):
        scope (Union[Unset, str]):
        ifname (Union[Unset, str]):
        srcid (Union[Unset, str]):
        dstid (Union[Unset, str]):
        proto (Union[Unset, str]):
        src (Union[Unset, str]):
        dst (Union[Unset, str]):
        unique (Union[Unset, str]):
    """

    dir_: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    ifname: Union[Unset, str] = UNSET
    srcid: Union[Unset, str] = UNSET
    dstid: Union[Unset, str] = UNSET
    proto: Union[Unset, str] = UNSET
    src: Union[Unset, str] = UNSET
    dst: Union[Unset, str] = UNSET
    unique: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dir_ = self.dir_

        scope = self.scope

        ifname = self.ifname

        srcid = self.srcid

        dstid = self.dstid

        proto = self.proto

        src = self.src

        dst = self.dst

        unique = self.unique

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if scope is not UNSET:
            field_dict["scope"] = scope
        if ifname is not UNSET:
            field_dict["ifname"] = ifname
        if srcid is not UNSET:
            field_dict["srcid"] = srcid
        if dstid is not UNSET:
            field_dict["dstid"] = dstid
        if proto is not UNSET:
            field_dict["proto"] = proto
        if src is not UNSET:
            field_dict["src"] = src
        if dst is not UNSET:
            field_dict["dst"] = dst
        if unique is not UNSET:
            field_dict["unique"] = unique

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dir_ = d.pop("dir", UNSET)

        scope = d.pop("scope", UNSET)

        ifname = d.pop("ifname", UNSET)

        srcid = d.pop("srcid", UNSET)

        dstid = d.pop("dstid", UNSET)

        proto = d.pop("proto", UNSET)

        src = d.pop("src", UNSET)

        dst = d.pop("dst", UNSET)

        unique = d.pop("unique", UNSET)

        ip_sec_spd = cls(
            dir_=dir_,
            scope=scope,
            ifname=ifname,
            srcid=srcid,
            dstid=dstid,
            proto=proto,
            src=src,
            dst=dst,
            unique=unique,
        )

        ip_sec_spd.additional_properties = d
        return ip_sec_spd

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
