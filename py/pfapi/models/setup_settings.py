from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.setup_dns_setting import SetupDNSSetting


T = TypeVar("T", bound="SetupSettings")


@_attrs_define
class SetupSettings:
    """
    Attributes:
        hostname (Union[Unset, str]):
        domain (Union[Unset, str]):
        timezone (Union[Unset, int]):
        timeservers (Union[Unset, str]):
        disablefwd (Union[Unset, bool]):
        dnsoveride (Union[Unset, bool]):
        lang (Union[Unset, str]):
        logincolor (Union[Unset, str]):
        fixednav (Union[Unset, bool]):
        showhost (Union[Unset, bool]):
        dark (Union[Unset, bool]):
        loginmsg (Union[Unset, str]):
        dnsservers (Union[Unset, List['SetupDNSSetting']]):
    """

    hostname: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    timezone: Union[Unset, int] = UNSET
    timeservers: Union[Unset, str] = UNSET
    disablefwd: Union[Unset, bool] = UNSET
    dnsoveride: Union[Unset, bool] = UNSET
    lang: Union[Unset, str] = UNSET
    logincolor: Union[Unset, str] = UNSET
    fixednav: Union[Unset, bool] = UNSET
    showhost: Union[Unset, bool] = UNSET
    dark: Union[Unset, bool] = UNSET
    loginmsg: Union[Unset, str] = UNSET
    dnsservers: Union[Unset, List["SetupDNSSetting"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostname = self.hostname

        domain = self.domain

        timezone = self.timezone

        timeservers = self.timeservers

        disablefwd = self.disablefwd

        dnsoveride = self.dnsoveride

        lang = self.lang

        logincolor = self.logincolor

        fixednav = self.fixednav

        showhost = self.showhost

        dark = self.dark

        loginmsg = self.loginmsg

        dnsservers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dnsservers, Unset):
            dnsservers = []
            for dnsservers_item_data in self.dnsservers:
                dnsservers_item = dnsservers_item_data.to_dict()
                dnsservers.append(dnsservers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if domain is not UNSET:
            field_dict["domain"] = domain
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if timeservers is not UNSET:
            field_dict["timeservers"] = timeservers
        if disablefwd is not UNSET:
            field_dict["disablefwd"] = disablefwd
        if dnsoveride is not UNSET:
            field_dict["dnsoveride"] = dnsoveride
        if lang is not UNSET:
            field_dict["lang"] = lang
        if logincolor is not UNSET:
            field_dict["logincolor"] = logincolor
        if fixednav is not UNSET:
            field_dict["fixednav"] = fixednav
        if showhost is not UNSET:
            field_dict["showhost"] = showhost
        if dark is not UNSET:
            field_dict["dark"] = dark
        if loginmsg is not UNSET:
            field_dict["loginmsg"] = loginmsg
        if dnsservers is not UNSET:
            field_dict["dnsservers"] = dnsservers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.setup_dns_setting import SetupDNSSetting

        d = src_dict.copy()
        hostname = d.pop("hostname", UNSET)

        domain = d.pop("domain", UNSET)

        timezone = d.pop("timezone", UNSET)

        timeservers = d.pop("timeservers", UNSET)

        disablefwd = d.pop("disablefwd", UNSET)

        dnsoveride = d.pop("dnsoveride", UNSET)

        lang = d.pop("lang", UNSET)

        logincolor = d.pop("logincolor", UNSET)

        fixednav = d.pop("fixednav", UNSET)

        showhost = d.pop("showhost", UNSET)

        dark = d.pop("dark", UNSET)

        loginmsg = d.pop("loginmsg", UNSET)

        dnsservers = []
        _dnsservers = d.pop("dnsservers", UNSET)
        for dnsservers_item_data in _dnsservers or []:
            dnsservers_item = SetupDNSSetting.from_dict(dnsservers_item_data)

            dnsservers.append(dnsservers_item)

        setup_settings = cls(
            hostname=hostname,
            domain=domain,
            timezone=timezone,
            timeservers=timeservers,
            disablefwd=disablefwd,
            dnsoveride=dnsoveride,
            lang=lang,
            logincolor=logincolor,
            fixednav=fixednav,
            showhost=showhost,
            dark=dark,
            loginmsg=loginmsg,
            dnsservers=dnsservers,
        )

        setup_settings.additional_properties = d
        return setup_settings

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
