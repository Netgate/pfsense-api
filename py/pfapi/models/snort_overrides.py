from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortOverrides")


@_attrs_define
class SnortOverrides:
    """Snort configuration variables that can be overridden

    Attributes:
        dns_servers (list[str] | Unset):
        ftp_servers (list[str] | Unset):
        http_servers (list[str] | Unset):
        sip_servers (list[str] | Unset):
        smtp_servers (list[str] | Unset):
        imap_servers (list[str] | Unset):
        sql_servers (list[str] | Unset):
        ssh_servers (list[str] | Unset):
        telnet_servers (list[str] | Unset):
    """

    dns_servers: list[str] | Unset = UNSET
    ftp_servers: list[str] | Unset = UNSET
    http_servers: list[str] | Unset = UNSET
    sip_servers: list[str] | Unset = UNSET
    smtp_servers: list[str] | Unset = UNSET
    imap_servers: list[str] | Unset = UNSET
    sql_servers: list[str] | Unset = UNSET
    ssh_servers: list[str] | Unset = UNSET
    telnet_servers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dns_servers: list[str] | Unset = UNSET
        if not isinstance(self.dns_servers, Unset):
            dns_servers = self.dns_servers

        ftp_servers: list[str] | Unset = UNSET
        if not isinstance(self.ftp_servers, Unset):
            ftp_servers = self.ftp_servers

        http_servers: list[str] | Unset = UNSET
        if not isinstance(self.http_servers, Unset):
            http_servers = self.http_servers

        sip_servers: list[str] | Unset = UNSET
        if not isinstance(self.sip_servers, Unset):
            sip_servers = self.sip_servers

        smtp_servers: list[str] | Unset = UNSET
        if not isinstance(self.smtp_servers, Unset):
            smtp_servers = self.smtp_servers

        imap_servers: list[str] | Unset = UNSET
        if not isinstance(self.imap_servers, Unset):
            imap_servers = self.imap_servers

        sql_servers: list[str] | Unset = UNSET
        if not isinstance(self.sql_servers, Unset):
            sql_servers = self.sql_servers

        ssh_servers: list[str] | Unset = UNSET
        if not isinstance(self.ssh_servers, Unset):
            ssh_servers = self.ssh_servers

        telnet_servers: list[str] | Unset = UNSET
        if not isinstance(self.telnet_servers, Unset):
            telnet_servers = self.telnet_servers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dns_servers is not UNSET:
            field_dict["dns_servers"] = dns_servers
        if ftp_servers is not UNSET:
            field_dict["ftp_servers"] = ftp_servers
        if http_servers is not UNSET:
            field_dict["http_servers"] = http_servers
        if sip_servers is not UNSET:
            field_dict["sip_servers"] = sip_servers
        if smtp_servers is not UNSET:
            field_dict["smtp_servers"] = smtp_servers
        if imap_servers is not UNSET:
            field_dict["imap_servers"] = imap_servers
        if sql_servers is not UNSET:
            field_dict["sql_servers"] = sql_servers
        if ssh_servers is not UNSET:
            field_dict["ssh_servers"] = ssh_servers
        if telnet_servers is not UNSET:
            field_dict["telnet_servers"] = telnet_servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dns_servers = cast(list[str], d.pop("dns_servers", UNSET))

        ftp_servers = cast(list[str], d.pop("ftp_servers", UNSET))

        http_servers = cast(list[str], d.pop("http_servers", UNSET))

        sip_servers = cast(list[str], d.pop("sip_servers", UNSET))

        smtp_servers = cast(list[str], d.pop("smtp_servers", UNSET))

        imap_servers = cast(list[str], d.pop("imap_servers", UNSET))

        sql_servers = cast(list[str], d.pop("sql_servers", UNSET))

        ssh_servers = cast(list[str], d.pop("ssh_servers", UNSET))

        telnet_servers = cast(list[str], d.pop("telnet_servers", UNSET))

        snort_overrides = cls(
            dns_servers=dns_servers,
            ftp_servers=ftp_servers,
            http_servers=http_servers,
            sip_servers=sip_servers,
            smtp_servers=smtp_servers,
            imap_servers=imap_servers,
            sql_servers=sql_servers,
            ssh_servers=ssh_servers,
            telnet_servers=telnet_servers,
        )

        snort_overrides.additional_properties = d
        return snort_overrides

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
