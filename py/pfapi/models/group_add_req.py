from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupAddReq")


@_attrs_define
class GroupAddReq:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        scope (Union[Unset, str]):
        gid (Union[Unset, int]):
        members (Union[Unset, List[int]]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    gid: Union[Unset, int] = UNSET
    members: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        scope = self.scope

        gid = self.gid

        members: Union[Unset, List[int]] = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if scope is not UNSET:
            field_dict["scope"] = scope
        if gid is not UNSET:
            field_dict["gid"] = gid
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        scope = d.pop("scope", UNSET)

        gid = d.pop("gid", UNSET)

        members = cast(List[int], d.pop("members", UNSET))

        group_add_req = cls(
            name=name,
            description=description,
            scope=scope,
            gid=gid,
            members=members,
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
