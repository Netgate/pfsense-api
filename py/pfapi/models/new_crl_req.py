from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crl_method_new import CRLMethodNew
    from ..models.crl_method_x509 import CRLMethodX509


T = TypeVar("T", bound="NewCRLReq")


@_attrs_define
class NewCRLReq:
    """
    Attributes:
        ca_refid (Union[Unset, str]): CA reference ID
        descr (Union[Unset, str]): descriptive name
        method_internal (Union[Unset, CRLMethodNew]):
        method_x509 (Union[Unset, CRLMethodX509]):
    """

    ca_refid: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    method_internal: Union[Unset, "CRLMethodNew"] = UNSET
    method_x509: Union[Unset, "CRLMethodX509"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ca_refid = self.ca_refid

        descr = self.descr

        method_internal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.method_internal, Unset):
            method_internal = self.method_internal.to_dict()

        method_x509: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.method_x509, Unset):
            method_x509 = self.method_x509.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ca_refid is not UNSET:
            field_dict["ca_refid"] = ca_refid
        if descr is not UNSET:
            field_dict["descr"] = descr
        if method_internal is not UNSET:
            field_dict["method_internal"] = method_internal
        if method_x509 is not UNSET:
            field_dict["method_x509"] = method_x509

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.crl_method_new import CRLMethodNew
        from ..models.crl_method_x509 import CRLMethodX509

        d = src_dict.copy()
        ca_refid = d.pop("ca_refid", UNSET)

        descr = d.pop("descr", UNSET)

        _method_internal = d.pop("method_internal", UNSET)
        method_internal: Union[Unset, CRLMethodNew]
        if isinstance(_method_internal, Unset):
            method_internal = UNSET
        else:
            method_internal = CRLMethodNew.from_dict(_method_internal)

        _method_x509 = d.pop("method_x509", UNSET)
        method_x509: Union[Unset, CRLMethodX509]
        if isinstance(_method_x509, Unset):
            method_x509 = UNSET
        else:
            method_x509 = CRLMethodX509.from_dict(_method_x509)

        new_crl_req = cls(
            ca_refid=ca_refid,
            descr=descr,
            method_internal=method_internal,
            method_x509=method_x509,
        )

        new_crl_req.additional_properties = d
        return new_crl_req

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
