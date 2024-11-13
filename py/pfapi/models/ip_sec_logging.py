from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecLogging")


@_attrs_define
class IPSecLogging:
    """
    Attributes:
        dmn (Union[Unset, str]):
        mgr (Union[Unset, str]):
        ike (Union[Unset, str]):
        chd (Union[Unset, str]):
        job (Union[Unset, str]):
        cfg (Union[Unset, str]):
        knl (Union[Unset, str]):
        net (Union[Unset, str]):
        asn (Union[Unset, str]):
        enc (Union[Unset, str]):
        imc (Union[Unset, str]):
        imv (Union[Unset, str]):
        pts (Union[Unset, str]):
        tls (Union[Unset, str]):
        esp (Union[Unset, str]):
        lib (Union[Unset, str]):
    """

    dmn: Union[Unset, str] = UNSET
    mgr: Union[Unset, str] = UNSET
    ike: Union[Unset, str] = UNSET
    chd: Union[Unset, str] = UNSET
    job: Union[Unset, str] = UNSET
    cfg: Union[Unset, str] = UNSET
    knl: Union[Unset, str] = UNSET
    net: Union[Unset, str] = UNSET
    asn: Union[Unset, str] = UNSET
    enc: Union[Unset, str] = UNSET
    imc: Union[Unset, str] = UNSET
    imv: Union[Unset, str] = UNSET
    pts: Union[Unset, str] = UNSET
    tls: Union[Unset, str] = UNSET
    esp: Union[Unset, str] = UNSET
    lib: Union[Unset, str] = UNSET
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
        field_dict.update({})
        if dmn is not UNSET:
            field_dict["dmn"] = dmn
        if mgr is not UNSET:
            field_dict["mgr"] = mgr
        if ike is not UNSET:
            field_dict["ike"] = ike
        if chd is not UNSET:
            field_dict["chd"] = chd
        if job is not UNSET:
            field_dict["job"] = job
        if cfg is not UNSET:
            field_dict["cfg"] = cfg
        if knl is not UNSET:
            field_dict["knl"] = knl
        if net is not UNSET:
            field_dict["net"] = net
        if asn is not UNSET:
            field_dict["asn"] = asn
        if enc is not UNSET:
            field_dict["enc"] = enc
        if imc is not UNSET:
            field_dict["imc"] = imc
        if imv is not UNSET:
            field_dict["imv"] = imv
        if pts is not UNSET:
            field_dict["pts"] = pts
        if tls is not UNSET:
            field_dict["tls"] = tls
        if esp is not UNSET:
            field_dict["esp"] = esp
        if lib is not UNSET:
            field_dict["lib"] = lib

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dmn = d.pop("dmn", UNSET)

        mgr = d.pop("mgr", UNSET)

        ike = d.pop("ike", UNSET)

        chd = d.pop("chd", UNSET)

        job = d.pop("job", UNSET)

        cfg = d.pop("cfg", UNSET)

        knl = d.pop("knl", UNSET)

        net = d.pop("net", UNSET)

        asn = d.pop("asn", UNSET)

        enc = d.pop("enc", UNSET)

        imc = d.pop("imc", UNSET)

        imv = d.pop("imv", UNSET)

        pts = d.pop("pts", UNSET)

        tls = d.pop("tls", UNSET)

        esp = d.pop("esp", UNSET)

        lib = d.pop("lib", UNSET)

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
