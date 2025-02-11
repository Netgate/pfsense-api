from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpRelayConfig")


@_attrs_define
class DhcpRelayConfig:
    """
    Attributes:
        enable (bool):
        carp_status_vip (str):
        append_circuit_agent_ids (bool):
        interfaces (Union[Unset, List[str]]):
        upstream_servers (Union[Unset, List[str]]):
    """

    enable: bool
    carp_status_vip: str
    append_circuit_agent_ids: bool
    interfaces: Union[Unset, List[str]] = UNSET
    upstream_servers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        carp_status_vip = self.carp_status_vip

        append_circuit_agent_ids = self.append_circuit_agent_ids

        interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        upstream_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.upstream_servers, Unset):
            upstream_servers = self.upstream_servers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "carp_status_vip": carp_status_vip,
                "append_circuit_agent_ids": append_circuit_agent_ids,
            }
        )
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if upstream_servers is not UNSET:
            field_dict["upstream_servers"] = upstream_servers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable")

        carp_status_vip = d.pop("carp_status_vip")

        append_circuit_agent_ids = d.pop("append_circuit_agent_ids")

        interfaces = cast(List[str], d.pop("interfaces", UNSET))

        upstream_servers = cast(List[str], d.pop("upstream_servers", UNSET))

        dhcp_relay_config = cls(
            enable=enable,
            carp_status_vip=carp_status_vip,
            append_circuit_agent_ids=append_circuit_agent_ids,
            interfaces=interfaces,
            upstream_servers=upstream_servers,
        )

        dhcp_relay_config.additional_properties = d
        return dhcp_relay_config

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
