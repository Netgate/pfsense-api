from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IPSecSAD")


@_attrs_define
class IPSecSAD:
    """
    Attributes:
        src (str):
        dst (str):
        proto (str):
        spi (str):
        reqid (str):
        ealgo (str):
        aalgo (str):
        data (str):
    """

    src: str
    dst: str
    proto: str
    spi: str
    reqid: str
    ealgo: str
    aalgo: str
    data: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        src = self.src

        dst = self.dst

        proto = self.proto

        spi = self.spi

        reqid = self.reqid

        ealgo = self.ealgo

        aalgo = self.aalgo

        data = self.data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src": src,
                "dst": dst,
                "proto": proto,
                "spi": spi,
                "reqid": reqid,
                "ealgo": ealgo,
                "aalgo": aalgo,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        src = d.pop("src")

        dst = d.pop("dst")

        proto = d.pop("proto")

        spi = d.pop("spi")

        reqid = d.pop("reqid")

        ealgo = d.pop("ealgo")

        aalgo = d.pop("aalgo")

        data = d.pop("data")

        ip_sec_sad = cls(
            src=src,
            dst=dst,
            proto=proto,
            spi=spi,
            reqid=reqid,
            ealgo=ealgo,
            aalgo=aalgo,
            data=data,
        )

        ip_sec_sad.additional_properties = d
        return ip_sec_sad

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
