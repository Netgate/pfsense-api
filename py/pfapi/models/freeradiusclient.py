from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Freeradiusclient")


@_attrs_define
class Freeradiusclient:
    r"""
    Attributes:
        clientip (str | Unset): (General Configuration) Client IP Address

            Enter the IP address or network of the RADIUS client(s) in CIDR notation. This is the IP of the NAS (switch,
            access point, firewall, router, etc.).
        clientipversion (str | Unset): (General Configuration) Client IP Version (ipaddr, ipv6addr)
        clientshortname (str | Unset): (General Configuration) Client Shortname

            Enter a short name for the client. This is generally the hostname of the NAS.
        clientsharedsecret (str | Unset): (General Configuration) Client Shared Secret

            Enter the shared secret of the RADIUS client here. This is the shared secret (password)
            which the NAS (switch, accesspoint, etc.) needs to communicate with the RADIUS server.
            FreeRADIUS is limited to 31 characters for the shared secret.

            Warning: Single quotes in shared secret must be escaped with a backslash (\').
            Backslash must be escaped by using two backslashes (\\).
        clientproto (str | Unset): (Miscellaneous Configuration) Client Protocol (udp, tcp)

            Enter the protocol the client uses.
            (Default: UDP)
        clientnastype (str | Unset): (Miscellaneous Configuration) Client Type (cisco, cvx, computone, digitro,
            livingston, juniper, max40xx, mikrotik, mikrotik_snmp, multitech, netserver, pathras, pr3000, pr4000, patton,
            portslave, redback, tc, usrhiper, versanet, dot1x, other)

            Enter the NAS type of the client. This is used by checkrad.pl for simultaneous use checks.
            (Default: other)
        requiremessageauthenticator (str | Unset): (Miscellaneous Configuration) Require Message Authenticator (no, yes)

            RFC5080 requires Message-Authenticator in Access-Request.
            But older NAS (switches or accesspoints) do not include that.

            (Default: no)
        clientmaxconnections (str | Unset): (Miscellaneous Configuration) Max Connections

            Takes only effect if you use TCP as protocol.
            Limits the number of simultaneous TCP connections from a client.

            (Default 16)
        clientlogininput (str | Unset): (Miscellaneous Configuration) NAS Login

            If supported by your NAS, you can use SNMP or finger for simultaneous-use checks instead of (s)radutmp file and
            accounting.

            Leave empty to choose (s)radutmp. (Default: empty)
        clientpasswordinput (str | Unset): (Miscellaneous Configuration) NAS Password

            If supported by your NAS, you can use SNMP or finger for simultaneous-use checks instead of (s)radutmp file and
            accounting.

            Leave empty to choose (s)radutmp. (Default: empty)
        description (str | Unset): (Miscellaneous Configuration) Description

            Enter any description you like for this client.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    clientip: str | Unset = UNSET
    clientipversion: str | Unset = UNSET
    clientshortname: str | Unset = UNSET
    clientsharedsecret: str | Unset = UNSET
    clientproto: str | Unset = UNSET
    clientnastype: str | Unset = UNSET
    requiremessageauthenticator: str | Unset = UNSET
    clientmaxconnections: str | Unset = UNSET
    clientlogininput: str | Unset = UNSET
    clientpasswordinput: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clientip = self.clientip

        clientipversion = self.clientipversion

        clientshortname = self.clientshortname

        clientsharedsecret = self.clientsharedsecret

        clientproto = self.clientproto

        clientnastype = self.clientnastype

        requiremessageauthenticator = self.requiremessageauthenticator

        clientmaxconnections = self.clientmaxconnections

        clientlogininput = self.clientlogininput

        clientpasswordinput = self.clientpasswordinput

        description = self.description

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clientip is not UNSET:
            field_dict["clientip"] = clientip
        if clientipversion is not UNSET:
            field_dict["clientipversion"] = clientipversion
        if clientshortname is not UNSET:
            field_dict["clientshortname"] = clientshortname
        if clientsharedsecret is not UNSET:
            field_dict["clientsharedsecret"] = clientsharedsecret
        if clientproto is not UNSET:
            field_dict["clientproto"] = clientproto
        if clientnastype is not UNSET:
            field_dict["clientnastype"] = clientnastype
        if requiremessageauthenticator is not UNSET:
            field_dict["requiremessageauthenticator"] = requiremessageauthenticator
        if clientmaxconnections is not UNSET:
            field_dict["clientmaxconnections"] = clientmaxconnections
        if clientlogininput is not UNSET:
            field_dict["clientlogininput"] = clientlogininput
        if clientpasswordinput is not UNSET:
            field_dict["clientpasswordinput"] = clientpasswordinput
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        clientip = d.pop("clientip", UNSET)

        clientipversion = d.pop("clientipversion", UNSET)

        clientshortname = d.pop("clientshortname", UNSET)

        clientsharedsecret = d.pop("clientsharedsecret", UNSET)

        clientproto = d.pop("clientproto", UNSET)

        clientnastype = d.pop("clientnastype", UNSET)

        requiremessageauthenticator = d.pop("requiremessageauthenticator", UNSET)

        clientmaxconnections = d.pop("clientmaxconnections", UNSET)

        clientlogininput = d.pop("clientlogininput", UNSET)

        clientpasswordinput = d.pop("clientpasswordinput", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        freeradiusclient = cls(
            clientip=clientip,
            clientipversion=clientipversion,
            clientshortname=clientshortname,
            clientsharedsecret=clientsharedsecret,
            clientproto=clientproto,
            clientnastype=clientnastype,
            requiremessageauthenticator=requiremessageauthenticator,
            clientmaxconnections=clientmaxconnections,
            clientlogininput=clientlogininput,
            clientpasswordinput=clientpasswordinput,
            description=description,
            id=id,
        )

        freeradiusclient.additional_properties = d
        return freeradiusclient

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
