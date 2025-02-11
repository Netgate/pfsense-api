from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cert_info import CertInfo


T = TypeVar("T", bound="CertAuthority")


@_attrs_define
class CertAuthority:
    """
    Attributes:
        name (str):
        refid (str):
        internal (bool):
        issuer (str):
        certificates (int):
        inuse (List[str]):
        trust (bool):
        randomize_serial (bool):
        next_serial (int):
        info (CertInfo):
    """

    name: str
    refid: str
    internal: bool
    issuer: str
    certificates: int
    inuse: List[str]
    trust: bool
    randomize_serial: bool
    next_serial: int
    info: "CertInfo"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        refid = self.refid

        internal = self.internal

        issuer = self.issuer

        certificates = self.certificates

        inuse = self.inuse

        trust = self.trust

        randomize_serial = self.randomize_serial

        next_serial = self.next_serial

        info = self.info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "refid": refid,
                "internal": internal,
                "issuer": issuer,
                "certificates": certificates,
                "inuse": inuse,
                "trust": trust,
                "randomize_serial": randomize_serial,
                "next_serial": next_serial,
                "info": info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cert_info import CertInfo

        d = src_dict.copy()
        name = d.pop("name")

        refid = d.pop("refid")

        internal = d.pop("internal")

        issuer = d.pop("issuer")

        certificates = d.pop("certificates")

        inuse = cast(List[str], d.pop("inuse"))

        trust = d.pop("trust")

        randomize_serial = d.pop("randomize_serial")

        next_serial = d.pop("next_serial")

        info = CertInfo.from_dict(d.pop("info"))

        cert_authority = cls(
            name=name,
            refid=refid,
            internal=internal,
            issuer=issuer,
            certificates=certificates,
            inuse=inuse,
            trust=trust,
            randomize_serial=randomize_serial,
            next_serial=next_serial,
            info=info,
        )

        cert_authority.additional_properties = d
        return cert_authority

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
