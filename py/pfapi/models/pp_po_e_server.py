from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.radius import Radius


T = TypeVar("T", bound="PPPoEServer")


@_attrs_define
class PPPoEServer:
    """
    Attributes:
        remoteip (str):
        localip (str):
        mode (str):
        interface (str):
        n_pppoe_units (str):
        n_pppoe_maxlogin (str):
        pppoe_subnet (str):
        descr (str):
        radius (Radius):
        dns1 (str):
        dns2 (str):
        pppoeid (str):
        username (str):
    """

    remoteip: str
    localip: str
    mode: str
    interface: str
    n_pppoe_units: str
    n_pppoe_maxlogin: str
    pppoe_subnet: str
    descr: str
    radius: "Radius"
    dns1: str
    dns2: str
    pppoeid: str
    username: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        remoteip = self.remoteip

        localip = self.localip

        mode = self.mode

        interface = self.interface

        n_pppoe_units = self.n_pppoe_units

        n_pppoe_maxlogin = self.n_pppoe_maxlogin

        pppoe_subnet = self.pppoe_subnet

        descr = self.descr

        radius = self.radius.to_dict()

        dns1 = self.dns1

        dns2 = self.dns2

        pppoeid = self.pppoeid

        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "remoteip": remoteip,
                "localip": localip,
                "mode": mode,
                "interface": interface,
                "n_pppoe_units": n_pppoe_units,
                "n_pppoe_maxlogin": n_pppoe_maxlogin,
                "pppoe_subnet": pppoe_subnet,
                "descr": descr,
                "radius": radius,
                "dns1": dns1,
                "dns2": dns2,
                "pppoeid": pppoeid,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.radius import Radius

        d = src_dict.copy()
        remoteip = d.pop("remoteip")

        localip = d.pop("localip")

        mode = d.pop("mode")

        interface = d.pop("interface")

        n_pppoe_units = d.pop("n_pppoe_units")

        n_pppoe_maxlogin = d.pop("n_pppoe_maxlogin")

        pppoe_subnet = d.pop("pppoe_subnet")

        descr = d.pop("descr")

        radius = Radius.from_dict(d.pop("radius"))

        dns1 = d.pop("dns1")

        dns2 = d.pop("dns2")

        pppoeid = d.pop("pppoeid")

        username = d.pop("username")

        pp_po_e_server = cls(
            remoteip=remoteip,
            localip=localip,
            mode=mode,
            interface=interface,
            n_pppoe_units=n_pppoe_units,
            n_pppoe_maxlogin=n_pppoe_maxlogin,
            pppoe_subnet=pppoe_subnet,
            descr=descr,
            radius=radius,
            dns1=dns1,
            dns2=dns2,
            pppoeid=pppoeid,
            username=username,
        )

        pp_po_e_server.additional_properties = d
        return pp_po_e_server

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
