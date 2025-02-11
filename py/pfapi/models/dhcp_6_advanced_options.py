from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Dhcp6AdvancedOptions")


@_attrs_define
class Dhcp6AdvancedOptions:
    """
    Attributes:
        duid (str):
        client_id (str):
        dhcp6_pfxdel_len (int): delegated prefix length
        prefix_selected_interface (str):
        ifreq_information_only_enable (bool):
        send_options (str):
        request_options (str):
        enable_override_options (bool):
        override_options (str):
        config_file_override_path (str):
    """

    duid: str
    client_id: str
    dhcp6_pfxdel_len: int
    prefix_selected_interface: str
    ifreq_information_only_enable: bool
    send_options: str
    request_options: str
    enable_override_options: bool
    override_options: str
    config_file_override_path: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid

        client_id = self.client_id

        dhcp6_pfxdel_len = self.dhcp6_pfxdel_len

        prefix_selected_interface = self.prefix_selected_interface

        ifreq_information_only_enable = self.ifreq_information_only_enable

        send_options = self.send_options

        request_options = self.request_options

        enable_override_options = self.enable_override_options

        override_options = self.override_options

        config_file_override_path = self.config_file_override_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "client_id": client_id,
                "dhcp6_pfxdel_len": dhcp6_pfxdel_len,
                "prefix_selected_interface": prefix_selected_interface,
                "ifreq_information_only_enable": ifreq_information_only_enable,
                "send_options": send_options,
                "request_options": request_options,
                "enable_override_options": enable_override_options,
                "override_options": override_options,
                "config_file_override_path": config_file_override_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        client_id = d.pop("client_id")

        dhcp6_pfxdel_len = d.pop("dhcp6_pfxdel_len")

        prefix_selected_interface = d.pop("prefix_selected_interface")

        ifreq_information_only_enable = d.pop("ifreq_information_only_enable")

        send_options = d.pop("send_options")

        request_options = d.pop("request_options")

        enable_override_options = d.pop("enable_override_options")

        override_options = d.pop("override_options")

        config_file_override_path = d.pop("config_file_override_path")

        dhcp_6_advanced_options = cls(
            duid=duid,
            client_id=client_id,
            dhcp6_pfxdel_len=dhcp6_pfxdel_len,
            prefix_selected_interface=prefix_selected_interface,
            ifreq_information_only_enable=ifreq_information_only_enable,
            send_options=send_options,
            request_options=request_options,
            enable_override_options=enable_override_options,
            override_options=override_options,
            config_file_override_path=config_file_override_path,
        )

        dhcp_6_advanced_options.additional_properties = d
        return dhcp_6_advanced_options

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
