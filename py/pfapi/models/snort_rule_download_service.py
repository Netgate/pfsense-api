from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_download_progress import SnortDownloadProgress


T = TypeVar("T", bound="SnortRuleDownloadService")


@_attrs_define
class SnortRuleDownloadService:
    """Location to download Snort rules, which is usually a URL with an oink-code.
    The rule files can be .rule, .tgz, .tar.gz, or .zip.
    When specifying the URL, also include the oink code as part of it.

    Download services start at the global configured rule_update_settings schedule

        Attributes:
            name (str | Unset): name of service or publisher
            descr (str | Unset): user provided description
            url (str | Unset): address of service to download Snort rules from
            checksum_url (str | Unset): address of the file containing the checkums of the rule archive, usually suffixed as
                .md5sum or sha256sum
            sig_hash (str | Unset): (readonly) checksum of the rules
            sig_date (str | Unset): (readonly) date of when the signature hash was retrieved
            sig_date_ts (int | Unset): (readonly) Epoch milliseconds timestamp of signature hash retrieval
            last_update_ts (int | Unset): (readonly) Epoch milliseconds timestamp of when the rule update was  attempted
            last_update_result (str | Unset): result of last update attempt - success or failure (with message)
            id (str | Unset): (readonly) the ID generated for this service
            skip_cert_check (bool | Unset): don't validate server certificate; if tls_fingerprint is provided, the cert is
                checked against value configured
            tls_fingerprint (str | Unset): (optional) for self-signed certs, the hex string or base64 encoded bytes of the
                SHA256 fingerprint of the certificate or the public key
            state (str | Unset): enabled (active) , disabled (suspended)
            progress (SnortDownloadProgress | Unset):
    """

    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    url: str | Unset = UNSET
    checksum_url: str | Unset = UNSET
    sig_hash: str | Unset = UNSET
    sig_date: str | Unset = UNSET
    sig_date_ts: int | Unset = UNSET
    last_update_ts: int | Unset = UNSET
    last_update_result: str | Unset = UNSET
    id: str | Unset = UNSET
    skip_cert_check: bool | Unset = UNSET
    tls_fingerprint: str | Unset = UNSET
    state: str | Unset = UNSET
    progress: SnortDownloadProgress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descr = self.descr

        url = self.url

        checksum_url = self.checksum_url

        sig_hash = self.sig_hash

        sig_date = self.sig_date

        sig_date_ts = self.sig_date_ts

        last_update_ts = self.last_update_ts

        last_update_result = self.last_update_result

        id = self.id

        skip_cert_check = self.skip_cert_check

        tls_fingerprint = self.tls_fingerprint

        state = self.state

        progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if url is not UNSET:
            field_dict["url"] = url
        if checksum_url is not UNSET:
            field_dict["checksum_url"] = checksum_url
        if sig_hash is not UNSET:
            field_dict["sig_hash"] = sig_hash
        if sig_date is not UNSET:
            field_dict["sig_date"] = sig_date
        if sig_date_ts is not UNSET:
            field_dict["sig_date_ts"] = sig_date_ts
        if last_update_ts is not UNSET:
            field_dict["last_update_ts"] = last_update_ts
        if last_update_result is not UNSET:
            field_dict["last_update_result"] = last_update_result
        if id is not UNSET:
            field_dict["id"] = id
        if skip_cert_check is not UNSET:
            field_dict["skip_cert_check"] = skip_cert_check
        if tls_fingerprint is not UNSET:
            field_dict["tls_fingerprint"] = tls_fingerprint
        if state is not UNSET:
            field_dict["state"] = state
        if progress is not UNSET:
            field_dict["progress"] = progress

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_download_progress import SnortDownloadProgress

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        url = d.pop("url", UNSET)

        checksum_url = d.pop("checksum_url", UNSET)

        sig_hash = d.pop("sig_hash", UNSET)

        sig_date = d.pop("sig_date", UNSET)

        sig_date_ts = d.pop("sig_date_ts", UNSET)

        last_update_ts = d.pop("last_update_ts", UNSET)

        last_update_result = d.pop("last_update_result", UNSET)

        id = d.pop("id", UNSET)

        skip_cert_check = d.pop("skip_cert_check", UNSET)

        tls_fingerprint = d.pop("tls_fingerprint", UNSET)

        state = d.pop("state", UNSET)

        _progress = d.pop("progress", UNSET)
        progress: SnortDownloadProgress | Unset
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = SnortDownloadProgress.from_dict(_progress)

        snort_rule_download_service = cls(
            name=name,
            descr=descr,
            url=url,
            checksum_url=checksum_url,
            sig_hash=sig_hash,
            sig_date=sig_date,
            sig_date_ts=sig_date_ts,
            last_update_ts=last_update_ts,
            last_update_result=last_update_result,
            id=id,
            skip_cert_check=skip_cert_check,
            tls_fingerprint=tls_fingerprint,
            state=state,
            progress=progress,
        )

        snort_rule_download_service.additional_properties = d
        return snort_rule_download_service

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
