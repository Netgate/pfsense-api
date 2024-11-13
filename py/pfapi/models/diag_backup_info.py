from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagBackupInfo")


@_attrs_define
class DiagBackupInfo:
    """
    Attributes:
        time (Union[Unset, int]):
        desc (Union[Unset, str]):
        size (Union[Unset, int]):
        vers (Union[Unset, str]):
    """

    time: Union[Unset, int] = UNSET
    desc: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    vers: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time

        desc = self.desc

        size = self.size

        vers = self.vers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if desc is not UNSET:
            field_dict["desc"] = desc
        if size is not UNSET:
            field_dict["size"] = size
        if vers is not UNSET:
            field_dict["vers"] = vers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = d.pop("time", UNSET)

        desc = d.pop("desc", UNSET)

        size = d.pop("size", UNSET)

        vers = d.pop("vers", UNSET)

        diag_backup_info = cls(
            time=time,
            desc=desc,
            size=size,
            vers=vers,
        )

        diag_backup_info.additional_properties = d
        return diag_backup_info

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
