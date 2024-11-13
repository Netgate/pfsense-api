from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceGroup")


@_attrs_define
class InterfaceGroup:
    """
    Attributes:
        members (Union[Unset, str]):
        member (Union[Unset, List[str]]):
        descr (Union[Unset, str]):
        ifname (Union[Unset, str]):
    """

    members: Union[Unset, str] = UNSET
    member: Union[Unset, List[str]] = UNSET
    descr: Union[Unset, str] = UNSET
    ifname: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        members = self.members

        member: Union[Unset, List[str]] = UNSET
        if not isinstance(self.member, Unset):
            member = self.member

        descr = self.descr

        ifname = self.ifname

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if members is not UNSET:
            field_dict["members"] = members
        if member is not UNSET:
            field_dict["member"] = member
        if descr is not UNSET:
            field_dict["descr"] = descr
        if ifname is not UNSET:
            field_dict["ifname"] = ifname

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        members = d.pop("members", UNSET)

        member = cast(List[str], d.pop("member", UNSET))

        descr = d.pop("descr", UNSET)

        ifname = d.pop("ifname", UNSET)

        interface_group = cls(
            members=members,
            member=member,
            descr=descr,
            ifname=ifname,
        )

        interface_group.additional_properties = d
        return interface_group

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
