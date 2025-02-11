from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DhcpAdvancedOptions")


@_attrs_define
class DhcpAdvancedOptions:
    """
    Attributes:
        req_timeout (str): protocol timeout
        req_retry (str): try again duration
        req_select_timeout (str): offer selection timeout when multiple are received
        req_restart (str): time before requiring new lease
        req_backoff_cutoff (str): backoff algorithm duration
        req_initial_interval (str): interval between initial requests
        send_options (str): options to send to DHCP server
        request_options (str): options wanting from DHCP server
        required_options (str): options that must be received in the offer to be accepted
        option_modifiers (str): modify options from offer received
        enable_override_options (bool):
        override_options (str): override options received
        config_file_override_path (str):
    """

    req_timeout: str
    req_retry: str
    req_select_timeout: str
    req_restart: str
    req_backoff_cutoff: str
    req_initial_interval: str
    send_options: str
    request_options: str
    required_options: str
    option_modifiers: str
    enable_override_options: bool
    override_options: str
    config_file_override_path: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "req_timeout": req_timeout,
                "req_retry": req_retry,
                "req_select_timeout": req_select_timeout,
                "req_restart": req_restart,
                "req_backoff_cutoff": req_backoff_cutoff,
                "req_initial_interval": req_initial_interval,
                "send_options": send_options,
                "request_options": request_options,
                "required_options": required_options,
                "option_modifiers": option_modifiers,
                "enable_override_options": enable_override_options,
                "override_options": override_options,
                "config_file_override_path": config_file_override_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        req_timeout = d.pop("req_timeout")

        req_retry = d.pop("req_retry")

        req_select_timeout = d.pop("req_select_timeout")

        req_restart = d.pop("req_restart")

        req_backoff_cutoff = d.pop("req_backoff_cutoff")

        req_initial_interval = d.pop("req_initial_interval")

        send_options = d.pop("send_options")

        request_options = d.pop("request_options")

        required_options = d.pop("required_options")

        option_modifiers = d.pop("option_modifiers")

        enable_override_options = d.pop("enable_override_options")

        override_options = d.pop("override_options")

        config_file_override_path = d.pop("config_file_override_path")

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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
