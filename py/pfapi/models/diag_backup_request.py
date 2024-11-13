from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagBackupRequest")


@_attrs_define
class DiagBackupRequest:
    """
    Attributes:
        area (Union[Unset, str]):
        nopkg (Union[Unset, bool]):
        norrd (Union[Unset, bool]):
        enc (Union[Unset, bool]):
        pwd (Union[Unset, str]):
        filename (Union[Unset, str]):
        contents (Union[Unset, str]):
    """

    area: Union[Unset, str] = UNSET
    nopkg: Union[Unset, bool] = UNSET
    norrd: Union[Unset, bool] = UNSET
    enc: Union[Unset, bool] = UNSET
    pwd: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    contents: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        area = self.area

        nopkg = self.nopkg

        norrd = self.norrd

        enc = self.enc

        pwd = self.pwd

        filename = self.filename

        contents = self.contents

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area is not UNSET:
            field_dict["area"] = area
        if nopkg is not UNSET:
            field_dict["nopkg"] = nopkg
        if norrd is not UNSET:
            field_dict["norrd"] = norrd
        if enc is not UNSET:
            field_dict["enc"] = enc
        if pwd is not UNSET:
            field_dict["pwd"] = pwd
        if filename is not UNSET:
            field_dict["filename"] = filename
        if contents is not UNSET:
            field_dict["contents"] = contents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        area = d.pop("area", UNSET)

        nopkg = d.pop("nopkg", UNSET)

        norrd = d.pop("norrd", UNSET)

        enc = d.pop("enc", UNSET)

        pwd = d.pop("pwd", UNSET)

        filename = d.pop("filename", UNSET)

        contents = d.pop("contents", UNSET)

        diag_backup_request = cls(
            area=area,
            nopkg=nopkg,
            norrd=norrd,
            enc=enc,
            pwd=pwd,
            filename=filename,
            contents=contents,
        )

        diag_backup_request.additional_properties = d
        return diag_backup_request

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
