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
        descr (str):
        method (str):
        serial (int):
        lifetime (int):
        internal (bool):
        inuse (bool):
        is_ovpn_crl (bool):
        text (str):
        pkgs (CRLConfigPkgs):
        cert (Union[Unset, List['CRLCert']]):
    """

    refid: str
    ca_refid: str
    descr: str
    method: str
    serial: int
    lifetime: int
    internal: bool
    inuse: bool
    is_ovpn_crl: bool
    text: str
    pkgs: "CRLConfigPkgs"
    cert: Union[Unset, List["CRLCert"]] = UNSET
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

        pkgs = self.pkgs.to_dict()

        cert: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cert, Unset):
            cert = []
            for cert_item_data in self.cert:
                cert_item = cert_item_data.to_dict()
                cert.append(cert_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refid": refid,
                "ca_refid": ca_refid,
                "descr": descr,
                "method": method,
                "serial": serial,
                "lifetime": lifetime,
                "internal": internal,
                "inuse": inuse,
                "is_ovpn_crl": is_ovpn_crl,
                "text": text,
                "pkgs": pkgs,
            }
        )
        if cert is not UNSET:
            field_dict["cert"] = cert

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.crl_cert import CRLCert
        from ..models.crl_config_pkgs import CRLConfigPkgs

        d = src_dict.copy()
        refid = d.pop("refid")

        ca_refid = d.pop("ca_refid")

        descr = d.pop("descr")

        method = d.pop("method")

        serial = d.pop("serial")

        lifetime = d.pop("lifetime")

        internal = d.pop("internal")

        inuse = d.pop("inuse")

        is_ovpn_crl = d.pop("is_ovpn_crl")

        text = d.pop("text")

        pkgs = CRLConfigPkgs.from_dict(d.pop("pkgs"))

        cert = []
        _cert = d.pop("cert", UNSET)
        for cert_item_data in _cert or []:
            cert_item = CRLCert.from_dict(cert_item_data)

            cert.append(cert_item)

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
            pkgs=pkgs,
            cert=cert,
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
