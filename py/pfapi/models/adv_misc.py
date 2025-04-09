from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvMisc")


@_attrs_define
class AdvMisc:
    """
    Attributes:
        available_kernel_memory (Union[Unset, int]):
        block_external_services (Union[Unset, bool]):
        crypto_hardware (Union[Unset, str]):
        do_not_send_uniqueid (Union[Unset, bool]):
        dpinger_dont_add_static_routes (Union[Unset, bool]):
        gw_down_kill_states (Union[Unset, bool]):
        harddiskstandby (Union[Unset, str]):
        hwpstate (Union[Unset, bool]):
        hwpstate_control_level (Union[Unset, str]):
        hwpstate_epp (Union[Unset, int]):
        ipsec_mb (Union[Unset, bool]):
        keep_failover_states (Union[Unset, bool]):
        lb_use_sticky (Union[Unset, bool]):
        mds (Union[Unset, str]):
        mds_disable (Union[Unset, str]): 0=disabled, 1=VERW instruction mitigation, 2=software sequence mitigation,
            3=automatic VERW or software
        php_memory_limit (Union[Unset, int]):
        powerd_ac_mode (Union[Unset, str]):
        powerd_battery_mode (Union[Unset, str]):
        powerd_enable (Union[Unset, bool]):
        powerd_normal_mode (Union[Unset, str]):
        proxypass (Union[Unset, str]):
        proxypass_confirm (Union[Unset, str]):
        proxyport (Union[Unset, int]):
        proxyurl (Union[Unset, str]):
        proxyuser (Union[Unset, str]):
        pti (Union[Unset, str]):
        pti_disabled (Union[Unset, bool]):
        remove_failover_states_default (Union[Unset, str]):
        schedule_states (Union[Unset, bool]):
        skip_rules_gw_down (Union[Unset, bool]):
        srctrack (Union[Unset, str]):
        thermal_hardware (Union[Unset, str]):
        use_mfs_tmp_size (Union[Unset, int]):
        use_mfs_tmpvar (Union[Unset, bool]):
        use_mfs_var_size (Union[Unset, int]):
        watchdogd_enable (Union[Unset, bool]):
        watchdogd_timeout (Union[Unset, str]):
    """

    available_kernel_memory: Union[Unset, int] = UNSET
    block_external_services: Union[Unset, bool] = UNSET
    crypto_hardware: Union[Unset, str] = UNSET
    do_not_send_uniqueid: Union[Unset, bool] = UNSET
    dpinger_dont_add_static_routes: Union[Unset, bool] = UNSET
    gw_down_kill_states: Union[Unset, bool] = UNSET
    harddiskstandby: Union[Unset, str] = UNSET
    hwpstate: Union[Unset, bool] = UNSET
    hwpstate_control_level: Union[Unset, str] = UNSET
    hwpstate_epp: Union[Unset, int] = UNSET
    ipsec_mb: Union[Unset, bool] = UNSET
    keep_failover_states: Union[Unset, bool] = UNSET
    lb_use_sticky: Union[Unset, bool] = UNSET
    mds: Union[Unset, str] = UNSET
    mds_disable: Union[Unset, str] = UNSET
    php_memory_limit: Union[Unset, int] = UNSET
    powerd_ac_mode: Union[Unset, str] = UNSET
    powerd_battery_mode: Union[Unset, str] = UNSET
    powerd_enable: Union[Unset, bool] = UNSET
    powerd_normal_mode: Union[Unset, str] = UNSET
    proxypass: Union[Unset, str] = UNSET
    proxypass_confirm: Union[Unset, str] = UNSET
    proxyport: Union[Unset, int] = UNSET
    proxyurl: Union[Unset, str] = UNSET
    proxyuser: Union[Unset, str] = UNSET
    pti: Union[Unset, str] = UNSET
    pti_disabled: Union[Unset, bool] = UNSET
    remove_failover_states_default: Union[Unset, str] = UNSET
    schedule_states: Union[Unset, bool] = UNSET
    skip_rules_gw_down: Union[Unset, bool] = UNSET
    srctrack: Union[Unset, str] = UNSET
    thermal_hardware: Union[Unset, str] = UNSET
    use_mfs_tmp_size: Union[Unset, int] = UNSET
    use_mfs_tmpvar: Union[Unset, bool] = UNSET
    use_mfs_var_size: Union[Unset, int] = UNSET
    watchdogd_enable: Union[Unset, bool] = UNSET
    watchdogd_timeout: Union[Unset, str] = UNSET
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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
