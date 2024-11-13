from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ntp_server_info import NtpServerInfo


T = TypeVar("T", bound="NtpStatus")


@_attrs_define
class NtpStatus:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        query_enabled (Union[Unset, bool]):
        servers (Union[Unset, List['NtpServerInfo']]):
    """

    enabled: Union[Unset, bool] = UNSET
    query_enabled: Union[Unset, bool] = UNSET
    servers: Union[Unset, List["NtpServerInfo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        query_enabled = self.query_enabled

        servers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if query_enabled is not UNSET:
            field_dict["query_enabled"] = query_enabled
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ntp_server_info import NtpServerInfo

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        query_enabled = d.pop("query_enabled", UNSET)

        servers = []
        _servers = d.pop("servers", UNSET)
        for servers_item_data in _servers or []:
            servers_item = NtpServerInfo.from_dict(servers_item_data)

            servers.append(servers_item)

        ntp_status = cls(
            enabled=enabled,
            query_enabled=query_enabled,
            servers=servers,
        )

        ntp_status.additional_properties = d
        return ntp_status

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
