from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adv_misc import AdvMisc


T = TypeVar("T", bound="AdvMiscSetting")


@_attrs_define
class AdvMiscSetting:
    """
    Attributes:
        misc (AdvMisc | Unset):
    """

    misc: AdvMisc | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        misc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.misc, Unset):
            misc = self.misc.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if misc is not UNSET:
            field_dict["misc"] = misc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adv_misc import AdvMisc

        d = dict(src_dict)
        _misc = d.pop("misc", UNSET)
        misc: AdvMisc | Unset
        if isinstance(_misc, Unset):
            misc = UNSET
        else:
            misc = AdvMisc.from_dict(_misc)

        adv_misc_setting = cls(
            misc=misc,
        )

        adv_misc_setting.additional_properties = d
        return adv_misc_setting

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
