from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_group import UserGroup


T = TypeVar("T", bound="UserGroups")


@_attrs_define
class UserGroups:
    """
    Attributes:
        groups (Union[Unset, List['UserGroup']]):
        errmsg (Union[Unset, str]): errors in group modify operations
    """

    groups: Union[Unset, List["UserGroup"]] = UNSET
    errmsg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        errmsg = self.errmsg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if errmsg is not UNSET:
            field_dict["errmsg"] = errmsg

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_group import UserGroup

        d = src_dict.copy()
        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = UserGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        errmsg = d.pop("errmsg", UNSET)

        user_groups = cls(
            groups=groups,
            errmsg=errmsg,
        )

        user_groups.additional_properties = d
        return user_groups

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
