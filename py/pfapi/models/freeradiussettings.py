from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Freeradiussettings")


@_attrs_define
class Freeradiussettings:
    """
    Attributes:
        settingsmaxrequests (str | Unset): (General Configuration) Maximum Requests Tracked

            The maximum number of requests which the server keeps track of until 'Cleanup Delay' deletes them.

            If set too low, it will make FreeRADIUS server busy. A higher value is better (but means increased RAM usage).

            Useful range: (256 * < number of NAS >). Shouldn't be higher than (1000 * < number of NAS >).
            (Default: 1024)
        settingsmaxrequesttime (str | Unset): (General Configuration) Maximum Request Timeout

            The maximum time to handle a request (in seconds).
            (Default: 30)
        settingscleanupdelay (str | Unset): (General Configuration) Cleanup Delay

            The time to wait before cleaning up a reply which was sent to the NAS (in seconds).
            (Default: 5)
        settingsallowcoredumps (str | Unset): (General Configuration) Allow Core Dumps (no, yes)

            Only enable if you need to debug the RADIUS server!
            (Default: Disable)
        settingsregularexpressions (str | Unset): (General Configuration) Regular Expressions (no, yes)

            Allows to use regular expressions.
            (Default: Enable)
        settingsextendedexpressions (str | Unset): (General Configuration) Extended Expressions (no, yes)

            Allows to use extended expressions.
            (Default: Enable)
        keep_settings (bool | Unset): (General Configuration) Save settings after deletion
            Important: If disabled, all settings will be wiped on package uninstall/reinstall/upgrade.

            If enabled, the settings will be preserved across package reinstalls.
        settingslogdir (str | Unset): (Logging Configuration) RADIUS Logging Destination (files, syslog)

            Choose the destination for FreeRADIUS logs.
            This will log general service information, but no authentication information.

            (Default: System Logs)
        settingsauth (str | Unset): (Logging Configuration) RADIUS Logging (no, yes)

            This enables logging of accepted or rejected authentication.
            (Default: Enable)
        settingsauthbadpass (str | Unset): (Logging Configuration) Log Password on Authentication Failure (no, yes)

            Log the password of failed authentication attempts to syslog.
            Not recommended for security reasons.

            'RADIUS Logging' must be enabled. (Default: No)
        settingsauthbadpassmessage (str | Unset): (Logging Configuration) Additional Information for Bad Attempts

            You can add additional information to the syslog output if a user is rejected. Click Info for details.

            You can use variables for any attributes.

            %{User-Name} - Logs the username.

            %{reply:Acct-Output-Octets} - Logs the remaining output octets.
        settingsauthgoodpass (str | Unset): (Logging Configuration) Log Password on Authentication Success (no, yes)

            Log the password of successful authentication attempts to syslog.
            Not recommended for security reasons.

            'RADIUS Logging' must be enabled. (Default: No)
        settingsauthgoodpassmessage (str | Unset): (Logging Configuration) Additional Information for Good Attempts

            You can add additional information to the syslog output if a user connects. Click Info for details.

            You can use variables for any attributes.

            %{User-Name} - Logs the username.

            %{reply:Acct-Output-Octets} - Logs the remaining output octets.
        settingsstrippednames (str | Unset): (Logging Configuration) Log Stripped Names (no, yes)

            Choose this if you want to log the full User-Name attribute as it was found in the request.

            'RADIUS Logging' must be enabled. (Default: No)
        settingshostnamelookups (str | Unset): (Logging Configuration) NAS Hostname Lookup (no, yes)

            Log the names of NAS instead of IP addresses.

            Warning: Turning this on can result in lock-ups of the RADIUS server.
            (Default: Disable)
        settingsmaxattributes (str | Unset): (Security Configuration) Maximum Number of Attributes

            The maximum number of attributes permitted in a RADIUS packet.
            Packets which have more than this number of attributes in them will be dropped.

            (Default: 200)
        settingsrejectdelay (str | Unset): (Security Configuration) Access-Reject Delay

            When sending an Access-Reject it can be delayed for a few seconds.

            This may help to slow down a DoS attack. It also helps to slow down people trying to brute-force crack a user's
            password.

            To send Access-Reject immediately, set to '0'. (Default: 1)
        settingsstartservers (str | Unset): (Thread Pool Configuration) Number of Threads After Start

            The thread pool is a long-lived group of threads which take turns (round-robin) handling any incoming requests.
            (Default: 5)
        settingsmaxservers (str | Unset): (Thread Pool Configuration) Maximum Number of Threads

            If this limit is ever reached, clients will be locked out; it should not be set too low.
            (Default: 32)
        settingsminspareservers (str | Unset): (Thread Pool Configuration) Minimum Spare Servers

            This dynamically adjusts the 'Number of Threads After Start'. If the RADIUS server has to handle many requests
            and less than 'Minimum Spare Servers' are left, the RADIUS server will increase the number of running threads.

            (Default: 3)
        settingsmaxspareservers (str | Unset): (Thread Pool Configuration) Maximum Spare Servers

            This dynamically adjusts the 'Number of Threads After Start'. If the RADIUS server has to handle few requests
            and more than 'Maximum Spare Servers' are left, the RADIUS server will decrease the number of running threads.

            (Default: 10)
        settingsmaxqueuesize (str | Unset): (Thread Pool Configuration) Server Packet Queue Size

            This is the queue size where the server stores packets before processing them.
            (Default: 65536)
        settingsmaxrequestsperserver (str | Unset): (Thread Pool Configuration) Maximum Requests Per Server

            You should only change this if you encounter memory leaks while running RADIUS.
            (Default: 0)
        settingsmotpenable (bool | Unset): (Mobile-One-Time-Password Configuration) Mobile-One-Time-Password
            This enables the possibility to authenticate with username and one-time-password. The client used to generate
            OTP can be installed on various mobile device platforms like Android, iOS and others. (Default: Disabled)

            Enable Mobile-One-Time-Password Support
        settingsmotptimespan (str | Unset): (Mobile-One-Time-Password Configuration) OTP Lifetime

            The resulting lifetime (in seconds) is the value entered here multiplied by 10 (i.e., 1 ~ 10s, 2 ~ 20s, 3 ~30s).

            Values higher than 12 are not allowed for security reasons. (Default: 2)
        settingsmotppasswordattempts (str | Unset): (Mobile-One-Time-Password Configuration) Number of Invalid Password
            Attempts

            After this many failed attempts, the user will be locked out until an admin unlocks the user.

            Values higher than 20 are not allowed for security reasons. (Default: 5)
        settingsmotpchecksumtype (str | Unset): (Mobile-One-Time-Password Configuration) Hash Algorithm (md5, sha1,
            sha256)

            We build a hash of EPOCHTIME+INIT-SECRET+PIN and then use the digits as password.

            If some other (hardware) tokens use other hash types, you can adjust the calculation here.

            Note: This must be equal on both sides!(Default: md5)
        settingsmotptokenlength (str | Unset): (Mobile-One-Time-Password Configuration) Token Password Length

            We build a hash of EPOCHTIME+INIT-SECRET+PIN and then use the first 6 digits as password.

            If some other (hardware) tokens use other digits, you can adjust the used digits here.

            Note: This must be equal on both sides! (Default: 1-6)
        settingsenablemacauth (bool | Unset): (Miscellaneous Configuration) Plain MAC Auth
            The Calling-Station-Id in an Access-Request is first checked against the authorized_macs list, before all other
            authorization methods. If the NAS is not able to convert the MAC address to the 802.1X format, this field can be
            enabled. Leave this disabled (unchecked) unless absolutely necessary. (Default: Disabled)

            Enable Plain MAC Authentication
        settingsenableacctunique (bool | Unset): (Miscellaneous Configuration) Disable Acct_Unique
            If you encounter problems with some counters when using 'Amount of Download/Upload/Time', you can check this to
            disable the module. (Default: Enabled)

            Disable the "rlm_acct_unique" module in FreeRADIUS "preacct" section.
    """

    settingsmaxrequests: str | Unset = UNSET
    settingsmaxrequesttime: str | Unset = UNSET
    settingscleanupdelay: str | Unset = UNSET
    settingsallowcoredumps: str | Unset = UNSET
    settingsregularexpressions: str | Unset = UNSET
    settingsextendedexpressions: str | Unset = UNSET
    keep_settings: bool | Unset = UNSET
    settingslogdir: str | Unset = UNSET
    settingsauth: str | Unset = UNSET
    settingsauthbadpass: str | Unset = UNSET
    settingsauthbadpassmessage: str | Unset = UNSET
    settingsauthgoodpass: str | Unset = UNSET
    settingsauthgoodpassmessage: str | Unset = UNSET
    settingsstrippednames: str | Unset = UNSET
    settingshostnamelookups: str | Unset = UNSET
    settingsmaxattributes: str | Unset = UNSET
    settingsrejectdelay: str | Unset = UNSET
    settingsstartservers: str | Unset = UNSET
    settingsmaxservers: str | Unset = UNSET
    settingsminspareservers: str | Unset = UNSET
    settingsmaxspareservers: str | Unset = UNSET
    settingsmaxqueuesize: str | Unset = UNSET
    settingsmaxrequestsperserver: str | Unset = UNSET
    settingsmotpenable: bool | Unset = UNSET
    settingsmotptimespan: str | Unset = UNSET
    settingsmotppasswordattempts: str | Unset = UNSET
    settingsmotpchecksumtype: str | Unset = UNSET
    settingsmotptokenlength: str | Unset = UNSET
    settingsenablemacauth: bool | Unset = UNSET
    settingsenableacctunique: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settingsmaxrequests = self.settingsmaxrequests

        settingsmaxrequesttime = self.settingsmaxrequesttime

        settingscleanupdelay = self.settingscleanupdelay

        settingsallowcoredumps = self.settingsallowcoredumps

        settingsregularexpressions = self.settingsregularexpressions

        settingsextendedexpressions = self.settingsextendedexpressions

        keep_settings = self.keep_settings

        settingslogdir = self.settingslogdir

        settingsauth = self.settingsauth

        settingsauthbadpass = self.settingsauthbadpass

        settingsauthbadpassmessage = self.settingsauthbadpassmessage

        settingsauthgoodpass = self.settingsauthgoodpass

        settingsauthgoodpassmessage = self.settingsauthgoodpassmessage

        settingsstrippednames = self.settingsstrippednames

        settingshostnamelookups = self.settingshostnamelookups

        settingsmaxattributes = self.settingsmaxattributes

        settingsrejectdelay = self.settingsrejectdelay

        settingsstartservers = self.settingsstartservers

        settingsmaxservers = self.settingsmaxservers

        settingsminspareservers = self.settingsminspareservers

        settingsmaxspareservers = self.settingsmaxspareservers

        settingsmaxqueuesize = self.settingsmaxqueuesize

        settingsmaxrequestsperserver = self.settingsmaxrequestsperserver

        settingsmotpenable = self.settingsmotpenable

        settingsmotptimespan = self.settingsmotptimespan

        settingsmotppasswordattempts = self.settingsmotppasswordattempts

        settingsmotpchecksumtype = self.settingsmotpchecksumtype

        settingsmotptokenlength = self.settingsmotptokenlength

        settingsenablemacauth = self.settingsenablemacauth

        settingsenableacctunique = self.settingsenableacctunique

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settingsmaxrequests is not UNSET:
            field_dict["settingsmaxrequests"] = settingsmaxrequests
        if settingsmaxrequesttime is not UNSET:
            field_dict["settingsmaxrequesttime"] = settingsmaxrequesttime
        if settingscleanupdelay is not UNSET:
            field_dict["settingscleanupdelay"] = settingscleanupdelay
        if settingsallowcoredumps is not UNSET:
            field_dict["settingsallowcoredumps"] = settingsallowcoredumps
        if settingsregularexpressions is not UNSET:
            field_dict["settingsregularexpressions"] = settingsregularexpressions
        if settingsextendedexpressions is not UNSET:
            field_dict["settingsextendedexpressions"] = settingsextendedexpressions
        if keep_settings is not UNSET:
            field_dict["keep_settings"] = keep_settings
        if settingslogdir is not UNSET:
            field_dict["settingslogdir"] = settingslogdir
        if settingsauth is not UNSET:
            field_dict["settingsauth"] = settingsauth
        if settingsauthbadpass is not UNSET:
            field_dict["settingsauthbadpass"] = settingsauthbadpass
        if settingsauthbadpassmessage is not UNSET:
            field_dict["settingsauthbadpassmessage"] = settingsauthbadpassmessage
        if settingsauthgoodpass is not UNSET:
            field_dict["settingsauthgoodpass"] = settingsauthgoodpass
        if settingsauthgoodpassmessage is not UNSET:
            field_dict["settingsauthgoodpassmessage"] = settingsauthgoodpassmessage
        if settingsstrippednames is not UNSET:
            field_dict["settingsstrippednames"] = settingsstrippednames
        if settingshostnamelookups is not UNSET:
            field_dict["settingshostnamelookups"] = settingshostnamelookups
        if settingsmaxattributes is not UNSET:
            field_dict["settingsmaxattributes"] = settingsmaxattributes
        if settingsrejectdelay is not UNSET:
            field_dict["settingsrejectdelay"] = settingsrejectdelay
        if settingsstartservers is not UNSET:
            field_dict["settingsstartservers"] = settingsstartservers
        if settingsmaxservers is not UNSET:
            field_dict["settingsmaxservers"] = settingsmaxservers
        if settingsminspareservers is not UNSET:
            field_dict["settingsminspareservers"] = settingsminspareservers
        if settingsmaxspareservers is not UNSET:
            field_dict["settingsmaxspareservers"] = settingsmaxspareservers
        if settingsmaxqueuesize is not UNSET:
            field_dict["settingsmaxqueuesize"] = settingsmaxqueuesize
        if settingsmaxrequestsperserver is not UNSET:
            field_dict["settingsmaxrequestsperserver"] = settingsmaxrequestsperserver
        if settingsmotpenable is not UNSET:
            field_dict["settingsmotpenable"] = settingsmotpenable
        if settingsmotptimespan is not UNSET:
            field_dict["settingsmotptimespan"] = settingsmotptimespan
        if settingsmotppasswordattempts is not UNSET:
            field_dict["settingsmotppasswordattempts"] = settingsmotppasswordattempts
        if settingsmotpchecksumtype is not UNSET:
            field_dict["settingsmotpchecksumtype"] = settingsmotpchecksumtype
        if settingsmotptokenlength is not UNSET:
            field_dict["settingsmotptokenlength"] = settingsmotptokenlength
        if settingsenablemacauth is not UNSET:
            field_dict["settingsenablemacauth"] = settingsenablemacauth
        if settingsenableacctunique is not UNSET:
            field_dict["settingsenableacctunique"] = settingsenableacctunique

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        settingsmaxrequests = d.pop("settingsmaxrequests", UNSET)

        settingsmaxrequesttime = d.pop("settingsmaxrequesttime", UNSET)

        settingscleanupdelay = d.pop("settingscleanupdelay", UNSET)

        settingsallowcoredumps = d.pop("settingsallowcoredumps", UNSET)

        settingsregularexpressions = d.pop("settingsregularexpressions", UNSET)

        settingsextendedexpressions = d.pop("settingsextendedexpressions", UNSET)

        keep_settings = d.pop("keep_settings", UNSET)

        settingslogdir = d.pop("settingslogdir", UNSET)

        settingsauth = d.pop("settingsauth", UNSET)

        settingsauthbadpass = d.pop("settingsauthbadpass", UNSET)

        settingsauthbadpassmessage = d.pop("settingsauthbadpassmessage", UNSET)

        settingsauthgoodpass = d.pop("settingsauthgoodpass", UNSET)

        settingsauthgoodpassmessage = d.pop("settingsauthgoodpassmessage", UNSET)

        settingsstrippednames = d.pop("settingsstrippednames", UNSET)

        settingshostnamelookups = d.pop("settingshostnamelookups", UNSET)

        settingsmaxattributes = d.pop("settingsmaxattributes", UNSET)

        settingsrejectdelay = d.pop("settingsrejectdelay", UNSET)

        settingsstartservers = d.pop("settingsstartservers", UNSET)

        settingsmaxservers = d.pop("settingsmaxservers", UNSET)

        settingsminspareservers = d.pop("settingsminspareservers", UNSET)

        settingsmaxspareservers = d.pop("settingsmaxspareservers", UNSET)

        settingsmaxqueuesize = d.pop("settingsmaxqueuesize", UNSET)

        settingsmaxrequestsperserver = d.pop("settingsmaxrequestsperserver", UNSET)

        settingsmotpenable = d.pop("settingsmotpenable", UNSET)

        settingsmotptimespan = d.pop("settingsmotptimespan", UNSET)

        settingsmotppasswordattempts = d.pop("settingsmotppasswordattempts", UNSET)

        settingsmotpchecksumtype = d.pop("settingsmotpchecksumtype", UNSET)

        settingsmotptokenlength = d.pop("settingsmotptokenlength", UNSET)

        settingsenablemacauth = d.pop("settingsenablemacauth", UNSET)

        settingsenableacctunique = d.pop("settingsenableacctunique", UNSET)

        freeradiussettings = cls(
            settingsmaxrequests=settingsmaxrequests,
            settingsmaxrequesttime=settingsmaxrequesttime,
            settingscleanupdelay=settingscleanupdelay,
            settingsallowcoredumps=settingsallowcoredumps,
            settingsregularexpressions=settingsregularexpressions,
            settingsextendedexpressions=settingsextendedexpressions,
            keep_settings=keep_settings,
            settingslogdir=settingslogdir,
            settingsauth=settingsauth,
            settingsauthbadpass=settingsauthbadpass,
            settingsauthbadpassmessage=settingsauthbadpassmessage,
            settingsauthgoodpass=settingsauthgoodpass,
            settingsauthgoodpassmessage=settingsauthgoodpassmessage,
            settingsstrippednames=settingsstrippednames,
            settingshostnamelookups=settingshostnamelookups,
            settingsmaxattributes=settingsmaxattributes,
            settingsrejectdelay=settingsrejectdelay,
            settingsstartservers=settingsstartservers,
            settingsmaxservers=settingsmaxservers,
            settingsminspareservers=settingsminspareservers,
            settingsmaxspareservers=settingsmaxspareservers,
            settingsmaxqueuesize=settingsmaxqueuesize,
            settingsmaxrequestsperserver=settingsmaxrequestsperserver,
            settingsmotpenable=settingsmotpenable,
            settingsmotptimespan=settingsmotptimespan,
            settingsmotppasswordattempts=settingsmotppasswordattempts,
            settingsmotpchecksumtype=settingsmotpchecksumtype,
            settingsmotptokenlength=settingsmotptokenlength,
            settingsenablemacauth=settingsenablemacauth,
            settingsenableacctunique=settingsenableacctunique,
        )

        freeradiussettings.additional_properties = d
        return freeradiussettings

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
