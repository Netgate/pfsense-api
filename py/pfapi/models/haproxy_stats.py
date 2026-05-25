from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.haproxy_backend_stat import HaproxyBackendStat
    from ..models.haproxy_frontend_stat import HaproxyFrontendStat
    from ..models.haproxy_server_stat import HaproxyServerStat


T = TypeVar("T", bound="HaproxyStats")


@_attrs_define
class HaproxyStats:
    """
    Attributes:
        frontends (list[HaproxyFrontendStat] | Unset):
        backends (list[HaproxyBackendStat] | Unset):
        servers (list[HaproxyServerStat] | Unset):
    """

    frontends: list[HaproxyFrontendStat] | Unset = UNSET
    backends: list[HaproxyBackendStat] | Unset = UNSET
    servers: list[HaproxyServerStat] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frontends: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.frontends, Unset):
            frontends = []
            for frontends_item_data in self.frontends:
                frontends_item = frontends_item_data.to_dict()
                frontends.append(frontends_item)

        backends: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.backends, Unset):
            backends = []
            for backends_item_data in self.backends:
                backends_item = backends_item_data.to_dict()
                backends.append(backends_item)

        servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if frontends is not UNSET:
            field_dict["frontends"] = frontends
        if backends is not UNSET:
            field_dict["backends"] = backends
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.haproxy_backend_stat import HaproxyBackendStat
        from ..models.haproxy_frontend_stat import HaproxyFrontendStat
        from ..models.haproxy_server_stat import HaproxyServerStat

        d = dict(src_dict)
        _frontends = d.pop("frontends", UNSET)
        frontends: list[HaproxyFrontendStat] | Unset = UNSET
        if _frontends is not UNSET:
            frontends = []
            for frontends_item_data in _frontends:
                frontends_item = HaproxyFrontendStat.from_dict(frontends_item_data)

                frontends.append(frontends_item)

        _backends = d.pop("backends", UNSET)
        backends: list[HaproxyBackendStat] | Unset = UNSET
        if _backends is not UNSET:
            backends = []
            for backends_item_data in _backends:
                backends_item = HaproxyBackendStat.from_dict(backends_item_data)

                backends.append(backends_item)

        _servers = d.pop("servers", UNSET)
        servers: list[HaproxyServerStat] | Unset = UNSET
        if _servers is not UNSET:
            servers = []
            for servers_item_data in _servers:
                servers_item = HaproxyServerStat.from_dict(servers_item_data)

                servers.append(servers_item)

        haproxy_stats = cls(
            frontends=frontends,
            backends=backends,
            servers=servers,
        )

        haproxy_stats.additional_properties = d
        return haproxy_stats

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
