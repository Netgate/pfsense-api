from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_value import TextValue


T = TypeVar("T", bound="Siproxdsettings")


@_attrs_define
class Siproxdsettings:
    """
    Attributes:
        sipenable (bool | Unset): Enable siproxd
        if_inbound (str | Unset): Inbound Interface

            Select the inbound interface.
        if_outbound (str | Unset): Outbound Interface

            Select the outbound interface.
        port (str | Unset): (SIP Settings) Listening Port

            Enter the port on which to listen for SIP traffic (default 5060).
            WARNING: Do not change this unless you know what you're doing.
        hosts_allow_reg (str | Unset): (SIP Settings) Allow Registration from

            List of etworks from which we accept registrations. Empty means, allow from everywhere.
            Note that registrations are ONLY allowed from INBOUND!
            (Default: allow all)
        hosts_allow_sip (str | Unset): (SIP Settings) Allow SIP Traffic from

            List of networks from which we accept SIP traffic. Empty means, allow from everywhere.
            (Default: allow all)
        hosts_deny_sip (str | Unset): (SIP Settings) Deny SIP Traffic from

            List of networks from which we deny SIP traffic. Empty means, no blocked networks.
            Note: The DENY list takes precedence over the ALLOW lists.
            (Default: no deny list)
        defaulttimeout (str | Unset): (SIP Settings) Default Expiration Timeout

            If a REGISTER request does not contain an Expires header or expires= parameter, this number of seconds will be
            used and reported back to the UA in the answer.
        ua_string (str | Unset): (SIP Settings) User-Agent Masquerading
            Siproxd can masquerade the User Agent string of your local UAs. Useful for Providers that do not work with some
            specific UAs (e.g. sipcall.ch - it does not work if your outgoing SIP traffic contains an Asterisk UA
            string...). Default is to do no replacement.

            Masquerade all User-Agent identifiers from local UAs with the string provided here.
            Empty means no substitution.
        use_rport (str | Unset): (SIP Settings) Use ;rport in via header (0, 1, 2, 3)

            Add a ;rport targ to Via headers.

            May be required in some cases where you have a NAT router that remaps the source port 5060
            to something different and the registrar sends back the responses to port 5060.

            Options:
            - 0: Do not add ;rport to via Header
            - 1: Add ;rport to INCOMING via Header
            - 2: Add ;rport to OUTGOING via Header
            - 3: Add ;rport to OUTGOING and INCOMING via Headers
        tcp_timeout (str | Unset): (SIP over TCP Settings) TCP Inactivity Timeout

            Inactivity timeout (seconds). After that an idling TCP connection is disconnected.
            NOTE: Making this too short may cause multiple parallel registrations for the same phone.
            This timeout must be set larger than the used registration interval.
            Default: 600 sec
        tcp_connect_timeout (str | Unset): (SIP over TCP Settings) TCP Connect Timeout

            Defines how many msecs siproxd will wait for a successful connect when establishing
            an outgoing SIP signalling connection.
            This should be kept as short as possible as waiting for an TCP connection to establish
            is a BLOCKING operation - no other SIP messages are processed while waiting for a connect
            to succeed (RTP is not affected).
            Default: 500 msec
        tcp_keepalive (str | Unset): (SIP over TCP Settings) TCP Keepalive

            For TCP SIP signalling, if > 0 empty SIP packets will be sent every 'n' seconds to keep
            the connection alive.
            Default is off.
        rtpenable (str | Unset): (RTP Settings) Enable RTP Proxy (1, 0)

            1: Enable or,
            0: Disable the RTP proxy.

            Default is enabled.
        rtplower (str | Unset): (RTP Settings) RTP Port Range (Lower)

            Enter the bottom edge of the port range siproxd will allocate for incoming RTP traffic. This range must not be
            blocked by the firewall. (Default: 7070)
        rtpupper (str | Unset): (RTP Settings) RTP Port Range (Upper)

            Enter the top edge of the port range siproxd will allocate for incoming RTP traffic. This range must not be
            blocked by the firewall. (Default: 7079)
        rtptimeout (str | Unset): (RTP Settings) RTP Stream Timeout

            After this number of seconds, an RTP stream is considered dead and proxying it will be stopped. (Default:
            300sec)
        rtp_input_dejitter (str | Unset): (Dejittering Settings) Input Dejitter

            Artificial delay to be used to de-jitter RTP data streams. This time is in microseconds. 0 - completely disable
            dejitter (default)
        rtp_output_dejitter (str | Unset): (Dejittering Settings) Output Dejitter

            Artificial delay to be used to de-jitter RTP data streams. This time is in microseconds. 0 - completely disable
            dejitter (default)
        authentication (bool | Unset): (Proxy Settings) Proxy Authentication
            If checked, clients will be forced to authenticate themselves at the proxy (for registration only).

            Enable Proxy Authentication
        outboundproxyhost (str | Unset): (Proxy Settings) Outbound Proxy Hostname

            Enter the hostname of an outbound proxy to send all traffic to. This is only useful if you have multiple
            masquerading firewalls to cross.
        outboundproxyport (str | Unset): (Proxy Settings) Outbound Proxy Port

            Enter the port of the outbound proxy to send all traffic to. This is only useful if you have multiple
            masquerading firewalls to cross.
        expeditedsipforwarding (bool | Unset): (DSCP Settings) Expedited SIP Forwarding
            This service is designed to allow ISPs to offer a service with attributes similar to a "leased line". This
            service offers the ULTIMATE IN LOW LOSS, LOW LATENCY AND LOW JITTER by ensuring that there is always sufficient
            room in output queues for the contracted expedited forwarding traffic.

            Enable DSCP tagging of SIP traffic
        expeditedforwarding (bool | Unset): (DSCP Settings) Expedited RTP Forwarding
            This service is designed to allow ISPs to offer a service with attributes similar to a "leased line". This
            service offers the ULTIMATE IN LOW LOSS, LOW LATENCY AND LOW JITTER by ensuring that there is always sufficient
            room in output queues for the contracted expedited forwarding traffic.

            Enable DSCP tagging of RTP traffic
        plugin_defaulttarget (bool | Unset): (Plugin Settings - Default Target) Enable Default Target Plugin

            Redirect unknown calls to a specified target.
        plugin_defaulttarget_target (str | Unset): (Plugin Settings - Default Target) Default Target

            Target must be a full SIP URI with the syntax sip:user@host[:port]
        plugin_defaulttarget_log (bool | Unset): (Plugin Settings - Default Target) Log Redirected Calls

            Log redirected calls.
        plugin_fix_bogus_via (bool | Unset): (Plugin Settings - Fix bogus VIA Headers) Enable Bogus Via Plugin
            If enabled, incoming (from public network) SIP messages are checked for broken SIP Via headers. If the IP
            address in the latest Via Header is part of the list below, it will be replaced by the IP address where the SIP
            message has been received from.

            Enable the Fix Bogus Via Plugin
        plugin_fix_bogus_via_networks (str | Unset): (Plugin Settings - Fix bogus VIA Headers) Bogus Via Networks

            Comma separated list of networks which should have their via headers rewritten.
            Example: 10.0.0.0/8,172.16.0.0/12,192.168.0.0/16
        plugin_stun (bool | Unset): (Plugin Settings - STUN) STUN Plugin
            Uses an external STUN server to determine the public IP address of siproxd. Useful for "in-front-of-NAT-router"
            scenarios.

            Enable STUN Plugin
        plugin_stun_server (str | Unset): (Plugin Settings - STUN) STUN Hostname

            External STUN server hostname.
        plugin_stun_port (str | Unset): (Plugin Settings - STUN) STUN Port

            External STUN server port.
        plugin_stun_period (str | Unset): (Plugin Settings - STUN) STUN Period

            Period in seconds to request IP info from STUN server.
        plugin_fix_dtag (bool | Unset): (Plugin Settings - Fix DTAG) Enable fix_DTAG Plugin

            Work around some issues with DTAG (Deutsche Telekom AG) as REGISTRAR.
        plugin_fix_dtag_networks (str | Unset): (Plugin Settings - Fix DTAG) List of remote Networks to apply DTAG
            workaround

            Comma separated list of networks where DTAG REGISTRARs are located.
            Example: 217.0.23.100/32
        plugin_stripheader (bool | Unset): (Plugin Settings - Strip Headers) Enable Strip Header Plugin

            Unconditionally strip the specified SIP header from the packet.
        plugin_stripheader_remove1 (str | Unset): (Plugin Settings - Strip Headers) Header to remove (1)

            Unconditionally strip the specified SIP header from the packet.
            May be used to workaround IP fragmentation by removing "unimportant"
            SIP headers - this is clearly a ugly hack but sometimes saves one
            from headache.

            Format is `<header>[:<value>]`, the `:<value>` part is optional - if not
            present the full header will be removed.
        plugin_stripheader_remove2 (str | Unset): (Plugin Settings - Strip Headers) Header to remove (2)
        plugin_stripheader_remove3 (str | Unset): (Plugin Settings - Strip Headers) Header to remove (3)
        plugin_codecfilter (bool | Unset): (Plugin Settings - Codec Filter) Enable Codec Filter Plugin

            Removes blacklisted codecs from any passing SDP payload in both (incoming and outgoing) directions.
        plugin_codecfilter_blacklist1 (str | Unset): (Plugin Settings - Codec Filter) Codec to remove (1)

            Removes blacklisted (plugin_codecfilter_blacklist) codecs
            from any passing SDP payload in both (incoming and outgoing)
            directions. This allows the proxy to force the exclusion of
            particular codecs in the negotiation between a local UA and a
            remote side.
            The match is done as case-insensitive substring match. The config
            string "726" would match the codecs "G726-32/800", "g726", etc.
        plugin_codecfilter_blacklist2 (str | Unset): (Plugin Settings - Codec Filter) Codec to remove (2)
        plugin_codecfilter_blacklist3 (str | Unset): (Plugin Settings - Codec Filter) Codec to remove (3)
        plugin_fix_fbox_anoncall (bool | Unset): (Plugin Settings - Fix Anonymous Calls on Fritzboxes) fix_fbox_anoncall
            Plugin
            Fixes incoming anonymous phone calls with local Fritzbox UAs

            Enable fix_fbox_anoncall Plugin
        plugin_fix_fbox_anoncall_networks (str | Unset): (Plugin Settings - Fix Anonymous Calls on Fritzboxes) Local
            Networks to apply workaround

            Comma separated list of local networks which contain Fritzbox UAs that need fixing.
            Example: 192.168.0.0/16,10.0.0.0/8,172.16.0.0/20
        plugin_siptrunk (bool | Unset): (Plugin Settings - SIP Trunk) SIP Trunk
            Plugin to handle SIP Trunks where using *one* single SIP account to which a whole number block is routed. This
            means an incoming INVITE does carry the target number (in SIP URI or To: header field) but does not really carry
            any clear indications to which account it belongs to.

            Enable SIP Trunk Plugin
        plugin_siptrunk_account (str | Unset): (Plugin Settings - SIP Trunk) SIP account

            SIP account in the form of 'sip:user@host', identical as used for registration.
        plugin_siptrunk_numbers_regex (str | Unset): (Plugin Settings - SIP Trunk) REGEX number

            Regular expression that matches the whole number block associated with this account. Example:
            ^555123(10[0-9]|11[012])$
        debug_level (str | Unset): (Debug Options) Debug Level

            options (flags):
            - 0x00000000: No Debug Info
            - 0x00000001: babble (like entering/leaving func)
            - 0x00000002: network
            - 0x00000004: SIP manipulations
            - 0x00000008: Client registration
            - 0x00000010: non specified class
            - 0x00000020: proxy
            - 0x00000040: DNS stuff
            - 0x00000080: network traffic
            - 0x00000100: configuration
            - 0x00000200: RTP proxy
            - 0x00000400: Access list evaluation
            - 0x00000800: Authentication
            - 0x00001000: Plugins
            - 0x00002000: RTP babble
            - -1        : Everything
        debug_port (str | Unset): (Debug Options) TCP Debug Port

            You may connect to this port from a remote machine and receive debug output.
            This allows better creation of debug output on embedded systems that do not
            have enough memory for large disk files.
            NOTE: Port number 0 means this feature is disabled.
        if_inbound_options (list[TextValue] | Unset):
        if_outbound_options (list[TextValue] | Unset):
    """

    sipenable: bool | Unset = UNSET
    if_inbound: str | Unset = UNSET
    if_outbound: str | Unset = UNSET
    port: str | Unset = UNSET
    hosts_allow_reg: str | Unset = UNSET
    hosts_allow_sip: str | Unset = UNSET
    hosts_deny_sip: str | Unset = UNSET
    defaulttimeout: str | Unset = UNSET
    ua_string: str | Unset = UNSET
    use_rport: str | Unset = UNSET
    tcp_timeout: str | Unset = UNSET
    tcp_connect_timeout: str | Unset = UNSET
    tcp_keepalive: str | Unset = UNSET
    rtpenable: str | Unset = UNSET
    rtplower: str | Unset = UNSET
    rtpupper: str | Unset = UNSET
    rtptimeout: str | Unset = UNSET
    rtp_input_dejitter: str | Unset = UNSET
    rtp_output_dejitter: str | Unset = UNSET
    authentication: bool | Unset = UNSET
    outboundproxyhost: str | Unset = UNSET
    outboundproxyport: str | Unset = UNSET
    expeditedsipforwarding: bool | Unset = UNSET
    expeditedforwarding: bool | Unset = UNSET
    plugin_defaulttarget: bool | Unset = UNSET
    plugin_defaulttarget_target: str | Unset = UNSET
    plugin_defaulttarget_log: bool | Unset = UNSET
    plugin_fix_bogus_via: bool | Unset = UNSET
    plugin_fix_bogus_via_networks: str | Unset = UNSET
    plugin_stun: bool | Unset = UNSET
    plugin_stun_server: str | Unset = UNSET
    plugin_stun_port: str | Unset = UNSET
    plugin_stun_period: str | Unset = UNSET
    plugin_fix_dtag: bool | Unset = UNSET
    plugin_fix_dtag_networks: str | Unset = UNSET
    plugin_stripheader: bool | Unset = UNSET
    plugin_stripheader_remove1: str | Unset = UNSET
    plugin_stripheader_remove2: str | Unset = UNSET
    plugin_stripheader_remove3: str | Unset = UNSET
    plugin_codecfilter: bool | Unset = UNSET
    plugin_codecfilter_blacklist1: str | Unset = UNSET
    plugin_codecfilter_blacklist2: str | Unset = UNSET
    plugin_codecfilter_blacklist3: str | Unset = UNSET
    plugin_fix_fbox_anoncall: bool | Unset = UNSET
    plugin_fix_fbox_anoncall_networks: str | Unset = UNSET
    plugin_siptrunk: bool | Unset = UNSET
    plugin_siptrunk_account: str | Unset = UNSET
    plugin_siptrunk_numbers_regex: str | Unset = UNSET
    debug_level: str | Unset = UNSET
    debug_port: str | Unset = UNSET
    if_inbound_options: list[TextValue] | Unset = UNSET
    if_outbound_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sipenable = self.sipenable

        if_inbound = self.if_inbound

        if_outbound = self.if_outbound

        port = self.port

        hosts_allow_reg = self.hosts_allow_reg

        hosts_allow_sip = self.hosts_allow_sip

        hosts_deny_sip = self.hosts_deny_sip

        defaulttimeout = self.defaulttimeout

        ua_string = self.ua_string

        use_rport = self.use_rport

        tcp_timeout = self.tcp_timeout

        tcp_connect_timeout = self.tcp_connect_timeout

        tcp_keepalive = self.tcp_keepalive

        rtpenable = self.rtpenable

        rtplower = self.rtplower

        rtpupper = self.rtpupper

        rtptimeout = self.rtptimeout

        rtp_input_dejitter = self.rtp_input_dejitter

        rtp_output_dejitter = self.rtp_output_dejitter

        authentication = self.authentication

        outboundproxyhost = self.outboundproxyhost

        outboundproxyport = self.outboundproxyport

        expeditedsipforwarding = self.expeditedsipforwarding

        expeditedforwarding = self.expeditedforwarding

        plugin_defaulttarget = self.plugin_defaulttarget

        plugin_defaulttarget_target = self.plugin_defaulttarget_target

        plugin_defaulttarget_log = self.plugin_defaulttarget_log

        plugin_fix_bogus_via = self.plugin_fix_bogus_via

        plugin_fix_bogus_via_networks = self.plugin_fix_bogus_via_networks

        plugin_stun = self.plugin_stun

        plugin_stun_server = self.plugin_stun_server

        plugin_stun_port = self.plugin_stun_port

        plugin_stun_period = self.plugin_stun_period

        plugin_fix_dtag = self.plugin_fix_dtag

        plugin_fix_dtag_networks = self.plugin_fix_dtag_networks

        plugin_stripheader = self.plugin_stripheader

        plugin_stripheader_remove1 = self.plugin_stripheader_remove1

        plugin_stripheader_remove2 = self.plugin_stripheader_remove2

        plugin_stripheader_remove3 = self.plugin_stripheader_remove3

        plugin_codecfilter = self.plugin_codecfilter

        plugin_codecfilter_blacklist1 = self.plugin_codecfilter_blacklist1

        plugin_codecfilter_blacklist2 = self.plugin_codecfilter_blacklist2

        plugin_codecfilter_blacklist3 = self.plugin_codecfilter_blacklist3

        plugin_fix_fbox_anoncall = self.plugin_fix_fbox_anoncall

        plugin_fix_fbox_anoncall_networks = self.plugin_fix_fbox_anoncall_networks

        plugin_siptrunk = self.plugin_siptrunk

        plugin_siptrunk_account = self.plugin_siptrunk_account

        plugin_siptrunk_numbers_regex = self.plugin_siptrunk_numbers_regex

        debug_level = self.debug_level

        debug_port = self.debug_port

        if_inbound_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.if_inbound_options, Unset):
            if_inbound_options = []
            for if_inbound_options_item_data in self.if_inbound_options:
                if_inbound_options_item = if_inbound_options_item_data.to_dict()
                if_inbound_options.append(if_inbound_options_item)

        if_outbound_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.if_outbound_options, Unset):
            if_outbound_options = []
            for if_outbound_options_item_data in self.if_outbound_options:
                if_outbound_options_item = if_outbound_options_item_data.to_dict()
                if_outbound_options.append(if_outbound_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sipenable is not UNSET:
            field_dict["sipenable"] = sipenable
        if if_inbound is not UNSET:
            field_dict["if_inbound"] = if_inbound
        if if_outbound is not UNSET:
            field_dict["if_outbound"] = if_outbound
        if port is not UNSET:
            field_dict["port"] = port
        if hosts_allow_reg is not UNSET:
            field_dict["hosts_allow_reg"] = hosts_allow_reg
        if hosts_allow_sip is not UNSET:
            field_dict["hosts_allow_sip"] = hosts_allow_sip
        if hosts_deny_sip is not UNSET:
            field_dict["hosts_deny_sip"] = hosts_deny_sip
        if defaulttimeout is not UNSET:
            field_dict["defaulttimeout"] = defaulttimeout
        if ua_string is not UNSET:
            field_dict["ua_string"] = ua_string
        if use_rport is not UNSET:
            field_dict["use_rport"] = use_rport
        if tcp_timeout is not UNSET:
            field_dict["tcp_timeout"] = tcp_timeout
        if tcp_connect_timeout is not UNSET:
            field_dict["tcp_connect_timeout"] = tcp_connect_timeout
        if tcp_keepalive is not UNSET:
            field_dict["tcp_keepalive"] = tcp_keepalive
        if rtpenable is not UNSET:
            field_dict["rtpenable"] = rtpenable
        if rtplower is not UNSET:
            field_dict["rtplower"] = rtplower
        if rtpupper is not UNSET:
            field_dict["rtpupper"] = rtpupper
        if rtptimeout is not UNSET:
            field_dict["rtptimeout"] = rtptimeout
        if rtp_input_dejitter is not UNSET:
            field_dict["rtp_input_dejitter"] = rtp_input_dejitter
        if rtp_output_dejitter is not UNSET:
            field_dict["rtp_output_dejitter"] = rtp_output_dejitter
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if outboundproxyhost is not UNSET:
            field_dict["outboundproxyhost"] = outboundproxyhost
        if outboundproxyport is not UNSET:
            field_dict["outboundproxyport"] = outboundproxyport
        if expeditedsipforwarding is not UNSET:
            field_dict["expeditedsipforwarding"] = expeditedsipforwarding
        if expeditedforwarding is not UNSET:
            field_dict["expeditedforwarding"] = expeditedforwarding
        if plugin_defaulttarget is not UNSET:
            field_dict["plugin_defaulttarget"] = plugin_defaulttarget
        if plugin_defaulttarget_target is not UNSET:
            field_dict["plugin_defaulttarget_target"] = plugin_defaulttarget_target
        if plugin_defaulttarget_log is not UNSET:
            field_dict["plugin_defaulttarget_log"] = plugin_defaulttarget_log
        if plugin_fix_bogus_via is not UNSET:
            field_dict["plugin_fix_bogus_via"] = plugin_fix_bogus_via
        if plugin_fix_bogus_via_networks is not UNSET:
            field_dict["plugin_fix_bogus_via_networks"] = plugin_fix_bogus_via_networks
        if plugin_stun is not UNSET:
            field_dict["plugin_stun"] = plugin_stun
        if plugin_stun_server is not UNSET:
            field_dict["plugin_stun_server"] = plugin_stun_server
        if plugin_stun_port is not UNSET:
            field_dict["plugin_stun_port"] = plugin_stun_port
        if plugin_stun_period is not UNSET:
            field_dict["plugin_stun_period"] = plugin_stun_period
        if plugin_fix_dtag is not UNSET:
            field_dict["plugin_fix_dtag"] = plugin_fix_dtag
        if plugin_fix_dtag_networks is not UNSET:
            field_dict["plugin_fix_dtag_networks"] = plugin_fix_dtag_networks
        if plugin_stripheader is not UNSET:
            field_dict["plugin_stripheader"] = plugin_stripheader
        if plugin_stripheader_remove1 is not UNSET:
            field_dict["plugin_stripheader_remove1"] = plugin_stripheader_remove1
        if plugin_stripheader_remove2 is not UNSET:
            field_dict["plugin_stripheader_remove2"] = plugin_stripheader_remove2
        if plugin_stripheader_remove3 is not UNSET:
            field_dict["plugin_stripheader_remove3"] = plugin_stripheader_remove3
        if plugin_codecfilter is not UNSET:
            field_dict["plugin_codecfilter"] = plugin_codecfilter
        if plugin_codecfilter_blacklist1 is not UNSET:
            field_dict["plugin_codecfilter_blacklist1"] = plugin_codecfilter_blacklist1
        if plugin_codecfilter_blacklist2 is not UNSET:
            field_dict["plugin_codecfilter_blacklist2"] = plugin_codecfilter_blacklist2
        if plugin_codecfilter_blacklist3 is not UNSET:
            field_dict["plugin_codecfilter_blacklist3"] = plugin_codecfilter_blacklist3
        if plugin_fix_fbox_anoncall is not UNSET:
            field_dict["plugin_fix_fbox_anoncall"] = plugin_fix_fbox_anoncall
        if plugin_fix_fbox_anoncall_networks is not UNSET:
            field_dict["plugin_fix_fbox_anoncall_networks"] = plugin_fix_fbox_anoncall_networks
        if plugin_siptrunk is not UNSET:
            field_dict["plugin_siptrunk"] = plugin_siptrunk
        if plugin_siptrunk_account is not UNSET:
            field_dict["plugin_siptrunk_account"] = plugin_siptrunk_account
        if plugin_siptrunk_numbers_regex is not UNSET:
            field_dict["plugin_siptrunk_numbers_regex"] = plugin_siptrunk_numbers_regex
        if debug_level is not UNSET:
            field_dict["debug_level"] = debug_level
        if debug_port is not UNSET:
            field_dict["debug_port"] = debug_port
        if if_inbound_options is not UNSET:
            field_dict["if_inbound_options"] = if_inbound_options
        if if_outbound_options is not UNSET:
            field_dict["if_outbound_options"] = if_outbound_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_value import TextValue

        d = dict(src_dict)
        sipenable = d.pop("sipenable", UNSET)

        if_inbound = d.pop("if_inbound", UNSET)

        if_outbound = d.pop("if_outbound", UNSET)

        port = d.pop("port", UNSET)

        hosts_allow_reg = d.pop("hosts_allow_reg", UNSET)

        hosts_allow_sip = d.pop("hosts_allow_sip", UNSET)

        hosts_deny_sip = d.pop("hosts_deny_sip", UNSET)

        defaulttimeout = d.pop("defaulttimeout", UNSET)

        ua_string = d.pop("ua_string", UNSET)

        use_rport = d.pop("use_rport", UNSET)

        tcp_timeout = d.pop("tcp_timeout", UNSET)

        tcp_connect_timeout = d.pop("tcp_connect_timeout", UNSET)

        tcp_keepalive = d.pop("tcp_keepalive", UNSET)

        rtpenable = d.pop("rtpenable", UNSET)

        rtplower = d.pop("rtplower", UNSET)

        rtpupper = d.pop("rtpupper", UNSET)

        rtptimeout = d.pop("rtptimeout", UNSET)

        rtp_input_dejitter = d.pop("rtp_input_dejitter", UNSET)

        rtp_output_dejitter = d.pop("rtp_output_dejitter", UNSET)

        authentication = d.pop("authentication", UNSET)

        outboundproxyhost = d.pop("outboundproxyhost", UNSET)

        outboundproxyport = d.pop("outboundproxyport", UNSET)

        expeditedsipforwarding = d.pop("expeditedsipforwarding", UNSET)

        expeditedforwarding = d.pop("expeditedforwarding", UNSET)

        plugin_defaulttarget = d.pop("plugin_defaulttarget", UNSET)

        plugin_defaulttarget_target = d.pop("plugin_defaulttarget_target", UNSET)

        plugin_defaulttarget_log = d.pop("plugin_defaulttarget_log", UNSET)

        plugin_fix_bogus_via = d.pop("plugin_fix_bogus_via", UNSET)

        plugin_fix_bogus_via_networks = d.pop("plugin_fix_bogus_via_networks", UNSET)

        plugin_stun = d.pop("plugin_stun", UNSET)

        plugin_stun_server = d.pop("plugin_stun_server", UNSET)

        plugin_stun_port = d.pop("plugin_stun_port", UNSET)

        plugin_stun_period = d.pop("plugin_stun_period", UNSET)

        plugin_fix_dtag = d.pop("plugin_fix_dtag", UNSET)

        plugin_fix_dtag_networks = d.pop("plugin_fix_dtag_networks", UNSET)

        plugin_stripheader = d.pop("plugin_stripheader", UNSET)

        plugin_stripheader_remove1 = d.pop("plugin_stripheader_remove1", UNSET)

        plugin_stripheader_remove2 = d.pop("plugin_stripheader_remove2", UNSET)

        plugin_stripheader_remove3 = d.pop("plugin_stripheader_remove3", UNSET)

        plugin_codecfilter = d.pop("plugin_codecfilter", UNSET)

        plugin_codecfilter_blacklist1 = d.pop("plugin_codecfilter_blacklist1", UNSET)

        plugin_codecfilter_blacklist2 = d.pop("plugin_codecfilter_blacklist2", UNSET)

        plugin_codecfilter_blacklist3 = d.pop("plugin_codecfilter_blacklist3", UNSET)

        plugin_fix_fbox_anoncall = d.pop("plugin_fix_fbox_anoncall", UNSET)

        plugin_fix_fbox_anoncall_networks = d.pop("plugin_fix_fbox_anoncall_networks", UNSET)

        plugin_siptrunk = d.pop("plugin_siptrunk", UNSET)

        plugin_siptrunk_account = d.pop("plugin_siptrunk_account", UNSET)

        plugin_siptrunk_numbers_regex = d.pop("plugin_siptrunk_numbers_regex", UNSET)

        debug_level = d.pop("debug_level", UNSET)

        debug_port = d.pop("debug_port", UNSET)

        _if_inbound_options = d.pop("if_inbound_options", UNSET)
        if_inbound_options: list[TextValue] | Unset = UNSET
        if _if_inbound_options is not UNSET:
            if_inbound_options = []
            for if_inbound_options_item_data in _if_inbound_options:
                if_inbound_options_item = TextValue.from_dict(if_inbound_options_item_data)

                if_inbound_options.append(if_inbound_options_item)

        _if_outbound_options = d.pop("if_outbound_options", UNSET)
        if_outbound_options: list[TextValue] | Unset = UNSET
        if _if_outbound_options is not UNSET:
            if_outbound_options = []
            for if_outbound_options_item_data in _if_outbound_options:
                if_outbound_options_item = TextValue.from_dict(if_outbound_options_item_data)

                if_outbound_options.append(if_outbound_options_item)

        siproxdsettings = cls(
            sipenable=sipenable,
            if_inbound=if_inbound,
            if_outbound=if_outbound,
            port=port,
            hosts_allow_reg=hosts_allow_reg,
            hosts_allow_sip=hosts_allow_sip,
            hosts_deny_sip=hosts_deny_sip,
            defaulttimeout=defaulttimeout,
            ua_string=ua_string,
            use_rport=use_rport,
            tcp_timeout=tcp_timeout,
            tcp_connect_timeout=tcp_connect_timeout,
            tcp_keepalive=tcp_keepalive,
            rtpenable=rtpenable,
            rtplower=rtplower,
            rtpupper=rtpupper,
            rtptimeout=rtptimeout,
            rtp_input_dejitter=rtp_input_dejitter,
            rtp_output_dejitter=rtp_output_dejitter,
            authentication=authentication,
            outboundproxyhost=outboundproxyhost,
            outboundproxyport=outboundproxyport,
            expeditedsipforwarding=expeditedsipforwarding,
            expeditedforwarding=expeditedforwarding,
            plugin_defaulttarget=plugin_defaulttarget,
            plugin_defaulttarget_target=plugin_defaulttarget_target,
            plugin_defaulttarget_log=plugin_defaulttarget_log,
            plugin_fix_bogus_via=plugin_fix_bogus_via,
            plugin_fix_bogus_via_networks=plugin_fix_bogus_via_networks,
            plugin_stun=plugin_stun,
            plugin_stun_server=plugin_stun_server,
            plugin_stun_port=plugin_stun_port,
            plugin_stun_period=plugin_stun_period,
            plugin_fix_dtag=plugin_fix_dtag,
            plugin_fix_dtag_networks=plugin_fix_dtag_networks,
            plugin_stripheader=plugin_stripheader,
            plugin_stripheader_remove1=plugin_stripheader_remove1,
            plugin_stripheader_remove2=plugin_stripheader_remove2,
            plugin_stripheader_remove3=plugin_stripheader_remove3,
            plugin_codecfilter=plugin_codecfilter,
            plugin_codecfilter_blacklist1=plugin_codecfilter_blacklist1,
            plugin_codecfilter_blacklist2=plugin_codecfilter_blacklist2,
            plugin_codecfilter_blacklist3=plugin_codecfilter_blacklist3,
            plugin_fix_fbox_anoncall=plugin_fix_fbox_anoncall,
            plugin_fix_fbox_anoncall_networks=plugin_fix_fbox_anoncall_networks,
            plugin_siptrunk=plugin_siptrunk,
            plugin_siptrunk_account=plugin_siptrunk_account,
            plugin_siptrunk_numbers_regex=plugin_siptrunk_numbers_regex,
            debug_level=debug_level,
            debug_port=debug_port,
            if_inbound_options=if_inbound_options,
            if_outbound_options=if_outbound_options,
        )

        siproxdsettings.additional_properties = d
        return siproxdsettings

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
