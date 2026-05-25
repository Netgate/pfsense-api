from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.saml_server_group_map import SamlServerGroupMap


T = TypeVar("T", bound="SamlServer")


@_attrs_define
class SamlServer:
    """
    Attributes:
        name (str):
        entity_id (str): SP entity ID (unique identifier, typically a URL)
        type_ (str | Unset):
        enable (bool | Unset): enable authenticating with this SAML service
        acs_url (str | Unset): SP assertion consumer service URL (our SAML callback endpoint, defaults to
            /api/login/saml/acs/{name})
        metadata_url (str | Unset): IdP metadata URL; if provided, idp_cert_pem and idp_sso_url are not required
        idp_entity_id (str | Unset): IdP Entity ID; required when idp_cert_pem is set
        idp_sso_url (str | Unset): IdP SSO redirect endpoint URL; required when idp_cert_pem is set
        idp_cert_pem (str | Unset): PEM-encoded IdP signing certificate; required when metadata_url is not set
        sp_cert_pem (str | Unset): PEM-encoded SP X.509 certificate for signing requests
        sp_key_pem (str | Unset): PEM-encoded SP private key (RSA PKCS1/PKCS8 or Ed25519 PKCS8)
        sign_requests (bool | Unset): sign AuthnRequests with the SP key
        user_attr (str | Unset): SAML attribute name for username; empty means use NameID
        group_attr (str | Unset): SAML attribute name for group membership values (e.g. groups)
        session_timeout (int | Unset): seconds to retain session data after assertion validation (default 300)
        group_map (SamlServerGroupMap | Unset):
    """

    name: str
    entity_id: str
    type_: str | Unset = UNSET
    enable: bool | Unset = UNSET
    acs_url: str | Unset = UNSET
    metadata_url: str | Unset = UNSET
    idp_entity_id: str | Unset = UNSET
    idp_sso_url: str | Unset = UNSET
    idp_cert_pem: str | Unset = UNSET
    sp_cert_pem: str | Unset = UNSET
    sp_key_pem: str | Unset = UNSET
    sign_requests: bool | Unset = UNSET
    user_attr: str | Unset = UNSET
    group_attr: str | Unset = UNSET
    session_timeout: int | Unset = UNSET
    group_map: SamlServerGroupMap | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        entity_id = self.entity_id

        type_ = self.type_

        enable = self.enable

        acs_url = self.acs_url

        metadata_url = self.metadata_url

        idp_entity_id = self.idp_entity_id

        idp_sso_url = self.idp_sso_url

        idp_cert_pem = self.idp_cert_pem

        sp_cert_pem = self.sp_cert_pem

        sp_key_pem = self.sp_key_pem

        sign_requests = self.sign_requests

        user_attr = self.user_attr

        group_attr = self.group_attr

        session_timeout = self.session_timeout

        group_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_map, Unset):
            group_map = self.group_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "entity_id": entity_id,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if enable is not UNSET:
            field_dict["enable"] = enable
        if acs_url is not UNSET:
            field_dict["acs_url"] = acs_url
        if metadata_url is not UNSET:
            field_dict["metadata_url"] = metadata_url
        if idp_entity_id is not UNSET:
            field_dict["idp_entity_id"] = idp_entity_id
        if idp_sso_url is not UNSET:
            field_dict["idp_sso_url"] = idp_sso_url
        if idp_cert_pem is not UNSET:
            field_dict["idp_cert_pem"] = idp_cert_pem
        if sp_cert_pem is not UNSET:
            field_dict["sp_cert_pem"] = sp_cert_pem
        if sp_key_pem is not UNSET:
            field_dict["sp_key_pem"] = sp_key_pem
        if sign_requests is not UNSET:
            field_dict["sign_requests"] = sign_requests
        if user_attr is not UNSET:
            field_dict["user_attr"] = user_attr
        if group_attr is not UNSET:
            field_dict["group_attr"] = group_attr
        if session_timeout is not UNSET:
            field_dict["session_timeout"] = session_timeout
        if group_map is not UNSET:
            field_dict["group_map"] = group_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.saml_server_group_map import SamlServerGroupMap

        d = dict(src_dict)
        name = d.pop("name")

        entity_id = d.pop("entity_id")

        type_ = d.pop("type", UNSET)

        enable = d.pop("enable", UNSET)

        acs_url = d.pop("acs_url", UNSET)

        metadata_url = d.pop("metadata_url", UNSET)

        idp_entity_id = d.pop("idp_entity_id", UNSET)

        idp_sso_url = d.pop("idp_sso_url", UNSET)

        idp_cert_pem = d.pop("idp_cert_pem", UNSET)

        sp_cert_pem = d.pop("sp_cert_pem", UNSET)

        sp_key_pem = d.pop("sp_key_pem", UNSET)

        sign_requests = d.pop("sign_requests", UNSET)

        user_attr = d.pop("user_attr", UNSET)

        group_attr = d.pop("group_attr", UNSET)

        session_timeout = d.pop("session_timeout", UNSET)

        _group_map = d.pop("group_map", UNSET)
        group_map: SamlServerGroupMap | Unset
        if isinstance(_group_map, Unset):
            group_map = UNSET
        else:
            group_map = SamlServerGroupMap.from_dict(_group_map)

        saml_server = cls(
            name=name,
            entity_id=entity_id,
            type_=type_,
            enable=enable,
            acs_url=acs_url,
            metadata_url=metadata_url,
            idp_entity_id=idp_entity_id,
            idp_sso_url=idp_sso_url,
            idp_cert_pem=idp_cert_pem,
            sp_cert_pem=sp_cert_pem,
            sp_key_pem=sp_key_pem,
            sign_requests=sign_requests,
            user_attr=user_attr,
            group_attr=group_attr,
            session_timeout=session_timeout,
            group_map=group_map,
        )

        saml_server.additional_properties = d
        return saml_server

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
