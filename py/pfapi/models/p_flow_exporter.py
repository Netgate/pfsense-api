from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PFlowExporter")


@_attrs_define
class PFlowExporter:
    """
    Attributes:
        id (str):
        descr (str):
        enable (bool):
        src (str):
        srcport (int):
        dst (str):
        dstport (int):
        proto (str):
        domain (int):
    """

    id: str
    descr: str
    enable: bool
    src: str
    srcport: int
    dst: str
    dstport: int
    proto: str
    domain: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        descr = self.descr

        enable = self.enable

        src = self.src

        srcport = self.srcport

        dst = self.dst

        dstport = self.dstport

        proto = self.proto

        domain = self.domain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "descr": descr,
                "enable": enable,
                "src": src,
                "srcport": srcport,
                "dst": dst,
                "dstport": dstport,
                "proto": proto,
                "domain": domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        descr = d.pop("descr")

        enable = d.pop("enable")

        src = d.pop("src")

        srcport = d.pop("srcport")

        dst = d.pop("dst")

        dstport = d.pop("dstport")

        proto = d.pop("proto")

        domain = d.pop("domain")

        p_flow_exporter = cls(
            id=id,
            descr=descr,
            enable=enable,
            src=src,
            srcport=srcport,
            dst=dst,
            dstport=dstport,
            proto=proto,
            domain=domain,
        )

        p_flow_exporter.additional_properties = d
        return p_flow_exporter

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
