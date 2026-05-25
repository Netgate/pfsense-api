from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_client_export_config import OpenVPNClientExportConfig
    from ..models.open_vpn_remote_access_server import OpenVPNRemoteAccessServer
    from ..models.text_value import TextValue


T = TypeVar("T", bound="OpenVPNClientExportConfigs")


@_attrs_define
class OpenVPNClientExportConfigs:
    """
    Attributes:
        config (list[OpenVPNClientExportConfig] | Unset):
        server_list (list[OpenVPNRemoteAccessServer] | Unset):
        useaddr_list (list[TextValue] | Unset):
    """

    config: list[OpenVPNClientExportConfig] | Unset = UNSET
    server_list: list[OpenVPNRemoteAccessServer] | Unset = UNSET
    useaddr_list: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = []
            for config_item_data in self.config:
                config_item = config_item_data.to_dict()
                config.append(config_item)

        server_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.server_list, Unset):
            server_list = []
            for server_list_item_data in self.server_list:
                server_list_item = server_list_item_data.to_dict()
                server_list.append(server_list_item)

        useaddr_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.useaddr_list, Unset):
            useaddr_list = []
            for useaddr_list_item_data in self.useaddr_list:
                useaddr_list_item = useaddr_list_item_data.to_dict()
                useaddr_list.append(useaddr_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if server_list is not UNSET:
            field_dict["server_list"] = server_list
        if useaddr_list is not UNSET:
            field_dict["useaddr_list"] = useaddr_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_vpn_client_export_config import OpenVPNClientExportConfig
        from ..models.open_vpn_remote_access_server import OpenVPNRemoteAccessServer
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: list[OpenVPNClientExportConfig] | Unset = UNSET
        if _config is not UNSET:
            config = []
            for config_item_data in _config:
                config_item = OpenVPNClientExportConfig.from_dict(config_item_data)

                config.append(config_item)

        _server_list = d.pop("server_list", UNSET)
        server_list: list[OpenVPNRemoteAccessServer] | Unset = UNSET
        if _server_list is not UNSET:
            server_list = []
            for server_list_item_data in _server_list:
                server_list_item = OpenVPNRemoteAccessServer.from_dict(server_list_item_data)

                server_list.append(server_list_item)

        _useaddr_list = d.pop("useaddr_list", UNSET)
        useaddr_list: list[TextValue] | Unset = UNSET
        if _useaddr_list is not UNSET:
            useaddr_list = []
            for useaddr_list_item_data in _useaddr_list:
                useaddr_list_item = TextValue.from_dict(useaddr_list_item_data)

                useaddr_list.append(useaddr_list_item)

        open_vpn_client_export_configs = cls(
            config=config,
            server_list=server_list,
            useaddr_list=useaddr_list,
        )

        open_vpn_client_export_configs.additional_properties = d
        return open_vpn_client_export_configs

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
