from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_auth_server import LdapAuthServer
    from ..models.radius_auth_server import RadiusAuthServer
    from ..models.saml_server import SamlServer


T = TypeVar("T", bound="AuthServer")


@_attrs_define
class AuthServer:
    """
    Attributes:
        ldap (LdapAuthServer | Unset):
        radius (RadiusAuthServer | Unset):
        saml (SamlServer | Unset):
    """

    ldap: LdapAuthServer | Unset = UNSET
    radius: RadiusAuthServer | Unset = UNSET
    saml: SamlServer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ldap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ldap, Unset):
            ldap = self.ldap.to_dict()

        radius: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radius, Unset):
            radius = self.radius.to_dict()

        saml: dict[str, Any] | Unset = UNSET
        if not isinstance(self.saml, Unset):
            saml = self.saml.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ldap is not UNSET:
            field_dict["ldap"] = ldap
        if radius is not UNSET:
            field_dict["radius"] = radius
        if saml is not UNSET:
            field_dict["saml"] = saml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_auth_server import LdapAuthServer
        from ..models.radius_auth_server import RadiusAuthServer
        from ..models.saml_server import SamlServer

        d = dict(src_dict)
        _ldap = d.pop("ldap", UNSET)
        ldap: LdapAuthServer | Unset
        if isinstance(_ldap, Unset):
            ldap = UNSET
        else:
            ldap = LdapAuthServer.from_dict(_ldap)

        _radius = d.pop("radius", UNSET)
        radius: RadiusAuthServer | Unset
        if isinstance(_radius, Unset):
            radius = UNSET
        else:
            radius = RadiusAuthServer.from_dict(_radius)

        _saml = d.pop("saml", UNSET)
        saml: SamlServer | Unset
        if isinstance(_saml, Unset):
            saml = UNSET
        else:
            saml = SamlServer.from_dict(_saml)

        auth_server = cls(
            ldap=ldap,
            radius=radius,
            saml=saml,
        )

        auth_server.additional_properties = d
        return auth_server

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
