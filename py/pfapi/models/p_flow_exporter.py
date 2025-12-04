from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PFlowExporter")


@_attrs_define
class PFlowExporter:
    """
    Attributes:
        id (str | Unset):
        descr (str | Unset):
        enable (bool | Unset):
        src (str | Unset):
        srcport (int | Unset):
        dst (str | Unset):
        dstport (int | Unset):
        proto (str | Unset):
        domain (int | Unset):
    """

    id: str | Unset = UNSET
    descr: str | Unset = UNSET
    enable: bool | Unset = UNSET
    src: str | Unset = UNSET
    srcport: int | Unset = UNSET
    dst: str | Unset = UNSET
    dstport: int | Unset = UNSET
    proto: str | Unset = UNSET
    domain: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        descr = self.descr

        enable = self.enable

        src = self.src

        srcport = self.srcport

        dst = self.dst

        dstport = self.dstport

        proto = self.proto

        domain = self.domain

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
