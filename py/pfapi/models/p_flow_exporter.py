from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PFlowExporter")


@_attrs_define
class PFlowExporter:
    """
    Attributes:
        id (Union[Unset, str]):
        descr (Union[Unset, str]):
        enable (Union[Unset, bool]):
        src (Union[Unset, str]):
        srcport (Union[Unset, int]):
        dst (Union[Unset, str]):
        dstport (Union[Unset, int]):
        proto (Union[Unset, str]):
        domain (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    enable: Union[Unset, bool] = UNSET
    src: Union[Unset, str] = UNSET
    srcport: Union[Unset, int] = UNSET
    dst: Union[Unset, str] = UNSET
    dstport: Union[Unset, int] = UNSET
    proto: Union[Unset, str] = UNSET
    domain: Union[Unset, int] = UNSET
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
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if descr is not UNSET:
            field_dict["descr"] = descr
        if enable is not UNSET:
            field_dict["enable"] = enable
        if src is not UNSET:
            field_dict["src"] = src
        if srcport is not UNSET:
            field_dict["srcport"] = srcport
        if dst is not UNSET:
            field_dict["dst"] = dst
        if dstport is not UNSET:
            field_dict["dstport"] = dstport
        if proto is not UNSET:
            field_dict["proto"] = proto
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        descr = d.pop("descr", UNSET)

        enable = d.pop("enable", UNSET)

        src = d.pop("src", UNSET)

        srcport = d.pop("srcport", UNSET)

        dst = d.pop("dst", UNSET)

        dstport = d.pop("dstport", UNSET)

        proto = d.pop("proto", UNSET)

        domain = d.pop("domain", UNSET)

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
