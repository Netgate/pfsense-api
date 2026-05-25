from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspAppid")


@_attrs_define
class SnortInspAppid:
    """
    Attributes:
        memcap (int | Unset): max size of the service cache before we start pruning the cache { 1024:maxSZ }; default
            1048576
        log_stats (bool | Unset): enable logging of appid statistics; default false
        app_stats_period (int | Unset): time period for collecting and logging appid statistics { 1:max32 }; default 300
        app_stats_rollover_size (int | Unset): max file size for appid stats before rolling over the log file { 0:max32
            }; default 20971520
        app_detector_dir (str | Unset): directory to load appid detectors from
        list_odp_detectors (bool | Unset): enable logging of odp detectors statistics; default false
        tp_appid_path (str | Unset): path to third party appid dynamic library
        tp_appid_config (str | Unset): path to third party appid configuration file
        tp_appid_stats_enable (bool | Unset): enable collection of stats and print stats on exit in third party module
        tp_appid_config_dump (bool | Unset): print third party configuration on startup
        log_all_sessions (bool | Unset): enable logging of all appid sessions; default false
        enable_rna_filter (bool | Unset): monitor only the networks specified in rna configuration; default false
        rna_conf_path (str | Unset): path to rna configuration file
    """

    memcap: int | Unset = UNSET
    log_stats: bool | Unset = UNSET
    app_stats_period: int | Unset = UNSET
    app_stats_rollover_size: int | Unset = UNSET
    app_detector_dir: str | Unset = UNSET
    list_odp_detectors: bool | Unset = UNSET
    tp_appid_path: str | Unset = UNSET
    tp_appid_config: str | Unset = UNSET
    tp_appid_stats_enable: bool | Unset = UNSET
    tp_appid_config_dump: bool | Unset = UNSET
    log_all_sessions: bool | Unset = UNSET
    enable_rna_filter: bool | Unset = UNSET
    rna_conf_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memcap = self.memcap

        log_stats = self.log_stats

        app_stats_period = self.app_stats_period

        app_stats_rollover_size = self.app_stats_rollover_size

        app_detector_dir = self.app_detector_dir

        list_odp_detectors = self.list_odp_detectors

        tp_appid_path = self.tp_appid_path

        tp_appid_config = self.tp_appid_config

        tp_appid_stats_enable = self.tp_appid_stats_enable

        tp_appid_config_dump = self.tp_appid_config_dump

        log_all_sessions = self.log_all_sessions

        enable_rna_filter = self.enable_rna_filter

        rna_conf_path = self.rna_conf_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if memcap is not UNSET:
            field_dict["memcap"] = memcap
        if log_stats is not UNSET:
            field_dict["log_stats"] = log_stats
        if app_stats_period is not UNSET:
            field_dict["app_stats_period"] = app_stats_period
        if app_stats_rollover_size is not UNSET:
            field_dict["app_stats_rollover_size"] = app_stats_rollover_size
        if app_detector_dir is not UNSET:
            field_dict["app_detector_dir"] = app_detector_dir
        if list_odp_detectors is not UNSET:
            field_dict["list_odp_detectors"] = list_odp_detectors
        if tp_appid_path is not UNSET:
            field_dict["tp_appid_path"] = tp_appid_path
        if tp_appid_config is not UNSET:
            field_dict["tp_appid_config"] = tp_appid_config
        if tp_appid_stats_enable is not UNSET:
            field_dict["tp_appid_stats_enable"] = tp_appid_stats_enable
        if tp_appid_config_dump is not UNSET:
            field_dict["tp_appid_config_dump"] = tp_appid_config_dump
        if log_all_sessions is not UNSET:
            field_dict["log_all_sessions"] = log_all_sessions
        if enable_rna_filter is not UNSET:
            field_dict["enable_rna_filter"] = enable_rna_filter
        if rna_conf_path is not UNSET:
            field_dict["rna_conf_path"] = rna_conf_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        memcap = d.pop("memcap", UNSET)

        log_stats = d.pop("log_stats", UNSET)

        app_stats_period = d.pop("app_stats_period", UNSET)

        app_stats_rollover_size = d.pop("app_stats_rollover_size", UNSET)

        app_detector_dir = d.pop("app_detector_dir", UNSET)

        list_odp_detectors = d.pop("list_odp_detectors", UNSET)

        tp_appid_path = d.pop("tp_appid_path", UNSET)

        tp_appid_config = d.pop("tp_appid_config", UNSET)

        tp_appid_stats_enable = d.pop("tp_appid_stats_enable", UNSET)

        tp_appid_config_dump = d.pop("tp_appid_config_dump", UNSET)

        log_all_sessions = d.pop("log_all_sessions", UNSET)

        enable_rna_filter = d.pop("enable_rna_filter", UNSET)

        rna_conf_path = d.pop("rna_conf_path", UNSET)

        snort_insp_appid = cls(
            memcap=memcap,
            log_stats=log_stats,
            app_stats_period=app_stats_period,
            app_stats_rollover_size=app_stats_rollover_size,
            app_detector_dir=app_detector_dir,
            list_odp_detectors=list_odp_detectors,
            tp_appid_path=tp_appid_path,
            tp_appid_config=tp_appid_config,
            tp_appid_stats_enable=tp_appid_stats_enable,
            tp_appid_config_dump=tp_appid_config_dump,
            log_all_sessions=log_all_sessions,
            enable_rna_filter=enable_rna_filter,
            rna_conf_path=rna_conf_path,
        )

        snort_insp_appid.additional_properties = d
        return snort_insp_appid

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
