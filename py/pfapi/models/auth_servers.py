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
        active_type (str):
        active_name (str):
        local (LocalServer):
        ldap (Union[Unset, List['LdapAuthServer']]):
        radius (Union[Unset, List['RadiusAuthServer']]):
    """

    active_type: str
    active_name: str
    local: "LocalServer"
    ldap: Union[Unset, List["LdapAuthServer"]] = UNSET
    radius: Union[Unset, List["RadiusAuthServer"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active_type = self.active_type

        active_name = self.active_name

        local = self.local.to_dict()

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active_type": active_type,
                "active_name": active_name,
                "local": local,
            }
        )
        if ldap is not UNSET:
            field_dict["ldap"] = ldap
        if radius is not UNSET:
            field_dict["radius"] = radius

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ldap_auth_server import LdapAuthServer
        from ..models.local_server import LocalServer
        from ..models.radius_auth_server import RadiusAuthServer

        d = src_dict.copy()
        active_type = d.pop("active_type")

        active_name = d.pop("active_name")

        local = LocalServer.from_dict(d.pop("local"))

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

        auth_servers = cls(
            active_type=active_type,
            active_name=active_name,
            local=local,
            ldap=ldap,
            radius=radius,
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
