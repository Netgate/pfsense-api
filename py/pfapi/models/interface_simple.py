from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceSimple")


@_attrs_define
class InterfaceSimple:
    """
    Attributes:
        name (str):
        descr (str):
        if_ (str):
        ipaddr (str):
        ipaddrv6 (str):
        mac (str):
        tag (int):
        member (str):
        enable (bool):
        addresses (Union[Unset, List[str]]):
    """

    name: str
    descr: str
    if_: str
    ipaddr: str
    ipaddrv6: str
    mac: str
    tag: int
    member: str
    enable: bool
    addresses: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        descr = self.descr

        if_ = self.if_

        ipaddr = self.ipaddr

        ipaddrv6 = self.ipaddrv6

        mac = self.mac

        tag = self.tag

        member = self.member

        enable = self.enable

        addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "descr": descr,
                "if": if_,
                "ipaddr": ipaddr,
                "ipaddrv6": ipaddrv6,
                "mac": mac,
                "tag": tag,
                "member": member,
                "enable": enable,
            }
        )
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        descr = d.pop("descr")

        if_ = d.pop("if")

        ipaddr = d.pop("ipaddr")

        ipaddrv6 = d.pop("ipaddrv6")

        mac = d.pop("mac")

        tag = d.pop("tag")

        member = d.pop("member")

        enable = d.pop("enable")

        addresses = cast(List[str], d.pop("addresses", UNSET))

        interface_simple = cls(
            name=name,
            descr=descr,
            if_=if_,
            ipaddr=ipaddr,
            ipaddrv6=ipaddrv6,
            mac=mac,
            tag=tag,
            member=member,
            enable=enable,
            addresses=addresses,
        )

        interface_simple.additional_properties = d
        return interface_simple

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
