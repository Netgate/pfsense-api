from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_interface_config import SnortInterfaceConfig
    from ..models.snort_pass_list import SnortPassList
    from ..models.snort_rule_download_service import SnortRuleDownloadService
    from ..models.snort_rule_update_settings import SnortRuleUpdateSettings
    from ..models.snort_suppress_list_basic import SnortSuppressListBasic


T = TypeVar("T", bound="SnortConfig")


@_attrs_define
class SnortConfig:
    """Global Snort configuration

    Attributes:
        installed (bool | Unset): if Snort has been installed
        version (str | Unset): installed Snort version
        intf_configs (list[SnortInterfaceConfig] | Unset):
        download_svc (list[SnortRuleDownloadService] | Unset):
        rule_update_settings (SnortRuleUpdateSettings | Unset):
        pass_lists (list[SnortPassList] | Unset):
        suppress_lists (list[SnortSuppressListBasic] | Unset):
    """

    installed: bool | Unset = UNSET
    version: str | Unset = UNSET
    intf_configs: list[SnortInterfaceConfig] | Unset = UNSET
    download_svc: list[SnortRuleDownloadService] | Unset = UNSET
    rule_update_settings: SnortRuleUpdateSettings | Unset = UNSET
    pass_lists: list[SnortPassList] | Unset = UNSET
    suppress_lists: list[SnortSuppressListBasic] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        installed = self.installed

        version = self.version

        intf_configs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.intf_configs, Unset):
            intf_configs = []
            for intf_configs_item_data in self.intf_configs:
                intf_configs_item = intf_configs_item_data.to_dict()
                intf_configs.append(intf_configs_item)

        download_svc: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.download_svc, Unset):
            download_svc = []
            for download_svc_item_data in self.download_svc:
                download_svc_item = download_svc_item_data.to_dict()
                download_svc.append(download_svc_item)

        rule_update_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rule_update_settings, Unset):
            rule_update_settings = self.rule_update_settings.to_dict()

        pass_lists: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pass_lists, Unset):
            pass_lists = []
            for pass_lists_item_data in self.pass_lists:
                pass_lists_item = pass_lists_item_data.to_dict()
                pass_lists.append(pass_lists_item)

        suppress_lists: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.suppress_lists, Unset):
            suppress_lists = []
            for suppress_lists_item_data in self.suppress_lists:
                suppress_lists_item = suppress_lists_item_data.to_dict()
                suppress_lists.append(suppress_lists_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if installed is not UNSET:
            field_dict["installed"] = installed
        if version is not UNSET:
            field_dict["version"] = version
        if intf_configs is not UNSET:
            field_dict["intf_configs"] = intf_configs
        if download_svc is not UNSET:
            field_dict["download_svc"] = download_svc
        if rule_update_settings is not UNSET:
            field_dict["rule_update_settings"] = rule_update_settings
        if pass_lists is not UNSET:
            field_dict["pass_lists"] = pass_lists
        if suppress_lists is not UNSET:
            field_dict["suppress_lists"] = suppress_lists

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_interface_config import SnortInterfaceConfig
        from ..models.snort_pass_list import SnortPassList
        from ..models.snort_rule_download_service import SnortRuleDownloadService
        from ..models.snort_rule_update_settings import SnortRuleUpdateSettings
        from ..models.snort_suppress_list_basic import SnortSuppressListBasic

        d = dict(src_dict)
        installed = d.pop("installed", UNSET)

        version = d.pop("version", UNSET)

        _intf_configs = d.pop("intf_configs", UNSET)
        intf_configs: list[SnortInterfaceConfig] | Unset = UNSET
        if _intf_configs is not UNSET:
            intf_configs = []
            for intf_configs_item_data in _intf_configs:
                intf_configs_item = SnortInterfaceConfig.from_dict(intf_configs_item_data)

                intf_configs.append(intf_configs_item)

        _download_svc = d.pop("download_svc", UNSET)
        download_svc: list[SnortRuleDownloadService] | Unset = UNSET
        if _download_svc is not UNSET:
            download_svc = []
            for download_svc_item_data in _download_svc:
                download_svc_item = SnortRuleDownloadService.from_dict(download_svc_item_data)

                download_svc.append(download_svc_item)

        _rule_update_settings = d.pop("rule_update_settings", UNSET)
        rule_update_settings: SnortRuleUpdateSettings | Unset
        if isinstance(_rule_update_settings, Unset):
            rule_update_settings = UNSET
        else:
            rule_update_settings = SnortRuleUpdateSettings.from_dict(_rule_update_settings)

        _pass_lists = d.pop("pass_lists", UNSET)
        pass_lists: list[SnortPassList] | Unset = UNSET
        if _pass_lists is not UNSET:
            pass_lists = []
            for pass_lists_item_data in _pass_lists:
                pass_lists_item = SnortPassList.from_dict(pass_lists_item_data)

                pass_lists.append(pass_lists_item)

        _suppress_lists = d.pop("suppress_lists", UNSET)
        suppress_lists: list[SnortSuppressListBasic] | Unset = UNSET
        if _suppress_lists is not UNSET:
            suppress_lists = []
            for suppress_lists_item_data in _suppress_lists:
                suppress_lists_item = SnortSuppressListBasic.from_dict(suppress_lists_item_data)

                suppress_lists.append(suppress_lists_item)

        snort_config = cls(
            installed=installed,
            version=version,
            intf_configs=intf_configs,
            download_svc=download_svc,
            rule_update_settings=rule_update_settings,
            pass_lists=pass_lists,
            suppress_lists=suppress_lists,
        )

        snort_config.additional_properties = d
        return snort_config

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
