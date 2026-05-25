from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.acme_account_key_key_type import ACMEAccountKeyKeyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acme_registration import ACMERegistration


T = TypeVar("T", bound="ACMEAccountKey")


@_attrs_define
class ACMEAccountKey:
    """
    Attributes:
        name (str | Unset): name of this account key
        desc (str | Unset):
        email (str | Unset): e-mail address to register for account key
        acme_server (str | Unset): the acme server which will be used to issue certificates using this account key
        key_type (ACMEAccountKeyKeyType | Unset): type of the cert's private key
            valid value = rsa2048, rsa3072, rsa4096, rsa8192, ec256, ec384, custom
        account_key (str | Unset): if key_type is not "custom", system will overwrite this field with generated private
            key
        registration (ACMERegistration | Unset): Read only info about the account created on a ACME server
    """

    name: str | Unset = UNSET
    desc: str | Unset = UNSET
    email: str | Unset = UNSET
    acme_server: str | Unset = UNSET
    key_type: ACMEAccountKeyKeyType | Unset = UNSET
    account_key: str | Unset = UNSET
    registration: ACMERegistration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        desc = self.desc

        email = self.email

        acme_server = self.acme_server

        key_type: str | Unset = UNSET
        if not isinstance(self.key_type, Unset):
            key_type = self.key_type.value

        account_key = self.account_key

        registration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration, Unset):
            registration = self.registration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if desc is not UNSET:
            field_dict["desc"] = desc
        if email is not UNSET:
            field_dict["email"] = email
        if acme_server is not UNSET:
            field_dict["acme_server"] = acme_server
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if account_key is not UNSET:
            field_dict["account_key"] = account_key
        if registration is not UNSET:
            field_dict["registration"] = registration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acme_registration import ACMERegistration

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        desc = d.pop("desc", UNSET)

        email = d.pop("email", UNSET)

        acme_server = d.pop("acme_server", UNSET)

        _key_type = d.pop("key_type", UNSET)
        key_type: ACMEAccountKeyKeyType | Unset
        if isinstance(_key_type, Unset):
            key_type = UNSET
        else:
            key_type = ACMEAccountKeyKeyType(_key_type)

        account_key = d.pop("account_key", UNSET)

        _registration = d.pop("registration", UNSET)
        registration: ACMERegistration | Unset
        if isinstance(_registration, Unset):
            registration = UNSET
        else:
            registration = ACMERegistration.from_dict(_registration)

        acme_account_key = cls(
            name=name,
            desc=desc,
            email=email,
            acme_server=acme_server,
            key_type=key_type,
            account_key=account_key,
            registration=registration,
        )

        acme_account_key.additional_properties = d
        return acme_account_key

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
