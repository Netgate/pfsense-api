from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.haproxy_frontend import HaproxyFrontend
    from ..models.text_value import TextValue


T = TypeVar("T", bound="HaproxyFrontendList")


@_attrs_define
class HaproxyFrontendList:
    """
    Attributes:
        frontends (list[HaproxyFrontend] | Unset):
        backend_serverpool_options (list[TextValue] | Unset):
        primary_frontend_options (list[TextValue] | Unset):
        ssl_certificate_options (list[TextValue] | Unset):
        client_ca_options (list[TextValue] | Unset):
        client_crl_options (list[TextValue] | Unset):
        extaddr_options (list[TextValue] | Unset):
    """

    frontends: list[HaproxyFrontend] | Unset = UNSET
    backend_serverpool_options: list[TextValue] | Unset = UNSET
    primary_frontend_options: list[TextValue] | Unset = UNSET
    ssl_certificate_options: list[TextValue] | Unset = UNSET
    client_ca_options: list[TextValue] | Unset = UNSET
    client_crl_options: list[TextValue] | Unset = UNSET
    extaddr_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frontends: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.frontends, Unset):
            frontends = []
            for frontends_item_data in self.frontends:
                frontends_item = frontends_item_data.to_dict()
                frontends.append(frontends_item)

        backend_serverpool_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.backend_serverpool_options, Unset):
            backend_serverpool_options = []
            for backend_serverpool_options_item_data in self.backend_serverpool_options:
                backend_serverpool_options_item = backend_serverpool_options_item_data.to_dict()
                backend_serverpool_options.append(backend_serverpool_options_item)

        primary_frontend_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.primary_frontend_options, Unset):
            primary_frontend_options = []
            for primary_frontend_options_item_data in self.primary_frontend_options:
                primary_frontend_options_item = primary_frontend_options_item_data.to_dict()
                primary_frontend_options.append(primary_frontend_options_item)

        ssl_certificate_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssl_certificate_options, Unset):
            ssl_certificate_options = []
            for ssl_certificate_options_item_data in self.ssl_certificate_options:
                ssl_certificate_options_item = ssl_certificate_options_item_data.to_dict()
                ssl_certificate_options.append(ssl_certificate_options_item)

        client_ca_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.client_ca_options, Unset):
            client_ca_options = []
            for client_ca_options_item_data in self.client_ca_options:
                client_ca_options_item = client_ca_options_item_data.to_dict()
                client_ca_options.append(client_ca_options_item)

        client_crl_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.client_crl_options, Unset):
            client_crl_options = []
            for client_crl_options_item_data in self.client_crl_options:
                client_crl_options_item = client_crl_options_item_data.to_dict()
                client_crl_options.append(client_crl_options_item)

        extaddr_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extaddr_options, Unset):
            extaddr_options = []
            for extaddr_options_item_data in self.extaddr_options:
                extaddr_options_item = extaddr_options_item_data.to_dict()
                extaddr_options.append(extaddr_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if frontends is not UNSET:
            field_dict["frontends"] = frontends
        if backend_serverpool_options is not UNSET:
            field_dict["backend_serverpool_options"] = backend_serverpool_options
        if primary_frontend_options is not UNSET:
            field_dict["primary_frontend_options"] = primary_frontend_options
        if ssl_certificate_options is not UNSET:
            field_dict["ssl_certificate_options"] = ssl_certificate_options
        if client_ca_options is not UNSET:
            field_dict["client_ca_options"] = client_ca_options
        if client_crl_options is not UNSET:
            field_dict["client_crl_options"] = client_crl_options
        if extaddr_options is not UNSET:
            field_dict["extaddr_options"] = extaddr_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.haproxy_frontend import HaproxyFrontend
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _frontends = d.pop("frontends", UNSET)
        frontends: list[HaproxyFrontend] | Unset = UNSET
        if _frontends is not UNSET:
            frontends = []
            for frontends_item_data in _frontends:
                frontends_item = HaproxyFrontend.from_dict(frontends_item_data)

                frontends.append(frontends_item)

        _backend_serverpool_options = d.pop("backend_serverpool_options", UNSET)
        backend_serverpool_options: list[TextValue] | Unset = UNSET
        if _backend_serverpool_options is not UNSET:
            backend_serverpool_options = []
            for backend_serverpool_options_item_data in _backend_serverpool_options:
                backend_serverpool_options_item = TextValue.from_dict(backend_serverpool_options_item_data)

                backend_serverpool_options.append(backend_serverpool_options_item)

        _primary_frontend_options = d.pop("primary_frontend_options", UNSET)
        primary_frontend_options: list[TextValue] | Unset = UNSET
        if _primary_frontend_options is not UNSET:
            primary_frontend_options = []
            for primary_frontend_options_item_data in _primary_frontend_options:
                primary_frontend_options_item = TextValue.from_dict(primary_frontend_options_item_data)

                primary_frontend_options.append(primary_frontend_options_item)

        _ssl_certificate_options = d.pop("ssl_certificate_options", UNSET)
        ssl_certificate_options: list[TextValue] | Unset = UNSET
        if _ssl_certificate_options is not UNSET:
            ssl_certificate_options = []
            for ssl_certificate_options_item_data in _ssl_certificate_options:
                ssl_certificate_options_item = TextValue.from_dict(ssl_certificate_options_item_data)

                ssl_certificate_options.append(ssl_certificate_options_item)

        _client_ca_options = d.pop("client_ca_options", UNSET)
        client_ca_options: list[TextValue] | Unset = UNSET
        if _client_ca_options is not UNSET:
            client_ca_options = []
            for client_ca_options_item_data in _client_ca_options:
                client_ca_options_item = TextValue.from_dict(client_ca_options_item_data)

                client_ca_options.append(client_ca_options_item)

        _client_crl_options = d.pop("client_crl_options", UNSET)
        client_crl_options: list[TextValue] | Unset = UNSET
        if _client_crl_options is not UNSET:
            client_crl_options = []
            for client_crl_options_item_data in _client_crl_options:
                client_crl_options_item = TextValue.from_dict(client_crl_options_item_data)

                client_crl_options.append(client_crl_options_item)

        _extaddr_options = d.pop("extaddr_options", UNSET)
        extaddr_options: list[TextValue] | Unset = UNSET
        if _extaddr_options is not UNSET:
            extaddr_options = []
            for extaddr_options_item_data in _extaddr_options:
                extaddr_options_item = TextValue.from_dict(extaddr_options_item_data)

                extaddr_options.append(extaddr_options_item)

        haproxy_frontend_list = cls(
            frontends=frontends,
            backend_serverpool_options=backend_serverpool_options,
            primary_frontend_options=primary_frontend_options,
            ssl_certificate_options=ssl_certificate_options,
            client_ca_options=client_ca_options,
            client_crl_options=client_crl_options,
            extaddr_options=extaddr_options,
        )

        haproxy_frontend_list.additional_properties = d
        return haproxy_frontend_list

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
