from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagUploadRequest")


@_attrs_define
class DiagUploadRequest:
    """
    Attributes:
        filename (Union[Unset, str]):
        contents (Union[Unset, str]):
    """

    filename: Union[Unset, str] = UNSET
    contents: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filename = self.filename

        contents = self.contents

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filename is not UNSET:
            field_dict["filename"] = filename
        if contents is not UNSET:
            field_dict["contents"] = contents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filename = d.pop("filename", UNSET)

        contents = d.pop("contents", UNSET)

        diag_upload_request = cls(
            filename=filename,
            contents=contents,
        )

        diag_upload_request.additional_properties = d
        return diag_upload_request

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
