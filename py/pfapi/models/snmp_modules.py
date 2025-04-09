from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SNMPModules")


@_attrs_define
class SNMPModules:
    """
    Attributes:
        mibii (Union[Unset, bool]):
        netgraph (Union[Unset, bool]):
        pf (Union[Unset, bool]):
        hostres (Union[Unset, bool]):
        ucd (Union[Unset, bool]):
        regex (Union[Unset, bool]):
    """

    mibii: Union[Unset, bool] = UNSET
    netgraph: Union[Unset, bool] = UNSET
    pf: Union[Unset, bool] = UNSET
    hostres: Union[Unset, bool] = UNSET
    ucd: Union[Unset, bool] = UNSET
    regex: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mibii = self.mibii

        netgraph = self.netgraph

        pf = self.pf

        hostres = self.hostres

        ucd = self.ucd

        regex = self.regex

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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
