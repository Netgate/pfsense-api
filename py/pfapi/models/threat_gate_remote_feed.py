from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.threat_gate_remote_feed_headers import ThreatGateRemoteFeedHeaders


T = TypeVar("T", bound="ThreatGateRemoteFeed")


@_attrs_define
class ThreatGateRemoteFeed:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        enabled (bool | Unset):
        mode (str | Unset): block, alias
        url (str | Unset): Valid url http/https
        headers (ThreatGateRemoteFeedHeaders | Unset):
        suppress_domains (list[str] | Unset):
        suppress_prefixes (list[str] | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    mode: str | Unset = UNSET
    url: str | Unset = UNSET
    headers: ThreatGateRemoteFeedHeaders | Unset = UNSET
    suppress_domains: list[str] | Unset = UNSET
    suppress_prefixes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        enabled = self.enabled

        mode = self.mode

        url = self.url

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        suppress_domains: list[str] | Unset = UNSET
        if not isinstance(self.suppress_domains, Unset):
            suppress_domains = self.suppress_domains

        suppress_prefixes: list[str] | Unset = UNSET
        if not isinstance(self.suppress_prefixes, Unset):
            suppress_prefixes = self.suppress_prefixes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if mode is not UNSET:
            field_dict["mode"] = mode
        if url is not UNSET:
            field_dict["url"] = url
        if headers is not UNSET:
            field_dict["headers"] = headers
        if suppress_domains is not UNSET:
            field_dict["suppressDomains"] = suppress_domains
        if suppress_prefixes is not UNSET:
            field_dict["suppressPrefixes"] = suppress_prefixes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.threat_gate_remote_feed_headers import ThreatGateRemoteFeedHeaders

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        mode = d.pop("mode", UNSET)

        url = d.pop("url", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: ThreatGateRemoteFeedHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = ThreatGateRemoteFeedHeaders.from_dict(_headers)

        suppress_domains = cast(list[str], d.pop("suppressDomains", UNSET))

        suppress_prefixes = cast(list[str], d.pop("suppressPrefixes", UNSET))

        threat_gate_remote_feed = cls(
            id=id,
            name=name,
            enabled=enabled,
            mode=mode,
            url=url,
            headers=headers,
            suppress_domains=suppress_domains,
            suppress_prefixes=suppress_prefixes,
        )

        threat_gate_remote_feed.additional_properties = d
        return threat_gate_remote_feed

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
