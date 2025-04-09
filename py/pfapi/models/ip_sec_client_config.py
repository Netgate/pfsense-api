from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_servers import AuthServers
    from ..models.ip_sec_client import IPSecClient
    from ..models.user_group import UserGroup


T = TypeVar("T", bound="IPSecClientConfig")


@_attrs_define
class IPSecClientConfig:
    """
    Attributes:
        client (Union[Unset, IPSecClient]):
        user_groups (Union[Unset, List['UserGroup']]):
        auth_servers (Union[Unset, AuthServers]):
    """

    client: Union[Unset, "IPSecClient"] = UNSET
    user_groups: Union[Unset, List["UserGroup"]] = UNSET
    auth_servers: Union[Unset, "AuthServers"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        user_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_groups, Unset):
            user_groups = []
            for user_groups_item_data in self.user_groups:
                user_groups_item = user_groups_item_data.to_dict()
                user_groups.append(user_groups_item)

        auth_servers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auth_servers, Unset):
            auth_servers = self.auth_servers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client is not UNSET:
            field_dict["client"] = client
        if user_groups is not UNSET:
            field_dict["user_groups"] = user_groups
        if auth_servers is not UNSET:
            field_dict["auth_servers"] = auth_servers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.auth_servers import AuthServers
        from ..models.ip_sec_client import IPSecClient
        from ..models.user_group import UserGroup

        d = src_dict.copy()
        _client = d.pop("client", UNSET)
        client: Union[Unset, IPSecClient]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = IPSecClient.from_dict(_client)

        user_groups = []
        _user_groups = d.pop("user_groups", UNSET)
        for user_groups_item_data in _user_groups or []:
            user_groups_item = UserGroup.from_dict(user_groups_item_data)

            user_groups.append(user_groups_item)

        _auth_servers = d.pop("auth_servers", UNSET)
        auth_servers: Union[Unset, AuthServers]
        if isinstance(_auth_servers, Unset):
            auth_servers = UNSET
        else:
            auth_servers = AuthServers.from_dict(_auth_servers)

        ip_sec_client_config = cls(
            client=client,
            user_groups=user_groups,
            auth_servers=auth_servers,
        )

        ip_sec_client_config.additional_properties = d
        return ip_sec_client_config

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
