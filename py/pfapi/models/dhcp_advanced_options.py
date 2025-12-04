from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpAdvancedOptions")


@_attrs_define
class DhcpAdvancedOptions:
    """
    Attributes:
        req_timeout (str | Unset): protocol timeout
        req_retry (str | Unset): try again duration
        req_select_timeout (str | Unset): offer selection timeout when multiple are received
        req_restart (str | Unset): time before requiring new lease
        req_backoff_cutoff (str | Unset): backoff algorithm duration
        req_initial_interval (str | Unset): interval between initial requests
        send_options (str | Unset): options to send to DHCP server
        request_options (str | Unset): options wanting from DHCP server
        required_options (str | Unset): options that must be received in the offer to be accepted
        option_modifiers (str | Unset): modify options from offer received
        enable_override_options (bool | Unset):
        override_options (str | Unset): override options received
        config_file_override_path (str | Unset):
    """

    req_timeout: str | Unset = UNSET
    req_retry: str | Unset = UNSET
    req_select_timeout: str | Unset = UNSET
    req_restart: str | Unset = UNSET
    req_backoff_cutoff: str | Unset = UNSET
    req_initial_interval: str | Unset = UNSET
    send_options: str | Unset = UNSET
    request_options: str | Unset = UNSET
    required_options: str | Unset = UNSET
    option_modifiers: str | Unset = UNSET
    enable_override_options: bool | Unset = UNSET
    override_options: str | Unset = UNSET
    config_file_override_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        req_timeout = self.req_timeout

        req_retry = self.req_retry

        req_select_timeout = self.req_select_timeout

        req_restart = self.req_restart

        req_backoff_cutoff = self.req_backoff_cutoff

        req_initial_interval = self.req_initial_interval

        send_options = self.send_options

        request_options = self.request_options

        required_options = self.required_options

        option_modifiers = self.option_modifiers

        enable_override_options = self.enable_override_options

        override_options = self.override_options

        config_file_override_path = self.config_file_override_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if req_timeout is not UNSET:
            field_dict["req_timeout"] = req_timeout
        if req_retry is not UNSET:
            field_dict["req_retry"] = req_retry
        if req_select_timeout is not UNSET:
            field_dict["req_select_timeout"] = req_select_timeout
        if req_restart is not UNSET:
            field_dict["req_restart"] = req_restart
        if req_backoff_cutoff is not UNSET:
            field_dict["req_backoff_cutoff"] = req_backoff_cutoff
        if req_initial_interval is not UNSET:
            field_dict["req_initial_interval"] = req_initial_interval
        if send_options is not UNSET:
            field_dict["send_options"] = send_options
        if request_options is not UNSET:
            field_dict["request_options"] = request_options
        if required_options is not UNSET:
            field_dict["required_options"] = required_options
        if option_modifiers is not UNSET:
            field_dict["option_modifiers"] = option_modifiers
        if enable_override_options is not UNSET:
            field_dict["enable_override_options"] = enable_override_options
        if override_options is not UNSET:
            field_dict["override_options"] = override_options
        if config_file_override_path is not UNSET:
            field_dict["config_file_override_path"] = config_file_override_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        req_timeout = d.pop("req_timeout", UNSET)

        req_retry = d.pop("req_retry", UNSET)

        req_select_timeout = d.pop("req_select_timeout", UNSET)

        req_restart = d.pop("req_restart", UNSET)

        req_backoff_cutoff = d.pop("req_backoff_cutoff", UNSET)

        req_initial_interval = d.pop("req_initial_interval", UNSET)

        send_options = d.pop("send_options", UNSET)

        request_options = d.pop("request_options", UNSET)

        required_options = d.pop("required_options", UNSET)

        option_modifiers = d.pop("option_modifiers", UNSET)

        enable_override_options = d.pop("enable_override_options", UNSET)

        override_options = d.pop("override_options", UNSET)

        config_file_override_path = d.pop("config_file_override_path", UNSET)

        dhcp_advanced_options = cls(
            req_timeout=req_timeout,
            req_retry=req_retry,
            req_select_timeout=req_select_timeout,
            req_restart=req_restart,
            req_backoff_cutoff=req_backoff_cutoff,
            req_initial_interval=req_initial_interval,
            send_options=send_options,
            request_options=request_options,
            required_options=required_options,
            option_modifiers=option_modifiers,
            enable_override_options=enable_override_options,
            override_options=override_options,
            config_file_override_path=config_file_override_path,
        )

        dhcp_advanced_options.additional_properties = d
        return dhcp_advanced_options

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
