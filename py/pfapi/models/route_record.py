from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RouteRecord")


@_attrs_define
class RouteRecord:
    """
    Attributes:
        dest (str):
        gw (str):
        flag (str):
        uses (str):
        mtu (str):
        interface (str):
        exp (str):
    """

    dest: str
    gw: str
    flag: str
    uses: str
    mtu: str
    interface: str
    exp: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dest = self.dest

        gw = self.gw

        flag = self.flag

        uses = self.uses

        mtu = self.mtu

        interface = self.interface

        exp = self.exp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dest": dest,
                "gw": gw,
                "flag": flag,
                "uses": uses,
                "mtu": mtu,
                "interface": interface,
                "exp": exp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dest = d.pop("dest")

        gw = d.pop("gw")

        flag = d.pop("flag")

        uses = d.pop("uses")

        mtu = d.pop("mtu")

        interface = d.pop("interface")

        exp = d.pop("exp")

        route_record = cls(
            dest=dest,
            gw=gw,
            flag=flag,
            uses=uses,
            mtu=mtu,
            interface=interface,
            exp=exp,
        )

        route_record.additional_properties = d
        return route_record

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
