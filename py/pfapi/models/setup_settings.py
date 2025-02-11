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
        hostname (str):
        domain (str):
        dnsoveride (bool):
        dnsresolution (str): DNS resolution behavior, options - not-specified (default), local, remote
        timezone (str):
        timeservers (str): space separated list of time servers
        lang (str):
        login_message (str): message to display when user authenticates
        dnsservers (Union[Unset, List['SetupDNSSetting']]):
    """

    hostname: str
    domain: str
    dnsoveride: bool
    dnsresolution: str
    timezone: str
    timeservers: str
    lang: str
    login_message: str
    dnsservers: Union[Unset, List["SetupDNSSetting"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostname = self.hostname

        domain = self.domain

        dnsoveride = self.dnsoveride

        dnsresolution = self.dnsresolution

        timezone = self.timezone

        timeservers = self.timeservers

        lang = self.lang

        login_message = self.login_message

        dnsservers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dnsservers, Unset):
            dnsservers = []
            for dnsservers_item_data in self.dnsservers:
                dnsservers_item = dnsservers_item_data.to_dict()
                dnsservers.append(dnsservers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
                "domain": domain,
                "dnsoveride": dnsoveride,
                "dnsresolution": dnsresolution,
                "timezone": timezone,
                "timeservers": timeservers,
                "lang": lang,
                "login_message": login_message,
            }
        )
        if dnsservers is not UNSET:
            field_dict["dnsservers"] = dnsservers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.setup_dns_setting import SetupDNSSetting

        d = src_dict.copy()
        hostname = d.pop("hostname")

        domain = d.pop("domain")

        dnsoveride = d.pop("dnsoveride")

        dnsresolution = d.pop("dnsresolution")

        timezone = d.pop("timezone")

        timeservers = d.pop("timeservers")

        lang = d.pop("lang")

        login_message = d.pop("login_message")

        dnsservers = []
        _dnsservers = d.pop("dnsservers", UNSET)
        for dnsservers_item_data in _dnsservers or []:
            dnsservers_item = SetupDNSSetting.from_dict(dnsservers_item_data)

            dnsservers.append(dnsservers_item)

        setup_settings = cls(
            hostname=hostname,
            domain=domain,
            dnsoveride=dnsoveride,
            dnsresolution=dnsresolution,
            timezone=timezone,
            timeservers=timeservers,
            lang=lang,
            login_message=login_message,
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
