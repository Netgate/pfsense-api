from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TCPFlags")


@_attrs_define
class TCPFlags:
    """
    Attributes:
        fin (bool | Unset):
        syn (bool | Unset):
        rst (bool | Unset):
        psh (bool | Unset):
        ack (bool | Unset):
        urg (bool | Unset):
        ece (bool | Unset):
        cwr (bool | Unset):
    """

    fin: bool | Unset = UNSET
    syn: bool | Unset = UNSET
    rst: bool | Unset = UNSET
    psh: bool | Unset = UNSET
    ack: bool | Unset = UNSET
    urg: bool | Unset = UNSET
    ece: bool | Unset = UNSET
    cwr: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fin = self.fin

        syn = self.syn

        rst = self.rst

        psh = self.psh

        ack = self.ack

        urg = self.urg

        ece = self.ece

        cwr = self.cwr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fin is not UNSET:
            field_dict["fin"] = fin
        if syn is not UNSET:
            field_dict["syn"] = syn
        if rst is not UNSET:
            field_dict["rst"] = rst
        if psh is not UNSET:
            field_dict["psh"] = psh
        if ack is not UNSET:
            field_dict["ack"] = ack
        if urg is not UNSET:
            field_dict["urg"] = urg
        if ece is not UNSET:
            field_dict["ece"] = ece
        if cwr is not UNSET:
            field_dict["cwr"] = cwr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fin = d.pop("fin", UNSET)

        syn = d.pop("syn", UNSET)

        rst = d.pop("rst", UNSET)

        psh = d.pop("psh", UNSET)

        ack = d.pop("ack", UNSET)

        urg = d.pop("urg", UNSET)

        ece = d.pop("ece", UNSET)

        cwr = d.pop("cwr", UNSET)

        tcp_flags = cls(
            fin=fin,
            syn=syn,
            rst=rst,
            psh=psh,
            ack=ack,
            urg=urg,
            ece=ece,
            cwr=cwr,
        )

        tcp_flags.additional_properties = d
        return tcp_flags

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
