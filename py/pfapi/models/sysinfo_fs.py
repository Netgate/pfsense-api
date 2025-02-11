from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SysinfoFs")


@_attrs_define
class SysinfoFs:
    """
    Attributes:
        path (str):
        fs_name (str):
        fs_type (str):
        total (int):
        used (int):
    """

    path: str
    fs_name: str
    fs_type: str
    total: int
    used: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path

        fs_name = self.fs_name

        fs_type = self.fs_type

        total = self.total

        used = self.used

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "fs_name": fs_name,
                "fs_type": fs_type,
                "total": total,
                "used": used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        fs_name = d.pop("fs_name")

        fs_type = d.pop("fs_type")

        total = d.pop("total")

        used = d.pop("used")

        sysinfo_fs = cls(
            path=path,
            fs_name=fs_name,
            fs_type=fs_type,
            total=total,
            used=used,
        )

        sysinfo_fs.additional_properties = d
        return sysinfo_fs

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
