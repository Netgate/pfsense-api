from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_auth_server import LdapAuthServer
    from ..models.local_server import LocalServer
    from ..models.radius_auth_server import RadiusAuthServer
    from ..models.text_value import TextValue


T = TypeVar("T", bound="AuthServers")


@_attrs_define
class AuthServers:
    """
    Attributes:
        active_type (str | Unset):
        active_name (str | Unset):
        ldap (list[LdapAuthServer] | Unset):
        radius (list[RadiusAuthServer] | Unset):
        local (LocalServer | Unset):
        radius_nas_list (list[TextValue] | Unset):
    """

    active_type: str | Unset = UNSET
    active_name: str | Unset = UNSET
    ldap: list[LdapAuthServer] | Unset = UNSET
    radius: list[RadiusAuthServer] | Unset = UNSET
    local: LocalServer | Unset = UNSET
    radius_nas_list: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_type = self.active_type

        active_name = self.active_name

        ldap: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ldap, Unset):
            ldap = []
            for ldap_item_data in self.ldap:
                ldap_item = ldap_item_data.to_dict()
                ldap.append(ldap_item)

        radius: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.radius, Unset):
            radius = []
            for radius_item_data in self.radius:
                radius_item = radius_item_data.to_dict()
                radius.append(radius_item)

        local: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local, Unset):
            local = self.local.to_dict()

        radius_nas_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.radius_nas_list, Unset):
            radius_nas_list = []
            for radius_nas_list_item_data in self.radius_nas_list:
                radius_nas_list_item = radius_nas_list_item_data.to_dict()
                radius_nas_list.append(radius_nas_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_type is not UNSET:
            field_dict["active_type"] = active_type
        if active_name is not UNSET:
            field_dict["active_name"] = active_name
        if ldap is not UNSET:
            field_dict["ldap"] = ldap
        if radius is not UNSET:
            field_dict["radius"] = radius
        if local is not UNSET:
            field_dict["local"] = local
        if radius_nas_list is not UNSET:
            field_dict["radius_nas_list"] = radius_nas_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_auth_server import LdapAuthServer
        from ..models.local_server import LocalServer
        from ..models.radius_auth_server import RadiusAuthServer
        from ..models.text_value import TextValue

        d = dict(src_dict)
        active_type = d.pop("active_type", UNSET)

        active_name = d.pop("active_name", UNSET)

        _ldap = d.pop("ldap", UNSET)
        ldap: list[LdapAuthServer] | Unset = UNSET
        if _ldap is not UNSET:
            ldap = []
            for ldap_item_data in _ldap:
                ldap_item = LdapAuthServer.from_dict(ldap_item_data)

                ldap.append(ldap_item)

        _radius = d.pop("radius", UNSET)
        radius: list[RadiusAuthServer] | Unset = UNSET
        if _radius is not UNSET:
            radius = []
            for radius_item_data in _radius:
                radius_item = RadiusAuthServer.from_dict(radius_item_data)

                radius.append(radius_item)

        _local = d.pop("local", UNSET)
        local: LocalServer | Unset
        if isinstance(_local, Unset):
            local = UNSET
        else:
            local = LocalServer.from_dict(_local)

        _radius_nas_list = d.pop("radius_nas_list", UNSET)
        radius_nas_list: list[TextValue] | Unset = UNSET
        if _radius_nas_list is not UNSET:
            radius_nas_list = []
            for radius_nas_list_item_data in _radius_nas_list:
                radius_nas_list_item = TextValue.from_dict(radius_nas_list_item_data)

                radius_nas_list.append(radius_nas_list_item)

        auth_servers = cls(
            active_type=active_type,
            active_name=active_name,
            ldap=ldap,
            radius=radius,
            local=local,
            radius_nas_list=radius_nas_list,
        )

        auth_servers.additional_properties = d
        return auth_servers

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
