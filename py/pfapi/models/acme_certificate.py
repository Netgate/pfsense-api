from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.acme_certificate_key_type import ACMECertificateKeyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acme_action import ACMEAction
    from ..models.acme_domain import ACMEDomain
    from ..models.acme_issued_cert import ACMEIssuedCert


T = TypeVar("T", bound="ACMECertificate")


@_attrs_define
class ACMECertificate:
    """
    Attributes:
        name (str | Unset): this name will also be used to create or overwrite a certificate that might already exist in
            the pfSense Certificate Manager
        desc (str | Unset): description of this acme certificate
        enabled (bool | Unset): whether this certificate enabled for acme operation
        acme_account (str | Unset): name of the corresponding acme account key
        key_type (ACMECertificateKeyType | Unset): type of the certificate's private key
            valid value = rsa2048, rsa3072, rsa4096, rsa8192, ec256, ec384, custom
        custom_key (str | Unset): if key_type is not "custom", custom_key will be ignored
        preferred_chain (str | Unset): chooses an alternate preferred chain
        profile (str | Unset): chooses a profile the acme server supported
        dns_wait (int | Unset): disables all the dns propagation checks of the TXT record and uses a wait duration
            instead (in second)
        domain_list (list[ACMEDomain] | Unset):
        action_list (list[ACMEAction] | Unset):
        issued_cert (ACMEIssuedCert | Unset):
        ari_disable (bool | Unset): disable the use of acme renewal information extension to check if the certificate
            needs to be renewed
        renew_before (int | Unset): number of days before the certificate expires to renew the certificate
            if the use of acme renewal information extension is failed or disabled, this value will be
            used to determine whether the certificate should be renewed (default: 30)
        lastrenewal (str | Unset): read only timestamp of last issue/renew of certificate
    """

    name: str | Unset = UNSET
    desc: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    acme_account: str | Unset = UNSET
    key_type: ACMECertificateKeyType | Unset = UNSET
    custom_key: str | Unset = UNSET
    preferred_chain: str | Unset = UNSET
    profile: str | Unset = UNSET
    dns_wait: int | Unset = UNSET
    domain_list: list[ACMEDomain] | Unset = UNSET
    action_list: list[ACMEAction] | Unset = UNSET
    issued_cert: ACMEIssuedCert | Unset = UNSET
    ari_disable: bool | Unset = UNSET
    renew_before: int | Unset = UNSET
    lastrenewal: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        desc = self.desc

        enabled = self.enabled

        acme_account = self.acme_account

        key_type: str | Unset = UNSET
        if not isinstance(self.key_type, Unset):
            key_type = self.key_type.value

        custom_key = self.custom_key

        preferred_chain = self.preferred_chain

        profile = self.profile

        dns_wait = self.dns_wait

        domain_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.domain_list, Unset):
            domain_list = []
            for domain_list_item_data in self.domain_list:
                domain_list_item = domain_list_item_data.to_dict()
                domain_list.append(domain_list_item)

        action_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.action_list, Unset):
            action_list = []
            for action_list_item_data in self.action_list:
                action_list_item = action_list_item_data.to_dict()
                action_list.append(action_list_item)

        issued_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issued_cert, Unset):
            issued_cert = self.issued_cert.to_dict()

        ari_disable = self.ari_disable

        renew_before = self.renew_before

        lastrenewal = self.lastrenewal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if desc is not UNSET:
            field_dict["desc"] = desc
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if acme_account is not UNSET:
            field_dict["acme_account"] = acme_account
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if custom_key is not UNSET:
            field_dict["custom_key"] = custom_key
        if preferred_chain is not UNSET:
            field_dict["preferred_chain"] = preferred_chain
        if profile is not UNSET:
            field_dict["profile"] = profile
        if dns_wait is not UNSET:
            field_dict["dns_wait"] = dns_wait
        if domain_list is not UNSET:
            field_dict["domain_list"] = domain_list
        if action_list is not UNSET:
            field_dict["action_list"] = action_list
        if issued_cert is not UNSET:
            field_dict["issued_cert"] = issued_cert
        if ari_disable is not UNSET:
            field_dict["ari_disable"] = ari_disable
        if renew_before is not UNSET:
            field_dict["renew_before"] = renew_before
        if lastrenewal is not UNSET:
            field_dict["lastrenewal"] = lastrenewal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acme_action import ACMEAction
        from ..models.acme_domain import ACMEDomain
        from ..models.acme_issued_cert import ACMEIssuedCert

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        desc = d.pop("desc", UNSET)

        enabled = d.pop("enabled", UNSET)

        acme_account = d.pop("acme_account", UNSET)

        _key_type = d.pop("key_type", UNSET)
        key_type: ACMECertificateKeyType | Unset
        if isinstance(_key_type, Unset):
            key_type = UNSET
        else:
            key_type = ACMECertificateKeyType(_key_type)

        custom_key = d.pop("custom_key", UNSET)

        preferred_chain = d.pop("preferred_chain", UNSET)

        profile = d.pop("profile", UNSET)

        dns_wait = d.pop("dns_wait", UNSET)

        _domain_list = d.pop("domain_list", UNSET)
        domain_list: list[ACMEDomain] | Unset = UNSET
        if _domain_list is not UNSET:
            domain_list = []
            for domain_list_item_data in _domain_list:
                domain_list_item = ACMEDomain.from_dict(domain_list_item_data)

                domain_list.append(domain_list_item)

        _action_list = d.pop("action_list", UNSET)
        action_list: list[ACMEAction] | Unset = UNSET
        if _action_list is not UNSET:
            action_list = []
            for action_list_item_data in _action_list:
                action_list_item = ACMEAction.from_dict(action_list_item_data)

                action_list.append(action_list_item)

        _issued_cert = d.pop("issued_cert", UNSET)
        issued_cert: ACMEIssuedCert | Unset
        if isinstance(_issued_cert, Unset):
            issued_cert = UNSET
        else:
            issued_cert = ACMEIssuedCert.from_dict(_issued_cert)

        ari_disable = d.pop("ari_disable", UNSET)

        renew_before = d.pop("renew_before", UNSET)

        lastrenewal = d.pop("lastrenewal", UNSET)

        acme_certificate = cls(
            name=name,
            desc=desc,
            enabled=enabled,
            acme_account=acme_account,
            key_type=key_type,
            custom_key=custom_key,
            preferred_chain=preferred_chain,
            profile=profile,
            dns_wait=dns_wait,
            domain_list=domain_list,
            action_list=action_list,
            issued_cert=issued_cert,
            ari_disable=ari_disable,
            renew_before=renew_before,
            lastrenewal=lastrenewal,
        )

        acme_certificate.additional_properties = d
        return acme_certificate

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
