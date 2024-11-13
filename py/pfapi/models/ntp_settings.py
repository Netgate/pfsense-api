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
        enable (Union[Unset, bool]):
        interfaces (Union[Unset, List[str]]):
        servers (Union[Unset, List['NtpServer']]):
        ntpmaxpeers (Union[Unset, str]):
        orphan (Union[Unset, str]):
        ntpminpoll (Union[Unset, str]):
        ntpmaxpoll (Union[Unset, str]):
        statsgraph (Union[Unset, bool]):
        logpeer (Union[Unset, bool]):
        logsys (Union[Unset, bool]):
        log_stats (Union[Unset, LogStats]):
        leapsec (Union[Unset, str]):
        dnsresolv (Union[Unset, str]):
        serverauth (Union[Unset, bool]):
        serverauthkey (Union[Unset, str]):
        serverauthalgo (Union[Unset, str]):
    """

    enable: Union[Unset, bool] = UNSET
    interfaces: Union[Unset, List[str]] = UNSET
    servers: Union[Unset, List["NtpServer"]] = UNSET
    ntpmaxpeers: Union[Unset, str] = UNSET
    orphan: Union[Unset, str] = UNSET
    ntpminpoll: Union[Unset, str] = UNSET
    ntpmaxpoll: Union[Unset, str] = UNSET
    statsgraph: Union[Unset, bool] = UNSET
    logpeer: Union[Unset, bool] = UNSET
    logsys: Union[Unset, bool] = UNSET
    log_stats: Union[Unset, "LogStats"] = UNSET
    leapsec: Union[Unset, str] = UNSET
    dnsresolv: Union[Unset, str] = UNSET
    serverauth: Union[Unset, bool] = UNSET
    serverauthkey: Union[Unset, str] = UNSET
    serverauthalgo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        servers: Union[Unset, List[Dict[str, Any]]] = UNSET
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

        log_stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.log_stats, Unset):
            log_stats = self.log_stats.to_dict()

        leapsec = self.leapsec

        dnsresolv = self.dnsresolv

        serverauth = self.serverauth

        serverauthkey = self.serverauthkey

        serverauthalgo = self.serverauthalgo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.log_stats import LogStats
        from ..models.ntp_server import NtpServer

        d = src_dict.copy()
        enable = d.pop("enable", UNSET)

        interfaces = cast(List[str], d.pop("interfaces", UNSET))

        servers = []
        _servers = d.pop("servers", UNSET)
        for servers_item_data in _servers or []:
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
        log_stats: Union[Unset, LogStats]
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
