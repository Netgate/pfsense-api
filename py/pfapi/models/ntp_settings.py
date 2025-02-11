from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        ntpmaxpeers (str):
        orphan (str):
        ntpminpoll (str): Empty for default, "omit" or number ranged from 3 to 17 based on pfsense specific approach
        ntpmaxpoll (str): Empty for default, "omit" or number ranged from 3 to 17 based on pfsense specific approach
        statsgraph (bool):
        logpeer (bool):
        logsys (bool):
        log_stats (LogStats):
        leapsec (str):
        dnsresolv (str): auto | inet | inet6
        serverauth (bool):
        serverauthkey (str):
        serverauthalgo (str): md5 (length 1 to 20) | sha1 (length 40) | sha256 (length 64)
        interfaces (Union[Unset, List[str]]):
        servers (Union[Unset, List['NtpServer']]):
    """

    enable: bool
    ntpmaxpeers: str
    orphan: str
    ntpminpoll: str
    ntpmaxpoll: str
    statsgraph: bool
    logpeer: bool
    logsys: bool
    log_stats: "LogStats"
    leapsec: str
    dnsresolv: str
    serverauth: bool
    serverauthkey: str
    serverauthalgo: str
    interfaces: Union[Unset, List[str]] = UNSET
    servers: Union[Unset, List["NtpServer"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        ntpmaxpeers = self.ntpmaxpeers

        orphan = self.orphan

        ntpminpoll = self.ntpminpoll

        ntpmaxpoll = self.ntpmaxpoll

        statsgraph = self.statsgraph

        logpeer = self.logpeer

        logsys = self.logsys

        log_stats = self.log_stats.to_dict()

        leapsec = self.leapsec

        dnsresolv = self.dnsresolv

        serverauth = self.serverauth

        serverauthkey = self.serverauthkey

        serverauthalgo = self.serverauthalgo

        interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        servers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "ntpmaxpeers": ntpmaxpeers,
                "orphan": orphan,
                "ntpminpoll": ntpminpoll,
                "ntpmaxpoll": ntpmaxpoll,
                "statsgraph": statsgraph,
                "logpeer": logpeer,
                "logsys": logsys,
                "log_stats": log_stats,
                "leapsec": leapsec,
                "dnsresolv": dnsresolv,
                "serverauth": serverauth,
                "serverauthkey": serverauthkey,
                "serverauthalgo": serverauthalgo,
            }
        )
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.log_stats import LogStats
        from ..models.ntp_server import NtpServer

        d = src_dict.copy()
        enable = d.pop("enable")

        ntpmaxpeers = d.pop("ntpmaxpeers")

        orphan = d.pop("orphan")

        ntpminpoll = d.pop("ntpminpoll")

        ntpmaxpoll = d.pop("ntpmaxpoll")

        statsgraph = d.pop("statsgraph")

        logpeer = d.pop("logpeer")

        logsys = d.pop("logsys")

        log_stats = LogStats.from_dict(d.pop("log_stats"))

        leapsec = d.pop("leapsec")

        dnsresolv = d.pop("dnsresolv")

        serverauth = d.pop("serverauth")

        serverauthkey = d.pop("serverauthkey")

        serverauthalgo = d.pop("serverauthalgo")

        interfaces = cast(List[str], d.pop("interfaces", UNSET))

        servers = []
        _servers = d.pop("servers", UNSET)
        for servers_item_data in _servers or []:
            servers_item = NtpServer.from_dict(servers_item_data)

            servers.append(servers_item)

        ntp_settings = cls(
            enable=enable,
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
            interfaces=interfaces,
            servers=servers,
        )

        ntp_settings.additional_properties = d
        return ntp_settings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
