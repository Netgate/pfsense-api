from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_stats import LogStats
    from ..models.ntp_server import NtpServer


T = TypeVar("T", bound="NtpSettings")


@_attrs_define
class NtpSettings:
    """
    Attributes:
        enable (bool):
        interfaces (list[str] | Unset):
        servers (list[NtpServer] | Unset):
        ntpmaxpeers (str | Unset):
        orphan (str | Unset):
        ntpminpoll (str | Unset): Empty for default, "omit" or number ranged from 3 to 17 based on pfsense specific
            approach
        ntpmaxpoll (str | Unset): Empty for default, "omit" or number ranged from 3 to 17 based on pfsense specific
            approach
        statsgraph (bool | Unset):
        logpeer (bool | Unset):
        logsys (bool | Unset):
        log_stats (LogStats | Unset):
        leapsec (str | Unset):
        dnsresolv (str | Unset): auto | inet | inet6
        serverauth (bool | Unset):
        serverauthkey (str | Unset):
        serverauthalgo (str | Unset): md5 (length 1 to 20) | sha1 (length 40) | sha256 (length 64)
    """

    enable: bool
    interfaces: list[str] | Unset = UNSET
    servers: list[NtpServer] | Unset = UNSET
    ntpmaxpeers: str | Unset = UNSET
    orphan: str | Unset = UNSET
    ntpminpoll: str | Unset = UNSET
    ntpmaxpoll: str | Unset = UNSET
    statsgraph: bool | Unset = UNSET
    logpeer: bool | Unset = UNSET
    logsys: bool | Unset = UNSET
    log_stats: LogStats | Unset = UNSET
    leapsec: str | Unset = UNSET
    dnsresolv: str | Unset = UNSET
    serverauth: bool | Unset = UNSET
    serverauthkey: str | Unset = UNSET
    serverauthalgo: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        interfaces: list[str] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        ntpmaxpeers = self.ntpmaxpeers

        orphan = self.orphan

        ntpminpoll = self.ntpminpoll

        ntpmaxpoll = self.ntpmaxpoll

        statsgraph = self.statsgraph

        logpeer = self.logpeer

        logsys = self.logsys

        log_stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log_stats, Unset):
            log_stats = self.log_stats.to_dict()

        leapsec = self.leapsec

        dnsresolv = self.dnsresolv

        serverauth = self.serverauth

        serverauthkey = self.serverauthkey

        serverauthalgo = self.serverauthalgo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if servers is not UNSET:
            field_dict["servers"] = servers
        if ntpmaxpeers is not UNSET:
            field_dict["ntpmaxpeers"] = ntpmaxpeers
        if orphan is not UNSET:
            field_dict["orphan"] = orphan
        if ntpminpoll is not UNSET:
            field_dict["ntpminpoll"] = ntpminpoll
        if ntpmaxpoll is not UNSET:
            field_dict["ntpmaxpoll"] = ntpmaxpoll
        if statsgraph is not UNSET:
            field_dict["statsgraph"] = statsgraph
        if logpeer is not UNSET:
            field_dict["logpeer"] = logpeer
        if logsys is not UNSET:
            field_dict["logsys"] = logsys
        if log_stats is not UNSET:
            field_dict["log_stats"] = log_stats
        if leapsec is not UNSET:
            field_dict["leapsec"] = leapsec
        if dnsresolv is not UNSET:
            field_dict["dnsresolv"] = dnsresolv
        if serverauth is not UNSET:
            field_dict["serverauth"] = serverauth
        if serverauthkey is not UNSET:
            field_dict["serverauthkey"] = serverauthkey
        if serverauthalgo is not UNSET:
            field_dict["serverauthalgo"] = serverauthalgo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_stats import LogStats
        from ..models.ntp_server import NtpServer

        d = dict(src_dict)
        enable = d.pop("enable")

        interfaces = cast(list[str], d.pop("interfaces", UNSET))

        _servers = d.pop("servers", UNSET)
        servers: list[NtpServer] | Unset = UNSET
        if _servers is not UNSET:
            servers = []
            for servers_item_data in _servers:
                servers_item = NtpServer.from_dict(servers_item_data)

                servers.append(servers_item)

        ntpmaxpeers = d.pop("ntpmaxpeers", UNSET)

        orphan = d.pop("orphan", UNSET)

        ntpminpoll = d.pop("ntpminpoll", UNSET)

        ntpmaxpoll = d.pop("ntpmaxpoll", UNSET)

        statsgraph = d.pop("statsgraph", UNSET)

        logpeer = d.pop("logpeer", UNSET)

        logsys = d.pop("logsys", UNSET)

        _log_stats = d.pop("log_stats", UNSET)
        log_stats: LogStats | Unset
        if isinstance(_log_stats, Unset):
            log_stats = UNSET
        else:
            log_stats = LogStats.from_dict(_log_stats)

        leapsec = d.pop("leapsec", UNSET)

        dnsresolv = d.pop("dnsresolv", UNSET)

        serverauth = d.pop("serverauth", UNSET)

        serverauthkey = d.pop("serverauthkey", UNSET)

        serverauthalgo = d.pop("serverauthalgo", UNSET)

        ntp_settings = cls(
            enable=enable,
            interfaces=interfaces,
            servers=servers,
            ntpmaxpeers=ntpmaxpeers,
            orphan=orphan,
            ntpminpoll=ntpminpoll,
            ntpmaxpoll=ntpmaxpoll,
            statsgraph=statsgraph,
            logpeer=logpeer,
            logsys=logsys,
            log_stats=log_stats,
            leapsec=leapsec,
            dnsresolv=dnsresolv,
            serverauth=serverauth,
            serverauthkey=serverauthkey,
            serverauthalgo=serverauthalgo,
        )

        ntp_settings.additional_properties = d
        return ntp_settings

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
