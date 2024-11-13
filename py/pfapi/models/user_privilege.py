from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPrivilege")


@_attrs_define
class UserPrivilege:
    """
    Attributes:
        value (Union[Unset, str]):
        text (Union[Unset, str]):
        descr (Union[Unset, str]):
        warn (Union[Unset, str]):
    """

    value: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    warn: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        text = self.text

        descr = self.descr

        warn = self.warn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if text is not UNSET:
            field_dict["text"] = text
        if descr is not UNSET:
            field_dict["descr"] = descr
        if warn is not UNSET:
            field_dict["warn"] = warn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        text = d.pop("text", UNSET)

        descr = d.pop("descr", UNSET)

        warn = d.pop("warn", UNSET)

        user_privilege = cls(
            value=value,
            text=text,
            descr=descr,
            warn=warn,
        )

        user_privilege.additional_properties = d
        return user_privilege

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
