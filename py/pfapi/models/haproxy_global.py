from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyGlobal")


@_attrs_define
class HaproxyGlobal:
    """
    Attributes:
        enable (bool | Unset): (General Settings) Enable HAProxy

            Master switch to enable/disable the HAProxy service.
        terminate_on_reload (bool | Unset): (General Settings) Terminate on Reload

            Force termination of old process on reload instead of graceful stop.
        enablesync (bool | Unset): (General Settings) CARP XMLRpc Sync

            Enable XMLRPC configuration synchronization for CARP failover.
        maxconn (str | Unset): (General Settings) Maximum Connections

            Maximum per-process number of concurrent connections.
            (Default: uses HAProxy compiled default)
        nbthread (str | Unset): (General Settings) Number of Threads

            Number of threads to use. Each thread handles connections independently.
            (Default: 1)
        hard_stop_after (str | Unset): (General Settings) Hard Stop After

            Maximum time to wait for all connections to close during a soft stop,
            after which the process is killed. Format: time with suffix (e.g. 30s, 5m).
        localstatsport (str | Unset): (Stats Settings) Internal Stats Port

            Port for the internal statistics socket. Used for local stats page access.
        localstats_refreshtime (str | Unset): (Stats Settings) Internal Stats Refresh Time

            Refresh interval in seconds for the internal statistics page.
        localstats_sticktable_refreshtime (str | Unset): (Stats Settings) Stick Table Refresh Time

            Refresh interval in seconds for stick-table statistics.
        remotesyslog (str | Unset): (Logging) Remote Syslog Host

            IP address or hostname of a remote syslog server. HAProxy sends logs via UDP.
        logfacility (str | Unset): (Logging) Syslog Facility (local0, local1, local2, local3, local4, local5, local6,
            local7, kern, user, mail, daemon, auth)

            Syslog facility to use for HAProxy log messages.
            (Default: local0)
        loglevel (str | Unset): (Logging) Log Level (emerg, alert, crit, err, warning, notice, info, debug)

            Minimum log level for messages to be sent to syslog.
            (Default: info)
        log_send_hostname (str | Unset): (Logging) Log Hostname

            Hostname to use in syslog messages. If set, this value appears in the
            syslog header instead of the system hostname.
        carpdev (str | Unset): (Tuning) CARP Device IP

            IP address of the CARP device to monitor. HAProxy will only run when the
            CARP interface is in MASTER state.
        sslcompatibilitymode (str | Unset): (SSL) SSL Compatibility Mode (auto, modern, intermediate, old)

            Predefined SSL cipher suite and protocol settings.
            - auto: Use HAProxy defaults
            - modern: TLS 1.3 only, strongest ciphers
            - intermediate: TLS 1.2+, broad compatibility
            - old: TLS 1.0+, maximum compatibility (not recommended)
        ssldefaultdhparam (str | Unset): (SSL) SSL Default DH Parameter Size

            Size of the Diffie-Hellman parameters for DHE key exchanges.
            (Default: 2048)
        email_level (str | Unset): (Email) Email Alert Level (emerg, alert, crit, err, warning, notice, info, debug)

            Minimum severity level for email notifications.
        email_myhostname (str | Unset): (Email) Email Hostname

            Hostname used in SMTP HELO/EHLO when sending email alerts.
        email_from (str | Unset): (Email) Email From Address

            Sender email address for alert notifications.
        email_to (str | Unset): (Email) Email To Address

            Recipient email address for alert notifications.
        resolver_retries (str | Unset): (DNS) Resolver Retries

            Number of DNS resolution retry attempts before giving up.
            (Default: 3)
        resolver_timeoutretry (str | Unset): (DNS) Resolver Timeout Retry

            Timeout between DNS resolution retries. Format: time with suffix (e.g. 1s).
            (Default: 1s)
        resolver_holdvalid (str | Unset): (DNS) Resolver Hold Valid

            Duration to keep a valid DNS result in cache. Format: time with suffix (e.g. 10s).
            (Default: 10s)
        advanced (str | Unset): (Advanced) Custom Global Configuration

            Base64-encoded raw HAProxy configuration appended to the global section.
            Use with caution - invalid entries may prevent HAProxy from starting.
        version (str | Unset): (readonly) HAProxy version
    """

    enable: bool | Unset = UNSET
    terminate_on_reload: bool | Unset = UNSET
    enablesync: bool | Unset = UNSET
    maxconn: str | Unset = UNSET
    nbthread: str | Unset = UNSET
    hard_stop_after: str | Unset = UNSET
    localstatsport: str | Unset = UNSET
    localstats_refreshtime: str | Unset = UNSET
    localstats_sticktable_refreshtime: str | Unset = UNSET
    remotesyslog: str | Unset = UNSET
    logfacility: str | Unset = UNSET
    loglevel: str | Unset = UNSET
    log_send_hostname: str | Unset = UNSET
    carpdev: str | Unset = UNSET
    sslcompatibilitymode: str | Unset = UNSET
    ssldefaultdhparam: str | Unset = UNSET
    email_level: str | Unset = UNSET
    email_myhostname: str | Unset = UNSET
    email_from: str | Unset = UNSET
    email_to: str | Unset = UNSET
    resolver_retries: str | Unset = UNSET
    resolver_timeoutretry: str | Unset = UNSET
    resolver_holdvalid: str | Unset = UNSET
    advanced: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        terminate_on_reload = self.terminate_on_reload

        enablesync = self.enablesync

        maxconn = self.maxconn

        nbthread = self.nbthread

        hard_stop_after = self.hard_stop_after

        localstatsport = self.localstatsport

        localstats_refreshtime = self.localstats_refreshtime

        localstats_sticktable_refreshtime = self.localstats_sticktable_refreshtime

        remotesyslog = self.remotesyslog

        logfacility = self.logfacility

        loglevel = self.loglevel

        log_send_hostname = self.log_send_hostname

        carpdev = self.carpdev

        sslcompatibilitymode = self.sslcompatibilitymode

        ssldefaultdhparam = self.ssldefaultdhparam

        email_level = self.email_level

        email_myhostname = self.email_myhostname

        email_from = self.email_from

        email_to = self.email_to

        resolver_retries = self.resolver_retries

        resolver_timeoutretry = self.resolver_timeoutretry

        resolver_holdvalid = self.resolver_holdvalid

        advanced = self.advanced

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if terminate_on_reload is not UNSET:
            field_dict["terminate_on_reload"] = terminate_on_reload
        if enablesync is not UNSET:
            field_dict["enablesync"] = enablesync
        if maxconn is not UNSET:
            field_dict["maxconn"] = maxconn
        if nbthread is not UNSET:
            field_dict["nbthread"] = nbthread
        if hard_stop_after is not UNSET:
            field_dict["hard_stop_after"] = hard_stop_after
        if localstatsport is not UNSET:
            field_dict["localstatsport"] = localstatsport
        if localstats_refreshtime is not UNSET:
            field_dict["localstats_refreshtime"] = localstats_refreshtime
        if localstats_sticktable_refreshtime is not UNSET:
            field_dict["localstats_sticktable_refreshtime"] = localstats_sticktable_refreshtime
        if remotesyslog is not UNSET:
            field_dict["remotesyslog"] = remotesyslog
        if logfacility is not UNSET:
            field_dict["logfacility"] = logfacility
        if loglevel is not UNSET:
            field_dict["loglevel"] = loglevel
        if log_send_hostname is not UNSET:
            field_dict["log_send_hostname"] = log_send_hostname
        if carpdev is not UNSET:
            field_dict["carpdev"] = carpdev
        if sslcompatibilitymode is not UNSET:
            field_dict["sslcompatibilitymode"] = sslcompatibilitymode
        if ssldefaultdhparam is not UNSET:
            field_dict["ssldefaultdhparam"] = ssldefaultdhparam
        if email_level is not UNSET:
            field_dict["email_level"] = email_level
        if email_myhostname is not UNSET:
            field_dict["email_myhostname"] = email_myhostname
        if email_from is not UNSET:
            field_dict["email_from"] = email_from
        if email_to is not UNSET:
            field_dict["email_to"] = email_to
        if resolver_retries is not UNSET:
            field_dict["resolver_retries"] = resolver_retries
        if resolver_timeoutretry is not UNSET:
            field_dict["resolver_timeoutretry"] = resolver_timeoutretry
        if resolver_holdvalid is not UNSET:
            field_dict["resolver_holdvalid"] = resolver_holdvalid
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        terminate_on_reload = d.pop("terminate_on_reload", UNSET)

        enablesync = d.pop("enablesync", UNSET)

        maxconn = d.pop("maxconn", UNSET)

        nbthread = d.pop("nbthread", UNSET)

        hard_stop_after = d.pop("hard_stop_after", UNSET)

        localstatsport = d.pop("localstatsport", UNSET)

        localstats_refreshtime = d.pop("localstats_refreshtime", UNSET)

        localstats_sticktable_refreshtime = d.pop("localstats_sticktable_refreshtime", UNSET)

        remotesyslog = d.pop("remotesyslog", UNSET)

        logfacility = d.pop("logfacility", UNSET)

        loglevel = d.pop("loglevel", UNSET)

        log_send_hostname = d.pop("log_send_hostname", UNSET)

        carpdev = d.pop("carpdev", UNSET)

        sslcompatibilitymode = d.pop("sslcompatibilitymode", UNSET)

        ssldefaultdhparam = d.pop("ssldefaultdhparam", UNSET)

        email_level = d.pop("email_level", UNSET)

        email_myhostname = d.pop("email_myhostname", UNSET)

        email_from = d.pop("email_from", UNSET)

        email_to = d.pop("email_to", UNSET)

        resolver_retries = d.pop("resolver_retries", UNSET)

        resolver_timeoutretry = d.pop("resolver_timeoutretry", UNSET)

        resolver_holdvalid = d.pop("resolver_holdvalid", UNSET)

        advanced = d.pop("advanced", UNSET)

        version = d.pop("version", UNSET)

        haproxy_global = cls(
            enable=enable,
            terminate_on_reload=terminate_on_reload,
            enablesync=enablesync,
            maxconn=maxconn,
            nbthread=nbthread,
            hard_stop_after=hard_stop_after,
            localstatsport=localstatsport,
            localstats_refreshtime=localstats_refreshtime,
            localstats_sticktable_refreshtime=localstats_sticktable_refreshtime,
            remotesyslog=remotesyslog,
            logfacility=logfacility,
            loglevel=loglevel,
            log_send_hostname=log_send_hostname,
            carpdev=carpdev,
            sslcompatibilitymode=sslcompatibilitymode,
            ssldefaultdhparam=ssldefaultdhparam,
            email_level=email_level,
            email_myhostname=email_myhostname,
            email_from=email_from,
            email_to=email_to,
            resolver_retries=resolver_retries,
            resolver_timeoutretry=resolver_timeoutretry,
            resolver_holdvalid=resolver_holdvalid,
            advanced=advanced,
            version=version,
        )

        haproxy_global.additional_properties = d
        return haproxy_global

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
