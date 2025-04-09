from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DirtySubsystem")


@_attrs_define
class DirtySubsystem:
    """
    Attributes:
        name (Union[Unset, str]):
        descr (Union[Unset, str]):
        file (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    file: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        descr = self.descr

        file = self.file

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        file = d.pop("file", UNSET)

        dirty_subsystem = cls(
            name=name,
            descr=descr,
            file=file,
        )

        dirty_subsystem.additional_properties = d
        return dirty_subsystem

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
