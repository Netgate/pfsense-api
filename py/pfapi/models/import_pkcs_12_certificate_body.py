import json
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
    from ..models.new_cert_req import NewCertReq


T = TypeVar("T", bound="ImportPkcs12CertificateBody")


@_attrs_define
class ImportPkcs12CertificateBody:
    """
    Attributes:
        reqdata (Union[Unset, NewCertReq]): Request for creating a cert or updating an existing one.
            - name: short description about certificate
            - userid: user-ID for user-specific certificate, eg for VPN
            - description:  Descriptive name
            - one of the method_xxxx
        pkcs12file (Union[Unset, File]):
    """

    reqdata: Union[Unset, "NewCertReq"] = UNSET
    pkcs12file: Union[Unset, File] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reqdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reqdata, Unset):
            reqdata = self.reqdata.to_dict()

        pkcs12file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.pkcs12file, Unset):
            pkcs12file = self.pkcs12file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reqdata is not UNSET:
            field_dict["reqdata"] = reqdata
        if pkcs12file is not UNSET:
            field_dict["pkcs12file"] = pkcs12file

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        reqdata: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.reqdata, Unset):
            reqdata = (None, json.dumps(self.reqdata.to_dict()).encode(), "application/json")

        pkcs12file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.pkcs12file, Unset):
            pkcs12file = self.pkcs12file.to_tuple()

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if reqdata is not UNSET:
            field_dict["reqdata"] = reqdata
        if pkcs12file is not UNSET:
            field_dict["pkcs12file"] = pkcs12file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.new_cert_req import NewCertReq

        d = src_dict.copy()
        _reqdata = d.pop("reqdata", UNSET)
        reqdata: Union[Unset, NewCertReq]
        if isinstance(_reqdata, Unset):
            reqdata = UNSET
        else:
            reqdata = NewCertReq.from_dict(_reqdata)

        _pkcs12file = d.pop("pkcs12file", UNSET)
        pkcs12file: Union[Unset, File]
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
