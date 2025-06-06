from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceSimple")


@_attrs_define
class InterfaceSimple:
    """Basic interface details.

    Attributes:
        name (str): alias to identity
        identity (Union[Unset, str]): interface identity
        assigned (Union[Unset, str]): assigned interface name
        if_ (Union[Unset, str]): operating system device name
        descr (Union[Unset, str]): interface description
        ipaddr (Union[Unset, str]):
        ipaddrv6 (Union[Unset, str]):
        mac (Union[Unset, str]):
        tag (Union[Unset, int]):
        member (Union[Unset, str]):
        addresses (Union[Unset, List[str]]):
        enable (Union[Unset, bool]):
    """

    name: str
    identity: Union[Unset, str] = UNSET
    assigned: Union[Unset, str] = UNSET
    if_: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    ipaddr: Union[Unset, str] = UNSET
    ipaddrv6: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    tag: Union[Unset, int] = UNSET
    member: Union[Unset, str] = UNSET
    addresses: Union[Unset, List[str]] = UNSET
    enable: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        identity = self.identity

        assigned = self.assigned

        if_ = self.if_

        descr = self.descr

        ipaddr = self.ipaddr

        ipaddrv6 = self.ipaddrv6

        mac = self.mac

        tag = self.tag

        member = self.member

        addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        enable = self.enable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if identity is not UNSET:
            field_dict["identity"] = identity
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if if_ is not UNSET:
            field_dict["if"] = if_
        if descr is not UNSET:
            field_dict["descr"] = descr
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
        if ipaddrv6 is not UNSET:
            field_dict["ipaddrv6"] = ipaddrv6
        if mac is not UNSET:
            field_dict["mac"] = mac
        if tag is not UNSET:
            field_dict["tag"] = tag
        if member is not UNSET:
            field_dict["member"] = member
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        identity = d.pop("identity", UNSET)

        assigned = d.pop("assigned", UNSET)

        if_ = d.pop("if", UNSET)

        descr = d.pop("descr", UNSET)

        ipaddr = d.pop("ipaddr", UNSET)

        ipaddrv6 = d.pop("ipaddrv6", UNSET)

        mac = d.pop("mac", UNSET)

        tag = d.pop("tag", UNSET)

        member = d.pop("member", UNSET)

        addresses = cast(List[str], d.pop("addresses", UNSET))

        enable = d.pop("enable", UNSET)

        interface_simple = cls(
            name=name,
            identity=identity,
            assigned=assigned,
            if_=if_,
            descr=descr,
            ipaddr=ipaddr,
            ipaddrv6=ipaddrv6,
            mac=mac,
            tag=tag,
            member=member,
            addresses=addresses,
            enable=enable,
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
