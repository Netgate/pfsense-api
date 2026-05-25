from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrOspf6DInterface")


@_attrs_define
class FrrOspf6DInterface:
    """
    Attributes:
        interface (str | Unset): (Interface Options) Interface

            Enter the desired participating interface here.

            If this interface has a gateway, rules on this interface will have "reply-to"
            by default. This will interfere with the operation of OSPFv3 on the interface. Add
            a rule at the top of the ruleset for this interface to pass IPv6 OSPF traffic with
            Disable reply-to checked in `Advanced Options`.
        descr (str | Unset): (Interface Options) Description
        networktype (str | Unset): (Interface Options) Network Type (, broadcast, point-to-point)

            Select OSPF6 Network Type of the interface.
        passive (bool | Unset): (Interface Options) Interface is Passive

            Prevent transmission and reception of OSPF6 packets on this interface. The specified interface will be announced
            as a stub network.
        mtuignore (bool | Unset): (Interface Options) Ignore MTU

            Ignore MTU values for OSPF6 peers on this interface. Allows OSPF6 to form full adjacencies even when there is an
            MTU mismatch.
        interfacearea (str | Unset): (OSPF6 Interface Handling) Area

            The area for this interface (leave blank for default).
        instanceid (str | Unset): (OSPF6 Interface Handling) Instance ID

            Instance ID for this OSPF6 interface (leave blank for default).
        metric (str | Unset): (OSPF6 Interface Handling) Metric

            Metric (cost) for this OSPF6 interface (leave blank for default).
        routerpriorityelections (str | Unset): (Advanced) Router Priority

            Router priority when participating in elections for DR (Default 1)
            Valid range is 0-255. 0 will cause the router to not participate in election.
        hellointervalinseconds (str | Unset): (Advanced) Hello Interval

            Hello Interval this OSPF6 interface in seconds (Default 10).
        deadtimer (str | Unset): (Advanced) Dead Timer

            Dead Timer for this OSPF6 interface in seconds (Default 40).
        retransmitinterval (str | Unset): (Advanced) Retransmit Interval

            Retransmit Interval this OSPF6 interface in seconds (Default 5).
        bfdenable (bool | Unset): (BFD) BFD Enable

            Listen for BFD events on peers created on the interface.
            When OSPF6 finds a new neighbor, it creates a BFD peer to monitor the link status for fast convergence.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    interface: str | Unset = UNSET
    descr: str | Unset = UNSET
    networktype: str | Unset = UNSET
    passive: bool | Unset = UNSET
    mtuignore: bool | Unset = UNSET
    interfacearea: str | Unset = UNSET
    instanceid: str | Unset = UNSET
    metric: str | Unset = UNSET
    routerpriorityelections: str | Unset = UNSET
    hellointervalinseconds: str | Unset = UNSET
    deadtimer: str | Unset = UNSET
    retransmitinterval: str | Unset = UNSET
    bfdenable: bool | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        descr = self.descr

        networktype = self.networktype

        passive = self.passive

        mtuignore = self.mtuignore

        interfacearea = self.interfacearea

        instanceid = self.instanceid

        metric = self.metric

        routerpriorityelections = self.routerpriorityelections

        hellointervalinseconds = self.hellointervalinseconds

        deadtimer = self.deadtimer

        retransmitinterval = self.retransmitinterval

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
        if interfacearea is not UNSET:
            field_dict["interfacearea"] = interfacearea
        if instanceid is not UNSET:
            field_dict["instanceid"] = instanceid
        if metric is not UNSET:
            field_dict["metric"] = metric
        if routerpriorityelections is not UNSET:
            field_dict["routerpriorityelections"] = routerpriorityelections
        if hellointervalinseconds is not UNSET:
            field_dict["hellointervalinseconds"] = hellointervalinseconds
        if deadtimer is not UNSET:
            field_dict["deadtimer"] = deadtimer
        if retransmitinterval is not UNSET:
            field_dict["retransmitinterval"] = retransmitinterval
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

        interfacearea = d.pop("interfacearea", UNSET)

        instanceid = d.pop("instanceid", UNSET)

        metric = d.pop("metric", UNSET)

        routerpriorityelections = d.pop("routerpriorityelections", UNSET)

        hellointervalinseconds = d.pop("hellointervalinseconds", UNSET)

        deadtimer = d.pop("deadtimer", UNSET)

        retransmitinterval = d.pop("retransmitinterval", UNSET)

        bfdenable = d.pop("bfdenable", UNSET)

        id = d.pop("id", UNSET)

        frr_ospf_6d_interface = cls(
            interface=interface,
            descr=descr,
            networktype=networktype,
            passive=passive,
            mtuignore=mtuignore,
            interfacearea=interfacearea,
            instanceid=instanceid,
            metric=metric,
            routerpriorityelections=routerpriorityelections,
            hellointervalinseconds=hellointervalinseconds,
            deadtimer=deadtimer,
            retransmitinterval=retransmitinterval,
            bfdenable=bfdenable,
            id=id,
        )

        frr_ospf_6d_interface.additional_properties = d
        return frr_ospf_6d_interface

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
