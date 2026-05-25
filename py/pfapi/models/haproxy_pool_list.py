from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.haproxy_pool import HaproxyPool
    from ..models.text_value import TextValue


T = TypeVar("T", bound="HaproxyPoolList")


@_attrs_define
class HaproxyPoolList:
    """
    Attributes:
        pools (list[HaproxyPool] | Unset):
        transparent_interface_options (list[TextValue] | Unset):
        ssl_server_ca_options (list[TextValue] | Unset):
        ssl_server_crl_options (list[TextValue] | Unset):
        ssl_server_clientcert_options (list[TextValue] | Unset):
    """

    pools: list[HaproxyPool] | Unset = UNSET
    transparent_interface_options: list[TextValue] | Unset = UNSET
    ssl_server_ca_options: list[TextValue] | Unset = UNSET
    ssl_server_crl_options: list[TextValue] | Unset = UNSET
    ssl_server_clientcert_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pools, Unset):
            pools = []
            for pools_item_data in self.pools:
                pools_item = pools_item_data.to_dict()
                pools.append(pools_item)

        transparent_interface_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transparent_interface_options, Unset):
            transparent_interface_options = []
            for transparent_interface_options_item_data in self.transparent_interface_options:
                transparent_interface_options_item = transparent_interface_options_item_data.to_dict()
                transparent_interface_options.append(transparent_interface_options_item)

        ssl_server_ca_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssl_server_ca_options, Unset):
            ssl_server_ca_options = []
            for ssl_server_ca_options_item_data in self.ssl_server_ca_options:
                ssl_server_ca_options_item = ssl_server_ca_options_item_data.to_dict()
                ssl_server_ca_options.append(ssl_server_ca_options_item)

        ssl_server_crl_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssl_server_crl_options, Unset):
            ssl_server_crl_options = []
            for ssl_server_crl_options_item_data in self.ssl_server_crl_options:
                ssl_server_crl_options_item = ssl_server_crl_options_item_data.to_dict()
                ssl_server_crl_options.append(ssl_server_crl_options_item)

        ssl_server_clientcert_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssl_server_clientcert_options, Unset):
            ssl_server_clientcert_options = []
            for ssl_server_clientcert_options_item_data in self.ssl_server_clientcert_options:
                ssl_server_clientcert_options_item = ssl_server_clientcert_options_item_data.to_dict()
                ssl_server_clientcert_options.append(ssl_server_clientcert_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pools is not UNSET:
            field_dict["pools"] = pools
        if transparent_interface_options is not UNSET:
            field_dict["transparent_interface_options"] = transparent_interface_options
        if ssl_server_ca_options is not UNSET:
            field_dict["ssl_server_ca_options"] = ssl_server_ca_options
        if ssl_server_crl_options is not UNSET:
            field_dict["ssl_server_crl_options"] = ssl_server_crl_options
        if ssl_server_clientcert_options is not UNSET:
            field_dict["ssl_server_clientcert_options"] = ssl_server_clientcert_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.haproxy_pool import HaproxyPool
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _pools = d.pop("pools", UNSET)
        pools: list[HaproxyPool] | Unset = UNSET
        if _pools is not UNSET:
            pools = []
            for pools_item_data in _pools:
                pools_item = HaproxyPool.from_dict(pools_item_data)

                pools.append(pools_item)

        _transparent_interface_options = d.pop("transparent_interface_options", UNSET)
        transparent_interface_options: list[TextValue] | Unset = UNSET
        if _transparent_interface_options is not UNSET:
            transparent_interface_options = []
            for transparent_interface_options_item_data in _transparent_interface_options:
                transparent_interface_options_item = TextValue.from_dict(transparent_interface_options_item_data)

                transparent_interface_options.append(transparent_interface_options_item)

        _ssl_server_ca_options = d.pop("ssl_server_ca_options", UNSET)
        ssl_server_ca_options: list[TextValue] | Unset = UNSET
        if _ssl_server_ca_options is not UNSET:
            ssl_server_ca_options = []
            for ssl_server_ca_options_item_data in _ssl_server_ca_options:
                ssl_server_ca_options_item = TextValue.from_dict(ssl_server_ca_options_item_data)

                ssl_server_ca_options.append(ssl_server_ca_options_item)

        _ssl_server_crl_options = d.pop("ssl_server_crl_options", UNSET)
        ssl_server_crl_options: list[TextValue] | Unset = UNSET
        if _ssl_server_crl_options is not UNSET:
            ssl_server_crl_options = []
            for ssl_server_crl_options_item_data in _ssl_server_crl_options:
                ssl_server_crl_options_item = TextValue.from_dict(ssl_server_crl_options_item_data)

                ssl_server_crl_options.append(ssl_server_crl_options_item)

        _ssl_server_clientcert_options = d.pop("ssl_server_clientcert_options", UNSET)
        ssl_server_clientcert_options: list[TextValue] | Unset = UNSET
        if _ssl_server_clientcert_options is not UNSET:
            ssl_server_clientcert_options = []
            for ssl_server_clientcert_options_item_data in _ssl_server_clientcert_options:
                ssl_server_clientcert_options_item = TextValue.from_dict(ssl_server_clientcert_options_item_data)

                ssl_server_clientcert_options.append(ssl_server_clientcert_options_item)

        haproxy_pool_list = cls(
            pools=pools,
            transparent_interface_options=transparent_interface_options,
            ssl_server_ca_options=ssl_server_ca_options,
            ssl_server_crl_options=ssl_server_crl_options,
            ssl_server_clientcert_options=ssl_server_clientcert_options,
        )

        haproxy_pool_list.additional_properties = d
        return haproxy_pool_list

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
