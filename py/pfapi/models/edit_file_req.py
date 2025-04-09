from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditFileReq")


@_attrs_define
class EditFileReq:
    """
    Attributes:
        fname (Union[Unset, str]):
        fcontents (Union[Unset, str]):
    """

    fname: Union[Unset, str] = UNSET
    fcontents: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fname = self.fname

        fcontents = self.fcontents

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fname is not UNSET:
            field_dict["fname"] = fname
        if fcontents is not UNSET:
            field_dict["fcontents"] = fcontents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fname = d.pop("fname", UNSET)

        fcontents = d.pop("fcontents", UNSET)

        edit_file_req = cls(
            fname=fname,
            fcontents=fcontents,
        )

        edit_file_req.additional_properties = d
        return edit_file_req

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
