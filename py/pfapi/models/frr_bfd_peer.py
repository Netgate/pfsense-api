from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrBfdPeer")


@_attrs_define
class FrrBfdPeer:
    """
    Attributes:
        peer (str | Unset): (Peer Configurations) Peer Address

            IP address of a peer
        descr (str | Unset): (Peer Configurations) Description
        profile (str | Unset): (Peer Configurations) Profile

            Select the profile for peer take configuration from.
        multihop (bool | Unset): (Options) Multihop

            Expect packets with TTL less than 254 due to more than one hop between peer addresses and listen on the multihop
            port 4784.
            When using multi-hop mode echo-mode will not work, see RFC 5883 section 3.
        shutdown (bool | Unset): (Options) Shutdown

            Enables or disables the peer.
            When the peer is disabled an "administrative down" message is sent to the remote peer.
        interface (str | Unset): (Source Address/Interface) Interface

            Select the interface which BFD will use as a packet source.
        local_address (str | Unset): (Source Address/Interface) Local Source Address

            Provide a local address to bind the BFD peer listener to for participating in a BFD session.
        detectmultiplier (str | Unset): (Advanced Options) Detect Multiplier

            Configures the detection multiplier to determine packet loss.

            The remote transmission interval will be multiplied by this value to determine the connection loss detection
            timer.

            The default value is 3.
        receiveinterval (str | Unset): (Advanced Options) Receive Interval

            Configures the minimum interval at which this system is capable of receiving control packets.

            The default value is 300 milliseconds.
        transmitinterval (str | Unset): (Advanced Options) Transmit Interval

            The minimum transmission interval for the system to use to send BFD control packets.
        echointerval (str | Unset): (Advanced Options) Echo Interval

            The minimal echo receive interval that the system is capable of handling.
        echomode (bool | Unset): (Advanced Options) Echo Mode

            Enables or disables the echo transmission mode. This mode is disabled by default.
            FRR documentation recommendeds that the transmission interval of control packets to be increased after enabling
            echo-mode to reduce bandwidth usage. For example: transmission-interval 2000.
            Echo mode is not supported on multi-hop setups, see RFC 5883 section 3.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    peer: str | Unset = UNSET
    descr: str | Unset = UNSET
    profile: str | Unset = UNSET
    multihop: bool | Unset = UNSET
    shutdown: bool | Unset = UNSET
    interface: str | Unset = UNSET
    local_address: str | Unset = UNSET
    detectmultiplier: str | Unset = UNSET
    receiveinterval: str | Unset = UNSET
    transmitinterval: str | Unset = UNSET
    echointerval: str | Unset = UNSET
    echomode: bool | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        peer = self.peer

        descr = self.descr

        profile = self.profile

        multihop = self.multihop

        shutdown = self.shutdown

        interface = self.interface

        local_address = self.local_address

        detectmultiplier = self.detectmultiplier

        receiveinterval = self.receiveinterval

        transmitinterval = self.transmitinterval

        echointerval = self.echointerval

        echomode = self.echomode

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if peer is not UNSET:
            field_dict["peer"] = peer
        if descr is not UNSET:
            field_dict["descr"] = descr
        if profile is not UNSET:
            field_dict["profile"] = profile
        if multihop is not UNSET:
            field_dict["multihop"] = multihop
        if shutdown is not UNSET:
            field_dict["shutdown"] = shutdown
        if interface is not UNSET:
            field_dict["interface"] = interface
        if local_address is not UNSET:
            field_dict["local_address"] = local_address
        if detectmultiplier is not UNSET:
            field_dict["detectmultiplier"] = detectmultiplier
        if receiveinterval is not UNSET:
            field_dict["receiveinterval"] = receiveinterval
        if transmitinterval is not UNSET:
            field_dict["transmitinterval"] = transmitinterval
        if echointerval is not UNSET:
            field_dict["echointerval"] = echointerval
        if echomode is not UNSET:
            field_dict["echomode"] = echomode
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        peer = d.pop("peer", UNSET)

        descr = d.pop("descr", UNSET)

        profile = d.pop("profile", UNSET)

        multihop = d.pop("multihop", UNSET)

        shutdown = d.pop("shutdown", UNSET)

        interface = d.pop("interface", UNSET)

        local_address = d.pop("local_address", UNSET)

        detectmultiplier = d.pop("detectmultiplier", UNSET)

        receiveinterval = d.pop("receiveinterval", UNSET)

        transmitinterval = d.pop("transmitinterval", UNSET)

        echointerval = d.pop("echointerval", UNSET)

        echomode = d.pop("echomode", UNSET)

        id = d.pop("id", UNSET)

        frr_bfd_peer = cls(
            peer=peer,
            descr=descr,
            profile=profile,
            multihop=multihop,
            shutdown=shutdown,
            interface=interface,
            local_address=local_address,
            detectmultiplier=detectmultiplier,
            receiveinterval=receiveinterval,
            transmitinterval=transmitinterval,
            echointerval=echointerval,
            echomode=echomode,
            id=id,
        )

        frr_bfd_peer.additional_properties = d
        return frr_bfd_peer

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
