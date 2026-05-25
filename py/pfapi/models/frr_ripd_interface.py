from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrRipdInterface")


@_attrs_define
class FrrRipdInterface:
    """
    Attributes:
        interface (str | Unset): (Interface Options) Interface

            Enter the desired participating interface here.
        descr (str | Unset): (Interface Options) Description
        passive (bool | Unset): (Interface Options) Interface is Passive

            Prevent transmission of RIP packets on this interface.
        authtype (str | Unset): (Authentication) Authentication Type (, digest, simple)

            The type of RIP authentication to use on this interface.
            This type must match all neighbors reachable through this interface.

            Using Message Digest is the best practice as Simple Password authentication is weak.
        password (str | Unset): (Authentication) Password

            Password to use with Simple Password or Message Digest authentication.
            This value must match all neighbors reachable through this interface.

            Passwords may be up to 16 characters.
        splithorizon (str | Unset): (Advanced) Split Horizon (none, splithorizon, reversepoison)

            Perform Split Horizon.
        sendbroadcast (bool | Unset): (Advanced) Send Broadcast

            Send Broadcast updates instead of multicast for RIPv2.
        sendversion (str | Unset): (Advanced) Send Version (2, 1, 1 2, none)

            Advertisement transmission version.
        receiveversion (str | Unset): (Advanced) Receive Version (2, 1, 1 2, none)

            Advertisement reception version.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    interface: str | Unset = UNSET
    descr: str | Unset = UNSET
    passive: bool | Unset = UNSET
    authtype: str | Unset = UNSET
    password: str | Unset = UNSET
    splithorizon: str | Unset = UNSET
    sendbroadcast: bool | Unset = UNSET
    sendversion: str | Unset = UNSET
    receiveversion: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        descr = self.descr

        passive = self.passive

        authtype = self.authtype

        password = self.password

        splithorizon = self.splithorizon

        sendbroadcast = self.sendbroadcast

        sendversion = self.sendversion

        receiveversion = self.receiveversion

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface is not UNSET:
            field_dict["interface"] = interface
        if descr is not UNSET:
            field_dict["descr"] = descr
        if passive is not UNSET:
            field_dict["passive"] = passive
        if authtype is not UNSET:
            field_dict["authtype"] = authtype
        if password is not UNSET:
            field_dict["password"] = password
        if splithorizon is not UNSET:
            field_dict["splithorizon"] = splithorizon
        if sendbroadcast is not UNSET:
            field_dict["sendbroadcast"] = sendbroadcast
        if sendversion is not UNSET:
            field_dict["sendversion"] = sendversion
        if receiveversion is not UNSET:
            field_dict["receiveversion"] = receiveversion
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interface = d.pop("interface", UNSET)

        descr = d.pop("descr", UNSET)

        passive = d.pop("passive", UNSET)

        authtype = d.pop("authtype", UNSET)

        password = d.pop("password", UNSET)

        splithorizon = d.pop("splithorizon", UNSET)

        sendbroadcast = d.pop("sendbroadcast", UNSET)

        sendversion = d.pop("sendversion", UNSET)

        receiveversion = d.pop("receiveversion", UNSET)

        id = d.pop("id", UNSET)

        frr_ripd_interface = cls(
            interface=interface,
            descr=descr,
            passive=passive,
            authtype=authtype,
            password=password,
            splithorizon=splithorizon,
            sendbroadcast=sendbroadcast,
            sendversion=sendversion,
            receiveversion=receiveversion,
            id=id,
        )

        frr_ripd_interface.additional_properties = d
        return frr_ripd_interface

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
