from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acme_account_key import ACMEAccountKey
    from ..models.acme_certificate import ACMECertificate
    from ..models.acme_server import ACMEServer
    from ..models.acme_settings import ACMESettings


T = TypeVar("T", bound="ACMEConfig")


@_attrs_define
class ACMEConfig:
    """
    Attributes:
        account_keys (list[ACMEAccountKey] | Unset):
        certs (list[ACMECertificate] | Unset):
        servers (list[ACMEServer] | Unset):
        settings (ACMESettings | Unset):
    """

    account_keys: list[ACMEAccountKey] | Unset = UNSET
    certs: list[ACMECertificate] | Unset = UNSET
    servers: list[ACMEServer] | Unset = UNSET
    settings: ACMESettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.account_keys, Unset):
            account_keys = []
            for account_keys_item_data in self.account_keys:
                account_keys_item = account_keys_item_data.to_dict()
                account_keys.append(account_keys_item)

        certs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.certs, Unset):
            certs = []
            for certs_item_data in self.certs:
                certs_item = certs_item_data.to_dict()
                certs.append(certs_item)

        servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_keys is not UNSET:
            field_dict["account_keys"] = account_keys
        if certs is not UNSET:
            field_dict["certs"] = certs
        if servers is not UNSET:
            field_dict["servers"] = servers
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acme_account_key import ACMEAccountKey
        from ..models.acme_certificate import ACMECertificate
        from ..models.acme_server import ACMEServer
        from ..models.acme_settings import ACMESettings

        d = dict(src_dict)
        _account_keys = d.pop("account_keys", UNSET)
        account_keys: list[ACMEAccountKey] | Unset = UNSET
        if _account_keys is not UNSET:
            account_keys = []
            for account_keys_item_data in _account_keys:
                account_keys_item = ACMEAccountKey.from_dict(account_keys_item_data)

                account_keys.append(account_keys_item)

        _certs = d.pop("certs", UNSET)
        certs: list[ACMECertificate] | Unset = UNSET
        if _certs is not UNSET:
            certs = []
            for certs_item_data in _certs:
                certs_item = ACMECertificate.from_dict(certs_item_data)

                certs.append(certs_item)

        _servers = d.pop("servers", UNSET)
        servers: list[ACMEServer] | Unset = UNSET
        if _servers is not UNSET:
            servers = []
            for servers_item_data in _servers:
                servers_item = ACMEServer.from_dict(servers_item_data)

                servers.append(servers_item)

        _settings = d.pop("settings", UNSET)
        settings: ACMESettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ACMESettings.from_dict(_settings)

        acme_config = cls(
            account_keys=account_keys,
            certs=certs,
            servers=servers,
            settings=settings,
        )

        acme_config.additional_properties = d
        return acme_config

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
