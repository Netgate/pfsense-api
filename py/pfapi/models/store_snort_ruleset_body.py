from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

if TYPE_CHECKING:
    from ..models.snort_rules_upload_req import SnortRulesUploadReq


T = TypeVar("T", bound="StoreSnortRulesetBody")


@_attrs_define
class StoreSnortRulesetBody:
    """
    Attributes:
        req (SnortRulesUploadReq | Unset):
        rules (File | Unset):
    """

    req: SnortRulesUploadReq | Unset = UNSET
    rules: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        req: dict[str, Any] | Unset = UNSET
        if not isinstance(self.req, Unset):
            req = self.req.to_dict()

        rules: FileTypes | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if req is not UNSET:
            field_dict["req"] = req
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.req, Unset):
            files.append(("req", (None, json.dumps(self.req.to_dict()).encode(), "application/json")))

        if not isinstance(self.rules, Unset):
            files.append(("rules", self.rules.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_rules_upload_req import SnortRulesUploadReq

        d = dict(src_dict)
        _req = d.pop("req", UNSET)
        req: SnortRulesUploadReq | Unset
        if isinstance(_req, Unset):
            req = UNSET
        else:
            req = SnortRulesUploadReq.from_dict(_req)

        _rules = d.pop("rules", UNSET)
        rules: File | Unset
        if isinstance(_rules, Unset):
            rules = UNSET
        else:
            rules = File(payload=BytesIO(_rules))

        store_snort_ruleset_body = cls(
            req=req,
            rules=rules,
        )

        store_snort_ruleset_body.additional_properties = d
        return store_snort_ruleset_body

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
