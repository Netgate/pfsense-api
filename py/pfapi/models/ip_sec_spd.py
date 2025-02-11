from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IPSecSPD")


@_attrs_define
class IPSecSPD:
    """
    Attributes:
        dir_ (str):
        scope (str):
        ifname (str):
        srcid (str):
        dstid (str):
        proto (str):
        src (str):
        dst (str):
        unique (str):
    """

    dir_: str
    scope: str
    ifname: str
    srcid: str
    dstid: str
    proto: str
    src: str
    dst: str
    unique: str
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
        field_dict.update(
            {
                "dir": dir_,
                "scope": scope,
                "ifname": ifname,
                "srcid": srcid,
                "dstid": dstid,
                "proto": proto,
                "src": src,
                "dst": dst,
                "unique": unique,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dir_ = d.pop("dir")

        scope = d.pop("scope")

        ifname = d.pop("ifname")

        srcid = d.pop("srcid")

        dstid = d.pop("dstid")

        proto = d.pop("proto")

        src = d.pop("src")

        dst = d.pop("dst")

        unique = d.pop("unique")

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
