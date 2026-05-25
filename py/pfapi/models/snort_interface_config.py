from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.snort_interface_config_block_addr_opt import SnortInterfaceConfigBlockAddrOpt
from ..models.snort_interface_config_detection_method import SnortInterfaceConfigDetectionMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_binder import SnortInspBinder
    from ..models.snort_inspectors import SnortInspectors
    from ..models.snort_interface_rulesets_opt import SnortInterfaceRulesetsOpt
    from ..models.snort_overrides import SnortOverrides
    from ..models.snort_reputation_config import SnortReputationConfig


T = TypeVar("T", bound="SnortInterfaceConfig")


@_attrs_define
class SnortInterfaceConfig:
    """Per-interface group Snort configuration

    Attributes:
        id (str | Unset): (readonly) unique identifier for this configuration
        log_id (int | Unset): (readonly) id of applied to -G/--logid of snort command
        enable (bool | Unset): enable service to run
        status (str | Unset): (readonly) current running state - started, stopped, error
        descr (str | Unset): user provided description
        interfaces (list[str] | Unset):
        inline_ips (bool | Unset): enable inline IPS; not all systems support this
        home_networks (list[str] | Unset):
        external_networks (list[str] | Unset):
        overrides (SnortOverrides | Unset): Snort configuration variables that can be overridden
        use_syslog (bool | Unset): send alerts to system log
        use_alert_unified2 (bool | Unset): write alerts to unified2 logs instead of CSV
        block_on_alert (bool | Unset): block offending address triggering alert
        kill_states (bool | Unset): kill the firewall states for blocked address
        block_addr_opt (SnortInterfaceConfigBlockAddrOpt | Unset): which address to block - src, dst, or both (default)
        detection_method (SnortInterfaceConfigDetectionMethod | Unset): fast pattern matching algorithm (ac_bnfa,
            ac_full, hyperscan)
        split_any_any (bool | Unset): split ANY-ANY port group
        search_optimize (bool | Unset): enable search optimization
        stream_inserts (bool | Unset): do not evaulate stream inserted packets against the detection algorithm
        csum_disabled (bool | Unset): disable checksum checking to improve performance
        pass_list_name (str | Unset): pass list reference (to SnortPassList)
        suppress_list_name (str | Unset): suppress list reference (to SnortSuppressList)
        custom_head_include (str | Unset): path to custom Lua script, to be included at the start of
            the main snort.lua script. This should reside in /var/db/snort/config.
        custom_tail_include (str | Unset): path to custom Lua script, to be included at the end of
            the main snort.lua script. This should reside in /var/db/snort/config.
        bindings (list[SnortInspBinder] | Unset):
        inspectors (SnortInspectors | Unset): Snort inspectors, also known is preprocessors, are modules
            that perform a variety of functions. The configuration of each
            inspector is complex and should only have defaults overridden
            with care.
        reputation (SnortReputationConfig | Unset):
        rule_sets (SnortInterfaceRulesetsOpt | Unset):
        raw_config (str | Unset): output - the raw configuration that was generated or user explicitly set
        config_path (str | Unset): output - the location of the interface's config files
        custom_raw_config (str | Unset): input - user provided raw config override
    """

    id: str | Unset = UNSET
    log_id: int | Unset = UNSET
    enable: bool | Unset = UNSET
    status: str | Unset = UNSET
    descr: str | Unset = UNSET
    interfaces: list[str] | Unset = UNSET
    inline_ips: bool | Unset = UNSET
    home_networks: list[str] | Unset = UNSET
    external_networks: list[str] | Unset = UNSET
    overrides: SnortOverrides | Unset = UNSET
    use_syslog: bool | Unset = UNSET
    use_alert_unified2: bool | Unset = UNSET
    block_on_alert: bool | Unset = UNSET
    kill_states: bool | Unset = UNSET
    block_addr_opt: SnortInterfaceConfigBlockAddrOpt | Unset = UNSET
    detection_method: SnortInterfaceConfigDetectionMethod | Unset = UNSET
    split_any_any: bool | Unset = UNSET
    search_optimize: bool | Unset = UNSET
    stream_inserts: bool | Unset = UNSET
    csum_disabled: bool | Unset = UNSET
    pass_list_name: str | Unset = UNSET
    suppress_list_name: str | Unset = UNSET
    custom_head_include: str | Unset = UNSET
    custom_tail_include: str | Unset = UNSET
    bindings: list[SnortInspBinder] | Unset = UNSET
    inspectors: SnortInspectors | Unset = UNSET
    reputation: SnortReputationConfig | Unset = UNSET
    rule_sets: SnortInterfaceRulesetsOpt | Unset = UNSET
    raw_config: str | Unset = UNSET
    config_path: str | Unset = UNSET
    custom_raw_config: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        log_id = self.log_id

        enable = self.enable

        status = self.status

        descr = self.descr

        interfaces: list[str] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        inline_ips = self.inline_ips

        home_networks: list[str] | Unset = UNSET
        if not isinstance(self.home_networks, Unset):
            home_networks = self.home_networks

        external_networks: list[str] | Unset = UNSET
        if not isinstance(self.external_networks, Unset):
            external_networks = self.external_networks

        overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = self.overrides.to_dict()

        use_syslog = self.use_syslog

        use_alert_unified2 = self.use_alert_unified2

        block_on_alert = self.block_on_alert

        kill_states = self.kill_states

        block_addr_opt: str | Unset = UNSET
        if not isinstance(self.block_addr_opt, Unset):
            block_addr_opt = self.block_addr_opt.value

        detection_method: str | Unset = UNSET
        if not isinstance(self.detection_method, Unset):
            detection_method = self.detection_method.value

        split_any_any = self.split_any_any

        search_optimize = self.search_optimize

        stream_inserts = self.stream_inserts

        csum_disabled = self.csum_disabled

        pass_list_name = self.pass_list_name

        suppress_list_name = self.suppress_list_name

        custom_head_include = self.custom_head_include

        custom_tail_include = self.custom_tail_include

        bindings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bindings, Unset):
            bindings = []
            for bindings_item_data in self.bindings:
                bindings_item = bindings_item_data.to_dict()
                bindings.append(bindings_item)

        inspectors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inspectors, Unset):
            inspectors = self.inspectors.to_dict()

        reputation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reputation, Unset):
            reputation = self.reputation.to_dict()

        rule_sets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rule_sets, Unset):
            rule_sets = self.rule_sets.to_dict()

        raw_config = self.raw_config

        config_path = self.config_path

        custom_raw_config = self.custom_raw_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if log_id is not UNSET:
            field_dict["log_id"] = log_id
        if enable is not UNSET:
            field_dict["enable"] = enable
        if status is not UNSET:
            field_dict["status"] = status
        if descr is not UNSET:
            field_dict["descr"] = descr
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if inline_ips is not UNSET:
            field_dict["inline_ips"] = inline_ips
        if home_networks is not UNSET:
            field_dict["home_networks"] = home_networks
        if external_networks is not UNSET:
            field_dict["external_networks"] = external_networks
        if overrides is not UNSET:
            field_dict["overrides"] = overrides
        if use_syslog is not UNSET:
            field_dict["use_syslog"] = use_syslog
        if use_alert_unified2 is not UNSET:
            field_dict["use_alert_unified2"] = use_alert_unified2
        if block_on_alert is not UNSET:
            field_dict["block_on_alert"] = block_on_alert
        if kill_states is not UNSET:
            field_dict["kill_states"] = kill_states
        if block_addr_opt is not UNSET:
            field_dict["block_addr_opt"] = block_addr_opt
        if detection_method is not UNSET:
            field_dict["detection_method"] = detection_method
        if split_any_any is not UNSET:
            field_dict["split_any_any"] = split_any_any
        if search_optimize is not UNSET:
            field_dict["search_optimize"] = search_optimize
        if stream_inserts is not UNSET:
            field_dict["stream_inserts"] = stream_inserts
        if csum_disabled is not UNSET:
            field_dict["csum_disabled"] = csum_disabled
        if pass_list_name is not UNSET:
            field_dict["pass_list_name"] = pass_list_name
        if suppress_list_name is not UNSET:
            field_dict["suppress_list_name"] = suppress_list_name
        if custom_head_include is not UNSET:
            field_dict["custom_head_include"] = custom_head_include
        if custom_tail_include is not UNSET:
            field_dict["custom_tail_include"] = custom_tail_include
        if bindings is not UNSET:
            field_dict["bindings"] = bindings
        if inspectors is not UNSET:
            field_dict["inspectors"] = inspectors
        if reputation is not UNSET:
            field_dict["reputation"] = reputation
        if rule_sets is not UNSET:
            field_dict["rule_sets"] = rule_sets
        if raw_config is not UNSET:
            field_dict["raw_config"] = raw_config
        if config_path is not UNSET:
            field_dict["config_path"] = config_path
        if custom_raw_config is not UNSET:
            field_dict["custom_raw_config"] = custom_raw_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_binder import SnortInspBinder
        from ..models.snort_inspectors import SnortInspectors
        from ..models.snort_interface_rulesets_opt import SnortInterfaceRulesetsOpt
        from ..models.snort_overrides import SnortOverrides
        from ..models.snort_reputation_config import SnortReputationConfig

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        log_id = d.pop("log_id", UNSET)

        enable = d.pop("enable", UNSET)

        status = d.pop("status", UNSET)

        descr = d.pop("descr", UNSET)

        interfaces = cast(list[str], d.pop("interfaces", UNSET))

        inline_ips = d.pop("inline_ips", UNSET)

        home_networks = cast(list[str], d.pop("home_networks", UNSET))

        external_networks = cast(list[str], d.pop("external_networks", UNSET))

        _overrides = d.pop("overrides", UNSET)
        overrides: SnortOverrides | Unset
        if isinstance(_overrides, Unset):
            overrides = UNSET
        else:
            overrides = SnortOverrides.from_dict(_overrides)

        use_syslog = d.pop("use_syslog", UNSET)

        use_alert_unified2 = d.pop("use_alert_unified2", UNSET)

        block_on_alert = d.pop("block_on_alert", UNSET)

        kill_states = d.pop("kill_states", UNSET)

        _block_addr_opt = d.pop("block_addr_opt", UNSET)
        block_addr_opt: SnortInterfaceConfigBlockAddrOpt | Unset
        if isinstance(_block_addr_opt, Unset):
            block_addr_opt = UNSET
        else:
            block_addr_opt = SnortInterfaceConfigBlockAddrOpt(_block_addr_opt)

        _detection_method = d.pop("detection_method", UNSET)
        detection_method: SnortInterfaceConfigDetectionMethod | Unset
        if isinstance(_detection_method, Unset):
            detection_method = UNSET
        else:
            detection_method = SnortInterfaceConfigDetectionMethod(_detection_method)

        split_any_any = d.pop("split_any_any", UNSET)

        search_optimize = d.pop("search_optimize", UNSET)

        stream_inserts = d.pop("stream_inserts", UNSET)

        csum_disabled = d.pop("csum_disabled", UNSET)

        pass_list_name = d.pop("pass_list_name", UNSET)

        suppress_list_name = d.pop("suppress_list_name", UNSET)

        custom_head_include = d.pop("custom_head_include", UNSET)

        custom_tail_include = d.pop("custom_tail_include", UNSET)

        _bindings = d.pop("bindings", UNSET)
        bindings: list[SnortInspBinder] | Unset = UNSET
        if _bindings is not UNSET:
            bindings = []
            for bindings_item_data in _bindings:
                bindings_item = SnortInspBinder.from_dict(bindings_item_data)

                bindings.append(bindings_item)

        _inspectors = d.pop("inspectors", UNSET)
        inspectors: SnortInspectors | Unset
        if isinstance(_inspectors, Unset):
            inspectors = UNSET
        else:
            inspectors = SnortInspectors.from_dict(_inspectors)

        _reputation = d.pop("reputation", UNSET)
        reputation: SnortReputationConfig | Unset
        if isinstance(_reputation, Unset):
            reputation = UNSET
        else:
            reputation = SnortReputationConfig.from_dict(_reputation)

        _rule_sets = d.pop("rule_sets", UNSET)
        rule_sets: SnortInterfaceRulesetsOpt | Unset
        if isinstance(_rule_sets, Unset):
            rule_sets = UNSET
        else:
            rule_sets = SnortInterfaceRulesetsOpt.from_dict(_rule_sets)

        raw_config = d.pop("raw_config", UNSET)

        config_path = d.pop("config_path", UNSET)

        custom_raw_config = d.pop("custom_raw_config", UNSET)

        snort_interface_config = cls(
            id=id,
            log_id=log_id,
            enable=enable,
            status=status,
            descr=descr,
            interfaces=interfaces,
            inline_ips=inline_ips,
            home_networks=home_networks,
            external_networks=external_networks,
            overrides=overrides,
            use_syslog=use_syslog,
            use_alert_unified2=use_alert_unified2,
            block_on_alert=block_on_alert,
            kill_states=kill_states,
            block_addr_opt=block_addr_opt,
            detection_method=detection_method,
            split_any_any=split_any_any,
            search_optimize=search_optimize,
            stream_inserts=stream_inserts,
            csum_disabled=csum_disabled,
            pass_list_name=pass_list_name,
            suppress_list_name=suppress_list_name,
            custom_head_include=custom_head_include,
            custom_tail_include=custom_tail_include,
            bindings=bindings,
            inspectors=inspectors,
            reputation=reputation,
            rule_sets=rule_sets,
            raw_config=raw_config,
            config_path=config_path,
            custom_raw_config=custom_raw_config,
        )

        snort_interface_config.additional_properties = d
        return snort_interface_config

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
