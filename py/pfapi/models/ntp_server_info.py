from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NtpServerInfo")


@_attrs_define
class NtpServerInfo:
    """
    Attributes:
        status (str | Unset):
        server (str | Unset):
        refid (str | Unset):
        stratum (str | Unset):
        type_ (str | Unset):
        when (str | Unset):
        poll (str | Unset):
        reach (str | Unset):
        delay (str | Unset):
        offset (str | Unset):
        jitter (str | Unset):
    """

    status: str | Unset = UNSET
    server: str | Unset = UNSET
    refid: str | Unset = UNSET
    stratum: str | Unset = UNSET
    type_: str | Unset = UNSET
    when: str | Unset = UNSET
    poll: str | Unset = UNSET
    reach: str | Unset = UNSET
    delay: str | Unset = UNSET
    offset: str | Unset = UNSET
    jitter: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        server = self.server

        refid = self.refid

        stratum = self.stratum

        type_ = self.type_

        when = self.when

        poll = self.poll

        reach = self.reach

        delay = self.delay

        offset = self.offset

        jitter = self.jitter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if server is not UNSET:
            field_dict["server"] = server
        if refid is not UNSET:
            field_dict["refid"] = refid
        if stratum is not UNSET:
            field_dict["stratum"] = stratum
        if type_ is not UNSET:
            field_dict["type"] = type_
        if when is not UNSET:
            field_dict["when"] = when
        if poll is not UNSET:
            field_dict["poll"] = poll
        if reach is not UNSET:
            field_dict["reach"] = reach
        if delay is not UNSET:
            field_dict["delay"] = delay
        if offset is not UNSET:
            field_dict["offset"] = offset
        if jitter is not UNSET:
            field_dict["jitter"] = jitter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        server = d.pop("server", UNSET)

        refid = d.pop("refid", UNSET)

        stratum = d.pop("stratum", UNSET)

        type_ = d.pop("type", UNSET)

        when = d.pop("when", UNSET)

        poll = d.pop("poll", UNSET)

        reach = d.pop("reach", UNSET)

        delay = d.pop("delay", UNSET)

        offset = d.pop("offset", UNSET)

        jitter = d.pop("jitter", UNSET)

        ntp_server_info = cls(
            status=status,
            server=server,
            refid=refid,
            stratum=stratum,
            type_=type_,
            when=when,
            poll=poll,
            reach=reach,
            delay=delay,
            offset=offset,
            jitter=jitter,
        )

        ntp_server_info.additional_properties = d
        return ntp_server_info

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
