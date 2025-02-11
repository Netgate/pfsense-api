from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SNMPModules")


@_attrs_define
class SNMPModules:
    """
    Attributes:
        mibii (bool):
        netgraph (bool):
        pf (bool):
        hostres (bool):
        ucd (bool):
        regex (bool):
    """

    mibii: bool
    netgraph: bool
    pf: bool
    hostres: bool
    ucd: bool
    regex: bool
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
        field_dict.update(
            {
                "mibii": mibii,
                "netgraph": netgraph,
                "pf": pf,
                "hostres": hostres,
                "ucd": ucd,
                "regex": regex,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mibii = d.pop("mibii")

        netgraph = d.pop("netgraph")

        pf = d.pop("pf")

        hostres = d.pop("hostres")

        ucd = d.pop("ucd")

        regex = d.pop("regex")

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
