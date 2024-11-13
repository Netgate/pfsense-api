import json
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
    from ..models.update_pkcs12_cert_req import UpdatePKCS12CertReq


T = TypeVar("T", bound="PatchSystemCertificatesRefidBody")


@_attrs_define
class PatchSystemCertificatesRefidBody:
    """
    Attributes:
        reqdata (Union[Unset, UpdatePKCS12CertReq]): Update the certificate with PKCS12 appended file upload
        pcsk12file (Union[Unset, File]):
    """

    reqdata: Union[Unset, "UpdatePKCS12CertReq"] = UNSET
    pcsk12file: Union[Unset, File] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reqdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reqdata, Unset):
            reqdata = self.reqdata.to_dict()

        pcsk12file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.pcsk12file, Unset):
            pcsk12file = self.pcsk12file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reqdata is not UNSET:
            field_dict["reqdata"] = reqdata
        if pcsk12file is not UNSET:
            field_dict["pcsk12file"] = pcsk12file

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        reqdata: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.reqdata, Unset):
            reqdata = (None, json.dumps(self.reqdata.to_dict()).encode(), "application/json")

        pcsk12file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.pcsk12file, Unset):
            pcsk12file = self.pcsk12file.to_tuple()

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if reqdata is not UNSET:
            field_dict["reqdata"] = reqdata
        if pcsk12file is not UNSET:
            field_dict["pcsk12file"] = pcsk12file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_pkcs12_cert_req import UpdatePKCS12CertReq

        d = src_dict.copy()
        _reqdata = d.pop("reqdata", UNSET)
        reqdata: Union[Unset, UpdatePKCS12CertReq]
        if isinstance(_reqdata, Unset):
            reqdata = UNSET
        else:
            reqdata = UpdatePKCS12CertReq.from_dict(_reqdata)

        _pcsk12file = d.pop("pcsk12file", UNSET)
        pcsk12file: Union[Unset, File]
        if isinstance(_pcsk12file, Unset):
            pcsk12file = UNSET
        else:
            pcsk12file = File(payload=BytesIO(_pcsk12file))

        patch_system_certificates_refid_body = cls(
            reqdata=reqdata,
            pcsk12file=pcsk12file,
        )

        patch_system_certificates_refid_body.additional_properties = d
        return patch_system_certificates_refid_body

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
