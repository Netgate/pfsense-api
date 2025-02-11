from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserGroup")


@_attrs_define
class UserGroup:
    """
    Attributes:
        name (str):
        description (str):
        scope (str):
        gid (int):
        member (Union[Unset, List[int]]):
        members (Union[Unset, List[int]]):
        privs (Union[Unset, List[str]]):
    """

    name: str
    description: str
    scope: str
    gid: int
    member: Union[Unset, List[int]] = UNSET
    members: Union[Unset, List[int]] = UNSET
    privs: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        scope = self.scope

        gid = self.gid

        member: Union[Unset, List[int]] = UNSET
        if not isinstance(self.member, Unset):
            member = self.member

        members: Union[Unset, List[int]] = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        privs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.privs, Unset):
            privs = self.privs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "scope": scope,
                "gid": gid,
            }
        )
        if member is not UNSET:
            field_dict["member"] = member
        if members is not UNSET:
            field_dict["members"] = members
        if privs is not UNSET:
            field_dict["privs"] = privs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        scope = d.pop("scope")

        gid = d.pop("gid")

        member = cast(List[int], d.pop("member", UNSET))

        members = cast(List[int], d.pop("members", UNSET))

        privs = cast(List[str], d.pop("privs", UNSET))

        user_group = cls(
            name=name,
            description=description,
            scope=scope,
            gid=gid,
            member=member,
            members=members,
            privs=privs,
        )

        user_group.additional_properties = d
        return user_group

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
