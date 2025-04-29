from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualIP")


@_attrs_define
class VirtualIP:
    """
    Attributes:
        mode (Union[Unset, str]):
        interface (Union[Unset, str]):
        vhid (Union[Unset, int]):
        advskew (Union[Unset, int]):
        advbase (Union[Unset, int]):
        password (Union[Unset, str]):
        password_confirm (Union[Unset, str]):
        uniqid (Union[Unset, str]):
        descr (Union[Unset, str]):
        subnet (Union[Unset, str]):
        id (Union[Unset, str]):
        carp_mode (Union[Unset, str]):
        carp_peer (Union[Unset, str]):
    """

    mode: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    vhid: Union[Unset, int] = UNSET
    advskew: Union[Unset, int] = UNSET
    advbase: Union[Unset, int] = UNSET
    password: Union[Unset, str] = UNSET
    password_confirm: Union[Unset, str] = UNSET
    uniqid: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    subnet: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    carp_mode: Union[Unset, str] = UNSET
    carp_peer: Union[Unset, str] = UNSET
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

        carp_peer = self.carp_peer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if interface is not UNSET:
            field_dict["interface"] = interface
        if vhid is not UNSET:
            field_dict["vhid"] = vhid
        if advskew is not UNSET:
            field_dict["advskew"] = advskew
        if advbase is not UNSET:
            field_dict["advbase"] = advbase
        if password is not UNSET:
            field_dict["password"] = password
        if password_confirm is not UNSET:
            field_dict["password_confirm"] = password_confirm
        if uniqid is not UNSET:
            field_dict["uniqid"] = uniqid
        if descr is not UNSET:
            field_dict["descr"] = descr
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if id is not UNSET:
            field_dict["id"] = id
        if carp_mode is not UNSET:
            field_dict["carp_mode"] = carp_mode
        if carp_peer is not UNSET:
            field_dict["carp_peer"] = carp_peer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mode = d.pop("mode", UNSET)

        interface = d.pop("interface", UNSET)

        vhid = d.pop("vhid", UNSET)

        advskew = d.pop("advskew", UNSET)

        advbase = d.pop("advbase", UNSET)

        password = d.pop("password", UNSET)

        password_confirm = d.pop("password_confirm", UNSET)

        uniqid = d.pop("uniqid", UNSET)

        descr = d.pop("descr", UNSET)

        subnet = d.pop("subnet", UNSET)

        id = d.pop("id", UNSET)

        carp_mode = d.pop("carp_mode", UNSET)

        carp_peer = d.pop("carp_peer", UNSET)

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
            carp_peer=carp_peer,
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
