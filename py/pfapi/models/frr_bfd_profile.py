from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrBfdProfile")


@_attrs_define
class FrrBfdProfile:
    """
    Attributes:
        name (str | Unset): (Profile Configuration) Name
        descr (str | Unset): (Profile Configuration) Description
        shutdown (bool | Unset): (Profile Configuration) Shutdown

            Enables or disables the peer.
            When the peer is disabled an "administrative down" message is sent to the remote peer.
        passive (bool | Unset): (Profile Configuration) Passive

            Mark session as passive.
            A passive session will not attempt to start the connection and will wait for control packets from peer before it
            begins replying.
        detectmultiplier (str | Unset): (Profile Options) Detect Multiplier

            Configures the detection multiplier to determine packet loss.

            The remote transmission interval will be multiplied by this value to determine the connection loss detection
            timer.

            The default value is 3.
        receiveinterval (str | Unset): (Profile Options) Receive Interval

            Configures the minimum interval at which this system is capable of receiving control packets.

            The default value is 300 milliseconds.
        transmitinterval (str | Unset): (Profile Options) Transmit Interval

            The minimum transmission interval for the system to use to send BFD control packets.
        echointerval (str | Unset): (Profile Options) Echo Interval

            The minimal echo receive interval that the system is capable of handling.
        minimumttl (str | Unset): (Profile Options) Minimum TTL

            For multi hop sessions only, configure the minimum expected TTL for an incoming BFD control packet.
            This feature serves the purpose of tightening the packet validation requirements to avoid receiving BFD control
            packets from other sessions.
            The default value is 254 (which means we only expect one hop between this system and the peer).
        echomode (bool | Unset): (Profile Options) Echo Mode

            Enables or disables the echo transmission mode. This mode is disabled by default.
            FRR documentation recommendeds that the transmission interval of control packets to be increased after enabling
            echo-mode to reduce bandwidth usage. For example: transmission-interval 2000.
            Echo mode is not supported on multi-hop setups, see RFC 5883 section 3.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    shutdown: bool | Unset = UNSET
    passive: bool | Unset = UNSET
    detectmultiplier: str | Unset = UNSET
    receiveinterval: str | Unset = UNSET
    transmitinterval: str | Unset = UNSET
    echointerval: str | Unset = UNSET
    minimumttl: str | Unset = UNSET
    echomode: bool | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descr = self.descr

        shutdown = self.shutdown

        passive = self.passive

        detectmultiplier = self.detectmultiplier

        receiveinterval = self.receiveinterval

        transmitinterval = self.transmitinterval

        echointerval = self.echointerval

        minimumttl = self.minimumttl

        echomode = self.echomode

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if shutdown is not UNSET:
            field_dict["shutdown"] = shutdown
        if passive is not UNSET:
            field_dict["passive"] = passive
        if detectmultiplier is not UNSET:
            field_dict["detectmultiplier"] = detectmultiplier
        if receiveinterval is not UNSET:
            field_dict["receiveinterval"] = receiveinterval
        if transmitinterval is not UNSET:
            field_dict["transmitinterval"] = transmitinterval
        if echointerval is not UNSET:
            field_dict["echointerval"] = echointerval
        if minimumttl is not UNSET:
            field_dict["minimumttl"] = minimumttl
        if echomode is not UNSET:
            field_dict["echomode"] = echomode
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        shutdown = d.pop("shutdown", UNSET)

        passive = d.pop("passive", UNSET)

        detectmultiplier = d.pop("detectmultiplier", UNSET)

        receiveinterval = d.pop("receiveinterval", UNSET)

        transmitinterval = d.pop("transmitinterval", UNSET)

        echointerval = d.pop("echointerval", UNSET)

        minimumttl = d.pop("minimumttl", UNSET)

        echomode = d.pop("echomode", UNSET)

        id = d.pop("id", UNSET)

        frr_bfd_profile = cls(
            name=name,
            descr=descr,
            shutdown=shutdown,
            passive=passive,
            detectmultiplier=detectmultiplier,
            receiveinterval=receiveinterval,
            transmitinterval=transmitinterval,
            echointerval=echointerval,
            minimumttl=minimumttl,
            echomode=echomode,
            id=id,
        )

        frr_bfd_profile.additional_properties = d
        return frr_bfd_profile

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
