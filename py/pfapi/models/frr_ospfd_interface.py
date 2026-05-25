from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrOspfdInterface")


@_attrs_define
class FrrOspfdInterface:
    """
    Attributes:
        interface (str | Unset): (Interface Options) Interface

            Enter the desired participating interface here.
        descr (str | Unset): (Interface Options) Description
        networktype (str | Unset): (Interface Options) Network Type (, broadcast, non-broadcast, point-to-multipoint,
            point-to-point)

            Select OSPF Network Type of the interface.
        passive (bool | Unset): (Interface Options) Interface is Passive

            Prevent transmission and reception of OSPF packets on this interface. The specified interface will be announced
            as a stub network.
        mtuignore (bool | Unset): (Interface Options) Ignore MTU

            Ignore MTU values for OSPF peers on this interface. Allows OSPF to form full adjacencies even when there is an
            MTU mismatch.
        metric (str | Unset): (OSPF Interface Handling) Metric

            Metric (Cost) for this OSPF interface (leave blank for default).
        interfacearea (str | Unset): (OSPF Interface Handling) Area

            The area for this interface (leave blank for default).
        acceptfilter (bool | Unset): (OSPF Interface Handling) Accept Filter

            Prevent routes for this interface subnet or IP address from being distributed by OSPF (Suggested for Multi-WAN
            environments).
        authtype (str | Unset): (Authentication) Authentication Type (, digest, simple, null)

            The type of OSPF authentication to use on this interface.
            This type must match all neighbors reachable through this interface.

            Using Message Digest is the best practice as Simple Password authentication is weak.
        password (str | Unset): (Authentication) Password

            Password to use with Simple Password or Message Digest authentication.
            This value must match all neighbors reachable through this interface.

            Simple passwords may be up to 8 characters, Message Digest passwords (keys) may be up to 16 characters.
        routerpriorityelections (str | Unset): (Advanced) Router Priority

            Router priority when participating in elections for DR (0-255, Default 1)
            0 will cause the router to not participate in election.
        retransmitinterval (str | Unset): (Advanced) Retransmit Interval

            Retransmit Interval this OSPF interface in seconds (3-65535, Default 5).
        hellointervalinseconds (str | Unset): (Advanced) Hello Interval

            Hello Interval this OSPF interface in seconds (1-65535, Default 10).
        deadtimer (str | Unset): (Advanced) Dead Interval

            Dead Interval for this OSPF interface in seconds (1-65535, Default 40).
        minimalhello (str | Unset): (Advanced) Minimal Hello

            Minimal Hello multiplier for this OSPF interface in seconds (1-10, Default disabled).
            Overrides the Hello Interval and Dead Interval and instead sends this number of Hello messages per second.
        bfdenable (bool | Unset): (BFD) BFD Enable

            Listen for BFD events on peers created on the interface.
            When OSPF finds a new neighbor, it creates a BFD peer to monitor the link status for fast convergence.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    interface: str | Unset = UNSET
    descr: str | Unset = UNSET
    networktype: str | Unset = UNSET
    passive: bool | Unset = UNSET
    mtuignore: bool | Unset = UNSET
    metric: str | Unset = UNSET
    interfacearea: str | Unset = UNSET
    acceptfilter: bool | Unset = UNSET
    authtype: str | Unset = UNSET
    password: str | Unset = UNSET
    routerpriorityelections: str | Unset = UNSET
    retransmitinterval: str | Unset = UNSET
    hellointervalinseconds: str | Unset = UNSET
    deadtimer: str | Unset = UNSET
    minimalhello: str | Unset = UNSET
    bfdenable: bool | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        descr = self.descr

        networktype = self.networktype

        passive = self.passive

        mtuignore = self.mtuignore

        metric = self.metric

        interfacearea = self.interfacearea

        acceptfilter = self.acceptfilter

        authtype = self.authtype

        password = self.password

        routerpriorityelections = self.routerpriorityelections

        retransmitinterval = self.retransmitinterval

        hellointervalinseconds = self.hellointervalinseconds

        deadtimer = self.deadtimer

        minimalhello = self.minimalhello

        bfdenable = self.bfdenable

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface is not UNSET:
            field_dict["interface"] = interface
        if descr is not UNSET:
            field_dict["descr"] = descr
        if networktype is not UNSET:
            field_dict["networktype"] = networktype
        if passive is not UNSET:
            field_dict["passive"] = passive
        if mtuignore is not UNSET:
            field_dict["mtuignore"] = mtuignore
        if metric is not UNSET:
            field_dict["metric"] = metric
        if interfacearea is not UNSET:
            field_dict["interfacearea"] = interfacearea
        if acceptfilter is not UNSET:
            field_dict["acceptfilter"] = acceptfilter
        if authtype is not UNSET:
            field_dict["authtype"] = authtype
        if password is not UNSET:
            field_dict["password"] = password
        if routerpriorityelections is not UNSET:
            field_dict["routerpriorityelections"] = routerpriorityelections
        if retransmitinterval is not UNSET:
            field_dict["retransmitinterval"] = retransmitinterval
        if hellointervalinseconds is not UNSET:
            field_dict["hellointervalinseconds"] = hellointervalinseconds
        if deadtimer is not UNSET:
            field_dict["deadtimer"] = deadtimer
        if minimalhello is not UNSET:
            field_dict["minimalhello"] = minimalhello
        if bfdenable is not UNSET:
            field_dict["bfdenable"] = bfdenable
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interface = d.pop("interface", UNSET)

        descr = d.pop("descr", UNSET)

        networktype = d.pop("networktype", UNSET)

        passive = d.pop("passive", UNSET)

        mtuignore = d.pop("mtuignore", UNSET)

        metric = d.pop("metric", UNSET)

        interfacearea = d.pop("interfacearea", UNSET)

        acceptfilter = d.pop("acceptfilter", UNSET)

        authtype = d.pop("authtype", UNSET)

        password = d.pop("password", UNSET)

        routerpriorityelections = d.pop("routerpriorityelections", UNSET)

        retransmitinterval = d.pop("retransmitinterval", UNSET)

        hellointervalinseconds = d.pop("hellointervalinseconds", UNSET)

        deadtimer = d.pop("deadtimer", UNSET)

        minimalhello = d.pop("minimalhello", UNSET)

        bfdenable = d.pop("bfdenable", UNSET)

        id = d.pop("id", UNSET)

        frr_ospfd_interface = cls(
            interface=interface,
            descr=descr,
            networktype=networktype,
            passive=passive,
            mtuignore=mtuignore,
            metric=metric,
            interfacearea=interfacearea,
            acceptfilter=acceptfilter,
            authtype=authtype,
            password=password,
            routerpriorityelections=routerpriorityelections,
            retransmitinterval=retransmitinterval,
            hellointervalinseconds=hellointervalinseconds,
            deadtimer=deadtimer,
            minimalhello=minimalhello,
            bfdenable=bfdenable,
            id=id,
        )

        frr_ospfd_interface.additional_properties = d
        return frr_ospfd_interface

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
