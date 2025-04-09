from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.setup_pp_po_e_cfg import SetupPPPoECfg


T = TypeVar("T", bound="SetupWizardOptions")


@_attrs_define
class SetupWizardOptions:
    """
    Attributes:
        hostname (str):
        domain (Union[Unset, str]):
        pridns (Union[Unset, str]):
        secdns (Union[Unset, str]):
        dnsoverride (Union[Unset, bool]):
        tz (Union[Unset, str]):
        timeservers (Union[Unset, str]):
        wantype (Union[Unset, str]):
        wanip (Union[Unset, str]):
        gw (Union[Unset, str]):
        spoofmac (Union[Unset, str]):
        mtu (Union[Unset, str]):
        mss (Union[Unset, str]):
        dhcphost (Union[Unset, str]):
        lanip (Union[Unset, str]):
        bogons (Union[Unset, bool]):
        rfc1918 (Union[Unset, bool]):
        pppoe (Union[Unset, SetupPPPoECfg]):
    """

    hostname: str
    domain: Union[Unset, str] = UNSET
    pridns: Union[Unset, str] = UNSET
    secdns: Union[Unset, str] = UNSET
    dnsoverride: Union[Unset, bool] = UNSET
    tz: Union[Unset, str] = UNSET
    timeservers: Union[Unset, str] = UNSET
    wantype: Union[Unset, str] = UNSET
    wanip: Union[Unset, str] = UNSET
    gw: Union[Unset, str] = UNSET
    spoofmac: Union[Unset, str] = UNSET
    mtu: Union[Unset, str] = UNSET
    mss: Union[Unset, str] = UNSET
    dhcphost: Union[Unset, str] = UNSET
    lanip: Union[Unset, str] = UNSET
    bogons: Union[Unset, bool] = UNSET
    rfc1918: Union[Unset, bool] = UNSET
    pppoe: Union[Unset, "SetupPPPoECfg"] = UNSET
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

        pppoe: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pppoe, Unset):
            pppoe = self.pppoe.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if pridns is not UNSET:
            field_dict["pridns"] = pridns
        if secdns is not UNSET:
            field_dict["secdns"] = secdns
        if dnsoverride is not UNSET:
            field_dict["dnsoverride"] = dnsoverride
        if tz is not UNSET:
            field_dict["tz"] = tz
        if timeservers is not UNSET:
            field_dict["timeservers"] = timeservers
        if wantype is not UNSET:
            field_dict["wantype"] = wantype
        if wanip is not UNSET:
            field_dict["wanip"] = wanip
        if gw is not UNSET:
            field_dict["gw"] = gw
        if spoofmac is not UNSET:
            field_dict["spoofmac"] = spoofmac
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if mss is not UNSET:
            field_dict["mss"] = mss
        if dhcphost is not UNSET:
            field_dict["dhcphost"] = dhcphost
        if lanip is not UNSET:
            field_dict["lanip"] = lanip
        if bogons is not UNSET:
            field_dict["bogons"] = bogons
        if rfc1918 is not UNSET:
            field_dict["rfc1918"] = rfc1918
        if pppoe is not UNSET:
            field_dict["pppoe"] = pppoe

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.setup_pp_po_e_cfg import SetupPPPoECfg

        d = src_dict.copy()
        hostname = d.pop("hostname")

        domain = d.pop("domain", UNSET)

        pridns = d.pop("pridns", UNSET)

        secdns = d.pop("secdns", UNSET)

        dnsoverride = d.pop("dnsoverride", UNSET)

        tz = d.pop("tz", UNSET)

        timeservers = d.pop("timeservers", UNSET)

        wantype = d.pop("wantype", UNSET)

        wanip = d.pop("wanip", UNSET)

        gw = d.pop("gw", UNSET)

        spoofmac = d.pop("spoofmac", UNSET)

        mtu = d.pop("mtu", UNSET)

        mss = d.pop("mss", UNSET)

        dhcphost = d.pop("dhcphost", UNSET)

        lanip = d.pop("lanip", UNSET)

        bogons = d.pop("bogons", UNSET)

        rfc1918 = d.pop("rfc1918", UNSET)

        _pppoe = d.pop("pppoe", UNSET)
        pppoe: Union[Unset, SetupPPPoECfg]
        if isinstance(_pppoe, Unset):
            pppoe = UNSET
        else:
            pppoe = SetupPPPoECfg.from_dict(_pppoe)

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
