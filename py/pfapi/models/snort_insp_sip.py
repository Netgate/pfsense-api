from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspSip")


@_attrs_define
class SnortInspSip:
    """
    Attributes:
        ignore_call_channel (bool | Unset): enables the support for ignoring audio/video data channel; default false
        max_call_id_len (int | Unset): maximum call id field size { 0:65535 }; default 256
        max_contact_len (int | Unset): maximum contact field size { 0:65535 }; default 256
        max_content_len (int | Unset): maximum content length of the message body { 0:65535 }; default 1024
        max_dialogs (int | Unset): maximum number of dialogs within one stream session { 1:max32 }; default 4
        max_from_len (int | Unset): maximum from field size { 0:65535 }; default 256
        max_request_name_len (int | Unset): maximum request name field size { 0:65535 }; default 20
        max_to_len (int | Unset): maximum to field size { 0:65535 }; default 256
        max_uri_len (int | Unset): maximum request uri field size { 0:65535 }; default 256
        max_via_len (int | Unset): maximum via field size { 0:65535 }; default 1024
        methods (str | Unset): list of methods to check in SIP messages; default invite
        sip_timeout (int | Unset): SIP Timeout value in milliseconds { 0: }; default 0
        sip_media_timeout (int | Unset): SIP Media timeout milliseconds { 0: }; default 0
        sip_invite_timeout (int | Unset): SIP Invite timeout milliseconds { 0: }; default 0
        sip_disconnect_timeout (int | Unset): SIP Disconnect timeout milliseconds { 0: }; default 0
    """

    ignore_call_channel: bool | Unset = UNSET
    max_call_id_len: int | Unset = UNSET
    max_contact_len: int | Unset = UNSET
    max_content_len: int | Unset = UNSET
    max_dialogs: int | Unset = UNSET
    max_from_len: int | Unset = UNSET
    max_request_name_len: int | Unset = UNSET
    max_to_len: int | Unset = UNSET
    max_uri_len: int | Unset = UNSET
    max_via_len: int | Unset = UNSET
    methods: str | Unset = UNSET
    sip_timeout: int | Unset = UNSET
    sip_media_timeout: int | Unset = UNSET
    sip_invite_timeout: int | Unset = UNSET
    sip_disconnect_timeout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ignore_call_channel = self.ignore_call_channel

        max_call_id_len = self.max_call_id_len

        max_contact_len = self.max_contact_len

        max_content_len = self.max_content_len

        max_dialogs = self.max_dialogs

        max_from_len = self.max_from_len

        max_request_name_len = self.max_request_name_len

        max_to_len = self.max_to_len

        max_uri_len = self.max_uri_len

        max_via_len = self.max_via_len

        methods = self.methods

        sip_timeout = self.sip_timeout

        sip_media_timeout = self.sip_media_timeout

        sip_invite_timeout = self.sip_invite_timeout

        sip_disconnect_timeout = self.sip_disconnect_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ignore_call_channel is not UNSET:
            field_dict["ignore_call_channel"] = ignore_call_channel
        if max_call_id_len is not UNSET:
            field_dict["max_call_id_len"] = max_call_id_len
        if max_contact_len is not UNSET:
            field_dict["max_contact_len"] = max_contact_len
        if max_content_len is not UNSET:
            field_dict["max_content_len"] = max_content_len
        if max_dialogs is not UNSET:
            field_dict["max_dialogs"] = max_dialogs
        if max_from_len is not UNSET:
            field_dict["max_from_len"] = max_from_len
        if max_request_name_len is not UNSET:
            field_dict["max_request_name_len"] = max_request_name_len
        if max_to_len is not UNSET:
            field_dict["max_to_len"] = max_to_len
        if max_uri_len is not UNSET:
            field_dict["max_uri_len"] = max_uri_len
        if max_via_len is not UNSET:
            field_dict["max_via_len"] = max_via_len
        if methods is not UNSET:
            field_dict["methods"] = methods
        if sip_timeout is not UNSET:
            field_dict["sip_timeout"] = sip_timeout
        if sip_media_timeout is not UNSET:
            field_dict["sip_media_timeout"] = sip_media_timeout
        if sip_invite_timeout is not UNSET:
            field_dict["sip_invite_timeout"] = sip_invite_timeout
        if sip_disconnect_timeout is not UNSET:
            field_dict["sip_disconnect_timeout"] = sip_disconnect_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ignore_call_channel = d.pop("ignore_call_channel", UNSET)

        max_call_id_len = d.pop("max_call_id_len", UNSET)

        max_contact_len = d.pop("max_contact_len", UNSET)

        max_content_len = d.pop("max_content_len", UNSET)

        max_dialogs = d.pop("max_dialogs", UNSET)

        max_from_len = d.pop("max_from_len", UNSET)

        max_request_name_len = d.pop("max_request_name_len", UNSET)

        max_to_len = d.pop("max_to_len", UNSET)

        max_uri_len = d.pop("max_uri_len", UNSET)

        max_via_len = d.pop("max_via_len", UNSET)

        methods = d.pop("methods", UNSET)

        sip_timeout = d.pop("sip_timeout", UNSET)

        sip_media_timeout = d.pop("sip_media_timeout", UNSET)

        sip_invite_timeout = d.pop("sip_invite_timeout", UNSET)

        sip_disconnect_timeout = d.pop("sip_disconnect_timeout", UNSET)

        snort_insp_sip = cls(
            ignore_call_channel=ignore_call_channel,
            max_call_id_len=max_call_id_len,
            max_contact_len=max_contact_len,
            max_content_len=max_content_len,
            max_dialogs=max_dialogs,
            max_from_len=max_from_len,
            max_request_name_len=max_request_name_len,
            max_to_len=max_to_len,
            max_uri_len=max_uri_len,
            max_via_len=max_via_len,
            methods=methods,
            sip_timeout=sip_timeout,
            sip_media_timeout=sip_media_timeout,
            sip_invite_timeout=sip_invite_timeout,
            sip_disconnect_timeout=sip_disconnect_timeout,
        )

        snort_insp_sip.additional_properties = d
        return snort_insp_sip

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
