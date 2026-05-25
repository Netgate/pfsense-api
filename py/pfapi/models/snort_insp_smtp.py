from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_smtp_alt_max_command_line_len import SnortInspSmtpAltMaxCommandLineLen


T = TypeVar("T", bound="SnortInspSmtp")


@_attrs_define
class SnortInspSmtp:
    """
    Attributes:
        alt_max_command_line_len (list[SnortInspSmtpAltMaxCommandLineLen] | Unset):
        auth_cmds (str | Unset): commands that initiate an authentication exchange
        b64_decode_depth (int | Unset): depth used to decode the base64 encoded MIME attachments (-1 no limit) {
            -1:65535 }; default -1
        binary_data_cmds (str | Unset): commands that initiate sending of data and use a length value after the command
        bitenc_decode_depth (int | Unset): depth used to extract the non-encoded MIME attachments (-1 no limit) {
            -1:65535 }; default -1
        data_cmds (str | Unset): commands that initiate sending of data with an end of data delimiter
        decompress_pdf (bool | Unset): decompress pdf files in MIME attachments; default false
        decompress_swf (bool | Unset): decompress swf files in MIME attachments; default false
        decompress_zip (bool | Unset): decompress zip files in MIME attachments; default false
        decompress_vba (bool | Unset): decompress MS Office Visual Basic for Applications macro files in MIME
            attachments; default false
        email_hdrs_log_depth (int | Unset): depth for logging email headers { 0:20480 }; default 1464
        ignore_data (bool | Unset): ignore data section of mail; default false
        ignore_tls_data (bool | Unset): ignore TLS-encrypted data when processing rules; default false
        invalid_cmds (str | Unset): alert if this command is sent from client side
        log_email_hdrs (bool | Unset): log the SMTP email headers extracted from SMTP data; default false
        log_filename (bool | Unset): log the MIME attachment filenames extracted from the Content-Disposition header
            within the MIME body; default false
        log_mailfrom (bool | Unset): log the sender’s email address extracted from the MAIL FROM command; default false
        log_rcptto (bool | Unset): log the recipient’s email address extracted from the RCPT TO command; default false
        max_auth_command_line_len (int | Unset): max auth command Line Length { 0:65535 }; default 1000
        max_command_line_len (int | Unset): max Command Line Length { 0:65535 }; default 512
        max_header_line_len (int | Unset): max SMTP DATA header line { 0:65535 }; default 1000
        max_response_line_len (int | Unset): max SMTP response line { 0:65535 }; default 512
        normalize (str | Unset): turns on/off normalization { none | cmds | all }; default none
        normalize_cmds (str | Unset): list of commands to normalize
        qp_decode_depth (int | Unset): quoted-Printable decoding depth (-1 no limit) { -1:65535 }; default -1
        uu_decode_depth (int | Unset): Unix-to-Unix decoding depth (-1 no limit) { -1:65535 }; default -1
        valid_cmds (str | Unset): list of valid commands
        xlink2state (str | Unset): enable/disable xlink2state alert { disable | alert | drop }; default alert
    """

    alt_max_command_line_len: list[SnortInspSmtpAltMaxCommandLineLen] | Unset = UNSET
    auth_cmds: str | Unset = UNSET
    b64_decode_depth: int | Unset = UNSET
    binary_data_cmds: str | Unset = UNSET
    bitenc_decode_depth: int | Unset = UNSET
    data_cmds: str | Unset = UNSET
    decompress_pdf: bool | Unset = UNSET
    decompress_swf: bool | Unset = UNSET
    decompress_zip: bool | Unset = UNSET
    decompress_vba: bool | Unset = UNSET
    email_hdrs_log_depth: int | Unset = UNSET
    ignore_data: bool | Unset = UNSET
    ignore_tls_data: bool | Unset = UNSET
    invalid_cmds: str | Unset = UNSET
    log_email_hdrs: bool | Unset = UNSET
    log_filename: bool | Unset = UNSET
    log_mailfrom: bool | Unset = UNSET
    log_rcptto: bool | Unset = UNSET
    max_auth_command_line_len: int | Unset = UNSET
    max_command_line_len: int | Unset = UNSET
    max_header_line_len: int | Unset = UNSET
    max_response_line_len: int | Unset = UNSET
    normalize: str | Unset = UNSET
    normalize_cmds: str | Unset = UNSET
    qp_decode_depth: int | Unset = UNSET
    uu_decode_depth: int | Unset = UNSET
    valid_cmds: str | Unset = UNSET
    xlink2state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alt_max_command_line_len: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alt_max_command_line_len, Unset):
            alt_max_command_line_len = []
            for alt_max_command_line_len_item_data in self.alt_max_command_line_len:
                alt_max_command_line_len_item = alt_max_command_line_len_item_data.to_dict()
                alt_max_command_line_len.append(alt_max_command_line_len_item)

        auth_cmds = self.auth_cmds

        b64_decode_depth = self.b64_decode_depth

        binary_data_cmds = self.binary_data_cmds

        bitenc_decode_depth = self.bitenc_decode_depth

        data_cmds = self.data_cmds

        decompress_pdf = self.decompress_pdf

        decompress_swf = self.decompress_swf

        decompress_zip = self.decompress_zip

        decompress_vba = self.decompress_vba

        email_hdrs_log_depth = self.email_hdrs_log_depth

        ignore_data = self.ignore_data

        ignore_tls_data = self.ignore_tls_data

        invalid_cmds = self.invalid_cmds

        log_email_hdrs = self.log_email_hdrs

        log_filename = self.log_filename

        log_mailfrom = self.log_mailfrom

        log_rcptto = self.log_rcptto

        max_auth_command_line_len = self.max_auth_command_line_len

        max_command_line_len = self.max_command_line_len

        max_header_line_len = self.max_header_line_len

        max_response_line_len = self.max_response_line_len

        normalize = self.normalize

        normalize_cmds = self.normalize_cmds

        qp_decode_depth = self.qp_decode_depth

        uu_decode_depth = self.uu_decode_depth

        valid_cmds = self.valid_cmds

        xlink2state = self.xlink2state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alt_max_command_line_len is not UNSET:
            field_dict["alt_max_command_line_len"] = alt_max_command_line_len
        if auth_cmds is not UNSET:
            field_dict["auth_cmds"] = auth_cmds
        if b64_decode_depth is not UNSET:
            field_dict["b64_decode_depth"] = b64_decode_depth
        if binary_data_cmds is not UNSET:
            field_dict["binary_data_cmds"] = binary_data_cmds
        if bitenc_decode_depth is not UNSET:
            field_dict["bitenc_decode_depth"] = bitenc_decode_depth
        if data_cmds is not UNSET:
            field_dict["data_cmds"] = data_cmds
        if decompress_pdf is not UNSET:
            field_dict["decompress_pdf"] = decompress_pdf
        if decompress_swf is not UNSET:
            field_dict["decompress_swf"] = decompress_swf
        if decompress_zip is not UNSET:
            field_dict["decompress_zip"] = decompress_zip
        if decompress_vba is not UNSET:
            field_dict["decompress_vba"] = decompress_vba
        if email_hdrs_log_depth is not UNSET:
            field_dict["email_hdrs_log_depth"] = email_hdrs_log_depth
        if ignore_data is not UNSET:
            field_dict["ignore_data"] = ignore_data
        if ignore_tls_data is not UNSET:
            field_dict["ignore_tls_data"] = ignore_tls_data
        if invalid_cmds is not UNSET:
            field_dict["invalid_cmds"] = invalid_cmds
        if log_email_hdrs is not UNSET:
            field_dict["log_email_hdrs"] = log_email_hdrs
        if log_filename is not UNSET:
            field_dict["log_filename"] = log_filename
        if log_mailfrom is not UNSET:
            field_dict["log_mailfrom"] = log_mailfrom
        if log_rcptto is not UNSET:
            field_dict["log_rcptto"] = log_rcptto
        if max_auth_command_line_len is not UNSET:
            field_dict["max_auth_command_line_len"] = max_auth_command_line_len
        if max_command_line_len is not UNSET:
            field_dict["max_command_line_len"] = max_command_line_len
        if max_header_line_len is not UNSET:
            field_dict["max_header_line_len"] = max_header_line_len
        if max_response_line_len is not UNSET:
            field_dict["max_response_line_len"] = max_response_line_len
        if normalize is not UNSET:
            field_dict["normalize"] = normalize
        if normalize_cmds is not UNSET:
            field_dict["normalize_cmds"] = normalize_cmds
        if qp_decode_depth is not UNSET:
            field_dict["qp_decode_depth"] = qp_decode_depth
        if uu_decode_depth is not UNSET:
            field_dict["uu_decode_depth"] = uu_decode_depth
        if valid_cmds is not UNSET:
            field_dict["valid_cmds"] = valid_cmds
        if xlink2state is not UNSET:
            field_dict["xlink2state"] = xlink2state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_smtp_alt_max_command_line_len import SnortInspSmtpAltMaxCommandLineLen

        d = dict(src_dict)
        _alt_max_command_line_len = d.pop("alt_max_command_line_len", UNSET)
        alt_max_command_line_len: list[SnortInspSmtpAltMaxCommandLineLen] | Unset = UNSET
        if _alt_max_command_line_len is not UNSET:
            alt_max_command_line_len = []
            for alt_max_command_line_len_item_data in _alt_max_command_line_len:
                alt_max_command_line_len_item = SnortInspSmtpAltMaxCommandLineLen.from_dict(
                    alt_max_command_line_len_item_data
                )

                alt_max_command_line_len.append(alt_max_command_line_len_item)

        auth_cmds = d.pop("auth_cmds", UNSET)

        b64_decode_depth = d.pop("b64_decode_depth", UNSET)

        binary_data_cmds = d.pop("binary_data_cmds", UNSET)

        bitenc_decode_depth = d.pop("bitenc_decode_depth", UNSET)

        data_cmds = d.pop("data_cmds", UNSET)

        decompress_pdf = d.pop("decompress_pdf", UNSET)

        decompress_swf = d.pop("decompress_swf", UNSET)

        decompress_zip = d.pop("decompress_zip", UNSET)

        decompress_vba = d.pop("decompress_vba", UNSET)

        email_hdrs_log_depth = d.pop("email_hdrs_log_depth", UNSET)

        ignore_data = d.pop("ignore_data", UNSET)

        ignore_tls_data = d.pop("ignore_tls_data", UNSET)

        invalid_cmds = d.pop("invalid_cmds", UNSET)

        log_email_hdrs = d.pop("log_email_hdrs", UNSET)

        log_filename = d.pop("log_filename", UNSET)

        log_mailfrom = d.pop("log_mailfrom", UNSET)

        log_rcptto = d.pop("log_rcptto", UNSET)

        max_auth_command_line_len = d.pop("max_auth_command_line_len", UNSET)

        max_command_line_len = d.pop("max_command_line_len", UNSET)

        max_header_line_len = d.pop("max_header_line_len", UNSET)

        max_response_line_len = d.pop("max_response_line_len", UNSET)

        normalize = d.pop("normalize", UNSET)

        normalize_cmds = d.pop("normalize_cmds", UNSET)

        qp_decode_depth = d.pop("qp_decode_depth", UNSET)

        uu_decode_depth = d.pop("uu_decode_depth", UNSET)

        valid_cmds = d.pop("valid_cmds", UNSET)

        xlink2state = d.pop("xlink2state", UNSET)

        snort_insp_smtp = cls(
            alt_max_command_line_len=alt_max_command_line_len,
            auth_cmds=auth_cmds,
            b64_decode_depth=b64_decode_depth,
            binary_data_cmds=binary_data_cmds,
            bitenc_decode_depth=bitenc_decode_depth,
            data_cmds=data_cmds,
            decompress_pdf=decompress_pdf,
            decompress_swf=decompress_swf,
            decompress_zip=decompress_zip,
            decompress_vba=decompress_vba,
            email_hdrs_log_depth=email_hdrs_log_depth,
            ignore_data=ignore_data,
            ignore_tls_data=ignore_tls_data,
            invalid_cmds=invalid_cmds,
            log_email_hdrs=log_email_hdrs,
            log_filename=log_filename,
            log_mailfrom=log_mailfrom,
            log_rcptto=log_rcptto,
            max_auth_command_line_len=max_auth_command_line_len,
            max_command_line_len=max_command_line_len,
            max_header_line_len=max_header_line_len,
            max_response_line_len=max_response_line_len,
            normalize=normalize,
            normalize_cmds=normalize_cmds,
            qp_decode_depth=qp_decode_depth,
            uu_decode_depth=uu_decode_depth,
            valid_cmds=valid_cmds,
            xlink2state=xlink2state,
        )

        snort_insp_smtp.additional_properties = d
        return snort_insp_smtp

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
