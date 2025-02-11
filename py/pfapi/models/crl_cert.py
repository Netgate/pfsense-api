from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CRLCert")


@_attrs_define
class CRLCert:
    """
    Attributes:
        refid (str):
        ca_refid (str):
        descr (str):
        type (str):
        cert (str):
        privkey (str):
        serial (int):
        reason (str):
        revoke_time (int):
    """

    refid: str
    ca_refid: str
    descr: str
    type: str
    cert: str
    privkey: str
    serial: int
    reason: str
    revoke_time: int
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
        field_dict.update(
            {
                "refid": refid,
                "ca_refid": ca_refid,
                "descr": descr,
                "type": type,
                "cert": cert,
                "privkey": privkey,
                "serial": serial,
                "reason": reason,
                "revoke_time": revoke_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        refid = d.pop("refid")

        ca_refid = d.pop("ca_refid")

        descr = d.pop("descr")

        type = d.pop("type")

        cert = d.pop("cert")

        privkey = d.pop("privkey")

        serial = d.pop("serial")

        reason = d.pop("reason")

        revoke_time = d.pop("revoke_time")

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
