from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_generic import UserGeneric
    from ..models.user_group import UserGroup


T = TypeVar("T", bound="UsersConfigGeneric")


@_attrs_define
class UsersConfigGeneric:
    """Generic user for all platforms

    Attributes:
        users (List['UserGeneric']):
        groups (List['UserGroup']):
    """

    users: List["UserGeneric"]
    groups: List["UserGroup"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
                "groups": groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_generic import UserGeneric
        from ..models.user_group import UserGroup

        d = src_dict.copy()
        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = UserGeneric.from_dict(users_item_data)

            users.append(users_item)

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = UserGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        users_config_generic = cls(
            users=users,
            groups=groups,
        )

        users_config_generic.additional_properties = d
        return users_config_generic

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
