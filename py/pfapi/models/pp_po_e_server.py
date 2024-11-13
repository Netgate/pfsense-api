from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.radius import Radius


T = TypeVar("T", bound="PPPoEServer")


@_attrs_define
class PPPoEServer:
    """
    Attributes:
        remoteip (Union[Unset, str]):
        localip (Union[Unset, str]):
        mode (Union[Unset, str]):
        interface (Union[Unset, str]):
        n_pppoe_units (Union[Unset, str]):
        n_pppoe_maxlogin (Union[Unset, str]):
        pppoe_subnet (Union[Unset, str]):
        descr (Union[Unset, str]):
        radius (Union[Unset, Radius]):
        dns1 (Union[Unset, str]):
        dns2 (Union[Unset, str]):
        pppoeid (Union[Unset, str]):
        username (Union[Unset, str]):
    """

    remoteip: Union[Unset, str] = UNSET
    localip: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    n_pppoe_units: Union[Unset, str] = UNSET
    n_pppoe_maxlogin: Union[Unset, str] = UNSET
    pppoe_subnet: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    radius: Union[Unset, "Radius"] = UNSET
    dns1: Union[Unset, str] = UNSET
    dns2: Union[Unset, str] = UNSET
    pppoeid: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
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

        radius: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.radius, Unset):
            radius = self.radius.to_dict()

        dns1 = self.dns1

        dns2 = self.dns2

        pppoeid = self.pppoeid

        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if remoteip is not UNSET:
            field_dict["remoteip"] = remoteip
        if localip is not UNSET:
            field_dict["localip"] = localip
        if mode is not UNSET:
            field_dict["mode"] = mode
        if interface is not UNSET:
            field_dict["interface"] = interface
        if n_pppoe_units is not UNSET:
            field_dict["n_pppoe_units"] = n_pppoe_units
        if n_pppoe_maxlogin is not UNSET:
            field_dict["n_pppoe_maxlogin"] = n_pppoe_maxlogin
        if pppoe_subnet is not UNSET:
            field_dict["pppoe_subnet"] = pppoe_subnet
        if descr is not UNSET:
            field_dict["descr"] = descr
        if radius is not UNSET:
            field_dict["radius"] = radius
        if dns1 is not UNSET:
            field_dict["dns1"] = dns1
        if dns2 is not UNSET:
            field_dict["dns2"] = dns2
        if pppoeid is not UNSET:
            field_dict["pppoeid"] = pppoeid
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.radius import Radius

        d = src_dict.copy()
        remoteip = d.pop("remoteip", UNSET)

        localip = d.pop("localip", UNSET)

        mode = d.pop("mode", UNSET)

        interface = d.pop("interface", UNSET)

        n_pppoe_units = d.pop("n_pppoe_units", UNSET)

        n_pppoe_maxlogin = d.pop("n_pppoe_maxlogin", UNSET)

        pppoe_subnet = d.pop("pppoe_subnet", UNSET)

        descr = d.pop("descr", UNSET)

        _radius = d.pop("radius", UNSET)
        radius: Union[Unset, Radius]
        if isinstance(_radius, Unset):
            radius = UNSET
        else:
            radius = Radius.from_dict(_radius)

        dns1 = d.pop("dns1", UNSET)

        dns2 = d.pop("dns2", UNSET)

        pppoeid = d.pop("pppoeid", UNSET)

        username = d.pop("username", UNSET)

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
