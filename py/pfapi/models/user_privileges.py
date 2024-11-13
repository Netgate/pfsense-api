from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_privilege import UserPrivilege


T = TypeVar("T", bound="UserPrivileges")


@_attrs_define
class UserPrivileges:
    """
    Attributes:
        privs (Union[Unset, List['UserPrivilege']]):
    """

    privs: Union[Unset, List["UserPrivilege"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        privs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.privs, Unset):
            privs = []
            for privs_item_data in self.privs:
                privs_item = privs_item_data.to_dict()
                privs.append(privs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if privs is not UNSET:
            field_dict["privs"] = privs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_privilege import UserPrivilege

        d = src_dict.copy()
        privs = []
        _privs = d.pop("privs", UNSET)
        for privs_item_data in _privs or []:
            privs_item = UserPrivilege.from_dict(privs_item_data)

            privs.append(privs_item)

        user_privileges = cls(
            privs=privs,
        )

        user_privileges.additional_properties = d
        return user_privileges

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
