from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyErrorFile")


@_attrs_define
class HaproxyErrorFile:
    """
    Attributes:
        errorcode (str | Unset): Error Code

            HTTP error code to intercept (e.g. 200, 400, 403, 405, 408, 425, 429, 500, 502, 503, 504).
        errorfile (str | Unset): Error File

            Reference name of the HAProxy file containing the custom error response.
    """

    errorcode: str | Unset = UNSET
    errorfile: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errorcode = self.errorcode

        errorfile = self.errorfile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errorcode is not UNSET:
            field_dict["errorcode"] = errorcode
        if errorfile is not UNSET:
            field_dict["errorfile"] = errorfile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        errorcode = d.pop("errorcode", UNSET)

        errorfile = d.pop("errorfile", UNSET)

        haproxy_error_file = cls(
            errorcode=errorcode,
            errorfile=errorfile,
        )

        haproxy_error_file.additional_properties = d
        return haproxy_error_file

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
