from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cert_info import CertInfo


T = TypeVar("T", bound="CertificateDetailed")


@_attrs_define
class CertificateDetailed:
    """
    Attributes:
        refid (Union[Unset, str]):
        descr (Union[Unset, str]):
        crt (Union[Unset, str]):
        csr (Union[Unset, str]):
        caref (Union[Unset, str]):
        cadata (Union[Unset, str]):
        ends (Union[Unset, str]):
        inuse (Union[Unset, str]):
        issuer (Union[Unset, str]):
        prv (Union[Unset, str]):
        starts (Union[Unset, str]):
        subj (Union[Unset, str]):
        type (Union[Unset, str]):
        name (Union[Unset, str]):
        dn (Union[Unset, str]):
        info (Union[Unset, CertInfo]):
        can_renew (Union[Unset, bool]):
    """

    refid: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    crt: Union[Unset, str] = UNSET
    csr: Union[Unset, str] = UNSET
    caref: Union[Unset, str] = UNSET
    cadata: Union[Unset, str] = UNSET
    ends: Union[Unset, str] = UNSET
    inuse: Union[Unset, str] = UNSET
    issuer: Union[Unset, str] = UNSET
    prv: Union[Unset, str] = UNSET
    starts: Union[Unset, str] = UNSET
    subj: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    dn: Union[Unset, str] = UNSET
    info: Union[Unset, "CertInfo"] = UNSET
    can_renew: Union[Unset, bool] = UNSET
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

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        can_renew = self.can_renew

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refid is not UNSET:
            field_dict["refid"] = refid
        if descr is not UNSET:
            field_dict["descr"] = descr
        if crt is not UNSET:
            field_dict["crt"] = crt
        if csr is not UNSET:
            field_dict["csr"] = csr
        if caref is not UNSET:
            field_dict["caref"] = caref
        if cadata is not UNSET:
            field_dict["cadata"] = cadata
        if ends is not UNSET:
            field_dict["ends"] = ends
        if inuse is not UNSET:
            field_dict["inuse"] = inuse
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if prv is not UNSET:
            field_dict["prv"] = prv
        if starts is not UNSET:
            field_dict["starts"] = starts
        if subj is not UNSET:
            field_dict["subj"] = subj
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if dn is not UNSET:
            field_dict["dn"] = dn
        if info is not UNSET:
            field_dict["info"] = info
        if can_renew is not UNSET:
            field_dict["can_renew"] = can_renew

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cert_info import CertInfo

        d = src_dict.copy()
        refid = d.pop("refid", UNSET)

        descr = d.pop("descr", UNSET)

        crt = d.pop("crt", UNSET)

        csr = d.pop("csr", UNSET)

        caref = d.pop("caref", UNSET)

        cadata = d.pop("cadata", UNSET)

        ends = d.pop("ends", UNSET)

        inuse = d.pop("inuse", UNSET)

        issuer = d.pop("issuer", UNSET)

        prv = d.pop("prv", UNSET)

        starts = d.pop("starts", UNSET)

        subj = d.pop("subj", UNSET)

        type = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        dn = d.pop("dn", UNSET)

        _info = d.pop("info", UNSET)
        info: Union[Unset, CertInfo]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = CertInfo.from_dict(_info)

        can_renew = d.pop("can_renew", UNSET)

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
