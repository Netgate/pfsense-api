from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QinQInterface")


@_attrs_define
class QinQInterface:
    """
    Attributes:
        if_device (Union[Unset, str]):
        if_assigned_name (Union[Unset, str]):
        tag (Union[Unset, int]):
        autogroup (Union[Unset, bool]):
        members (Union[Unset, str]):
        member (Union[Unset, List[str]]):
        descr (Union[Unset, str]):
        vlanif (Union[Unset, str]):
    """

    if_device: Union[Unset, str] = UNSET
    if_assigned_name: Union[Unset, str] = UNSET
    tag: Union[Unset, int] = UNSET
    autogroup: Union[Unset, bool] = UNSET
    members: Union[Unset, str] = UNSET
    member: Union[Unset, List[str]] = UNSET
    descr: Union[Unset, str] = UNSET
    vlanif: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if_device = self.if_device

        if_assigned_name = self.if_assigned_name

        tag = self.tag

        autogroup = self.autogroup

        members = self.members

        member: Union[Unset, List[str]] = UNSET
        if not isinstance(self.member, Unset):
            member = self.member

        descr = self.descr

        vlanif = self.vlanif

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if if_device is not UNSET:
            field_dict["if_device"] = if_device
        if if_assigned_name is not UNSET:
            field_dict["if_assigned_name"] = if_assigned_name
        if tag is not UNSET:
            field_dict["tag"] = tag
        if autogroup is not UNSET:
            field_dict["autogroup"] = autogroup
        if members is not UNSET:
            field_dict["members"] = members
        if member is not UNSET:
            field_dict["member"] = member
        if descr is not UNSET:
            field_dict["descr"] = descr
        if vlanif is not UNSET:
            field_dict["vlanif"] = vlanif

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        if_device = d.pop("if_device", UNSET)

        if_assigned_name = d.pop("if_assigned_name", UNSET)

        tag = d.pop("tag", UNSET)

        autogroup = d.pop("autogroup", UNSET)

        members = d.pop("members", UNSET)

        member = cast(List[str], d.pop("member", UNSET))

        descr = d.pop("descr", UNSET)

        vlanif = d.pop("vlanif", UNSET)

        qin_q_interface = cls(
            if_device=if_device,
            if_assigned_name=if_assigned_name,
            tag=tag,
            autogroup=autogroup,
            members=members,
            member=member,
            descr=descr,
            vlanif=vlanif,
        )

        qin_q_interface.additional_properties = d
        return qin_q_interface

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
