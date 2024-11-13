from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_adv_admin import SystemAdvAdmin


T = TypeVar("T", bound="SystemAdvAdminSetting")


@_attrs_define
class SystemAdvAdminSetting:
    """
    Attributes:
        admin (Union[Unset, SystemAdvAdmin]):
    """

    admin: Union[Unset, "SystemAdvAdmin"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        admin: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.admin, Unset):
            admin = self.admin.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin is not UNSET:
            field_dict["admin"] = admin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_adv_admin import SystemAdvAdmin

        d = src_dict.copy()
        _admin = d.pop("admin", UNSET)
        admin: Union[Unset, SystemAdvAdmin]
        if isinstance(_admin, Unset):
            admin = UNSET
        else:
            admin = SystemAdvAdmin.from_dict(_admin)

        system_adv_admin_setting = cls(
            admin=admin,
        )

        system_adv_admin_setting.additional_properties = d
        return system_adv_admin_setting

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
