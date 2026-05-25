from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.siproxd_config_files_files import SiproxdConfigFilesFiles


T = TypeVar("T", bound="SiproxdConfigFiles")


@_attrs_define
class SiproxdConfigFiles:
    """
    Attributes:
        files (SiproxdConfigFilesFiles | Unset):
    """

    files: SiproxdConfigFilesFiles | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.siproxd_config_files_files import SiproxdConfigFilesFiles

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: SiproxdConfigFilesFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = SiproxdConfigFilesFiles.from_dict(_files)

        siproxd_config_files = cls(
            files=files,
        )

        siproxd_config_files.additional_properties = d
        return siproxd_config_files

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
