from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Freeradiusauthorizedmac")


@_attrs_define
class Freeradiusauthorizedmac:
    """
    Attributes:
        macsaddress (str | Unset): (General Configuration) MAC Address

            Enter the MAC address. Leave empty if you want to use custom options instead of MAC address.

            Required format: 0a-1b-2c-4d-5f-fa or 0a:1b:2c:4d:5f:fa
        macsswisprredirectionurl (str | Unset): (Miscellaneous Configuration) Redirection URL

            Enter the URL the MAC should be redirected to after successful login.
            Example: http://www.google.com
        macssimultaneousconnect (str | Unset): (Miscellaneous Configuration) Number of Simultaneous Connections

            The maximum of simultaneous connections with this MAC address. Leave empty for no limit.

            If using FreeRADIUS with CaptivePortal you should leave this empty. Read the documentation!
        description (str | Unset): (Miscellaneous Configuration) Description

            Enter any description for this MAC address you like.
        macsframedipaddress (str | Unset): (IPv4 Network Configuration) IPv4 Address

            Framed-IP-Address must be supported by NAS. Click Info for details.

            IMPORTANT: You must enter an IPv4 address here if you checked "RADIUS issued IP" on PPPoE VPN configuration.
        macsframedipnetmask (str | Unset): (IPv4 Network Configuration) Subnet Mask

            Framed-IP-Netmask must be supported by NAS. Example: 255.255.255.0
        macsframedroute (str | Unset): (IPv4 Network Configuration) IPv4 Gateway

            Framed-Route must be supported by NAS.
            Required format: Subnet Gateway Metric(s) (e.g. 192.168.10.0/24 192.168.10.1 1)
        macsframedip6address (str | Unset): (IPv6 Network Configuration) IPv6 Address

            When the IPv6 prefix part is empty it uses Framed-IPv6-Address.
            When the prefix part is filled in, it uses Framed-IPv6-Prefix.

            Example: 2001:db8:abab::5 or 2001:db8:abab::/64
        macsframedip6route (str | Unset): (IPv6 Network Configuration) IPv6 Gateway

            Framed-IPv6-Route must be supported by NAS.
            Required format: Prefix Gateway Metric(s) (e.g. 2001:db8:0:16::/64 2001:db8::16:a0:20ff:fe99:a998 1)
        macsvlanid (str | Unset): (VLAN Configuration) VLAN ID

            Enter the VLAN ID (integer from 1-4095) or the VLAN name that this MAC address should be assigned to.

            Must be supported by the NAS. Click Info for details.

            This setting can be used for a NAS that supports the following RADIUS parameters:

            - Tunnel-Type: VLAN
            - Tunnel-Medium-Type: IEEE-802
            - Tunnel-Private-Group-ID: "This is your input"
        macsexpiration (str | Unset): (Time Configuration) Expiration Date

            Enter the date when this account should expire.

            Required format: Mmm dd yyyy (e.g. Jan 01 2012)
        macssessiontimeout (str | Unset): (Time Configuration) Session Timeout

            Enter the time this MAC address has until relogin (in seconds).
        macslogintime (str | Unset): (Time Configuration) Possible Login Times

            Enter the time when this MAC address should have access. "Always" if no time is entered. Click Info for details.

            Each simple time string must begin with a day definition. That can be just one day, multiple days, or a range of
            days separated by a hyphen.

            A day is Mo, Tu, We, Th, Fr, Sa or Su, or Wk for Mo-Fr. Any or Al means all days.

            After that, a range of hours follows in hhmm-hhmm format. A time string may be a list of simple time strings
            separated by ,


            Example: Wk0855-2305,Sa,Su2230-0230 - weekdays after 8:55 AM and before 11:05 PM | any time on Saturday | Sunday
            after 10:30 PM and before 02:30 AM.
        macsamountoftime (str | Unset): (Time Configuration) Amount of Time

            Enter the amount of time for this MAC address (in minutes).
        macspointoftime (str | Unset): (Time Configuration) Time Period (Daily, Weekly, Monthly, Forever)

            Select the time period after which the 'Amount of Time' is reset.
        macsmaxtotaloctets (str | Unset): (Traffic and Bandwidth) Amount of Download and Upload Traffic

            Enter the amount of download and upload traffic (summarized) in megabytes (MB) for this MAC.
        macsmaxtotaloctetstimerange (str | Unset): (Traffic and Bandwidth) Time Period (daily, weekly, monthly, forever)

            Select the time period for the amount of download and upload traffic. This does not automatically reset the
            counter.

            You need to setup a cronjob (with cron package) which will reset the counter. Read the documentation!
        macsmaxbandwidthdown (str | Unset): (Traffic and Bandwidth) Maximum Bandwidth Down

            Enter the maximum bandwidth for download in in kilobits per second (Kbps).
        macsmaxbandwidthup (str | Unset): (Traffic and Bandwidth) Maximum Bandwidth Up

            Enter the maximum bandwidth for upload in in kilobits per second (Kbps).
        macsacctinteriminterval (str | Unset): (Traffic and Bandwidth) Accounting Interim Interval

            Enter the interval in seconds which should elapse between interim-updates.

            It must be more than 60s and should not be less than 600s. (Default: 600)
        macstopadditionaloptions (str | Unset): (Advanced Configuration) Additional RADIUS Attributes on the TOP of this
            entry

            This is for experts only and should be treated with care! Click Info for details.

            You may append custom RADIUS options to this MAC address account. If required by syntax, you must use quotes and
            commas.

            Use a vertical bar | to put a command on a new line.

            Example: DEFAULT Auth-Type = System

            IMPORTANT: If you don't format this field correctly, FreeRADIUS will not start because of syntax errors.

            Verify your changes by checking the authorized_macs file (View config > macs).
        macscheckitemsadditionaloptions (str | Unset): (Advanced Configuration) Additional RADIUS Attributes (CHECK-
            ITEM)

            This is for experts only and should be treated with care! Click Info for details.

            You may append custom RADIUS options to this MAC address account. If required by syntax, you must use quotes and
            commas..

            Use a vertical bar | to put a command on a new line.

            Example: Max-Daily-Session := 36000

            IMPORTANT: If you don't format this field correctly, FreeRADIUS will not start because of syntax errors.

            Verify your changes by checking the authorized_macs file (View config > macs).
        macsreplyitemsadditionaloptions (str | Unset): (Advanced Configuration) Additional RADIUS Attributes (REPLY-
            ITEM)

            This is for experts only and should be treated with care! Click Info for details.

            You may append custom RADIUS options to this MAC address account. If required by syntax, you must use quotes and
            commas..

            Use a vertical bar | to put a command on a new line.

            Example: Service-Type == Login-User,|Login-Service == Telnet,|Login-IP-Host == 192.168.1.2

            IMPORTANT: If you don't format this field correctly, FreeRADIUS will not start because of syntax errors.

            Verify your changes by checking the authorized_macs file (View config > macs).
        id (str | Unset): (readonly) ID assigned to this entry
    """

    macsaddress: str | Unset = UNSET
    macsswisprredirectionurl: str | Unset = UNSET
    macssimultaneousconnect: str | Unset = UNSET
    description: str | Unset = UNSET
    macsframedipaddress: str | Unset = UNSET
    macsframedipnetmask: str | Unset = UNSET
    macsframedroute: str | Unset = UNSET
    macsframedip6address: str | Unset = UNSET
    macsframedip6route: str | Unset = UNSET
    macsvlanid: str | Unset = UNSET
    macsexpiration: str | Unset = UNSET
    macssessiontimeout: str | Unset = UNSET
    macslogintime: str | Unset = UNSET
    macsamountoftime: str | Unset = UNSET
    macspointoftime: str | Unset = UNSET
    macsmaxtotaloctets: str | Unset = UNSET
    macsmaxtotaloctetstimerange: str | Unset = UNSET
    macsmaxbandwidthdown: str | Unset = UNSET
    macsmaxbandwidthup: str | Unset = UNSET
    macsacctinteriminterval: str | Unset = UNSET
    macstopadditionaloptions: str | Unset = UNSET
    macscheckitemsadditionaloptions: str | Unset = UNSET
    macsreplyitemsadditionaloptions: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        macsaddress = self.macsaddress

        macsswisprredirectionurl = self.macsswisprredirectionurl

        macssimultaneousconnect = self.macssimultaneousconnect

        description = self.description

        macsframedipaddress = self.macsframedipaddress

        macsframedipnetmask = self.macsframedipnetmask

        macsframedroute = self.macsframedroute

        macsframedip6address = self.macsframedip6address

        macsframedip6route = self.macsframedip6route

        macsvlanid = self.macsvlanid

        macsexpiration = self.macsexpiration

        macssessiontimeout = self.macssessiontimeout

        macslogintime = self.macslogintime

        macsamountoftime = self.macsamountoftime

        macspointoftime = self.macspointoftime

        macsmaxtotaloctets = self.macsmaxtotaloctets

        macsmaxtotaloctetstimerange = self.macsmaxtotaloctetstimerange

        macsmaxbandwidthdown = self.macsmaxbandwidthdown

        macsmaxbandwidthup = self.macsmaxbandwidthup

        macsacctinteriminterval = self.macsacctinteriminterval

        macstopadditionaloptions = self.macstopadditionaloptions

        macscheckitemsadditionaloptions = self.macscheckitemsadditionaloptions

        macsreplyitemsadditionaloptions = self.macsreplyitemsadditionaloptions

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if macsaddress is not UNSET:
            field_dict["macsaddress"] = macsaddress
        if macsswisprredirectionurl is not UNSET:
            field_dict["macsswisprredirectionurl"] = macsswisprredirectionurl
        if macssimultaneousconnect is not UNSET:
            field_dict["macssimultaneousconnect"] = macssimultaneousconnect
        if description is not UNSET:
            field_dict["description"] = description
        if macsframedipaddress is not UNSET:
            field_dict["macsframedipaddress"] = macsframedipaddress
        if macsframedipnetmask is not UNSET:
            field_dict["macsframedipnetmask"] = macsframedipnetmask
        if macsframedroute is not UNSET:
            field_dict["macsframedroute"] = macsframedroute
        if macsframedip6address is not UNSET:
            field_dict["macsframedip6address"] = macsframedip6address
        if macsframedip6route is not UNSET:
            field_dict["macsframedip6route"] = macsframedip6route
        if macsvlanid is not UNSET:
            field_dict["macsvlanid"] = macsvlanid
        if macsexpiration is not UNSET:
            field_dict["macsexpiration"] = macsexpiration
        if macssessiontimeout is not UNSET:
            field_dict["macssessiontimeout"] = macssessiontimeout
        if macslogintime is not UNSET:
            field_dict["macslogintime"] = macslogintime
        if macsamountoftime is not UNSET:
            field_dict["macsamountoftime"] = macsamountoftime
        if macspointoftime is not UNSET:
            field_dict["macspointoftime"] = macspointoftime
        if macsmaxtotaloctets is not UNSET:
            field_dict["macsmaxtotaloctets"] = macsmaxtotaloctets
        if macsmaxtotaloctetstimerange is not UNSET:
            field_dict["macsmaxtotaloctetstimerange"] = macsmaxtotaloctetstimerange
        if macsmaxbandwidthdown is not UNSET:
            field_dict["macsmaxbandwidthdown"] = macsmaxbandwidthdown
        if macsmaxbandwidthup is not UNSET:
            field_dict["macsmaxbandwidthup"] = macsmaxbandwidthup
        if macsacctinteriminterval is not UNSET:
            field_dict["macsacctinteriminterval"] = macsacctinteriminterval
        if macstopadditionaloptions is not UNSET:
            field_dict["macstopadditionaloptions"] = macstopadditionaloptions
        if macscheckitemsadditionaloptions is not UNSET:
            field_dict["macscheckitemsadditionaloptions"] = macscheckitemsadditionaloptions
        if macsreplyitemsadditionaloptions is not UNSET:
            field_dict["macsreplyitemsadditionaloptions"] = macsreplyitemsadditionaloptions
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        macsaddress = d.pop("macsaddress", UNSET)

        macsswisprredirectionurl = d.pop("macsswisprredirectionurl", UNSET)

        macssimultaneousconnect = d.pop("macssimultaneousconnect", UNSET)

        description = d.pop("description", UNSET)

        macsframedipaddress = d.pop("macsframedipaddress", UNSET)

        macsframedipnetmask = d.pop("macsframedipnetmask", UNSET)

        macsframedroute = d.pop("macsframedroute", UNSET)

        macsframedip6address = d.pop("macsframedip6address", UNSET)

        macsframedip6route = d.pop("macsframedip6route", UNSET)

        macsvlanid = d.pop("macsvlanid", UNSET)

        macsexpiration = d.pop("macsexpiration", UNSET)

        macssessiontimeout = d.pop("macssessiontimeout", UNSET)

        macslogintime = d.pop("macslogintime", UNSET)

        macsamountoftime = d.pop("macsamountoftime", UNSET)

        macspointoftime = d.pop("macspointoftime", UNSET)

        macsmaxtotaloctets = d.pop("macsmaxtotaloctets", UNSET)

        macsmaxtotaloctetstimerange = d.pop("macsmaxtotaloctetstimerange", UNSET)

        macsmaxbandwidthdown = d.pop("macsmaxbandwidthdown", UNSET)

        macsmaxbandwidthup = d.pop("macsmaxbandwidthup", UNSET)

        macsacctinteriminterval = d.pop("macsacctinteriminterval", UNSET)

        macstopadditionaloptions = d.pop("macstopadditionaloptions", UNSET)

        macscheckitemsadditionaloptions = d.pop("macscheckitemsadditionaloptions", UNSET)

        macsreplyitemsadditionaloptions = d.pop("macsreplyitemsadditionaloptions", UNSET)

        id = d.pop("id", UNSET)

        freeradiusauthorizedmac = cls(
            macsaddress=macsaddress,
            macsswisprredirectionurl=macsswisprredirectionurl,
            macssimultaneousconnect=macssimultaneousconnect,
            description=description,
            macsframedipaddress=macsframedipaddress,
            macsframedipnetmask=macsframedipnetmask,
            macsframedroute=macsframedroute,
            macsframedip6address=macsframedip6address,
            macsframedip6route=macsframedip6route,
            macsvlanid=macsvlanid,
            macsexpiration=macsexpiration,
            macssessiontimeout=macssessiontimeout,
            macslogintime=macslogintime,
            macsamountoftime=macsamountoftime,
            macspointoftime=macspointoftime,
            macsmaxtotaloctets=macsmaxtotaloctets,
            macsmaxtotaloctetstimerange=macsmaxtotaloctetstimerange,
            macsmaxbandwidthdown=macsmaxbandwidthdown,
            macsmaxbandwidthup=macsmaxbandwidthup,
            macsacctinteriminterval=macsacctinteriminterval,
            macstopadditionaloptions=macstopadditionaloptions,
            macscheckitemsadditionaloptions=macscheckitemsadditionaloptions,
            macsreplyitemsadditionaloptions=macsreplyitemsadditionaloptions,
            id=id,
        )

        freeradiusauthorizedmac.additional_properties = d
        return freeradiusauthorizedmac

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
