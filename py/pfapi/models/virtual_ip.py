from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualIP")


@_attrs_define
class VirtualIP:
    """
    Attributes:
        mode (str | Unset):
        interface (str | Unset):
        vhid (int | Unset):
        advskew (int | Unset):
        advbase (int | Unset):
        password (str | Unset):
        password_confirm (str | Unset):
        uniqid (str | Unset):
        descr (str | Unset):
        subnet (str | Unset):
        id (str | Unset):
        carp_mode (str | Unset):
        carp_peer (str | Unset):
    """

    mode: str | Unset = UNSET
    interface: str | Unset = UNSET
    vhid: int | Unset = UNSET
    advskew: int | Unset = UNSET
    advbase: int | Unset = UNSET
    password: str | Unset = UNSET
    password_confirm: str | Unset = UNSET
    uniqid: str | Unset = UNSET
    descr: str | Unset = UNSET
    subnet: str | Unset = UNSET
    id: str | Unset = UNSET
    carp_mode: str | Unset = UNSET
    carp_peer: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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
