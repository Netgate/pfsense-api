from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crl_config_pkgs import CRLConfigPkgs


T = TypeVar("T", bound="CRLConfig")


@_attrs_define
class CRLConfig:
    """
    Attributes:
        refid (Union[Unset, str]):
        ca_refid (Union[Unset, str]):
        descr (Union[Unset, str]):
        method (Union[Unset, str]):
        serial (Union[Unset, int]):
        lifetime (Union[Unset, int]):
        cert (Union[Unset, str]):
        text (Union[Unset, str]):
        internal (Union[Unset, bool]):
        inuse (Union[Unset, bool]):
        is_ovpn_crl (Union[Unset, bool]):
        pkgs (Union[Unset, CRLConfigPkgs]):
    """

    refid: Union[Unset, str] = UNSET
    ca_refid: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    method: Union[Unset, str] = UNSET
    serial: Union[Unset, int] = UNSET
    lifetime: Union[Unset, int] = UNSET
    cert: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    internal: Union[Unset, bool] = UNSET
    inuse: Union[Unset, bool] = UNSET
    is_ovpn_crl: Union[Unset, bool] = UNSET
    pkgs: Union[Unset, "CRLConfigPkgs"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refid = self.refid

        ca_refid = self.ca_refid

        descr = self.descr

        method = self.method

        serial = self.serial

        lifetime = self.lifetime

        cert = self.cert

        text = self.text

        internal = self.internal

        inuse = self.inuse

        is_ovpn_crl = self.is_ovpn_crl

        pkgs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pkgs, Unset):
            pkgs = self.pkgs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refid is not UNSET:
            field_dict["refid"] = refid
        if ca_refid is not UNSET:
            field_dict["ca_refid"] = ca_refid
        if descr is not UNSET:
            field_dict["descr"] = descr
        if method is not UNSET:
            field_dict["method"] = method
        if serial is not UNSET:
            field_dict["serial"] = serial
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if cert is not UNSET:
            field_dict["cert"] = cert
        if text is not UNSET:
            field_dict["text"] = text
        if internal is not UNSET:
            field_dict["internal"] = internal
        if inuse is not UNSET:
            field_dict["inuse"] = inuse
        if is_ovpn_crl is not UNSET:
            field_dict["is_ovpn_crl"] = is_ovpn_crl
        if pkgs is not UNSET:
            field_dict["pkgs"] = pkgs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.crl_config_pkgs import CRLConfigPkgs

        d = src_dict.copy()
        refid = d.pop("refid", UNSET)

        ca_refid = d.pop("ca_refid", UNSET)

        descr = d.pop("descr", UNSET)

        method = d.pop("method", UNSET)

        serial = d.pop("serial", UNSET)

        lifetime = d.pop("lifetime", UNSET)

        cert = d.pop("cert", UNSET)

        text = d.pop("text", UNSET)

        internal = d.pop("internal", UNSET)

        inuse = d.pop("inuse", UNSET)

        is_ovpn_crl = d.pop("is_ovpn_crl", UNSET)

        _pkgs = d.pop("pkgs", UNSET)
        pkgs: Union[Unset, CRLConfigPkgs]
        if isinstance(_pkgs, Unset):
            pkgs = UNSET
        else:
            pkgs = CRLConfigPkgs.from_dict(_pkgs)

        crl_config = cls(
            refid=refid,
            ca_refid=ca_refid,
            descr=descr,
            method=method,
            serial=serial,
            lifetime=lifetime,
            cert=cert,
            text=text,
            internal=internal,
            inuse=inuse,
            is_ovpn_crl=is_ovpn_crl,
            pkgs=pkgs,
        )

        crl_config.additional_properties = d
        return crl_config

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
