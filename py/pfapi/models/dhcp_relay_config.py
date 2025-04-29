from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_value import TextValue


T = TypeVar("T", bound="DhcpRelayConfig")


@_attrs_define
class DhcpRelayConfig:
    """
    Attributes:
        enable (Union[Unset, bool]):
        interfaces (Union[Unset, List[str]]):
        carp_status_vip (Union[Unset, str]):
        append_circuit_agent_ids (Union[Unset, bool]):
        upstream_servers (Union[Unset, List[str]]):
        carp_status_vip_entries (Union[Unset, List['TextValue']]):
        interfaces_entries (Union[Unset, List['TextValue']]):
    """

    enable: Union[Unset, bool] = UNSET
    interfaces: Union[Unset, List[str]] = UNSET
    carp_status_vip: Union[Unset, str] = UNSET
    append_circuit_agent_ids: Union[Unset, bool] = UNSET
    upstream_servers: Union[Unset, List[str]] = UNSET
    carp_status_vip_entries: Union[Unset, List["TextValue"]] = UNSET
    interfaces_entries: Union[Unset, List["TextValue"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        carp_status_vip = self.carp_status_vip

        append_circuit_agent_ids = self.append_circuit_agent_ids

        upstream_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.upstream_servers, Unset):
            upstream_servers = self.upstream_servers

        carp_status_vip_entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.carp_status_vip_entries, Unset):
            carp_status_vip_entries = []
            for carp_status_vip_entries_item_data in self.carp_status_vip_entries:
                carp_status_vip_entries_item = carp_status_vip_entries_item_data.to_dict()
                carp_status_vip_entries.append(carp_status_vip_entries_item)

        interfaces_entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces_entries, Unset):
            interfaces_entries = []
            for interfaces_entries_item_data in self.interfaces_entries:
                interfaces_entries_item = interfaces_entries_item_data.to_dict()
                interfaces_entries.append(interfaces_entries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if carp_status_vip is not UNSET:
            field_dict["carp_status_vip"] = carp_status_vip
        if append_circuit_agent_ids is not UNSET:
            field_dict["append_circuit_agent_ids"] = append_circuit_agent_ids
        if upstream_servers is not UNSET:
            field_dict["upstream_servers"] = upstream_servers
        if carp_status_vip_entries is not UNSET:
            field_dict["carp_status_vip_entries"] = carp_status_vip_entries
        if interfaces_entries is not UNSET:
            field_dict["interfaces_entries"] = interfaces_entries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_value import TextValue

        d = src_dict.copy()
        enable = d.pop("enable", UNSET)

        interfaces = cast(List[str], d.pop("interfaces", UNSET))

        carp_status_vip = d.pop("carp_status_vip", UNSET)

        append_circuit_agent_ids = d.pop("append_circuit_agent_ids", UNSET)

        upstream_servers = cast(List[str], d.pop("upstream_servers", UNSET))

        carp_status_vip_entries = []
        _carp_status_vip_entries = d.pop("carp_status_vip_entries", UNSET)
        for carp_status_vip_entries_item_data in _carp_status_vip_entries or []:
            carp_status_vip_entries_item = TextValue.from_dict(carp_status_vip_entries_item_data)

            carp_status_vip_entries.append(carp_status_vip_entries_item)

        interfaces_entries = []
        _interfaces_entries = d.pop("interfaces_entries", UNSET)
        for interfaces_entries_item_data in _interfaces_entries or []:
            interfaces_entries_item = TextValue.from_dict(interfaces_entries_item_data)

            interfaces_entries.append(interfaces_entries_item)

        dhcp_relay_config = cls(
            enable=enable,
            interfaces=interfaces,
            carp_status_vip=carp_status_vip,
            append_circuit_agent_ids=append_circuit_agent_ids,
            upstream_servers=upstream_servers,
            carp_status_vip_entries=carp_status_vip_entries,
            interfaces_entries=interfaces_entries,
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
