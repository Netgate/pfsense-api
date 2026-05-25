from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_blocked_host import SnortBlockedHost


T = TypeVar("T", bound="SnortBlockedHosts")


@_attrs_define
class SnortBlockedHosts:
    """
    Attributes:
        hosts (list[SnortBlockedHost] | Unset):
    """

    hosts: list[SnortBlockedHost] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hosts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = []
            for hosts_item_data in self.hosts:
                hosts_item = hosts_item_data.to_dict()
                hosts.append(hosts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hosts is not UNSET:
            field_dict["hosts"] = hosts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_blocked_host import SnortBlockedHost

        d = dict(src_dict)
        _hosts = d.pop("hosts", UNSET)
        hosts: list[SnortBlockedHost] | Unset = UNSET
        if _hosts is not UNSET:
            hosts = []
            for hosts_item_data in _hosts:
                hosts_item = SnortBlockedHost.from_dict(hosts_item_data)

                hosts.append(hosts_item)

        snort_blocked_hosts = cls(
            hosts=hosts,
        )

        snort_blocked_hosts.additional_properties = d
        return snort_blocked_hosts

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
