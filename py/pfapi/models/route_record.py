from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteRecord")


@_attrs_define
class RouteRecord:
    """
    Attributes:
        dest (Union[Unset, str]):
        gw (Union[Unset, str]):
        flag (Union[Unset, str]):
        uses (Union[Unset, str]):
        mtu (Union[Unset, str]):
        interface (Union[Unset, str]):
        exp (Union[Unset, str]):
    """

    dest: Union[Unset, str] = UNSET
    gw: Union[Unset, str] = UNSET
    flag: Union[Unset, str] = UNSET
    uses: Union[Unset, str] = UNSET
    mtu: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    exp: Union[Unset, str] = UNSET
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
        field_dict.update({})
        if dest is not UNSET:
            field_dict["dest"] = dest
        if gw is not UNSET:
            field_dict["gw"] = gw
        if flag is not UNSET:
            field_dict["flag"] = flag
        if uses is not UNSET:
            field_dict["uses"] = uses
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if interface is not UNSET:
            field_dict["interface"] = interface
        if exp is not UNSET:
            field_dict["exp"] = exp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dest = d.pop("dest", UNSET)

        gw = d.pop("gw", UNSET)

        flag = d.pop("flag", UNSET)

        uses = d.pop("uses", UNSET)

        mtu = d.pop("mtu", UNSET)

        interface = d.pop("interface", UNSET)

        exp = d.pop("exp", UNSET)

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
