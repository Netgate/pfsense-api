from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ACMERegistration")


@_attrs_define
class ACMERegistration:
    """Read only info about the account created on a ACME server

    Attributes:
        uri (str | Unset):
        status (str | Unset): possible values are "valid", "deactivated", and "revoked"
        contact (list[str] | Unset):
        terms_of_service_agreed (bool | Unset):
        orders (str | Unset):
        only_return_existing (bool | Unset):
        external_account_binding (str | Unset):
    """

    uri: str | Unset = UNSET
    status: str | Unset = UNSET
    contact: list[str] | Unset = UNSET
    terms_of_service_agreed: bool | Unset = UNSET
    orders: str | Unset = UNSET
    only_return_existing: bool | Unset = UNSET
    external_account_binding: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        status = self.status

        contact: list[str] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact

        terms_of_service_agreed = self.terms_of_service_agreed

        orders = self.orders

        only_return_existing = self.only_return_existing

        external_account_binding = self.external_account_binding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uri is not UNSET:
            field_dict["uri"] = uri
        if status is not UNSET:
            field_dict["status"] = status
        if contact is not UNSET:
            field_dict["contact"] = contact
        if terms_of_service_agreed is not UNSET:
            field_dict["termsOfServiceAgreed"] = terms_of_service_agreed
        if orders is not UNSET:
            field_dict["orders"] = orders
        if only_return_existing is not UNSET:
            field_dict["onlyReturnExisting"] = only_return_existing
        if external_account_binding is not UNSET:
            field_dict["externalAccountBinding"] = external_account_binding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri", UNSET)

        status = d.pop("status", UNSET)

        contact = cast(list[str], d.pop("contact", UNSET))

        terms_of_service_agreed = d.pop("termsOfServiceAgreed", UNSET)

        orders = d.pop("orders", UNSET)

        only_return_existing = d.pop("onlyReturnExisting", UNSET)

        external_account_binding = d.pop("externalAccountBinding", UNSET)

        acme_registration = cls(
            uri=uri,
            status=status,
            contact=contact,
            terms_of_service_agreed=terms_of_service_agreed,
            orders=orders,
            only_return_existing=only_return_existing,
            external_account_binding=external_account_binding,
        )

        acme_registration.additional_properties = d
        return acme_registration

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
