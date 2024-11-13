from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_server_config import OpenVPNServerConfig


T = TypeVar("T", bound="OpenVPNServers")


@_attrs_define
class OpenVPNServers:
    """
    Attributes:
        authservers (Union[Unset, List[str]]):
        servers (Union[Unset, List['OpenVPNServerConfig']]):
    """

    authservers: Union[Unset, List[str]] = UNSET
    servers: Union[Unset, List["OpenVPNServerConfig"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authservers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authservers, Unset):
            authservers = self.authservers

        servers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authservers is not UNSET:
            field_dict["authservers"] = authservers
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_vpn_server_config import OpenVPNServerConfig

        d = src_dict.copy()
        authservers = cast(List[str], d.pop("authservers", UNSET))

        servers = []
        _servers = d.pop("servers", UNSET)
        for servers_item_data in _servers or []:
            servers_item = OpenVPNServerConfig.from_dict(servers_item_data)

            servers.append(servers_item)

        open_vpn_servers = cls(
            authservers=authservers,
            servers=servers,
        )

        open_vpn_servers.additional_properties = d
        return open_vpn_servers

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
