from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cert_info import CertInfo


T = TypeVar("T", bound="CertificateDetailed")


@_attrs_define
class CertificateDetailed:
    """
    Attributes:
        refid (str):
        descr (str):
        crt (str):
        csr (str):
        caref (str):
        cadata (str):
        ends (str):
        inuse (str):
        issuer (str):
        prv (str):
        starts (str):
        subj (str):
        type (str):
        name (str):
        dn (str):
        info (CertInfo):
        can_renew (bool):
    """

    refid: str
    descr: str
    crt: str
    csr: str
    caref: str
    cadata: str
    ends: str
    inuse: str
    issuer: str
    prv: str
    starts: str
    subj: str
    type: str
    name: str
    dn: str
    info: "CertInfo"
    can_renew: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refid = self.refid

        descr = self.descr

        crt = self.crt

        csr = self.csr

        caref = self.caref

        cadata = self.cadata

        ends = self.ends

        inuse = self.inuse

        issuer = self.issuer

        prv = self.prv

        starts = self.starts

        subj = self.subj

        type = self.type

        name = self.name

        dn = self.dn

        info = self.info.to_dict()

        can_renew = self.can_renew

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refid": refid,
                "descr": descr,
                "crt": crt,
                "csr": csr,
                "caref": caref,
                "cadata": cadata,
                "ends": ends,
                "inuse": inuse,
                "issuer": issuer,
                "prv": prv,
                "starts": starts,
                "subj": subj,
                "type": type,
                "name": name,
                "dn": dn,
                "info": info,
                "can_renew": can_renew,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cert_info import CertInfo

        d = src_dict.copy()
        refid = d.pop("refid")

        descr = d.pop("descr")

        crt = d.pop("crt")

        csr = d.pop("csr")

        caref = d.pop("caref")

        cadata = d.pop("cadata")

        ends = d.pop("ends")

        inuse = d.pop("inuse")

        issuer = d.pop("issuer")

        prv = d.pop("prv")

        starts = d.pop("starts")

        subj = d.pop("subj")

        type = d.pop("type")

        name = d.pop("name")

        dn = d.pop("dn")

        info = CertInfo.from_dict(d.pop("info"))

        can_renew = d.pop("can_renew")

        certificate_detailed = cls(
            refid=refid,
            descr=descr,
            crt=crt,
            csr=csr,
            caref=caref,
            cadata=cadata,
            ends=ends,
            inuse=inuse,
            issuer=issuer,
            prv=prv,
            starts=starts,
            subj=subj,
            type=type,
            name=name,
            dn=dn,
            info=info,
            can_renew=can_renew,
        )

        certificate_detailed.additional_properties = d
        return certificate_detailed

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
