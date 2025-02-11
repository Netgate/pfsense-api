from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VirtualIP")


@_attrs_define
class VirtualIP:
    """
    Attributes:
        mode (str):
        interface (str):
        vhid (int):
        advskew (int):
        advbase (int):
        password (str):
        password_confirm (str):
        uniqid (str):
        descr (str):
        subnet (str):
        id (str):
        carp_mode (str):
    """

    mode: str
    interface: str
    vhid: int
    advskew: int
    advbase: int
    password: str
    password_confirm: str
    uniqid: str
    descr: str
    subnet: str
    id: str
    carp_mode: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mode = self.mode

        interface = self.interface

        vhid = self.vhid

        advskew = self.advskew

        advbase = self.advbase

        password = self.password

        password_confirm = self.password_confirm

        uniqid = self.uniqid

        descr = self.descr

        subnet = self.subnet

        id = self.id

        carp_mode = self.carp_mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "interface": interface,
                "vhid": vhid,
                "advskew": advskew,
                "advbase": advbase,
                "password": password,
                "password_confirm": password_confirm,
                "uniqid": uniqid,
                "descr": descr,
                "subnet": subnet,
                "id": id,
                "carp_mode": carp_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mode = d.pop("mode")

        interface = d.pop("interface")

        vhid = d.pop("vhid")

        advskew = d.pop("advskew")

        advbase = d.pop("advbase")

        password = d.pop("password")

        password_confirm = d.pop("password_confirm")

        uniqid = d.pop("uniqid")

        descr = d.pop("descr")

        subnet = d.pop("subnet")

        id = d.pop("id")

        carp_mode = d.pop("carp_mode")

        virtual_ip = cls(
            mode=mode,
            interface=interface,
            vhid=vhid,
            advskew=advskew,
            advbase=advbase,
            password=password,
            password_confirm=password_confirm,
            uniqid=uniqid,
            descr=descr,
            subnet=subnet,
            id=id,
            carp_mode=carp_mode,
        )

        virtual_ip.additional_properties = d
        return virtual_ip

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
