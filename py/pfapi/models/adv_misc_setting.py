from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        misc (Union[Unset, AdvMisc]):
    """

    misc: Union[Unset, "AdvMisc"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        misc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.misc, Unset):
            misc = self.misc.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if misc is not UNSET:
            field_dict["misc"] = misc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adv_misc import AdvMisc

        d = src_dict.copy()
        _misc = d.pop("misc", UNSET)
        misc: Union[Unset, AdvMisc]
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
