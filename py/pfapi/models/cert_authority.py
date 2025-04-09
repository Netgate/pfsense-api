from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cert_info import CertInfo


T = TypeVar("T", bound="CertAuthority")


@_attrs_define
class CertAuthority:
    """
    Attributes:
        name (str):
        refid (str):
        internal (Union[Unset, bool]):
        issuer (Union[Unset, str]):
        certificates (Union[Unset, int]):
        inuse (Union[Unset, List[str]]):
        trust (Union[Unset, bool]):
        randomize_serial (Union[Unset, bool]):
        next_serial (Union[Unset, int]):
        info (Union[Unset, CertInfo]):
    """

    name: str
    refid: str
    internal: Union[Unset, bool] = UNSET
    issuer: Union[Unset, str] = UNSET
    certificates: Union[Unset, int] = UNSET
    inuse: Union[Unset, List[str]] = UNSET
    trust: Union[Unset, bool] = UNSET
    randomize_serial: Union[Unset, bool] = UNSET
    next_serial: Union[Unset, int] = UNSET
    info: Union[Unset, "CertInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        refid = self.refid

        internal = self.internal

        issuer = self.issuer

        certificates = self.certificates

        inuse: Union[Unset, List[str]] = UNSET
        if not isinstance(self.inuse, Unset):
            inuse = self.inuse

        trust = self.trust

        randomize_serial = self.randomize_serial

        next_serial = self.next_serial

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "refid": refid,
            }
        )
        if internal is not UNSET:
            field_dict["internal"] = internal
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if certificates is not UNSET:
            field_dict["certificates"] = certificates
        if inuse is not UNSET:
            field_dict["inuse"] = inuse
        if trust is not UNSET:
            field_dict["trust"] = trust
        if randomize_serial is not UNSET:
            field_dict["randomize_serial"] = randomize_serial
        if next_serial is not UNSET:
            field_dict["next_serial"] = next_serial
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cert_info import CertInfo

        d = src_dict.copy()
        name = d.pop("name")

        refid = d.pop("refid")

        internal = d.pop("internal", UNSET)

        issuer = d.pop("issuer", UNSET)

        certificates = d.pop("certificates", UNSET)

        inuse = cast(List[str], d.pop("inuse", UNSET))

        trust = d.pop("trust", UNSET)

        randomize_serial = d.pop("randomize_serial", UNSET)

        next_serial = d.pop("next_serial", UNSET)

        _info = d.pop("info", UNSET)
        info: Union[Unset, CertInfo]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = CertInfo.from_dict(_info)

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
