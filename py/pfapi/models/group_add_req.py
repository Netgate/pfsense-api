from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupAddReq")


@_attrs_define
class GroupAddReq:
    """
    Attributes:
        name (str):
        scope (str):
        description (Union[Unset, str]):
        gid (Union[Unset, int]):
        members (Union[Unset, List[int]]):
        privs (Union[Unset, List[str]]):
    """

    name: str
    scope: str
    description: Union[Unset, str] = UNSET
    gid: Union[Unset, int] = UNSET
    members: Union[Unset, List[int]] = UNSET
    privs: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        scope = self.scope

        description = self.description

        gid = self.gid

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
                "scope": scope,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if gid is not UNSET:
            field_dict["gid"] = gid
        if members is not UNSET:
            field_dict["members"] = members
        if privs is not UNSET:
            field_dict["privs"] = privs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        scope = d.pop("scope")

        description = d.pop("description", UNSET)

        gid = d.pop("gid", UNSET)

        members = cast(List[int], d.pop("members", UNSET))

        privs = cast(List[str], d.pop("privs", UNSET))

        group_add_req = cls(
            name=name,
            scope=scope,
            description=description,
            gid=gid,
            members=members,
            privs=privs,
        )

        group_add_req.additional_properties = d
        return group_add_req

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
