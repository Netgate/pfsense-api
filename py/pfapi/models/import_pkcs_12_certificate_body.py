from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

if TYPE_CHECKING:
    from ..models.new_cert_req import NewCertReq


T = TypeVar("T", bound="ImportPkcs12CertificateBody")


@_attrs_define
class ImportPkcs12CertificateBody:
    """
    Attributes:
        reqdata (NewCertReq | Unset): Request for creating a cert or updating an existing one.
            - name: short description about certificate
            - userid: user-ID for user-specific certificate, eg for VPN
            - description:  Descriptive name
            - one of the method_xxxx
        pkcs12file (File | Unset):
    """

    reqdata: NewCertReq | Unset = UNSET
    pkcs12file: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reqdata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reqdata, Unset):
            reqdata = self.reqdata.to_dict()

        pkcs12file: FileTypes | Unset = UNSET
        if not isinstance(self.pkcs12file, Unset):
            pkcs12file = self.pkcs12file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reqdata is not UNSET:
            field_dict["reqdata"] = reqdata
        if pkcs12file is not UNSET:
            field_dict["pkcs12file"] = pkcs12file

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.reqdata, Unset):
            files.append(("reqdata", (None, json.dumps(self.reqdata.to_dict()).encode(), "application/json")))

        if not isinstance(self.pkcs12file, Unset):
            files.append(("pkcs12file", self.pkcs12file.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_cert_req import NewCertReq

        d = dict(src_dict)
        _reqdata = d.pop("reqdata", UNSET)
        reqdata: NewCertReq | Unset
        if isinstance(_reqdata, Unset):
            reqdata = UNSET
        else:
            reqdata = NewCertReq.from_dict(_reqdata)

        _pkcs12file = d.pop("pkcs12file", UNSET)
        pkcs12file: File | Unset
        if isinstance(_pkcs12file, Unset):
            pkcs12file = UNSET
        else:
            pkcs12file = File(payload=BytesIO(_pkcs12file))

        import_pkcs_12_certificate_body = cls(
            reqdata=reqdata,
            pkcs12file=pkcs12file,
        )

        import_pkcs_12_certificate_body.additional_properties = d
        return import_pkcs_12_certificate_body

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
