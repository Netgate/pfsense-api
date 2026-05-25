from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_rules_archive import SnortRulesArchive
    from ..models.snort_ruleset_ips_states import SnortRulesetIpsStates
    from ..models.snort_ruleset_rules import SnortRulesetRules
    from ..models.snort_ruleset_so_ips_states import SnortRulesetSoIpsStates
    from ..models.snort_ruleset_so_rules import SnortRulesetSoRules


T = TypeVar("T", bound="SnortRuleset")


@_attrs_define
class SnortRuleset:
    """
    Attributes:
        name (str | Unset): name of ruleset (e.g. emerging-threat, community, lightspd, or filename from URL)
        ruleset_type (str | Unset): type of ruleset (rules files, snapshot, lightspd)
        policies (list[str] | Unset):
        rules (SnortRulesetRules | Unset):
        ips_states (SnortRulesetIpsStates | Unset):
        so_rules (SnortRulesetSoRules | Unset):
        so_ips_states (SnortRulesetSoIpsStates | Unset):
        archive_info (SnortRulesArchive | Unset): Archives are the bundles that contain the rulesets.
            For example, they are provided by Snort Talos subscription or
            from Emerging Threats.
            This object provides metadata about the contents of the archive.
        errors (list[str] | Unset):
    """

    name: str | Unset = UNSET
    ruleset_type: str | Unset = UNSET
    policies: list[str] | Unset = UNSET
    rules: SnortRulesetRules | Unset = UNSET
    ips_states: SnortRulesetIpsStates | Unset = UNSET
    so_rules: SnortRulesetSoRules | Unset = UNSET
    so_ips_states: SnortRulesetSoIpsStates | Unset = UNSET
    archive_info: SnortRulesArchive | Unset = UNSET
    errors: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        ruleset_type = self.ruleset_type

        policies: list[str] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = self.policies

        rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_dict()

        ips_states: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ips_states, Unset):
            ips_states = self.ips_states.to_dict()

        so_rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.so_rules, Unset):
            so_rules = self.so_rules.to_dict()

        so_ips_states: dict[str, Any] | Unset = UNSET
        if not isinstance(self.so_ips_states, Unset):
            so_ips_states = self.so_ips_states.to_dict()

        archive_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.archive_info, Unset):
            archive_info = self.archive_info.to_dict()

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if ruleset_type is not UNSET:
            field_dict["ruleset_type"] = ruleset_type
        if policies is not UNSET:
            field_dict["policies"] = policies
        if rules is not UNSET:
            field_dict["rules"] = rules
        if ips_states is not UNSET:
            field_dict["ips_states"] = ips_states
        if so_rules is not UNSET:
            field_dict["so_rules"] = so_rules
        if so_ips_states is not UNSET:
            field_dict["so_ips_states"] = so_ips_states
        if archive_info is not UNSET:
            field_dict["archive_info"] = archive_info
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_rules_archive import SnortRulesArchive
        from ..models.snort_ruleset_ips_states import SnortRulesetIpsStates
        from ..models.snort_ruleset_rules import SnortRulesetRules
        from ..models.snort_ruleset_so_ips_states import SnortRulesetSoIpsStates
        from ..models.snort_ruleset_so_rules import SnortRulesetSoRules

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        ruleset_type = d.pop("ruleset_type", UNSET)

        policies = cast(list[str], d.pop("policies", UNSET))

        _rules = d.pop("rules", UNSET)
        rules: SnortRulesetRules | Unset
        if isinstance(_rules, Unset):
            rules = UNSET
        else:
            rules = SnortRulesetRules.from_dict(_rules)

        _ips_states = d.pop("ips_states", UNSET)
        ips_states: SnortRulesetIpsStates | Unset
        if isinstance(_ips_states, Unset):
            ips_states = UNSET
        else:
            ips_states = SnortRulesetIpsStates.from_dict(_ips_states)

        _so_rules = d.pop("so_rules", UNSET)
        so_rules: SnortRulesetSoRules | Unset
        if isinstance(_so_rules, Unset):
            so_rules = UNSET
        else:
            so_rules = SnortRulesetSoRules.from_dict(_so_rules)

        _so_ips_states = d.pop("so_ips_states", UNSET)
        so_ips_states: SnortRulesetSoIpsStates | Unset
        if isinstance(_so_ips_states, Unset):
            so_ips_states = UNSET
        else:
            so_ips_states = SnortRulesetSoIpsStates.from_dict(_so_ips_states)

        _archive_info = d.pop("archive_info", UNSET)
        archive_info: SnortRulesArchive | Unset
        if isinstance(_archive_info, Unset):
            archive_info = UNSET
        else:
            archive_info = SnortRulesArchive.from_dict(_archive_info)

        errors = cast(list[str], d.pop("errors", UNSET))

        snort_ruleset = cls(
            name=name,
            ruleset_type=ruleset_type,
            policies=policies,
            rules=rules,
            ips_states=ips_states,
            so_rules=so_rules,
            so_ips_states=so_ips_states,
            archive_info=archive_info,
            errors=errors,
        )

        snort_ruleset.additional_properties = d
        return snort_ruleset

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
