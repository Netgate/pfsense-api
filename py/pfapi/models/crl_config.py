from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crl_cert import CRLCert
    from ..models.crl_config_pkgs import CRLConfigPkgs


T = TypeVar("T", bound="CRLConfig")


@_attrs_define
class CRLConfig:
    """
    Attributes:
        refid (str):
        ca_refid (str):
        descr (Union[Unset, str]):
        method (Union[Unset, str]):
        serial (Union[Unset, int]):
        lifetime (Union[Unset, int]):
        internal (Union[Unset, bool]):
        inuse (Union[Unset, bool]):
        is_ovpn_crl (Union[Unset, bool]):
        text (Union[Unset, str]):
        cert (Union[Unset, List['CRLCert']]):
        pkgs (Union[Unset, CRLConfigPkgs]):
    """

    refid: str
    ca_refid: str
    descr: Union[Unset, str] = UNSET
    method: Union[Unset, str] = UNSET
    serial: Union[Unset, int] = UNSET
    lifetime: Union[Unset, int] = UNSET
    internal: Union[Unset, bool] = UNSET
    inuse: Union[Unset, bool] = UNSET
    is_ovpn_crl: Union[Unset, bool] = UNSET
    text: Union[Unset, str] = UNSET
    cert: Union[Unset, List["CRLCert"]] = UNSET
    pkgs: Union[Unset, "CRLConfigPkgs"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refid = self.refid

        ca_refid = self.ca_refid

        descr = self.descr

        method = self.method

        serial = self.serial

        lifetime = self.lifetime

        internal = self.internal

        inuse = self.inuse

        is_ovpn_crl = self.is_ovpn_crl

        text = self.text

        cert: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cert, Unset):
            cert = []
            for cert_item_data in self.cert:
                cert_item = cert_item_data.to_dict()
                cert.append(cert_item)

        pkgs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pkgs, Unset):
            pkgs = self.pkgs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refid": refid,
                "ca_refid": ca_refid,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if method is not UNSET:
            field_dict["method"] = method
        if serial is not UNSET:
            field_dict["serial"] = serial
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if internal is not UNSET:
            field_dict["internal"] = internal
        if inuse is not UNSET:
            field_dict["inuse"] = inuse
        if is_ovpn_crl is not UNSET:
            field_dict["is_ovpn_crl"] = is_ovpn_crl
        if text is not UNSET:
            field_dict["text"] = text
        if cert is not UNSET:
            field_dict["cert"] = cert
        if pkgs is not UNSET:
            field_dict["pkgs"] = pkgs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.crl_cert import CRLCert
        from ..models.crl_config_pkgs import CRLConfigPkgs

        d = src_dict.copy()
        refid = d.pop("refid")

        ca_refid = d.pop("ca_refid")

        descr = d.pop("descr", UNSET)

        method = d.pop("method", UNSET)

        serial = d.pop("serial", UNSET)

        lifetime = d.pop("lifetime", UNSET)

        internal = d.pop("internal", UNSET)

        inuse = d.pop("inuse", UNSET)

        is_ovpn_crl = d.pop("is_ovpn_crl", UNSET)

        text = d.pop("text", UNSET)

        cert = []
        _cert = d.pop("cert", UNSET)
        for cert_item_data in _cert or []:
            cert_item = CRLCert.from_dict(cert_item_data)

            cert.append(cert_item)

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
            internal=internal,
            inuse=inuse,
            is_ovpn_crl=is_ovpn_crl,
            text=text,
            cert=cert,
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
