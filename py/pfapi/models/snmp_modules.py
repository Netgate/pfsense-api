from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SNMPModules")


@_attrs_define
class SNMPModules:
    """
    Attributes:
        mibii (bool | Unset):
        netgraph (bool | Unset):
        pf (bool | Unset):
        hostres (bool | Unset):
        ucd (bool | Unset):
        regex (bool | Unset):
    """

    mibii: bool | Unset = UNSET
    netgraph: bool | Unset = UNSET
    pf: bool | Unset = UNSET
    hostres: bool | Unset = UNSET
    ucd: bool | Unset = UNSET
    regex: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mibii = self.mibii

        netgraph = self.netgraph

        pf = self.pf

        hostres = self.hostres

        ucd = self.ucd

        regex = self.regex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mibii is not UNSET:
            field_dict["mibii"] = mibii
        if netgraph is not UNSET:
            field_dict["netgraph"] = netgraph
        if pf is not UNSET:
            field_dict["pf"] = pf
        if hostres is not UNSET:
            field_dict["hostres"] = hostres
        if ucd is not UNSET:
            field_dict["ucd"] = ucd
        if regex is not UNSET:
            field_dict["regex"] = regex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mibii = d.pop("mibii", UNSET)

        netgraph = d.pop("netgraph", UNSET)

        pf = d.pop("pf", UNSET)

        hostres = d.pop("hostres", UNSET)

        ucd = d.pop("ucd", UNSET)

        regex = d.pop("regex", UNSET)

        snmp_modules = cls(
            mibii=mibii,
            netgraph=netgraph,
            pf=pf,
            hostres=hostres,
            ucd=ucd,
            regex=regex,
        )

        snmp_modules.additional_properties = d
        return snmp_modules

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
