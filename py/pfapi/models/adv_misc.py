from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvMisc")


@_attrs_define
class AdvMisc:
    """
    Attributes:
        available_kernel_memory (int | Unset):
        block_external_services (bool | Unset):
        crypto_hardware (str | Unset):
        do_not_send_uniqueid (bool | Unset):
        dpinger_dont_add_static_routes (bool | Unset):
        gw_down_kill_states (bool | Unset):
        harddiskstandby (str | Unset):
        hwpstate (bool | Unset):
        hwpstate_control_level (str | Unset):
        hwpstate_epp (int | Unset):
        ipsec_mb (bool | Unset):
        keep_failover_states (bool | Unset):
        lb_use_sticky (bool | Unset):
        mds (str | Unset):
        mds_disable (str | Unset): 0=disabled, 1=VERW instruction mitigation, 2=software sequence mitigation,
            3=automatic VERW or software
        php_memory_limit (int | Unset):
        powerd_ac_mode (str | Unset):
        powerd_battery_mode (str | Unset):
        powerd_enable (bool | Unset):
        powerd_normal_mode (str | Unset):
        proxypass (str | Unset):
        proxypass_confirm (str | Unset):
        proxyport (int | Unset):
        proxyurl (str | Unset):
        proxyuser (str | Unset):
        pti (str | Unset):
        pti_disabled (bool | Unset):
        remove_failover_states_default (str | Unset):
        schedule_states (bool | Unset):
        skip_rules_gw_down (bool | Unset):
        srctrack (str | Unset):
        thermal_hardware (str | Unset):
        use_mfs_tmp_size (int | Unset):
        use_mfs_tmpvar (bool | Unset):
        use_mfs_var_size (int | Unset):
        watchdogd_enable (bool | Unset):
        watchdogd_timeout (str | Unset):
    """

    available_kernel_memory: int | Unset = UNSET
    block_external_services: bool | Unset = UNSET
    crypto_hardware: str | Unset = UNSET
    do_not_send_uniqueid: bool | Unset = UNSET
    dpinger_dont_add_static_routes: bool | Unset = UNSET
    gw_down_kill_states: bool | Unset = UNSET
    harddiskstandby: str | Unset = UNSET
    hwpstate: bool | Unset = UNSET
    hwpstate_control_level: str | Unset = UNSET
    hwpstate_epp: int | Unset = UNSET
    ipsec_mb: bool | Unset = UNSET
    keep_failover_states: bool | Unset = UNSET
    lb_use_sticky: bool | Unset = UNSET
    mds: str | Unset = UNSET
    mds_disable: str | Unset = UNSET
    php_memory_limit: int | Unset = UNSET
    powerd_ac_mode: str | Unset = UNSET
    powerd_battery_mode: str | Unset = UNSET
    powerd_enable: bool | Unset = UNSET
    powerd_normal_mode: str | Unset = UNSET
    proxypass: str | Unset = UNSET
    proxypass_confirm: str | Unset = UNSET
    proxyport: int | Unset = UNSET
    proxyurl: str | Unset = UNSET
    proxyuser: str | Unset = UNSET
    pti: str | Unset = UNSET
    pti_disabled: bool | Unset = UNSET
    remove_failover_states_default: str | Unset = UNSET
    schedule_states: bool | Unset = UNSET
    skip_rules_gw_down: bool | Unset = UNSET
    srctrack: str | Unset = UNSET
    thermal_hardware: str | Unset = UNSET
    use_mfs_tmp_size: int | Unset = UNSET
    use_mfs_tmpvar: bool | Unset = UNSET
    use_mfs_var_size: int | Unset = UNSET
    watchdogd_enable: bool | Unset = UNSET
    watchdogd_timeout: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_kernel_memory = self.available_kernel_memory

        block_external_services = self.block_external_services

        crypto_hardware = self.crypto_hardware

        do_not_send_uniqueid = self.do_not_send_uniqueid

        dpinger_dont_add_static_routes = self.dpinger_dont_add_static_routes

        gw_down_kill_states = self.gw_down_kill_states

        harddiskstandby = self.harddiskstandby

        hwpstate = self.hwpstate

        hwpstate_control_level = self.hwpstate_control_level

        hwpstate_epp = self.hwpstate_epp

        ipsec_mb = self.ipsec_mb

        keep_failover_states = self.keep_failover_states

        lb_use_sticky = self.lb_use_sticky

        mds = self.mds

        mds_disable = self.mds_disable

        php_memory_limit = self.php_memory_limit

        powerd_ac_mode = self.powerd_ac_mode

        powerd_battery_mode = self.powerd_battery_mode

        powerd_enable = self.powerd_enable

        powerd_normal_mode = self.powerd_normal_mode

        proxypass = self.proxypass

        proxypass_confirm = self.proxypass_confirm

        proxyport = self.proxyport

        proxyurl = self.proxyurl

        proxyuser = self.proxyuser

        pti = self.pti

        pti_disabled = self.pti_disabled

        remove_failover_states_default = self.remove_failover_states_default

        schedule_states = self.schedule_states

        skip_rules_gw_down = self.skip_rules_gw_down

        srctrack = self.srctrack

        thermal_hardware = self.thermal_hardware

        use_mfs_tmp_size = self.use_mfs_tmp_size

        use_mfs_tmpvar = self.use_mfs_tmpvar

        use_mfs_var_size = self.use_mfs_var_size

        watchdogd_enable = self.watchdogd_enable

        watchdogd_timeout = self.watchdogd_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_kernel_memory is not UNSET:
            field_dict["available_kernel_memory"] = available_kernel_memory
        if block_external_services is not UNSET:
            field_dict["block_external_services"] = block_external_services
        if crypto_hardware is not UNSET:
            field_dict["crypto_hardware"] = crypto_hardware
        if do_not_send_uniqueid is not UNSET:
            field_dict["do_not_send_uniqueid"] = do_not_send_uniqueid
        if dpinger_dont_add_static_routes is not UNSET:
            field_dict["dpinger_dont_add_static_routes"] = dpinger_dont_add_static_routes
        if gw_down_kill_states is not UNSET:
            field_dict["gw_down_kill_states"] = gw_down_kill_states
        if harddiskstandby is not UNSET:
            field_dict["harddiskstandby"] = harddiskstandby
        if hwpstate is not UNSET:
            field_dict["hwpstate"] = hwpstate
        if hwpstate_control_level is not UNSET:
            field_dict["hwpstate_control_level"] = hwpstate_control_level
        if hwpstate_epp is not UNSET:
            field_dict["hwpstate_epp"] = hwpstate_epp
        if ipsec_mb is not UNSET:
            field_dict["ipsec_mb"] = ipsec_mb
        if keep_failover_states is not UNSET:
            field_dict["keep_failover_states"] = keep_failover_states
        if lb_use_sticky is not UNSET:
            field_dict["lb_use_sticky"] = lb_use_sticky
        if mds is not UNSET:
            field_dict["mds"] = mds
        if mds_disable is not UNSET:
            field_dict["mds_disable"] = mds_disable
        if php_memory_limit is not UNSET:
            field_dict["php_memory_limit"] = php_memory_limit
        if powerd_ac_mode is not UNSET:
            field_dict["powerd_ac_mode"] = powerd_ac_mode
        if powerd_battery_mode is not UNSET:
            field_dict["powerd_battery_mode"] = powerd_battery_mode
        if powerd_enable is not UNSET:
            field_dict["powerd_enable"] = powerd_enable
        if powerd_normal_mode is not UNSET:
            field_dict["powerd_normal_mode"] = powerd_normal_mode
        if proxypass is not UNSET:
            field_dict["proxypass"] = proxypass
        if proxypass_confirm is not UNSET:
            field_dict["proxypass_confirm"] = proxypass_confirm
        if proxyport is not UNSET:
            field_dict["proxyport"] = proxyport
        if proxyurl is not UNSET:
            field_dict["proxyurl"] = proxyurl
        if proxyuser is not UNSET:
            field_dict["proxyuser"] = proxyuser
        if pti is not UNSET:
            field_dict["pti"] = pti
        if pti_disabled is not UNSET:
            field_dict["pti_disabled"] = pti_disabled
        if remove_failover_states_default is not UNSET:
            field_dict["remove_failover_states_default"] = remove_failover_states_default
        if schedule_states is not UNSET:
            field_dict["schedule_states"] = schedule_states
        if skip_rules_gw_down is not UNSET:
            field_dict["skip_rules_gw_down"] = skip_rules_gw_down
        if srctrack is not UNSET:
            field_dict["srctrack"] = srctrack
        if thermal_hardware is not UNSET:
            field_dict["thermal_hardware"] = thermal_hardware
        if use_mfs_tmp_size is not UNSET:
            field_dict["use_mfs_tmp_size"] = use_mfs_tmp_size
        if use_mfs_tmpvar is not UNSET:
            field_dict["use_mfs_tmpvar"] = use_mfs_tmpvar
        if use_mfs_var_size is not UNSET:
            field_dict["use_mfs_var_size"] = use_mfs_var_size
        if watchdogd_enable is not UNSET:
            field_dict["watchdogd_enable"] = watchdogd_enable
        if watchdogd_timeout is not UNSET:
            field_dict["watchdogd_timeout"] = watchdogd_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_kernel_memory = d.pop("available_kernel_memory", UNSET)

        block_external_services = d.pop("block_external_services", UNSET)

        crypto_hardware = d.pop("crypto_hardware", UNSET)

        do_not_send_uniqueid = d.pop("do_not_send_uniqueid", UNSET)

        dpinger_dont_add_static_routes = d.pop("dpinger_dont_add_static_routes", UNSET)

        gw_down_kill_states = d.pop("gw_down_kill_states", UNSET)

        harddiskstandby = d.pop("harddiskstandby", UNSET)

        hwpstate = d.pop("hwpstate", UNSET)

        hwpstate_control_level = d.pop("hwpstate_control_level", UNSET)

        hwpstate_epp = d.pop("hwpstate_epp", UNSET)

        ipsec_mb = d.pop("ipsec_mb", UNSET)

        keep_failover_states = d.pop("keep_failover_states", UNSET)

        lb_use_sticky = d.pop("lb_use_sticky", UNSET)

        mds = d.pop("mds", UNSET)

        mds_disable = d.pop("mds_disable", UNSET)

        php_memory_limit = d.pop("php_memory_limit", UNSET)

        powerd_ac_mode = d.pop("powerd_ac_mode", UNSET)

        powerd_battery_mode = d.pop("powerd_battery_mode", UNSET)

        powerd_enable = d.pop("powerd_enable", UNSET)

        powerd_normal_mode = d.pop("powerd_normal_mode", UNSET)

        proxypass = d.pop("proxypass", UNSET)

        proxypass_confirm = d.pop("proxypass_confirm", UNSET)

        proxyport = d.pop("proxyport", UNSET)

        proxyurl = d.pop("proxyurl", UNSET)

        proxyuser = d.pop("proxyuser", UNSET)

        pti = d.pop("pti", UNSET)

        pti_disabled = d.pop("pti_disabled", UNSET)

        remove_failover_states_default = d.pop("remove_failover_states_default", UNSET)

        schedule_states = d.pop("schedule_states", UNSET)

        skip_rules_gw_down = d.pop("skip_rules_gw_down", UNSET)

        srctrack = d.pop("srctrack", UNSET)

        thermal_hardware = d.pop("thermal_hardware", UNSET)

        use_mfs_tmp_size = d.pop("use_mfs_tmp_size", UNSET)

        use_mfs_tmpvar = d.pop("use_mfs_tmpvar", UNSET)

        use_mfs_var_size = d.pop("use_mfs_var_size", UNSET)

        watchdogd_enable = d.pop("watchdogd_enable", UNSET)

        watchdogd_timeout = d.pop("watchdogd_timeout", UNSET)

        adv_misc = cls(
            available_kernel_memory=available_kernel_memory,
            block_external_services=block_external_services,
            crypto_hardware=crypto_hardware,
            do_not_send_uniqueid=do_not_send_uniqueid,
            dpinger_dont_add_static_routes=dpinger_dont_add_static_routes,
            gw_down_kill_states=gw_down_kill_states,
            harddiskstandby=harddiskstandby,
            hwpstate=hwpstate,
            hwpstate_control_level=hwpstate_control_level,
            hwpstate_epp=hwpstate_epp,
            ipsec_mb=ipsec_mb,
            keep_failover_states=keep_failover_states,
            lb_use_sticky=lb_use_sticky,
            mds=mds,
            mds_disable=mds_disable,
            php_memory_limit=php_memory_limit,
            powerd_ac_mode=powerd_ac_mode,
            powerd_battery_mode=powerd_battery_mode,
            powerd_enable=powerd_enable,
            powerd_normal_mode=powerd_normal_mode,
            proxypass=proxypass,
            proxypass_confirm=proxypass_confirm,
            proxyport=proxyport,
            proxyurl=proxyurl,
            proxyuser=proxyuser,
            pti=pti,
            pti_disabled=pti_disabled,
            remove_failover_states_default=remove_failover_states_default,
            schedule_states=schedule_states,
            skip_rules_gw_down=skip_rules_gw_down,
            srctrack=srctrack,
            thermal_hardware=thermal_hardware,
            use_mfs_tmp_size=use_mfs_tmp_size,
            use_mfs_tmpvar=use_mfs_tmpvar,
            use_mfs_var_size=use_mfs_var_size,
            watchdogd_enable=watchdogd_enable,
            watchdogd_timeout=watchdogd_timeout,
        )

        adv_misc.additional_properties = d
        return adv_misc

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
