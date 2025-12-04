from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        domain (str | Unset):
        dnsservers (list[SetupDNSSetting] | Unset):
        dnsoveride (bool | Unset):
        dnsresolution (str | Unset): DNS resolution behavior, options - not-specified (default), local, remote
        timezone (str | Unset):
        timeservers (str | Unset): space separated list of time servers
        lang (str | Unset):
        login_message (str | Unset): message to display when user authenticates
        ui_req_state_filter (bool | Unset): require state filter in diagnostics-states
    """

    hostname: str
    domain: str | Unset = UNSET
    dnsservers: list[SetupDNSSetting] | Unset = UNSET
    dnsoveride: bool | Unset = UNSET
    dnsresolution: str | Unset = UNSET
    timezone: str | Unset = UNSET
    timeservers: str | Unset = UNSET
    lang: str | Unset = UNSET
    login_message: str | Unset = UNSET
    ui_req_state_filter: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        domain = self.domain

        dnsservers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dnsservers, Unset):
            dnsservers = []
            for dnsservers_item_data in self.dnsservers:
                dnsservers_item = dnsservers_item_data.to_dict()
                dnsservers.append(dnsservers_item)

        dnsoveride = self.dnsoveride

        dnsresolution = self.dnsresolution

        timezone = self.timezone

        timeservers = self.timeservers

        lang = self.lang

        login_message = self.login_message

        ui_req_state_filter = self.ui_req_state_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if dnsservers is not UNSET:
            field_dict["dnsservers"] = dnsservers
        if dnsoveride is not UNSET:
            field_dict["dnsoveride"] = dnsoveride
        if dnsresolution is not UNSET:
            field_dict["dnsresolution"] = dnsresolution
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if timeservers is not UNSET:
            field_dict["timeservers"] = timeservers
        if lang is not UNSET:
            field_dict["lang"] = lang
        if login_message is not UNSET:
            field_dict["login_message"] = login_message
        if ui_req_state_filter is not UNSET:
            field_dict["ui_req_state_filter"] = ui_req_state_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.setup_dns_setting import SetupDNSSetting

        d = dict(src_dict)
        hostname = d.pop("hostname")

        domain = d.pop("domain", UNSET)

        _dnsservers = d.pop("dnsservers", UNSET)
        dnsservers: list[SetupDNSSetting] | Unset = UNSET
        if _dnsservers is not UNSET:
            dnsservers = []
            for dnsservers_item_data in _dnsservers:
                dnsservers_item = SetupDNSSetting.from_dict(dnsservers_item_data)

                dnsservers.append(dnsservers_item)

        dnsoveride = d.pop("dnsoveride", UNSET)

        dnsresolution = d.pop("dnsresolution", UNSET)

        timezone = d.pop("timezone", UNSET)

        timeservers = d.pop("timeservers", UNSET)

        lang = d.pop("lang", UNSET)

        login_message = d.pop("login_message", UNSET)

        ui_req_state_filter = d.pop("ui_req_state_filter", UNSET)

        setup_settings = cls(
            hostname=hostname,
            domain=domain,
            dnsservers=dnsservers,
            dnsoveride=dnsoveride,
            dnsresolution=dnsresolution,
            timezone=timezone,
            timeservers=timeservers,
            lang=lang,
            login_message=login_message,
            ui_req_state_filter=ui_req_state_filter,
        )

        setup_settings.additional_properties = d
        return setup_settings

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
