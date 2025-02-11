from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdvMisc")


@_attrs_define
class AdvMisc:
    """
    Attributes:
        available_kernel_memory (int):
        block_external_services (bool):
        crypto_hardware (str):
        do_not_send_uniqueid (bool):
        dpinger_dont_add_static_routes (bool):
        gw_down_kill_states (bool):
        harddiskstandby (str):
        hwpstate (bool):
        hwpstate_control_level (str):
        hwpstate_epp (int):
        ipsec_mb (bool):
        keep_failover_states (bool):
        lb_use_sticky (bool):
        mds (str):
        mds_disable (str):
        php_memory_limit (int):
        powerd_ac_mode (str):
        powerd_battery_mode (str):
        powerd_enable (bool):
        powerd_normal_mode (str):
        proxypass (str):
        proxypass_confirm (str):
        proxyport (int):
        proxyurl (str):
        proxyuser (str):
        pti (str):
        pti_disabled (bool):
        remove_failover_states_default (str):
        schedule_states (bool):
        skip_rules_gw_down (bool):
        srctrack (str):
        thermal_hardware (str):
        use_mfs_tmp_size (int):
        use_mfs_tmpvar (bool):
        use_mfs_var_size (int):
        watchdogd_enable (bool):
        watchdogd_timeout (str):
    """

    available_kernel_memory: int
    block_external_services: bool
    crypto_hardware: str
    do_not_send_uniqueid: bool
    dpinger_dont_add_static_routes: bool
    gw_down_kill_states: bool
    harddiskstandby: str
    hwpstate: bool
    hwpstate_control_level: str
    hwpstate_epp: int
    ipsec_mb: bool
    keep_failover_states: bool
    lb_use_sticky: bool
    mds: str
    mds_disable: str
    php_memory_limit: int
    powerd_ac_mode: str
    powerd_battery_mode: str
    powerd_enable: bool
    powerd_normal_mode: str
    proxypass: str
    proxypass_confirm: str
    proxyport: int
    proxyurl: str
    proxyuser: str
    pti: str
    pti_disabled: bool
    remove_failover_states_default: str
    schedule_states: bool
    skip_rules_gw_down: bool
    srctrack: str
    thermal_hardware: str
    use_mfs_tmp_size: int
    use_mfs_tmpvar: bool
    use_mfs_var_size: int
    watchdogd_enable: bool
    watchdogd_timeout: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available_kernel_memory": available_kernel_memory,
                "block_external_services": block_external_services,
                "crypto_hardware": crypto_hardware,
                "do_not_send_uniqueid": do_not_send_uniqueid,
                "dpinger_dont_add_static_routes": dpinger_dont_add_static_routes,
                "gw_down_kill_states": gw_down_kill_states,
                "harddiskstandby": harddiskstandby,
                "hwpstate": hwpstate,
                "hwpstate_control_level": hwpstate_control_level,
                "hwpstate_epp": hwpstate_epp,
                "ipsec_mb": ipsec_mb,
                "keep_failover_states": keep_failover_states,
                "lb_use_sticky": lb_use_sticky,
                "mds": mds,
                "mds_disable": mds_disable,
                "php_memory_limit": php_memory_limit,
                "powerd_ac_mode": powerd_ac_mode,
                "powerd_battery_mode": powerd_battery_mode,
                "powerd_enable": powerd_enable,
                "powerd_normal_mode": powerd_normal_mode,
                "proxypass": proxypass,
                "proxypass_confirm": proxypass_confirm,
                "proxyport": proxyport,
                "proxyurl": proxyurl,
                "proxyuser": proxyuser,
                "pti": pti,
                "pti_disabled": pti_disabled,
                "remove_failover_states_default": remove_failover_states_default,
                "schedule_states": schedule_states,
                "skip_rules_gw_down": skip_rules_gw_down,
                "srctrack": srctrack,
                "thermal_hardware": thermal_hardware,
                "use_mfs_tmp_size": use_mfs_tmp_size,
                "use_mfs_tmpvar": use_mfs_tmpvar,
                "use_mfs_var_size": use_mfs_var_size,
                "watchdogd_enable": watchdogd_enable,
                "watchdogd_timeout": watchdogd_timeout,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        available_kernel_memory = d.pop("available_kernel_memory")

        block_external_services = d.pop("block_external_services")

        crypto_hardware = d.pop("crypto_hardware")

        do_not_send_uniqueid = d.pop("do_not_send_uniqueid")

        dpinger_dont_add_static_routes = d.pop("dpinger_dont_add_static_routes")

        gw_down_kill_states = d.pop("gw_down_kill_states")

        harddiskstandby = d.pop("harddiskstandby")

        hwpstate = d.pop("hwpstate")

        hwpstate_control_level = d.pop("hwpstate_control_level")

        hwpstate_epp = d.pop("hwpstate_epp")

        ipsec_mb = d.pop("ipsec_mb")

        keep_failover_states = d.pop("keep_failover_states")

        lb_use_sticky = d.pop("lb_use_sticky")

        mds = d.pop("mds")

        mds_disable = d.pop("mds_disable")

        php_memory_limit = d.pop("php_memory_limit")

        powerd_ac_mode = d.pop("powerd_ac_mode")

        powerd_battery_mode = d.pop("powerd_battery_mode")

        powerd_enable = d.pop("powerd_enable")

        powerd_normal_mode = d.pop("powerd_normal_mode")

        proxypass = d.pop("proxypass")

        proxypass_confirm = d.pop("proxypass_confirm")

        proxyport = d.pop("proxyport")

        proxyurl = d.pop("proxyurl")

        proxyuser = d.pop("proxyuser")

        pti = d.pop("pti")

        pti_disabled = d.pop("pti_disabled")

        remove_failover_states_default = d.pop("remove_failover_states_default")

        schedule_states = d.pop("schedule_states")

        skip_rules_gw_down = d.pop("skip_rules_gw_down")

        srctrack = d.pop("srctrack")

        thermal_hardware = d.pop("thermal_hardware")

        use_mfs_tmp_size = d.pop("use_mfs_tmp_size")

        use_mfs_tmpvar = d.pop("use_mfs_tmpvar")

        use_mfs_var_size = d.pop("use_mfs_var_size")

        watchdogd_enable = d.pop("watchdogd_enable")

        watchdogd_timeout = d.pop("watchdogd_timeout")

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
