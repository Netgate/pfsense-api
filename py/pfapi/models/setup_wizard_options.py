from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.setup_pp_po_e_cfg import SetupPPPoECfg


T = TypeVar("T", bound="SetupWizardOptions")


@_attrs_define
class SetupWizardOptions:
    """
    Attributes:
        hostname (str):
        domain (str):
        pridns (str):
        secdns (str):
        dnsoverride (bool):
        tz (str):
        timeservers (str):
        wantype (str):
        wanip (str):
        gw (str):
        spoofmac (str):
        mtu (str):
        mss (str):
        dhcphost (str):
        lanip (str):
        bogons (bool):
        rfc1918 (bool):
        pppoe (SetupPPPoECfg):
    """

    hostname: str
    domain: str
    pridns: str
    secdns: str
    dnsoverride: bool
    tz: str
    timeservers: str
    wantype: str
    wanip: str
    gw: str
    spoofmac: str
    mtu: str
    mss: str
    dhcphost: str
    lanip: str
    bogons: bool
    rfc1918: bool
    pppoe: "SetupPPPoECfg"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostname = self.hostname

        domain = self.domain

        pridns = self.pridns

        secdns = self.secdns

        dnsoverride = self.dnsoverride

        tz = self.tz

        timeservers = self.timeservers

        wantype = self.wantype

        wanip = self.wanip

        gw = self.gw

        spoofmac = self.spoofmac

        mtu = self.mtu

        mss = self.mss

        dhcphost = self.dhcphost

        lanip = self.lanip

        bogons = self.bogons

        rfc1918 = self.rfc1918

        pppoe = self.pppoe.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
                "domain": domain,
                "pridns": pridns,
                "secdns": secdns,
                "dnsoverride": dnsoverride,
                "tz": tz,
                "timeservers": timeservers,
                "wantype": wantype,
                "wanip": wanip,
                "gw": gw,
                "spoofmac": spoofmac,
                "mtu": mtu,
                "mss": mss,
                "dhcphost": dhcphost,
                "lanip": lanip,
                "bogons": bogons,
                "rfc1918": rfc1918,
                "pppoe": pppoe,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.setup_pp_po_e_cfg import SetupPPPoECfg

        d = src_dict.copy()
        hostname = d.pop("hostname")

        domain = d.pop("domain")

        pridns = d.pop("pridns")

        secdns = d.pop("secdns")

        dnsoverride = d.pop("dnsoverride")

        tz = d.pop("tz")

        timeservers = d.pop("timeservers")

        wantype = d.pop("wantype")

        wanip = d.pop("wanip")

        gw = d.pop("gw")

        spoofmac = d.pop("spoofmac")

        mtu = d.pop("mtu")

        mss = d.pop("mss")

        dhcphost = d.pop("dhcphost")

        lanip = d.pop("lanip")

        bogons = d.pop("bogons")

        rfc1918 = d.pop("rfc1918")

        pppoe = SetupPPPoECfg.from_dict(d.pop("pppoe"))

        setup_wizard_options = cls(
            hostname=hostname,
            domain=domain,
            pridns=pridns,
            secdns=secdns,
            dnsoverride=dnsoverride,
            tz=tz,
            timeservers=timeservers,
            wantype=wantype,
            wanip=wanip,
            gw=gw,
            spoofmac=spoofmac,
            mtu=mtu,
            mss=mss,
            dhcphost=dhcphost,
            lanip=lanip,
            bogons=bogons,
            rfc1918=rfc1918,
            pppoe=pppoe,
        )

        setup_wizard_options.additional_properties = d
        return setup_wizard_options

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
