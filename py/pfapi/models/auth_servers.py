from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_auth_server import LdapAuthServer
    from ..models.local_server import LocalServer
    from ..models.radius_auth_server import RadiusAuthServer


T = TypeVar("T", bound="AuthServers")


@_attrs_define
class AuthServers:
    """
    Attributes:
        ldap (Union[Unset, List['LdapAuthServer']]):
        radius (Union[Unset, List['RadiusAuthServer']]):
        local (Union[Unset, LocalServer]):
    """

    ldap: Union[Unset, List["LdapAuthServer"]] = UNSET
    radius: Union[Unset, List["RadiusAuthServer"]] = UNSET
    local: Union[Unset, "LocalServer"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ldap: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ldap, Unset):
            ldap = []
            for ldap_item_data in self.ldap:
                ldap_item = ldap_item_data.to_dict()
                ldap.append(ldap_item)

        radius: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.radius, Unset):
            radius = []
            for radius_item_data in self.radius:
                radius_item = radius_item_data.to_dict()
                radius.append(radius_item)

        local: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local, Unset):
            local = self.local.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ldap is not UNSET:
            field_dict["ldap"] = ldap
        if radius is not UNSET:
            field_dict["radius"] = radius
        if local is not UNSET:
            field_dict["local"] = local

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ldap_auth_server import LdapAuthServer
        from ..models.local_server import LocalServer
        from ..models.radius_auth_server import RadiusAuthServer

        d = src_dict.copy()
        ldap = []
        _ldap = d.pop("ldap", UNSET)
        for ldap_item_data in _ldap or []:
            ldap_item = LdapAuthServer.from_dict(ldap_item_data)

            ldap.append(ldap_item)

        radius = []
        _radius = d.pop("radius", UNSET)
        for radius_item_data in _radius or []:
            radius_item = RadiusAuthServer.from_dict(radius_item_data)

            radius.append(radius_item)

        _local = d.pop("local", UNSET)
        local: Union[Unset, LocalServer]
        if isinstance(_local, Unset):
            local = UNSET
        else:
            local = LocalServer.from_dict(_local)

        auth_servers = cls(
            ldap=ldap,
            radius=radius,
            local=local,
        )

        auth_servers.additional_properties = d
        return auth_servers

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
