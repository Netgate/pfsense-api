from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_netflow_rules import SnortInspNetflowRules


T = TypeVar("T", bound="SnortInspNetflow")


@_attrs_define
class SnortInspNetflow:
    """
    Attributes:
        dump_file (str | Unset): file name to dump netflow cache on shutdown; won’t dump by default
        update_timeout (int | Unset): the interval at which the system updates host cache information { 0:max32 };
            default 3600
        rules (list[SnortInspNetflowRules] | Unset):
        flow_memcap (int | Unset): maximum memory for flow record cache in bytes, 0 = unlimited { 0:maxSZ }; default 0
        template_memcap (int | Unset): maximum memory for template cache in bytes, 0 = unlimited { 0:maxSZ }; default 0
        netflow_service_id_path (str | Unset): path to file containing service IDs for NetFlow
    """

    dump_file: str | Unset = UNSET
    update_timeout: int | Unset = UNSET
    rules: list[SnortInspNetflowRules] | Unset = UNSET
    flow_memcap: int | Unset = UNSET
    template_memcap: int | Unset = UNSET
    netflow_service_id_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dump_file = self.dump_file

        update_timeout = self.update_timeout

        rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        flow_memcap = self.flow_memcap

        template_memcap = self.template_memcap

        netflow_service_id_path = self.netflow_service_id_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dump_file is not UNSET:
            field_dict["dump_file"] = dump_file
        if update_timeout is not UNSET:
            field_dict["update_timeout"] = update_timeout
        if rules is not UNSET:
            field_dict["rules"] = rules
        if flow_memcap is not UNSET:
            field_dict["flow_memcap"] = flow_memcap
        if template_memcap is not UNSET:
            field_dict["template_memcap"] = template_memcap
        if netflow_service_id_path is not UNSET:
            field_dict["netflow_service_id_path"] = netflow_service_id_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_netflow_rules import SnortInspNetflowRules

        d = dict(src_dict)
        dump_file = d.pop("dump_file", UNSET)

        update_timeout = d.pop("update_timeout", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: list[SnortInspNetflowRules] | Unset = UNSET
        if _rules is not UNSET:
            rules = []
            for rules_item_data in _rules:
                rules_item = SnortInspNetflowRules.from_dict(rules_item_data)

                rules.append(rules_item)

        flow_memcap = d.pop("flow_memcap", UNSET)

        template_memcap = d.pop("template_memcap", UNSET)

        netflow_service_id_path = d.pop("netflow_service_id_path", UNSET)

        snort_insp_netflow = cls(
            dump_file=dump_file,
            update_timeout=update_timeout,
            rules=rules,
            flow_memcap=flow_memcap,
            template_memcap=template_memcap,
            netflow_service_id_path=netflow_service_id_path,
        )

        snort_insp_netflow.additional_properties = d
        return snort_insp_netflow

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
