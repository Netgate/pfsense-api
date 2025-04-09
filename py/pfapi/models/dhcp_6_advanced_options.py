from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dhcp6AdvancedOptions")


@_attrs_define
class Dhcp6AdvancedOptions:
    """
    Attributes:
        duid (Union[Unset, str]):
        client_id (Union[Unset, str]):
        dhcp6_pfxdel_len (Union[Unset, int]): delegated prefix length
        prefix_selected_interface (Union[Unset, str]):
        ifreq_information_only_enable (Union[Unset, bool]):
        send_options (Union[Unset, str]):
        request_options (Union[Unset, str]):
        enable_override_options (Union[Unset, bool]):
        override_options (Union[Unset, str]):
        config_file_override_path (Union[Unset, str]):
    """

    duid: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    dhcp6_pfxdel_len: Union[Unset, int] = UNSET
    prefix_selected_interface: Union[Unset, str] = UNSET
    ifreq_information_only_enable: Union[Unset, bool] = UNSET
    send_options: Union[Unset, str] = UNSET
    request_options: Union[Unset, str] = UNSET
    enable_override_options: Union[Unset, bool] = UNSET
    override_options: Union[Unset, str] = UNSET
    config_file_override_path: Union[Unset, str] = UNSET
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
        field_dict.update({})
        if duid is not UNSET:
            field_dict["duid"] = duid
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if dhcp6_pfxdel_len is not UNSET:
            field_dict["dhcp6_pfxdel_len"] = dhcp6_pfxdel_len
        if prefix_selected_interface is not UNSET:
            field_dict["prefix_selected_interface"] = prefix_selected_interface
        if ifreq_information_only_enable is not UNSET:
            field_dict["ifreq_information_only_enable"] = ifreq_information_only_enable
        if send_options is not UNSET:
            field_dict["send_options"] = send_options
        if request_options is not UNSET:
            field_dict["request_options"] = request_options
        if enable_override_options is not UNSET:
            field_dict["enable_override_options"] = enable_override_options
        if override_options is not UNSET:
            field_dict["override_options"] = override_options
        if config_file_override_path is not UNSET:
            field_dict["config_file_override_path"] = config_file_override_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid", UNSET)

        client_id = d.pop("client_id", UNSET)

        dhcp6_pfxdel_len = d.pop("dhcp6_pfxdel_len", UNSET)

        prefix_selected_interface = d.pop("prefix_selected_interface", UNSET)

        ifreq_information_only_enable = d.pop("ifreq_information_only_enable", UNSET)

        send_options = d.pop("send_options", UNSET)

        request_options = d.pop("request_options", UNSET)

        enable_override_options = d.pop("enable_override_options", UNSET)

        override_options = d.pop("override_options", UNSET)

        config_file_override_path = d.pop("config_file_override_path", UNSET)

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
