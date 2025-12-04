from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_resolver_config import DNSResolverConfig


T = TypeVar("T", bound="DNSResolverUpdateReq")


@_attrs_define
class DNSResolverUpdateReq:
    """
    Attributes:
        config (DNSResolverConfig | Unset):
    """

    config: DNSResolverConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_resolver_config import DNSResolverConfig

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: DNSResolverConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = DNSResolverConfig.from_dict(_config)

        dns_resolver_update_req = cls(
            config=config,
        )

        dns_resolver_update_req.additional_properties = d
        return dns_resolver_update_req

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
