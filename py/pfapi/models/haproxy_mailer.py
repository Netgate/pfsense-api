from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyMailer")


@_attrs_define
class HaproxyMailer:
    """
    Attributes:
        name (str | Unset): Mailer Name

            Unique name for this mailer entry.
        mailserver (str | Unset): Mail Server

            Hostname or IP address of the SMTP server.
        mailserverport (str | Unset): Mail Server Port

            TCP port of the SMTP server.
            (Default: 25)
        id (str | Unset): (readonly) ID assigned to this entry
    """

    name: str | Unset = UNSET
    mailserver: str | Unset = UNSET
    mailserverport: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mailserver = self.mailserver

        mailserverport = self.mailserverport

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mailserver is not UNSET:
            field_dict["mailserver"] = mailserver
        if mailserverport is not UNSET:
            field_dict["mailserverport"] = mailserverport
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mailserver = d.pop("mailserver", UNSET)

        mailserverport = d.pop("mailserverport", UNSET)

        id = d.pop("id", UNSET)

        haproxy_mailer = cls(
            name=name,
            mailserver=mailserver,
            mailserverport=mailserverport,
            id=id,
        )

        haproxy_mailer.additional_properties = d
        return haproxy_mailer

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
