from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CRLCert")


@_attrs_define
class CRLCert:
    """
    Attributes:
        refid (Union[Unset, str]):
        ca_refid (Union[Unset, str]):
        descr (Union[Unset, str]):
        type (Union[Unset, str]):
        cert (Union[Unset, str]):
        privkey (Union[Unset, str]):
        serial (Union[Unset, int]):
        reason (Union[Unset, str]):
        revoke_time (Union[Unset, int]):
    """

    refid: Union[Unset, str] = UNSET
    ca_refid: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    cert: Union[Unset, str] = UNSET
    privkey: Union[Unset, str] = UNSET
    serial: Union[Unset, int] = UNSET
    reason: Union[Unset, str] = UNSET
    revoke_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refid = self.refid

        ca_refid = self.ca_refid

        descr = self.descr

        type = self.type

        cert = self.cert

        privkey = self.privkey

        serial = self.serial

        reason = self.reason

        revoke_time = self.revoke_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refid is not UNSET:
            field_dict["refid"] = refid
        if ca_refid is not UNSET:
            field_dict["ca_refid"] = ca_refid
        if descr is not UNSET:
            field_dict["descr"] = descr
        if type is not UNSET:
            field_dict["type"] = type
        if cert is not UNSET:
            field_dict["cert"] = cert
        if privkey is not UNSET:
            field_dict["privkey"] = privkey
        if serial is not UNSET:
            field_dict["serial"] = serial
        if reason is not UNSET:
            field_dict["reason"] = reason
        if revoke_time is not UNSET:
            field_dict["revoke_time"] = revoke_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        refid = d.pop("refid", UNSET)

        ca_refid = d.pop("ca_refid", UNSET)

        descr = d.pop("descr", UNSET)

        type = d.pop("type", UNSET)

        cert = d.pop("cert", UNSET)

        privkey = d.pop("privkey", UNSET)

        serial = d.pop("serial", UNSET)

        reason = d.pop("reason", UNSET)

        revoke_time = d.pop("revoke_time", UNSET)

        crl_cert = cls(
            refid=refid,
            ca_refid=ca_refid,
            descr=descr,
            type=type,
            cert=cert,
            privkey=privkey,
            serial=serial,
            reason=reason,
            revoke_time=revoke_time,
        )

        crl_cert.additional_properties = d
        return crl_cert

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
