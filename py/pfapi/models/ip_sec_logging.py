from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IPSecLogging")


@_attrs_define
class IPSecLogging:
    """
    Attributes:
        dmn (str):
        mgr (str):
        ike (str):
        chd (str):
        job (str):
        cfg (str):
        knl (str):
        net (str):
        asn (str):
        enc (str):
        imc (str):
        imv (str):
        pts (str):
        tls (str):
        esp (str):
        lib (str):
    """

    dmn: str
    mgr: str
    ike: str
    chd: str
    job: str
    cfg: str
    knl: str
    net: str
    asn: str
    enc: str
    imc: str
    imv: str
    pts: str
    tls: str
    esp: str
    lib: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dmn = self.dmn

        mgr = self.mgr

        ike = self.ike

        chd = self.chd

        job = self.job

        cfg = self.cfg

        knl = self.knl

        net = self.net

        asn = self.asn

        enc = self.enc

        imc = self.imc

        imv = self.imv

        pts = self.pts

        tls = self.tls

        esp = self.esp

        lib = self.lib

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dmn": dmn,
                "mgr": mgr,
                "ike": ike,
                "chd": chd,
                "job": job,
                "cfg": cfg,
                "knl": knl,
                "net": net,
                "asn": asn,
                "enc": enc,
                "imc": imc,
                "imv": imv,
                "pts": pts,
                "tls": tls,
                "esp": esp,
                "lib": lib,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dmn = d.pop("dmn")

        mgr = d.pop("mgr")

        ike = d.pop("ike")

        chd = d.pop("chd")

        job = d.pop("job")

        cfg = d.pop("cfg")

        knl = d.pop("knl")

        net = d.pop("net")

        asn = d.pop("asn")

        enc = d.pop("enc")

        imc = d.pop("imc")

        imv = d.pop("imv")

        pts = d.pop("pts")

        tls = d.pop("tls")

        esp = d.pop("esp")

        lib = d.pop("lib")

        ip_sec_logging = cls(
            dmn=dmn,
            mgr=mgr,
            ike=ike,
            chd=chd,
            job=job,
            cfg=cfg,
            knl=knl,
            net=net,
            asn=asn,
            enc=enc,
            imc=imc,
            imv=imv,
            pts=pts,
            tls=tls,
            esp=esp,
            lib=lib,
        )

        ip_sec_logging.additional_properties = d
        return ip_sec_logging

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
