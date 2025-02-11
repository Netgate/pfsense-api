from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SysFirmwareUpgradeOpt")


@_attrs_define
class SysFirmwareUpgradeOpt:
    """
    Attributes:
        upgrade (Union[Unset, bool]): set to true to confirm upgrade
    """

    upgrade: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upgrade = self.upgrade

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upgrade is not UNSET:
            field_dict["upgrade"] = upgrade

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        upgrade = d.pop("upgrade", UNSET)

        sys_firmware_upgrade_opt = cls(
            upgrade=upgrade,
        )

        sys_firmware_upgrade_opt.additional_properties = d
        return sys_firmware_upgrade_opt

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
