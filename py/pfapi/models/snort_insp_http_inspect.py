from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspHttpInspect")


@_attrs_define
class SnortInspHttpInspect:
    r"""
    Attributes:
        request_depth (int | Unset): maximum request message body bytes to examine (-1 no limit) { -1:max53 }; default
            -1
        response_depth (int | Unset): maximum response message body bytes to examine (-1 no limit) { -1:max53 }; default
            -1
        unzip (bool | Unset): decompress gzip and deflate message bodies; default true
        maximum_host_length (int | Unset): maximum allowed length for Host header value (-1 no limit) { -1:max53 };
            default -1
        maximum_chunk_length (int | Unset): maximum allowed length for a message body chunk { 0:4294967295 }; default
            4294967295
        maximum_header_length (int | Unset): alert when the length of a header exceeds this value { 0:65535 }; default
            4096
        maximum_headers (int | Unset): alert when the number of headers in a message exceeds this value { 0:65535 };
            default 200
        maximum_pipelined_requests (int | Unset): alert when the number of pipelined requests exceeds this value { 0:99
            }; default 99
        normalize_utf (bool | Unset): normalize charset utf encodings in response bodies; default true
        decompress_pdf (bool | Unset): decompress pdf files in response bodies; default false
        decompress_swf (bool | Unset): decompress swf files in response bodies; default false
        decompress_zip (bool | Unset): decompress zip files in response bodies; default false
        decompress_vba (bool | Unset): decompress MS Office Visual Basic for Applications macro files in response
            bodies; default false
        max_mime_attach (int | Unset): maximum number of mime attachments that will be inspected in a section of a
            request message { 1:65535 }; default 5
        script_detection (bool | Unset): inspect JavaScript immediately upon script end; default false
        normalize_javascript (bool | Unset): use legacy normalizer to normalize JavaScript in response bodies; default
            false
        max_javascript_whitespaces (int | Unset): maximum consecutive whitespaces allowed within the JavaScript
            obfuscated data { 1:65535 }; default 200
        bad_characters (list[str] | Unset):
        ignore_unreserved (str | Unset): do not alert when the specified unreserved characters are percent-encoded in a
            URI.Unreserved characters are 0-9, a-z, A-Z, period, underscore, tilde, and minus. { (optional) }
        percent_u (bool | Unset): normalize %uNNNN and %UNNNN encodings; default false
        utf8 (bool | Unset): normalize 2-byte and 3-byte UTF-8 characters to a single byte; default true
        utf8_bare_byte (bool | Unset): when doing UTF-8 character normalization include bytes that were not percent
            encoded; default false
        iis_unicode (bool | Unset): use IIS unicode code point mapping to normalize characters; default false
        iis_unicode_map_file (str | Unset): file containing code points for IIS unicode. { (optional) }
        iis_unicode_code_page (int | Unset): code page to use from the IIS unicode map file { 0:65535 }; default 1252
        iis_double_decode (bool | Unset): perform double decoding of percent encodings to normalize characters; default
            true
        oversize_dir_length (int | Unset): maximum length for URL directory { 1:65535 }; default 300
        backslash_to_slash (bool | Unset): replace \ with / when normalizing URIs; default true
        plus_to_space (bool | Unset): replace + with <sp> when normalizing URIs; default true
        simplify_path (bool | Unset): reduce URI directory path to simplest form; default true
        xff_headers (str | Unset): specifies the xff type headers to parse and consider in the same order of preference
            as defined; default x-forwarded-for
        request_body_app_detection (bool | Unset): make HTTP request message bodies available for application detection
            (AppId) and other inspectors; default true
        allowed_methods (str | Unset): list of allowed methods
        disallowed_methods (str | Unset): list of disallowed methods
    """

    request_depth: int | Unset = UNSET
    response_depth: int | Unset = UNSET
    unzip: bool | Unset = UNSET
    maximum_host_length: int | Unset = UNSET
    maximum_chunk_length: int | Unset = UNSET
    maximum_header_length: int | Unset = UNSET
    maximum_headers: int | Unset = UNSET
    maximum_pipelined_requests: int | Unset = UNSET
    normalize_utf: bool | Unset = UNSET
    decompress_pdf: bool | Unset = UNSET
    decompress_swf: bool | Unset = UNSET
    decompress_zip: bool | Unset = UNSET
    decompress_vba: bool | Unset = UNSET
    max_mime_attach: int | Unset = UNSET
    script_detection: bool | Unset = UNSET
    normalize_javascript: bool | Unset = UNSET
    max_javascript_whitespaces: int | Unset = UNSET
    bad_characters: list[str] | Unset = UNSET
    ignore_unreserved: str | Unset = UNSET
    percent_u: bool | Unset = UNSET
    utf8: bool | Unset = UNSET
    utf8_bare_byte: bool | Unset = UNSET
    iis_unicode: bool | Unset = UNSET
    iis_unicode_map_file: str | Unset = UNSET
    iis_unicode_code_page: int | Unset = UNSET
    iis_double_decode: bool | Unset = UNSET
    oversize_dir_length: int | Unset = UNSET
    backslash_to_slash: bool | Unset = UNSET
    plus_to_space: bool | Unset = UNSET
    simplify_path: bool | Unset = UNSET
    xff_headers: str | Unset = UNSET
    request_body_app_detection: bool | Unset = UNSET
    allowed_methods: str | Unset = UNSET
    disallowed_methods: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_depth = self.request_depth

        response_depth = self.response_depth

        unzip = self.unzip

        maximum_host_length = self.maximum_host_length

        maximum_chunk_length = self.maximum_chunk_length

        maximum_header_length = self.maximum_header_length

        maximum_headers = self.maximum_headers

        maximum_pipelined_requests = self.maximum_pipelined_requests

        normalize_utf = self.normalize_utf

        decompress_pdf = self.decompress_pdf

        decompress_swf = self.decompress_swf

        decompress_zip = self.decompress_zip

        decompress_vba = self.decompress_vba

        max_mime_attach = self.max_mime_attach

        script_detection = self.script_detection

        normalize_javascript = self.normalize_javascript

        max_javascript_whitespaces = self.max_javascript_whitespaces

        bad_characters: list[str] | Unset = UNSET
        if not isinstance(self.bad_characters, Unset):
            bad_characters = self.bad_characters

        ignore_unreserved = self.ignore_unreserved

        percent_u = self.percent_u

        utf8 = self.utf8

        utf8_bare_byte = self.utf8_bare_byte

        iis_unicode = self.iis_unicode

        iis_unicode_map_file = self.iis_unicode_map_file

        iis_unicode_code_page = self.iis_unicode_code_page

        iis_double_decode = self.iis_double_decode

        oversize_dir_length = self.oversize_dir_length

        backslash_to_slash = self.backslash_to_slash

        plus_to_space = self.plus_to_space

        simplify_path = self.simplify_path

        xff_headers = self.xff_headers

        request_body_app_detection = self.request_body_app_detection

        allowed_methods = self.allowed_methods

        disallowed_methods = self.disallowed_methods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_depth is not UNSET:
            field_dict["request_depth"] = request_depth
        if response_depth is not UNSET:
            field_dict["response_depth"] = response_depth
        if unzip is not UNSET:
            field_dict["unzip"] = unzip
        if maximum_host_length is not UNSET:
            field_dict["maximum_host_length"] = maximum_host_length
        if maximum_chunk_length is not UNSET:
            field_dict["maximum_chunk_length"] = maximum_chunk_length
        if maximum_header_length is not UNSET:
            field_dict["maximum_header_length"] = maximum_header_length
        if maximum_headers is not UNSET:
            field_dict["maximum_headers"] = maximum_headers
        if maximum_pipelined_requests is not UNSET:
            field_dict["maximum_pipelined_requests"] = maximum_pipelined_requests
        if normalize_utf is not UNSET:
            field_dict["normalize_utf"] = normalize_utf
        if decompress_pdf is not UNSET:
            field_dict["decompress_pdf"] = decompress_pdf
        if decompress_swf is not UNSET:
            field_dict["decompress_swf"] = decompress_swf
        if decompress_zip is not UNSET:
            field_dict["decompress_zip"] = decompress_zip
        if decompress_vba is not UNSET:
            field_dict["decompress_vba"] = decompress_vba
        if max_mime_attach is not UNSET:
            field_dict["max_mime_attach"] = max_mime_attach
        if script_detection is not UNSET:
            field_dict["script_detection"] = script_detection
        if normalize_javascript is not UNSET:
            field_dict["normalize_javascript"] = normalize_javascript
        if max_javascript_whitespaces is not UNSET:
            field_dict["max_javascript_whitespaces"] = max_javascript_whitespaces
        if bad_characters is not UNSET:
            field_dict["bad_characters"] = bad_characters
        if ignore_unreserved is not UNSET:
            field_dict["ignore_unreserved"] = ignore_unreserved
        if percent_u is not UNSET:
            field_dict["percent_u"] = percent_u
        if utf8 is not UNSET:
            field_dict["utf8"] = utf8
        if utf8_bare_byte is not UNSET:
            field_dict["utf8_bare_byte"] = utf8_bare_byte
        if iis_unicode is not UNSET:
            field_dict["iis_unicode"] = iis_unicode
        if iis_unicode_map_file is not UNSET:
            field_dict["iis_unicode_map_file"] = iis_unicode_map_file
        if iis_unicode_code_page is not UNSET:
            field_dict["iis_unicode_code_page"] = iis_unicode_code_page
        if iis_double_decode is not UNSET:
            field_dict["iis_double_decode"] = iis_double_decode
        if oversize_dir_length is not UNSET:
            field_dict["oversize_dir_length"] = oversize_dir_length
        if backslash_to_slash is not UNSET:
            field_dict["backslash_to_slash"] = backslash_to_slash
        if plus_to_space is not UNSET:
            field_dict["plus_to_space"] = plus_to_space
        if simplify_path is not UNSET:
            field_dict["simplify_path"] = simplify_path
        if xff_headers is not UNSET:
            field_dict["xff_headers"] = xff_headers
        if request_body_app_detection is not UNSET:
            field_dict["request_body_app_detection"] = request_body_app_detection
        if allowed_methods is not UNSET:
            field_dict["allowed_methods"] = allowed_methods
        if disallowed_methods is not UNSET:
            field_dict["disallowed_methods"] = disallowed_methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        request_depth = d.pop("request_depth", UNSET)

        response_depth = d.pop("response_depth", UNSET)

        unzip = d.pop("unzip", UNSET)

        maximum_host_length = d.pop("maximum_host_length", UNSET)

        maximum_chunk_length = d.pop("maximum_chunk_length", UNSET)

        maximum_header_length = d.pop("maximum_header_length", UNSET)

        maximum_headers = d.pop("maximum_headers", UNSET)

        maximum_pipelined_requests = d.pop("maximum_pipelined_requests", UNSET)

        normalize_utf = d.pop("normalize_utf", UNSET)

        decompress_pdf = d.pop("decompress_pdf", UNSET)

        decompress_swf = d.pop("decompress_swf", UNSET)

        decompress_zip = d.pop("decompress_zip", UNSET)

        decompress_vba = d.pop("decompress_vba", UNSET)

        max_mime_attach = d.pop("max_mime_attach", UNSET)

        script_detection = d.pop("script_detection", UNSET)

        normalize_javascript = d.pop("normalize_javascript", UNSET)

        max_javascript_whitespaces = d.pop("max_javascript_whitespaces", UNSET)

        bad_characters = cast(list[str], d.pop("bad_characters", UNSET))

        ignore_unreserved = d.pop("ignore_unreserved", UNSET)

        percent_u = d.pop("percent_u", UNSET)

        utf8 = d.pop("utf8", UNSET)

        utf8_bare_byte = d.pop("utf8_bare_byte", UNSET)

        iis_unicode = d.pop("iis_unicode", UNSET)

        iis_unicode_map_file = d.pop("iis_unicode_map_file", UNSET)

        iis_unicode_code_page = d.pop("iis_unicode_code_page", UNSET)

        iis_double_decode = d.pop("iis_double_decode", UNSET)

        oversize_dir_length = d.pop("oversize_dir_length", UNSET)

        backslash_to_slash = d.pop("backslash_to_slash", UNSET)

        plus_to_space = d.pop("plus_to_space", UNSET)

        simplify_path = d.pop("simplify_path", UNSET)

        xff_headers = d.pop("xff_headers", UNSET)

        request_body_app_detection = d.pop("request_body_app_detection", UNSET)

        allowed_methods = d.pop("allowed_methods", UNSET)

        disallowed_methods = d.pop("disallowed_methods", UNSET)

        snort_insp_http_inspect = cls(
            request_depth=request_depth,
            response_depth=response_depth,
            unzip=unzip,
            maximum_host_length=maximum_host_length,
            maximum_chunk_length=maximum_chunk_length,
            maximum_header_length=maximum_header_length,
            maximum_headers=maximum_headers,
            maximum_pipelined_requests=maximum_pipelined_requests,
            normalize_utf=normalize_utf,
            decompress_pdf=decompress_pdf,
            decompress_swf=decompress_swf,
            decompress_zip=decompress_zip,
            decompress_vba=decompress_vba,
            max_mime_attach=max_mime_attach,
            script_detection=script_detection,
            normalize_javascript=normalize_javascript,
            max_javascript_whitespaces=max_javascript_whitespaces,
            bad_characters=bad_characters,
            ignore_unreserved=ignore_unreserved,
            percent_u=percent_u,
            utf8=utf8,
            utf8_bare_byte=utf8_bare_byte,
            iis_unicode=iis_unicode,
            iis_unicode_map_file=iis_unicode_map_file,
            iis_unicode_code_page=iis_unicode_code_page,
            iis_double_decode=iis_double_decode,
            oversize_dir_length=oversize_dir_length,
            backslash_to_slash=backslash_to_slash,
            plus_to_space=plus_to_space,
            simplify_path=simplify_path,
            xff_headers=xff_headers,
            request_body_app_detection=request_body_app_detection,
            allowed_methods=allowed_methods,
            disallowed_methods=disallowed_methods,
        )

        snort_insp_http_inspect.additional_properties = d
        return snort_insp_http_inspect

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
