from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBootenv")


@_attrs_define
class UpdateBootenv:
    """
    Attributes:
        old_name (Union[Unset, str]):
        name (Union[Unset, str]):
        descr (Union[Unset, str]):
        protect (Union[Unset, bool]):
    """

    old_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    protect: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        old_name = self.old_name

        name = self.name

        descr = self.descr

        protect = self.protect

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if old_name is not UNSET:
            field_dict["old_name"] = old_name
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if protect is not UNSET:
            field_dict["protect"] = protect

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        old_name = d.pop("old_name", UNSET)

        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        protect = d.pop("protect", UNSET)

        update_bootenv = cls(
            old_name=old_name,
            name=name,
            descr=descr,
            protect=protect,
        )

        update_bootenv.additional_properties = d
        return update_bootenv

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
