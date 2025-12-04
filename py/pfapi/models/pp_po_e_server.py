from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        remoteip (str):
        localip (str | Unset):
        mode (str | Unset):
        interface (str | Unset):
        n_pppoe_units (str | Unset):
        n_pppoe_maxlogin (str | Unset):
        pppoe_subnet (str | Unset):
        descr (str | Unset):
        radius (Radius | Unset):
        dns1 (str | Unset):
        dns2 (str | Unset):
        pppoeid (str | Unset):
        username (str | Unset):
    """

    remoteip: str
    localip: str | Unset = UNSET
    mode: str | Unset = UNSET
    interface: str | Unset = UNSET
    n_pppoe_units: str | Unset = UNSET
    n_pppoe_maxlogin: str | Unset = UNSET
    pppoe_subnet: str | Unset = UNSET
    descr: str | Unset = UNSET
    radius: Radius | Unset = UNSET
    dns1: str | Unset = UNSET
    dns2: str | Unset = UNSET
    pppoeid: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        remoteip = self.remoteip

        localip = self.localip

        mode = self.mode

        interface = self.interface

        n_pppoe_units = self.n_pppoe_units

        n_pppoe_maxlogin = self.n_pppoe_maxlogin

        pppoe_subnet = self.pppoe_subnet

        descr = self.descr

        radius: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radius, Unset):
            radius = self.radius.to_dict()

        dns1 = self.dns1

        dns2 = self.dns2

        pppoeid = self.pppoeid

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "remoteip": remoteip,
            }
        )
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.radius import Radius

        d = dict(src_dict)
        remoteip = d.pop("remoteip")

        localip = d.pop("localip", UNSET)

        mode = d.pop("mode", UNSET)

        interface = d.pop("interface", UNSET)

        n_pppoe_units = d.pop("n_pppoe_units", UNSET)

        n_pppoe_maxlogin = d.pop("n_pppoe_maxlogin", UNSET)

        pppoe_subnet = d.pop("pppoe_subnet", UNSET)

        descr = d.pop("descr", UNSET)

        _radius = d.pop("radius", UNSET)
        radius: Radius | Unset
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
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
